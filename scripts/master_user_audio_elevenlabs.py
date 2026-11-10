#!/usr/bin/env python3
"""
Master User-Provided Audio into ElevenLabs-Grade Studio Broadcast Quality
Input:  /home/solyman/Downloads/Generated Audio November 10, 2026 - 5_22PM.wav
Output: 320 kbps 48 kHz Stereo MP3, EBU R128 (-16 LUFS), Broadcast Multi-band EQ & Optical Leveling
"""
import os
import sys
import time
import shutil
import subprocess
from pathlib import Path

INPUT_WAV = Path("/home/solyman/Downloads/Generated Audio November 10, 2026 - 5_22PM.wav")
OUTPUT_DIR = Path("/home/solyman/Documents/VoiceStudio-main/outputs")
DOWNLOADS_DIR = Path.home() / "Downloads"
DOC_DOWNLOADS_DIR = DOWNLOADS_DIR / "Bengali_Documentary"

OUTPUT_MP3 = OUTPUT_DIR / "generated_audio_elevenlabs_master.mp3"
DOWNLOAD_OUT_1 = DOWNLOADS_DIR / "Generated_Audio_ElevenLabs_Master.mp3"
DOWNLOAD_OUT_2 = DOC_DOWNLOADS_DIR / "Generated_Audio_ElevenLabs_Master.mp3"

MASTERING_FILTERGRAPH = (
    "volume=-2.5dB,"
    "highpass=f=75,"
    "equalizer=f=135:t=q:w=1.2:g=3.2,"
    "equalizer=f=380:t=q:w=1.6:g=-2.2,"
    "equalizer=f=3300:t=q:w=1.4:g=2.8,"
    "equalizer=f=11000:t=q:w=1.0:g=1.8,"
    "acompressor=threshold=-18dB:ratio=2.8:attack=15:release=140,"
    "loudnorm=I=-16:TP=-1.5:LRA=9"
)

def main():
    print("=" * 65)
    print("🎙️ Studio Broadcast Mastering: ElevenLabs-Grade Audio")
    print(f"   Input:  {INPUT_WAV}")
    print(f"   Output: {OUTPUT_MP3}")
    print("=" * 65)

    if not INPUT_WAV.exists():
        print(f"Error: Input file {INPUT_WAV} does not exist!")
        sys.exit(1)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    DOC_DOWNLOADS_DIR.mkdir(parents=True, exist_ok=True)

    t0 = time.time()
    cmd = [
        "ffmpeg", "-y", "-i", str(INPUT_WAV),
        "-af", MASTERING_FILTERGRAPH,
        "-ar", "48000",
        "-ac", "2",
        "-b:a", "320k",
        str(OUTPUT_MP3)
    ]

    print("[1/2] Processing audio through analog studio filtergraph...")
    subprocess.run(cmd, check=True)
    elapsed = time.time() - t0

    # Copy to downloads
    print("[2/2] Exporting to user directories...")
    shutil.copy(OUTPUT_MP3, DOWNLOAD_OUT_1)
    shutil.copy(OUTPUT_MP3, DOWNLOAD_OUT_2)

    file_size_mb = os.path.getsize(OUTPUT_MP3) / (1024 * 1024)
    print("\n" + "=" * 65)
    print("🎉 Success! ElevenLabs-Grade Broadcast Audio Mastered:")
    print(f"   Master File:        {OUTPUT_MP3}")
    print(f"   Downloads (Root):   {DOWNLOAD_OUT_1}")
    print(f"   Downloads (Folder): {DOWNLOAD_OUT_2}")
    print(f"   File Size:          {file_size_mb:.2f} MB")
    print(f"   Elapsed Time:       {elapsed:.1f}s")
    print("=" * 65)

if __name__ == "__main__":
    main()

