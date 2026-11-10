#!/usr/bin/env python3
"""
Master User-Provided Audio into Ultra-Smooth ElevenLabs Velvet-Silk Quality (0.90x Speed)
Input:  /home/solyman/Downloads/Generated Audio November 10, 2026 - 5_22PM.wav
Pacing: 0.90x deliberate documentary cadence (pitch-preserved)
DSP:    Spotify Pedalboard 64-bit Velvet Silk Chain + EBU R128 Broadcast Loudness
"""
import os
import sys
import time
import shutil
import tempfile
import subprocess
from pathlib import Path
import numpy as np
import soundfile as sf
from pedalboard import (
    Pedalboard, HighpassFilter, LowShelfFilter, PeakFilter,
    HighShelfFilter, Compressor, Limiter, Reverb
)

INPUT_WAV = Path("/home/solyman/Downloads/Generated Audio November 10, 2026 - 5_22PM.wav")
OUTPUT_DIR = Path("/home/solyman/Documents/VoiceStudio-main/outputs")
DOWNLOADS_DIR = Path.home() / "Downloads"
DOC_DOWNLOADS_DIR = DOWNLOADS_DIR / "Bengali_Documentary"

OUTPUT_MP3 = OUTPUT_DIR / "generated_audio_elevenlabs_velvet_silk_0.90x.mp3"
DOWNLOAD_OUT_1 = DOWNLOADS_DIR / "Generated_Audio_ElevenLabs_Velvet_Silk_0.90x.mp3"
DOWNLOAD_OUT_2 = DOC_DOWNLOADS_DIR / "Generated_Audio_ElevenLabs_Velvet_Silk_0.90x.mp3"

def main():
    print("=" * 70)
    print("🎙️ Ultra-Smooth ElevenLabs-Grade Velvet Silk Audio Masterer (0.90x)")
    print(f"   Input:      {INPUT_WAV}")
    print(f"   Output:     {OUTPUT_MP3}")
    print(f"   Pacing:     0.90x (Deliberate, relaxed, captivating documentary speed)")
    print("=" * 70)

    if not INPUT_WAV.exists():
        print(f"Error: Input file {INPUT_WAV} does not exist!")
        sys.exit(1)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    DOC_DOWNLOADS_DIR.mkdir(parents=True, exist_ok=True)

    t0 = time.time()

    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_slow_wav = os.path.join(tmp_dir, "slow_090x.wav")
        tmp_dsp_wav = os.path.join(tmp_dir, "dsp_velvet.wav")

        # Step 1: Pitch-preserved 0.90x speed scaling using high-precision atempo
        print("\n[1/3] Scaling speed to 0.90x with exact pitch preservation...")
        subprocess.run([
            "ffmpeg", "-y", "-i", str(INPUT_WAV),
            "-filter:a", "atempo=0.90",
            "-ar", "48000",
            tmp_slow_wav
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # Step 2: 64-bit Spotify Pedalboard Velvet Silk DSP Processing
        print("[2/3] Processing audio through Spotify Pedalboard Velvet-Silk Chain...")
        data, sr = sf.read(tmp_slow_wav)
        if data.ndim == 1:
            audio_tensor = np.expand_dims(data, axis=0)
        else:
            audio_tensor = data.T

        board = Pedalboard([
            # Plosive & rumble filter
            HighpassFilter(cutoff_frequency_hz=75),
            # Warm chest body
            LowShelfFilter(cutoff_frequency_hz=140, gain_db=3.0),
            # Clear out boxy mud (anti-cardboard cut)
            PeakFilter(cutoff_frequency_hz=380, gain_db=-3.5, q=1.5),
            # Smooth out ear fatigue zone (anti-fatigue dip)
            PeakFilter(cutoff_frequency_hz=2800, gain_db=-1.5, q=2.0),
            # Silky studio air & sheen
            HighShelfFilter(cutoff_frequency_hz=8500, gain_db=2.5),
            # Optical broadcast leveling compressor
            Compressor(threshold_db=-18.0, ratio=2.5, attack_ms=25.0, release_ms=180.0),
            # Acoustic studio room cohesion (replaces dry mono with warm documentary space)
            Reverb(room_size=0.08, damping=0.8, wet_level=0.04, dry_level=0.96, width=0.6),
            # Transparent peak limiter
            Limiter(threshold_db=-1.5, release_ms=100.0)
        ])

        effected = board(audio_tensor, sr)
        sf.write(tmp_dsp_wav, effected.T, sr)

        # Step 3: EBU R128 Broadcast Loudness Mastering to 320 kbps Stereo MP3
        print("[3/3] Final EBU R128 loudness mastering (-16 LUFS, 320k MP3)...")
        subprocess.run([
            "ffmpeg", "-y", "-i", tmp_dsp_wav,
            "-af", "loudnorm=I=-16:TP=-1.5:LRA=9",
            "-ar", "48000",
            "-ac", "2",
            "-b:a", "320k",
            str(OUTPUT_MP3)
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Export to Downloads
    shutil.copy(OUTPUT_MP3, DOWNLOAD_OUT_1)
    shutil.copy(OUTPUT_MP3, DOWNLOAD_OUT_2)

    elapsed = time.time() - t0
    size_mb = os.path.getsize(OUTPUT_MP3) / (1024 * 1024)

    # Read final duration
    final_data, final_sr = sf.read(str(OUTPUT_MP3))
    dur_s = len(final_data) / final_sr
    mins = int(dur_s // 60)
    secs = int(dur_s % 60)

    print("\n" + "=" * 70)
    print("🎉 Success! ElevenLabs-Grade Velvet-Silk Master Audio Generated:")
    print(f"   Master File:        {OUTPUT_MP3}")
    print(f"   Downloads (Root):   {DOWNLOAD_OUT_1}")
    print(f"   Downloads (Folder): {DOWNLOAD_OUT_2}")
    print(f"   Duration:           {mins}m {secs:02d}s ({dur_s:.1f}s) @ 0.90x pacing")
    print(f"   File Size:          {size_mb:.2f} MB")
    print(f"   Mastering Standard: EBU R128 (-16.0 LUFS, -1.5 dB True Peak, 48kHz Stereo)")
    print(f"   Elapsed Time:       {elapsed:.1f}s")
    print("=" * 70)

if __name__ == "__main__":
    main()

