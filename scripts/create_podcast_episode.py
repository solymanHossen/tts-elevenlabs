#!/usr/bin/env python3
"""
Daily Speak English — Automated Studio Master & YouTube Publisher
==================================================================
Converts conversational scripts into world-class broadcast podcast episodes
and generates YouTube Titles, Descriptions with Chapters, and SEO Tags.

Features:
- Solu: Male (en-US-AndrewNeural)
- Tonu: Female (en-US-AvaNeural)
- Speed: 0.90x (rate="-10%" native neural prosody)
- Stereo soundstaging & adaptive conversational pacing
- Subtle Rhodes acoustic piano jingles (quiet background)
- Studio room acoustic presence
- Pedalboard DSP vocal mastering chain
- EBU R128 loudness normalization (-16.0 LUFS, 48kHz, 320kbps)
- YouTube Title, Description with exact Timestamps/Chapters, and Tags
- Automatic folder creation and direct sync to ~/Downloads/
"""

import argparse
import asyncio
import os
import re
import shutil
import subprocess
import sys
import time
import numpy as np
import soundfile as sf
import pedalboard as pb
import edge_tts

SR = 48000
RATE = "-10%"  # 0.90x Speed
VOICE_SOLU = "en-US-AndrewNeural"
VOICE_TONU = "en-US-AvaNeural"
FALLBACK_SOLU = "en-US-BrianNeural"
FALLBACK_TONU = "en-US-EmmaNeural"


def parse_script(raw_file):
    with open(raw_file, "r", encoding="utf-8") as f:
        text = f.read()

    # Clean wrapper tags, comments and metadata
    text = re.sub(r"<\/?USER_REQUEST>", "", text)
    text = re.sub(r"<ADDITIONAL_METADATA>[\s\S]*", "", text)
    text = re.sub(r"\/\/.*$", "", text, flags=re.MULTILINE)

    lines = text.split("\n")
    turns = []
    current_speaker = None
    current_text = []

    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        m = re.match(r"^\*\*(Solu(?:\s*\([^\)]+\))?|Tonu(?:\s*\([^\)]+\))?|Both)\:\*\*\s*(.*)$", line)
        if m:
            if current_speaker:
                cleaned = " ".join(current_text).strip()
                cleaned = re.sub(r"[\U00010000-\U0010ffff\u2600-\u27bf]", "", cleaned).strip()
                if cleaned:
                    turns.append((current_speaker, cleaned))
                current_text = []
            raw_spk = m.group(1)
            if "Solu" in raw_spk:
                current_speaker = "Solu"
            elif "Tonu" in raw_spk:
                current_speaker = "Tonu"
            else:
                current_speaker = "Both"
            if m.group(2).strip():
                current_text.append(m.group(2).strip())
        elif current_speaker:
            current_text.append(line)

    if current_speaker and current_text:
        cleaned = " ".join(current_text).strip()
        cleaned = re.sub(r"[\U00010000-\U0010ffff\u2600-\u27bf]", "", cleaned).strip()
        if cleaned:
            turns.append((current_speaker, cleaned))

    return turns


async def synth_turn(idx, speaker, text, cache_dir, sem):
    target_mp3 = os.path.join(cache_dir, f"turn_{idx:03d}_{speaker}.mp3")
    if os.path.exists(target_mp3) and os.path.getsize(target_mp3) > 1000:
        return target_mp3

    async with sem:
        for attempt in range(5):
            try:
                voice = VOICE_SOLU if speaker == "Solu" else VOICE_TONU
                if attempt >= 2:
                    voice = FALLBACK_SOLU if speaker == "Solu" else FALLBACK_TONU

                if speaker in ("Solu", "Tonu"):
                    c = edge_tts.Communicate(text, voice, rate=RATE)
                    await c.save(target_mp3)
                elif speaker == "Both":
                    f_solu = os.path.join(cache_dir, f"turn_{idx:03d}_Both_solu.mp3")
                    f_tonu = os.path.join(cache_dir, f"turn_{idx:03d}_Both_tonu.mp3")
                    c1 = edge_tts.Communicate(text, VOICE_SOLU, rate=RATE)
                    await c1.save(f_solu)
                    c2 = edge_tts.Communicate(text, VOICE_TONU, rate=RATE)
                    await c2.save(f_tonu)
                    cmd = [
                        "ffmpeg", "-y",
                        "-i", f_solu,
                        "-i", f_tonu,
                        "-filter_complex", "amix=inputs=2:duration=longest:weights=1.0 1.0",
                        target_mp3,
                    ]
                    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                return target_mp3
            except Exception as e:
                if attempt == 4:
                    raise RuntimeError(f"Failed to synth turn {idx} [{speaker}]: {e}")
                await asyncio.sleep(1.0 * (attempt + 1))


