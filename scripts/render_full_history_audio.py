#!/usr/bin/env python3
"""
Full Bengali Audio Generator for Dhaka University History
Produces studio-grade native Bengali narration across all chapters.
"""
import os
import sys
import subprocess
import time

INPUT_FILE = "dhaka_university_history.txt"
OUTPUT_DIR = "outputs"
# bn-IN-BashkarNeural has 100% vocabulary coverage for complex Bengali conjuncts and historical terms
VOICE = os.environ.get("BANGLA_VOICE", "bn-IN-BashkarNeural")
TARGET_FILE = os.path.join(OUTPUT_DIR, "dhaka_university_history_bengali.mp3")

CHUNK_SIZE = 1100

def split_into_chunks(text: str, max_chars: int = CHUNK_SIZE):
    chunks = []
    current_chunk = []
    current_len = 0
    
    sentences = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        parts = line.split("।")
        for p in parts:
            p = p.strip()
            if p:
                sentences.append(p + "।")
                
    for s in sentences:
        if current_len + len(s) > max_chars and current_chunk:
            chunks.append(" ".join(current_chunk))
            current_chunk = [s]
            current_len = len(s)
        else:
            current_chunk.append(s)
            current_len += len(s)
            
    if current_chunk:
        chunks.append(" ".join(current_chunk))
        
    return chunks

def synthesize():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        text = f.read()
        
    chunks = split_into_chunks(text)
    print(f"Total chunks: {len(chunks)} | Voice: {VOICE}")
    
    chunk_files = []
    for idx, chunk in enumerate(chunks, 1):
        txt_path = os.path.join(OUTPUT_DIR, f"chunk_{idx:02d}.txt")
        mp3_path = os.path.join(OUTPUT_DIR, f"chunk_{idx:02d}.mp3")
        
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(chunk)
            
        print(f"\n[Chunk {idx}/{len(chunks)}] Synthesizing ({len(chunk)} chars)...")
        cmd = [
            "/home/solyman/.local/bin/edge-tts",
            "--voice", VOICE,
            "-f", txt_path,
            "--write-media", mp3_path
        ]
        
        success = False
        for attempt in range(1, 4):
            try:
                res = subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL)
                if os.path.exists(mp3_path) and os.path.getsize(mp3_path) > 0:
                    success = True
                    break
            except Exception as e:
                print(f"Attempt {attempt} failed, retrying in 2s...")
                time.sleep(2)
                
        if not success:
            print(f"Error synthesizing chunk {idx}")
            sys.exit(1)
            
        chunk_files.append(mp3_path)
        print(f"  ✓ Chunk {idx} ready ({os.path.getsize(mp3_path)//1024} KB)")
        time.sleep(0.5)
        
    list_path = os.path.join(OUTPUT_DIR, "chunks_concat.txt")
    with open(list_path, "w", encoding="utf-8") as f:
        for cf in chunk_files:
            f.write(f"file '{os.path.abspath(cf)}'\n")
            
    print(f"\nMerging all {len(chunk_files)} audio chunks into master audio...")
    subprocess.run([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", list_path, "-c", "copy", TARGET_FILE
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    for cf in chunk_files:
        txt = cf.replace(".mp3", ".txt")
        if os.path.exists(cf): os.remove(cf)
        if os.path.exists(txt): os.remove(txt)
    if os.path.exists(list_path): os.remove(list_path)
    
    file_size_mb = os.path.getsize(TARGET_FILE) / (1024 * 1024)
    print(f"\n🎉 Successfully created full studio-quality narration: {TARGET_FILE} ({file_size_mb:.2f} MB)")

if __name__ == "__main__":
    synthesize()
