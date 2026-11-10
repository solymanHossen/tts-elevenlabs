import asyncio
import os
import subprocess
import edge_tts

VOICE_MALE = "bn-BD-PradeepNeural"
VOICE_FEMALE = "bn-BD-NabanitaNeural"

INPUT_FILE = "dhaka_university_history.txt"
OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

async def generate_speech_for_text(text: str, voice: str, output_path: str):
    """Generate audio for paragraphs and concatenate seamlessly."""
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    temp_files = []
    
    print(f"[{voice}] Total paragraphs to synthesize: {len(paragraphs)}")
    
    for idx, para in enumerate(paragraphs, 1):
        temp_file = os.path.join(OUTPUT_DIR, f"temp_{idx:03d}.mp3")
        temp_files.append(temp_file)
        print(f"[{idx}/{len(paragraphs)}] Synthesizing paragraph ({len(para)} chars)...")
        communicate = edge_tts.Communicate(para, voice)
        await communicate.save(temp_file)
        # Small pause between paragraphs
        await asyncio.sleep(0.1)
    
    # Create concat list for ffmpeg
    list_file = os.path.join(OUTPUT_DIR, "concat_list.txt")
    with open(list_file, "w", encoding="utf-8") as f:
        for tf in temp_files:
            f.write(f"file '{os.path.abspath(tf)}'\n")
    
    print(f"Merging all segments into {output_path}...")
    subprocess.run(
        ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", list_file, "-c", "copy", output_path],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    
    # Cleanup temporary segment files
    for tf in temp_files:
        if os.path.exists(tf):
            os.remove(tf)
    if os.path.exists(list_file):
        os.remove(list_file)
        
    print(f"✓ Generated high-fidelity Bengali audio: {output_path}")

async def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        content = f.read().strip()
        
    # Generate Male Documentary voice (Pradeep)
    male_out = os.path.join(OUTPUT_DIR, "dhaka_university_history_male_pradeep.mp3")
    await generate_speech_for_text(content, VOICE_MALE, male_out)

if __name__ == "__main__":
    asyncio.run(main())