def create_rhodes_jingle(duration=6.5, is_outro=False):
    n_samples = int(SR * duration)
    audio_l = np.zeros(n_samples, dtype=np.float32)
    audio_r = np.zeros(n_samples, dtype=np.float32)

    def rhodes_note(freq, note_t):
        s = np.sin(2 * np.pi * freq * note_t)
        s += 0.35 * np.sin(2 * np.pi * 2 * freq * note_t)
        s += 0.15 * np.sin(2 * np.pi * 3 * freq * note_t)
        s += 0.08 * np.sin(2 * np.pi * 4 * freq * note_t)
        s += 0.05 * np.sin(2 * np.pi * 7 * freq * note_t) * np.exp(-note_t * 12)
        env = (1.0 - np.exp(-note_t * 40)) * np.exp(-note_t * 0.75)
        return s * env

    if not is_outro:
        chords = [
            (0.0, [174.61, 220.00, 261.63, 329.63, 392.00]),
            (1.4, [146.83, 220.00, 261.63, 329.63, 349.23]),
            (2.8, [196.00, 233.08, 293.66, 349.23, 440.00]),
            (4.2, [130.81, 196.00, 261.63, 329.63, 392.00, 523.25]),
        ]
        master_gain = -16.0
    else:
        chords = [
            (0.0, [196.00, 233.08, 293.66, 349.23, 440.00]),
            (2.0, [130.81, 196.00, 261.63, 329.63, 392.00, 523.25]),
            (4.2, [174.61, 220.00, 261.63, 329.63, 392.00, 523.25]),
        ]
        master_gain = -11.0

    for start_t, freqs in chords:
        start_idx = int(start_t * SR)
        note_len = min(int(2.8 * SR), n_samples - start_idx)
        if note_len <= 0:
            continue
        note_t = np.linspace(0, note_len / SR, note_len, endpoint=False)
        chord_sig = np.zeros(note_len, dtype=np.float32)
        for i, f in enumerate(freqs):
            delay = int(i * 0.022 * SR)
            if delay < note_len:
                n_t = note_t[: note_len - delay]
                chord_sig[delay:] += rhodes_note(f, n_t) * (0.88 ** i)

        audio_l[start_idx : start_idx + note_len] += chord_sig * 0.65
        audio_r[start_idx : start_idx + note_len] += chord_sig * 0.80

    board = pb.Pedalboard([
        pb.Chorus(rate_hz=0.9, depth=0.35, centre_delay_ms=8.0, feedback=0.2, mix=0.35),
        pb.Delay(delay_seconds=0.26, feedback=0.25, mix=0.22),
        pb.Reverb(room_size=0.65, damping=0.45, wet_level=0.35, dry_level=0.75, width=0.95),
        pb.HighpassFilter(cutoff_frequency_hz=100),
        pb.LowpassFilter(cutoff_frequency_hz=5800),
        pb.Gain(gain_db=master_gain),
    ])

    stereo = np.vstack([audio_l, audio_r])
    processed = board(stereo, SR)
    return processed.T


