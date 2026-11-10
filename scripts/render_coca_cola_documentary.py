#!/usr/bin/env python3
"""
Render Coca-Cola Documentary via 5-Stage Bengali Documentary Voice System
"""
import os
import sys
import json
import time
import asyncio
from pathlib import Path

# Add backend to path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR / "backend"))

from services.bangla_documentary_engine import generate_bangla_documentary

INPUT_FILE = BASE_DIR / "outputs" / "coca_cola_script_clean.txt"
OUTPUT_MP3 = BASE_DIR / "outputs" / "coca_cola_documentary_elevenlabs_grade.mp3"
CAPTIONS_JSON = BASE_DIR / "outputs" / "coca_cola_remotion_captions.json"
DOWNLOADS_DIR = Path.home() / "Downloads" / "Bengali_Documentary"

async def main():
    print("=" * 65)
    print("🎙️ Rendering Coca-Cola Documentary - ElevenLabs-Grade Bengali Voice")
    print("   Engine: 5-Stage Bengali Documentary Voice System")
    print(f"   Input:  {INPUT_FILE}")
    print(f"   Output: {OUTPUT_MP3}")
    print("=" * 65)

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        text = f.read()

    print(f"\n[1/3] Loaded script: {len(text)} characters.")
    print("[2/3] Synthesizing, crossfading, mastering and extracting Remotion captions...")

    start_time = time.time()
    result = await generate_bangla_documentary(
        text=text,
        output_path=str(OUTPUT_MP3),
        response_format="mp3",
        speed=0.94,
        num_step=40,
        guidance_scale=2.2,
        return_timestamps=True
    )

    elapsed = time.time() - start_time
    file_size_mb = os.path.getsize(OUTPUT_MP3) / (1024 * 1024)

    # Save Remotion Captions JSON
    with open(CAPTIONS_JSON, "w", encoding="utf-8") as f:
        json.dump({
            "duration_seconds": result["duration_seconds"],
            "remotion_captions": result["remotion_captions"],
            "segments": result["segments"]
        }, f, ensure_ascii=False, indent=2)

    # Copy to user Downloads
    DOWNLOADS_DIR.mkdir(parents=True, exist_ok=True)
    shutil_out = DOWNLOADS_DIR / "coca_cola_documentary_elevenlabs_grade.mp3"
    import shutil
    shutil.copy(OUTPUT_MP3, shutil_out)
    shutil.copy(CAPTIONS_JSON, DOWNLOADS_DIR / "remotion_captions.json")

    print("\n" + "=" * 65)
    print("🎉 Success! ElevenLabs-Grade Master Audio Rendered:")
    print(f"   Master File:      {OUTPUT_MP3}")
    print(f"   Downloads Copy:   {shutil_out}")
    print(f"   Remotion Captions: {CAPTIONS_JSON}")
    print(f"   Duration:         {int(result['duration_seconds'] // 60)}m {int(result['duration_seconds'] % 60):02d}s ({result['duration_seconds']:.1f}s)")
    print(f"   Size:             {file_size_mb:.2f} MB")
    print(f"   Word Captions:    {len(result['remotion_captions'])} words mapped")
    print(f"   Elapsed Time:     {elapsed:.1f}s")
    print("=" * 65)

if __name__ == "__main__":
    asyncio.run(main())

