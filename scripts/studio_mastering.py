#!/usr/bin/env python3
"""
Studio Audio Mastering Pipeline for Bengali Documentary Narration.
Applies broadcast mastering:
- 48 kHz High-Definition Upsampling
- Sub-bass rumble filter (80 Hz high-pass)
- Warm analog tube chest resonance (200 Hz low-shelf)
- Broadcast vocal presence & articulation (3.5 kHz peak)
- Silky air clarity (10 kHz high-shelf)
- Dynamic studio opto compression (2.8:1 ratio)
- ITU-R BS.1770-4 EBU R128 broadcast loudness normalization (-16.0 LUFS, -1.0 dB True Peak)
- 320 kbps High-Fidelity MP3 rendering
"""
import os
import subprocess
import soundfile as sf
import numpy as np
from pedalboard import (
    Pedalboard, HighpassFilter, LowShelfFilter, HighShelfFilter, PeakFilter, Compressor, Limiter, Gain
)

INPUT_MP3 = "outputs/dhaka_university_history_bengali_0.85x.mp3"
TEMP_WAV_IN = "outputs/temp_raw_48k.wav"
TEMP_WAV_DSP = "outputs/temp_dsp_processed.wav"
FINAL_MASTER_MP3 = "outputs/dhaka_university_history_bengali_STUDIO_MASTER.mp3"

def master_audio():
    print("1. Converting to 48kHz 32-bit float studio master format...")
    subprocess.run([
        "ffmpeg", "-y", "-i", INPUT_MP3,
        "-ar", "48000", "-ac", "2", "-c:a", "pcm_f32le", TEMP_WAV_IN
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    print("2. Applying Spotify Pedalboard Studio Analog Mastering Chain...")
    audio, sample_rate = sf.read(TEMP_WAV_IN)
    
    board = Pedalboard([
        # 1. Clean sub-bass mud and mic rumble
        HighpassFilter(cutoff_frequency_hz=80.0),
        
        # 2. Warm analog body (Neumann U87 / Avalon 737 warmth)
        LowShelfFilter(cutoff_frequency_hz=200.0, gain_db=2.2),
        
        # 3. Speech intelligibility & consonant crispness
        PeakFilter(cutoff_frequency_hz=3500.0, gain_db=1.8, q=1.0),
        
        # 4. Studio air & expensive shimmer
        HighShelfFilter(cutoff_frequency_hz=10000.0, gain_db=2.5),
        
        # 5. Broadcast optical compression for smooth dynamic range
        Compressor(threshold_db=-16.0, ratio=2.8, attack_ms=18.0, release_ms=160.0),
        
        # 6. Makeup gain
        Gain(gain_db=2.5),
        
        # 7. Transparent ceiling protection
        Limiter(threshold_db=-0.8)
    ])
    
    processed = board(audio, sample_rate)
    sf.write(TEMP_WAV_DSP, processed, sample_rate)
    
    print("3. Performing EBU R128 (-16 LUFS) Broadcast Loudness Normalization & 320kbps MP3 encoding...")
    subprocess.run([
        "ffmpeg", "-y", "-i", TEMP_WAV_DSP,
        "-af", "loudnorm=I=-16:TP=-1.0:LRA=11",
        "-b:a", "320k",
        "-ar", "48000",
        FINAL_MASTER_MP3
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    # Cleanup temp wav files
    for f in [TEMP_WAV_IN, TEMP_WAV_DSP]:
        if os.path.exists(f):
            os.remove(f)
            
    size_mb = os.path.getsize(FINAL_MASTER_MP3) / (1024 * 1024)
    print(f"\n🎉 Broadcast Studio Master Created: {FINAL_MASTER_MP3} ({size_mb:.2f} MB)")

if __name__ == "__main__":
    master_audio()