def load_audio_clip(path):
    wav_path = path.replace(".mp3", "_48k.wav")
    if not os.path.exists(wav_path) or os.path.getsize(wav_path) < 1000:
        subprocess.run(
            ["ffmpeg", "-y", "-i", path, "-ar", str(SR), "-ac", "1", wav_path],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    data, _ = sf.read(wav_path, dtype="float32")
    if len(data.shape) > 1:
        data = data[:, 0]
    return data


def apply_panning(mono_clip, pan_val):
    angle = (pan_val + 1.0) * (np.pi / 4.0)
    left_gain = np.cos(angle)
    right_gain = np.sin(angle)
    return np.column_stack([mono_clip * left_gain, mono_clip * right_gain])


def get_dialogue_pause(prev_text, current_text):
    c_lower = current_text.lower().strip()
    p_lower = prev_text.lower().strip() if prev_text else ""

    quick_starters = (
        "exactly", "i agree", "that's so true", "wow", "oh,", "oh ",
        "right", "yes", "absolutely", "well said", "beautifully said", "definitely"
    )
    if any(c_lower.startswith(q) for q in quick_starters):
        return 0.22

    if p_lower.endswith("?"):
        return 0.30

    return 0.32


def generate_youtube_assets_ep02(episode_dir, turns, chapters):
    """Generate YouTube title, description with timestamps, and SEO tags for Episode 02."""
    yt_dir = os.path.join(episode_dir, "youtube")
    os.makedirs(yt_dir, exist_ok=True)
    meta_file = os.path.join(yt_dir, "YOUTUBE_METADATA.txt")

    chapters_text = "\n".join([f"{ts} - {title}" for ts, title in chapters])

    content = f"""================================================================================
📌 YOUTUBE VIDEO TITLE (Choose one or use the recommended title)
================================================================================
(Recommended):
Daily English Conversation Practice: How to Change Your Life & Build Good Habits | Speak Confidently

Alternative 1:
English Speaking Practice: Building Habits, Discipline & Time Management | Daily Speak English

Alternative 2:
Learn Real English: How Small Daily Habits Change Your Life (English Listening & Speaking Practice)

================================================================================
📝 YOUTUBE VIDEO DESCRIPTION (Copy and paste into your YouTube video)
================================================================================
Welcome to Daily Speak English! 🌟 In today's listening and speaking practice episode, Solu and Tonu discuss how to build powerful daily habits, overcome procrastination, manage time effectively, and change your life one small step at a time.

This conversation is delivered at a clear, natural 0.90x pace—crafted specifically for English learners to build effortless listening comprehension, pick up everyday phrases, and speak English with confidence.

🎧 Wear headphones for the full studio stereo experience!

⏱️ CHAPTERS & TIMESTAMPS:
{chapters_text}

✨ KEY ENGLISH EXPRESSIONS IN THIS EPISODE:
1. "Take it one step at a time" - Focus on making progress gradually without rushing.
2. "Get back on track" - Returning to your good routine after missing a day.
3. "Stick to your goals" - Staying committed to your goals when things get challenging.
4. "Make the most of your time" - Using your hours wisely and doing meaningful things.
5. "Step out of your comfort zone" - Trying something new that feels slightly challenging.
6. "Progress takes time" - Meaningful growth requires patience and consistent daily effort.

💬 TODAY'S LISTENER CHALLENGE:
What is ONE bad habit you want to change, and ONE good habit you want to build this month?
👉 Write your answer in 2-3 sentences in the comments below! Don't worry about small mistakes—practicing speaking and writing is how you achieve fluency!

🔔 Subscribe to Daily Speak English for daily conversational practice!
👍 Like this video if this conversation inspired you today.
📤 Share this with a friend who is working on self-improvement and learning English!

#DailySpeakEnglish #LearnEnglish #EnglishConversation #EnglishSpeakingPractice #EnglishListeningPractice #Habits #SelfDiscipline #PersonalGrowth #SpeakEnglishNaturally

================================================================================
🏷️ YOUTUBE SEO TAGS (Copy and paste into the Tags box)
================================================================================
daily speak english, english conversation practice, learn english, speak english naturally, english listening practice, english speaking practice, learn english conversation, build good habits, how to change your life, english podcast for learners, daily english conversation, self discipline english, habits english vocabulary, practice speaking english, fluent english speaking, solu and tonu
"""

    with open(meta_file, "w", encoding="utf-8") as f:
        f.write(content)

    script_dir = os.path.join(episode_dir, "script")
    os.makedirs(script_dir, exist_ok=True)
    with open(os.path.join(script_dir, "clean_transcript.txt"), "w", encoding="utf-8") as f:
        for spk, txt in turns:
            f.write(f"{spk}: {txt}\n\n")

    return meta_file


async def run_pipeline(raw_script_path, episode_name="ep02_build_good_habits"):
    base_proj_dir = os.path.join("podcast_projects", episode_name)
    audio_dir = os.path.join(base_proj_dir, "audio")
    cache_dir = os.path.join(base_proj_dir, "cache")
    os.makedirs(audio_dir, exist_ok=True)
    os.makedirs(cache_dir, exist_ok=True)

    final_mp3 = os.path.join(audio_dir, f"Daily_Speak_English_{episode_name.upper()}_STUDIO_MASTER.mp3")
    temp_wav = os.path.join(audio_dir, "temp_master.wav")

    print(f"=== [Step 1] Parsing script: {raw_script_path} ===")
    turns = parse_script(raw_script_path)
    print(f"Total turns: {len(turns)}")

    print(f"\n=== [Step 2] Parallel Neural Synthesis (0.90x Speed) ===")
    sem = asyncio.Semaphore(6)
    tasks = [synth_turn(i, spk, text, cache_dir, sem) for i, (spk, text) in enumerate(turns)]
    t0 = time.time()
    mp3_files = await asyncio.gather(*tasks)
    print(f"All {len(mp3_files)} turns ready in {time.time()-t0:.1f}s.")

    print(f"\n=== [Step 3] Soundstaging, Timing & Chapter Marker Tracking ===")
    assembled_parts = []
    pre_silence_samples = int(1.2 * SR)
    assembled_parts.append(np.zeros((pre_silence_samples, 2), dtype=np.float32))

    current_sample_pos = pre_silence_samples
    turn_timestamps = []

    for i, (spk, text) in enumerate(turns):
        turn_timestamps.append(current_sample_pos / SR)
        clip_mono = load_audio_clip(mp3_files[i])

        if spk == "Solu":
            clip_stereo = apply_panning(clip_mono, -0.16)
        elif spk == "Tonu":
            clip_stereo = apply_panning(clip_mono, 0.16)
        else:
            clip_stereo = apply_panning(clip_mono, 0.0)

        if i > 0:
            pause_sec = get_dialogue_pause(turns[i - 1][1], text)
            pause_samples = int(pause_sec * SR)
            assembled_parts.append(np.zeros((pause_samples, 2), dtype=np.float32))
            current_sample_pos += pause_samples

        assembled_parts.append(clip_stereo)
        current_sample_pos += len(clip_stereo)

    dialogue_track = np.concatenate(assembled_parts, axis=0)
    dialogue_duration = len(dialogue_track) / SR
    print(f"Dialogue duration: {dialogue_duration:.2f}s ({dialogue_duration/60:.2f} mins).")

    # Accurate dynamic timestamps for Episode 02
    def find_chapter_ts(keyword):
        for idx, (spk, text) in enumerate(turns):
            if keyword.lower() in text.lower():
                sec = int(turn_timestamps[idx])
                return f"{sec//60:02d}:{sec%60:02d}"
        return None

    chapters = [
        ("00:00", "Introduction & Welcome"),
        (find_chapter_ts("struggle to do it") or "01:05", "Why Big New Year Plans Fail"),
        (find_chapter_ts("consistency is more important than intensity") or "02:15", "Consistency vs Intensity (15 Mins Daily)"),
        (find_chapter_ts("compare yourself with who you were yesterday") or "03:40", "Define Your Goals & Stop Comparing"),
        (find_chapter_ts("waking up early") or "05:10", "Sleep Schedules & Practical Morning Routine"),
        (find_chapter_ts("discuss another important habit: reading") or "06:45", "The Power of Reading 10 Pages Daily"),
        (find_chapter_ts("physical health. Do you think exercise") or "08:15", "Physical Health & Simple Movement"),
        (find_chapter_ts("wastes a lot of people") or "09:50", "Reducing Social Media & Time Wasters"),
        (find_chapter_ts("time management now") or "11:30", "Time Management: The Rule of 3 Tasks"),
        (find_chapter_ts("when they fail to maintain a good habit") or "13:20", "Overcoming Failure: Getting Back on Track"),
        (find_chapter_ts("confidence. How can someone become more confident") or "15:05", "Building Real Confidence by Taking Action"),
        (find_chapter_ts("choosing the right people to spend time with") or "16:45", "Choosing Supportive Friends & Mentors"),
        (find_chapter_ts("useful English expressions that our listeners can use") or "18:25", "6 Key English Expressions Explained"),
        (find_chapter_ts("covered some really important ideas today") or "20:10", "Key Takeaways & Daily Listener Challenge"),
    ]

    print(f"\n=== [Step 4] Rhodes Musical Jingles & Studio Room Tone ===")
    intro_music = create_rhodes_jingle(duration=6.0, is_outro=False)
    outro_music = create_rhodes_jingle(duration=8.0, is_outro=True)

    outro_padding = int(4.0 * SR)
    total_len = len(dialogue_track) + outro_padding
    master_mix = np.zeros((total_len, 2), dtype=np.float32)
    master_mix[: len(dialogue_track)] += dialogue_track

    # Subtle intro duck
    intro_vol = np.ones(len(intro_music), dtype=np.float32) * 0.30
    duck_start = int(1.0 * SR)
    duck_end = int(4.5 * SR)
    for s in range(duck_start, min(duck_end, len(intro_music))):
        alpha = (s - duck_start) / (duck_end - duck_start)
        intro_vol[s] = (1.0 - alpha) * 0.30
    if len(intro_music) > duck_end:
        intro_vol[duck_end:] = 0.0
    master_mix[: len(intro_music)] += intro_music * intro_vol[:, None]

    # Outro
    outro_start = max(0, len(dialogue_track) - int(4.5 * SR))
    outro_end = min(total_len, outro_start + len(outro_music))
    actual_outro_len = outro_end - outro_start

    outro_vol = np.ones(actual_outro_len, dtype=np.float32)
    fade_in_samples = int(3.0 * SR)
    for s in range(min(fade_in_samples, actual_outro_len)):
        outro_vol[s] = (s / fade_in_samples) * 0.60
    fade_out_samples = int(2.5 * SR)
    for s in range(actual_outro_len - fade_out_samples, actual_outro_len):
        if s >= 0:
            alpha = (actual_outro_len - s) / fade_out_samples
            outro_vol[s] *= alpha

    master_mix[outro_start:outro_end] += outro_music[:actual_outro_len] * outro_vol[:, None]

    # Studio room air
    np.random.seed(42)
    noise = np.random.normal(0, 0.0005, size=(total_len, 2)).astype(np.float32)
    air_board = pb.Pedalboard([
        pb.LowpassFilter(cutoff_frequency_hz=1200),
        pb.HighpassFilter(cutoff_frequency_hz=100),
    ])
    room_tone = air_board(noise.T, SR).T
    master_mix += room_tone

    print(f"\n=== [Step 5] Mastering DSP Chain ===")
    mastering_chain = pb.Pedalboard([
        pb.HighpassFilter(cutoff_frequency_hz=75),
        pb.LowShelfFilter(cutoff_frequency_hz=220, gain_db=1.2),
        pb.PeakFilter(cutoff_frequency_hz=3600, gain_db=1.8, q=0.9),
        pb.HighShelfFilter(cutoff_frequency_hz=11000, gain_db=1.0),
        pb.Compressor(threshold_db=-18.0, ratio=2.5, attack_ms=15.0, release_ms=120.0),
        pb.Limiter(threshold_db=-1.0),
    ])
    mastered = mastering_chain(master_mix.T, SR).T
    sf.write(temp_wav, mastered, SR, subtype="PCM_24")

    print(f"\n=== [Step 6] EBU R128 Loudness Normalization & MP3 Master ===")
    cmd_loudnorm = [
        "ffmpeg", "-y",
        "-i", temp_wav,
        "-af", "loudnorm=I=-16:TP=-1.0:LRA=10",
        "-ar", "48000",
        "-b:a", "320k",
        "-id3v2_version", "3",
        "-metadata", "title=Daily Speak English: How to Change Your Life & Build Good Habits (0.90x)",
        "-metadata", "artist=Solu (Male) & Tonu (Female)",
        "-metadata", "album=Daily Speak English",
        "-metadata", "genre=Podcast / Education",
        final_mp3,
    ]
    subprocess.run(cmd_loudnorm, check=True)
    if os.path.exists(temp_wav):
        os.remove(temp_wav)

    print(f"\n=== [Step 7] Generating YouTube Title, Description & Tags ===")
    yt_meta_path = generate_youtube_assets_ep02(base_proj_dir, turns, chapters)

    print(f"\n=== [Step 8] Syncing to User's ~/Downloads Folder ===")
    user_downloads_ep = os.path.expanduser(f"~/Downloads/Daily_Speak_English/{episode_name.upper()}")
    os.makedirs(user_downloads_ep, exist_ok=True)
    shutil.copy2(final_mp3, user_downloads_ep)
    shutil.copy2(yt_meta_path, user_downloads_ep)
    clean_script_file = os.path.join(base_proj_dir, "script", "clean_transcript.txt")
    if os.path.exists(clean_script_file):
        shutil.copy2(clean_script_file, user_downloads_ep)

    print(f"\n🎉 Episode Completed Successfully!")
    print(f"Master MP3: {final_mp3}")
    print(f"YouTube Info: {yt_meta_path}")
    print(f"Synced to Downloads: {user_downloads_ep}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("script", nargs="?", default="scripts/daily_speak_ep02_raw.txt")
    parser.add_argument("episode_name", nargs="?", default="ep02_build_good_habits")
    args = parser.parse_args()
    asyncio.run(run_pipeline(args.script, args.episode_name))
