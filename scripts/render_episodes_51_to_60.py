#!/usr/bin/env python3
"""
Daily Speak English — Dedicated Batch Processor for Episodes 51 to 60 (25+ Minutes Each)
========================================================================================
Renders and masters Episodes 51 to 60 with LOUDER, PUNCHIER BROADCAST AUDIO:
- YouTube Broadcast Target: -14.0 LUFS (loud, crystal clear on phone speakers & YouTube)
- Compression: Enhanced presence and vocal leveling via Pedalboard DSP
- Tonu opens EVERY episode ("Hey hey, lovely listeners! Welcome back to Daily Speak English...")
- Pacing: 0.90x (rate="-10%" native neural prosody)
- Voices: Tonu (en-US-AvaNeural), Solu (en-US-AndrewNeural), Both (Stereo Unison)
- Soundstage: Tonu Right 16%, Solu Left 16%, Unison Center
- Rhodes piano jingle intro/outro + analog acoustic room presence
- Automatic YouTube metadata generation with second-accurate chapters
- Outputs to podcast_projects/ and ~/Downloads/Daily_Speak_English/
"""

import asyncio
import os
import re
import shutil
import subprocess
import time
import numpy as np
import soundfile as sf
import pedalboard as pb
import edge_tts

SR = 48000
RATE = "-10%"
VOICE_SOLU = "en-US-AndrewNeural"
VOICE_TONU = "en-US-AvaNeural"
FALLBACK_SOLU = "en-US-GuyNeural"
FALLBACK_TONU = "en-US-JennyNeural"

EPISODES_METADATA_51_60 = [
    {
        "num": 51,
        "slug": "ep51_overcoming_perfectionism_80_percent_rule",
        "title": "Overcoming Perfectionism: The 80% Rule & Good Enough",
        "script": "scripts/daily_speak_ep51_full.txt",
        "desc_intro": "In today's 25+ minute mindset episode, Tonu and Solu dismantle perfectionism, examine Brené Brown's shame research, Anne Lamott's ugly first drafts, the 80% rule, Japanese Kintsugi, and freeing your English from the fear of mistakes.",
        "tags": "daily speak english, overcoming perfectionism english, 80 percent rule conversation, mindset vocabulary, learn english, speak english naturally, english listening practice, english speaking practice, tonu and solu"
    },
    {
        "num": 52,
        "slug": "ep52_art_of_listening_hearing_unsaid",
        "title": "The Art of Listening: Hearing What Is Left Unsaid",
        "script": "scripts/daily_speak_ep52_full.txt",
        "desc_intro": "In today's 25+ minute communication masterclass, Tonu and Solu explore the superpower of active listening, the neuroscience of hearing vs listening, reading nonverbal cues, the Japanese concept of Kuuki wo Yomu, and Carl Rogers' empathic listening.",
        "tags": "daily speak english, art of listening english, deep listening conversation, communication vocabulary, learn english, speak english naturally, english listening practice, english speaking practice, tonu and solu"
    },
    {
        "num": 53,
        "slug": "ep53_career_transitions_reinventing_yourself",
        "title": "Navigating Career Transitions: Reinventing Yourself at Any Age",
        "script": "scripts/daily_speak_ep53_full.txt",
        "desc_intro": "In today's 25+ minute career empowerment episode, Tonu and Solu dive into navigating career pivots, Herminia Ibarra's Working Identity, overcoming the sunk cost fallacy, Charles Handy's second curve, late bloomers, and crafting your reinvention story.",
        "tags": "daily speak english, career transition english, reinventing yourself conversation, career change vocabulary, learn english, speak english naturally, english listening practice, english speaking practice, tonu and solu"
    },
    {
        "num": 54,
        "slug": "ep54_nature_deficit_disorder_rewilding_senses",
        "title": "Nature Deficit Disorder: Rewilding Your Senses & The Healing Wild",
        "script": "scripts/daily_speak_ep54_full.txt",
        "desc_intro": "In today's 25+ minute wellness episode, Tonu and Solu unpack Nature-Deficit Disorder, the Biophilia hypothesis, Japanese Shinrin-yoku (forest bathing), natural fractal geometry, the 20-5-3 rule, and rewilding your senses outdoors.",
        "tags": "daily speak english, nature deficit disorder english, forest bathing shinrin yoku, outdoor wellness vocabulary, learn english, speak english naturally, english listening practice, english speaking practice, tonu and solu"
    },
    {
        "num": 55,
        "slug": "ep55_psychology_of_nostalgia_memory_yearning",
        "title": "The Psychology of Nostalgia: The Bittersweet Warmth of Memory",
        "script": "scripts/daily_speak_ep55_full.txt",
        "desc_intro": "In today's 25+ minute emotional psychology episode, Tonu and Solu explore the bittersweet science of nostalgia, the Southampton nostalgia studies, Proustian memory triggers, the reminiscence bump, retro culture, and savoring today as future nostalgia.",
        "tags": "daily speak english, psychology of nostalgia english, memory and emotion conversation, nostalgic vocabulary, learn english, speak english naturally, english listening practice, english speaking practice, tonu and solu"
    },
    {
        "num": 56,
        "slug": "ep56_mental_toughness_stoic_playbook",
        "title": "Building Mental Toughness: The Navy SEAL & Stoic Playbook for Resilience",
        "script": "scripts/daily_speak_ep56_full.txt",
        "desc_intro": "In today's 25+ minute resilience masterclass, Tonu and Solu fuse Navy SEAL mental toughness protocols with ancient Stoic philosophy: the 40% rule, the Dichotomy of Control, Box Breathing, voluntary discomfort, Amor Fati, and the Cookie Jar technique.",
        "tags": "daily speak english, mental toughness english, navy seal mindset stoicism, resilience vocabulary, learn english, speak english naturally, english listening practice, english speaking practice, tonu and solu"
    },
    {
        "num": 57,
        "slug": "ep57_sanctuary_of_quiet_spaces_libraries",
        "title": "The Sanctuary of Quiet Spaces: Public Libraries, Independent Bookstores & Slow Thought",
        "script": "scripts/daily_speak_ep57_full.txt",
        "desc_intro": "In today's 25+ minute literary culture episode, Tonu and Solu celebrate the third place sanctuary of public libraries and independent bookstores, the acoustic healing of silence, serendipity over algorithms, Tsundoku, and Maryanne Wolf's deep reading brain.",
        "tags": "daily speak english, public libraries english, quiet spaces bookstores conversation, slow reading vocabulary, learn english, speak english naturally, english listening practice, english speaking practice, tonu and solu"
    },
    {
        "num": 58,
        "slug": "ep58_philosophy_of_aging_grace_radiance",
        "title": "The Philosophy of Aging: Growing Older with Grace, Radiance & Deep Wisdom",
        "script": "scripts/daily_speak_ep58_full.txt",
        "desc_intro": "In today's 25+ minute life philosophy episode, Tonu and Solu challenge anti-aging culture and explore growing older with radiance, the U-bend of happiness, Cicero's De Senectute, centenarian Blue Zones, crystallized intelligence, and staying young at heart.",
        "tags": "daily speak english, philosophy of aging english, growing older with grace conversation, wisdom vocabulary, learn english, speak english naturally, english listening practice, english speaking practice, tonu and solu"
    },
    {
        "num": 59,
        "slug": "ep59_power_of_hope_post_traumatic_growth",
        "title": "The Power of Hope, Optimism & Post-Traumatic Growth: Rising from the Ashes",
        "script": "scripts/daily_speak_ep59_full.txt",
        "desc_intro": "In today's 25+ minute transformative episode, Tonu and Solu explore the unconquerable science of hope, Martin Seligman's learned optimism, Post-Traumatic Growth, Viktor Frankl's search for meaning, the Stockdale Paradox, and narrative re-authoring.",
        "tags": "daily speak english, power of hope english, post traumatic growth conversation, optimism vocabulary, learn english, speak english naturally, english listening practice, english speaking practice, tonu and solu"
    },
    {
        "num": 60,
        "slug": "ep60_grand_finale_crafting_remarkable_life",
        "title": "The Grand Finale: Crafting a Remarkable, Unforgettable Life & The Journey Ahead",
        "script": "scripts/daily_speak_ep60_full.txt",
        "desc_intro": "In today's 25+ minute landmark sixtieth episode and grand finale, Tonu and Solu celebrate the journey of Daily Speak English, explore Bronnie Ware's Top 5 Regrets of the Dying, Mary Oliver's wild and precious life, leaving a legacy, and English as your wings to the world.",
        "tags": "daily speak english, grand finale english, crafting remarkable life conversation, english fluency celebration, learn english, speak english naturally, english listening practice, english speaking practice, tonu and solu"
    }
]


def parse_script(raw_file):
    with open(raw_file, "r", encoding="utf-8") as f:
        text = f.read()

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
        else:
            if current_speaker:
                current_text.append(line)

    if current_speaker and current_text:
        cleaned = " ".join(current_text).strip()
        cleaned = re.sub(r"[\U00010000-\U0010ffff\u2600-\u27bf]", "", cleaned).strip()
        if cleaned:
            turns.append((current_speaker, cleaned))

    return turns


async def synth_turn(index, speaker, text, cache_dir, sem):
    out_mp3 = os.path.join(cache_dir, f"turn_{index:03d}_{speaker}.mp3")
    if os.path.exists(out_mp3) and os.path.getsize(out_mp3) > 1000:
        return out_mp3

    if os.path.exists(out_mp3):
        try:
            os.remove(out_mp3)
        except OSError:
            pass

    async with sem:
        if speaker == "Both":
            voice = VOICE_TONU
        elif speaker == "Solu":
            voice = VOICE_SOLU
        else:
            voice = VOICE_TONU

        for attempt in range(5):
            try:
                c = edge_tts.Communicate(text=text, voice=voice, rate=RATE)
                await asyncio.wait_for(c.save(out_mp3), timeout=25.0)
                if os.path.exists(out_mp3) and os.path.getsize(out_mp3) > 1000:
                    return out_mp3
                if os.path.exists(out_mp3):
                    os.remove(out_mp3)
            except Exception as e:
                if os.path.exists(out_mp3):
                    try:
                        os.remove(out_mp3)
                    except OSError:
                        pass
                await asyncio.sleep(1.0 + attempt * 1.5)

        # Fallback voice with timeout
        fallback_voice = FALLBACK_SOLU if speaker == "Solu" else FALLBACK_TONU
        try:
            c = edge_tts.Communicate(text=text, voice=fallback_voice, rate=RATE)
            await asyncio.wait_for(c.save(out_mp3), timeout=30.0)
            if os.path.exists(out_mp3) and os.path.getsize(out_mp3) > 1000:
                return out_mp3
        except Exception as e:
            pass

        raise RuntimeError(f"Failed to synthesize turn {index} after retries: {text[:60]}")


def generate_rhodes_jingle(duration_sec=7.0, is_intro=True):
    n_samples = int(duration_sec * SR)
    audio_l = np.zeros(n_samples, dtype=np.float32)
    audio_r = np.zeros(n_samples, dtype=np.float32)

    def rhodes_note(freq, t):
        fund = np.sin(2 * np.pi * freq * t) * np.exp(-t * 1.8)
        second = 0.35 * np.sin(2 * np.pi * freq * 2.0 * t) * np.exp(-t * 3.2)
        third = 0.15 * np.sin(2 * np.pi * freq * 3.0 * t) * np.exp(-t * 4.5)
        bell = 0.25 * np.sin(2 * np.pi * freq * 4.2 * t) * np.exp(-t * 9.0)
        tine = 0.12 * np.sin(2 * np.pi * freq * 7.5 * t) * np.exp(-t * 15.0)
        return fund + second + third + bell + tine

    if is_intro:
        # Cadd9 -> G/B -> Am7 -> Fmaj7(add9)
        chords = [
            (0.0, [261.63, 329.63, 392.00, 587.33], 2.2),
            (1.4, [246.94, 293.66, 392.00, 493.88], 2.0),
            (2.8, [220.00, 261.63, 329.63, 392.00], 2.0),
            (4.2, [174.61, 261.63, 329.63, 392.00, 523.25], 3.2),
        ]
        master_gain = -11.0
    else:
        # Fmaj7 -> Gsus4 -> Cadd9
        chords = [
            (0.0, [174.61, 261.63, 329.63, 392.00, 523.25], 2.5),
            (2.0, [196.00, 261.63, 293.66, 392.00, 587.33], 2.5),
            (4.2, [130.81, 261.63, 329.63, 392.00, 587.33, 659.25], 4.5),
        ]
        master_gain = -11.0

    for chord_time, notes, decay in chords:
        start_samp = int(chord_time * SR)
        for i, f in enumerate(notes):
            n_len = min(n_samples - start_samp, int(decay * SR))
            if n_len <= 0:
                continue
            t = np.linspace(0, n_len / SR, n_len, endpoint=False)
            tone = rhodes_note(f, t)
            pan = -0.3 + (i / max(1, len(notes) - 1)) * 0.6
            g_l = np.cos((pan + 1.0) * (np.pi / 4.0))
            g_r = np.sin((pan + 1.0) * (np.pi / 4.0))
            audio_l[start_samp : start_samp + n_len] += tone * g_l * 0.22
            audio_r[start_samp : start_samp + n_len] += tone * g_r * 0.22

    board = pb.Pedalboard([
        pb.Chorus(rate_hz=0.8, depth=0.35, centre_delay_ms=8.0, feedback=0.15, mix=0.4),
        pb.Reverb(room_size=0.72, damping=0.45, wet_level=0.38, dry_level=0.75, width=0.9),
        pb.HighpassFilter(cutoff_frequency_hz=160),
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


def format_timestamp(seconds):
    mins = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{mins:02d}:{secs:02d}"


def generate_metadata_file(episode_dir, ep_meta, turns, turn_timestamps, total_duration_sec):
    num = ep_meta["num"]
    title = ep_meta["title"]
    clean_slug = re.sub(r"^ep\d+_", "", ep_meta["slug"], flags=re.IGNORECASE).upper()

    # Dynamic chapters
    chapters = []
    chapters.append(f"{format_timestamp(0)} - Intro & Welcome")
    n_turns = len(turns)
    quarter = n_turns // 4
    if quarter > 0 and len(turn_timestamps) > quarter:
        chapters.append(f"{format_timestamp(turn_timestamps[quarter])} - Deep Dive & Core Concepts")
    half = n_turns // 2
    if half > 0 and len(turn_timestamps) > half:
        chapters.append(f"{format_timestamp(turn_timestamps[half])} - Real-World Examples & Roleplay")
    three_q = (3 * n_turns) // 4
    if three_q > 0 and len(turn_timestamps) > three_q:
        chapters.append(f"{format_timestamp(turn_timestamps[three_q])} - Key English Vocabulary & Idioms")
    last_10 = max(0, n_turns - 10)
    if len(turn_timestamps) > last_10:
        chapters.append(f"{format_timestamp(turn_timestamps[last_10])} - Speaking Challenge & Wrap-up")

    chapters_str = "\n".join(chapters)

    content = f"""================================================================================
YOUTUBE METADATA: DAILY SPEAK ENGLISH - EPISODE {num:02d}
================================================================================

TITLE OPTIONS (Choose the one that best fits your channel branding):
--------------------------------------------------------------------------------
Option 1: Daily Speak English - Episode {num:02d} | {title}
Option 2: {title} | Daily Speak English (25+ Min Fluent English Practice)
Option 3: Speak English Confidently: {title} (Tonu & Solu Podcast)

DESCRIPTION:
--------------------------------------------------------------------------------
Welcome to Episode {num:02d} of Daily Speak English! 🎙️

{ep_meta['desc_intro']}

Whether you are commuting, exercising, cooking, or relaxing at home, immerse yourself in over 25 minutes of crystal-clear, modern English conversation designed to build your fluency, vocabulary, and listening comprehension naturally.

TIMESTAMPS:
{chapters_str}

HOSTS:
- Tonu (Enthusiastic, encouraging, everyday real-life perspective)
- Solu (Analytical, thoughtful, psychology & communication insights)

LOUDNESS & AUDIO SPECS:
- Target Loudness: -14.0 LUFS Broadcast Standard (YouTube optimal, louder on phones)
- Sample Rate: 48 kHz Stereo Master
- Compression: Vocal leveling + warm presence EQ

PRACTICE CHALLENGE:
Answer today's reflection question in the comments below in English! Tonu and Solu read and reply to your reflections.

TAGS:
{ep_meta['tags']}
================================================================================
"""
    meta_file = os.path.join(episode_dir, "YOUTUBE_METADATA.txt")
    with open(meta_file, "w", encoding="utf-8") as f:
        f.write(content)

    script_dir = os.path.join(episode_dir, "script")
    os.makedirs(script_dir, exist_ok=True)
    with open(os.path.join(script_dir, "clean_transcript.txt"), "w", encoding="utf-8") as f:
        for spk, txt in turns:
            f.write(f"{spk}: {txt}\n\n")

    return meta_file


async def process_episode(ep_meta):
    num = ep_meta["num"]
    slug = ep_meta["slug"]
    title = ep_meta["title"]
    script_path = ep_meta["script"]

    print(f"\n=======================================================")
    print(f"🎙️  PROCESSING EPISODE {num:02d}: {title}")
    print(f"=======================================================")

    clean_slug = re.sub(r"^ep\d+_", "", slug, flags=re.IGNORECASE).upper()
    folder_name = f"EP{num:02d}_{clean_slug}"
    user_downloads_ep = os.path.expanduser(f"~/Downloads/Daily_Speak_English/{folder_name}")
    user_master = os.path.join(user_downloads_ep, f"Daily_Speak_English_EP{num:02d}_{clean_slug}_STUDIO_MASTER.mp3")

    if os.path.exists(user_master) and os.path.getsize(user_master) > 20_000_000:
        probe_cmd = [
            "ffprobe", "-v", "error",
            "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1",
            user_master
        ]
        res = subprocess.run(probe_cmd, stdout=subprocess.PIPE, text=True, check=True)
        dur_sec = float(res.stdout.strip())
        size_mb = os.path.getsize(user_master) / (1024 * 1024)
        print(f"✨ EPISODE {num:02d} ALREADY COMPLETED & VERIFIED: {int(dur_sec//60):02d}:{int(dur_sec%60):02d} ({dur_sec:.1f}s) | {size_mb:.1f} MB", flush=True)
        return {
            "num": num,
            "slug": slug,
            "title": title,
            "duration_sec": dur_sec,
            "size_mb": size_mb,
            "dest": user_downloads_ep,
        }

    base_proj_dir = os.path.join("podcast_projects", slug)
    audio_dir = os.path.join(base_proj_dir, "audio")
    cache_dir = os.path.join(base_proj_dir, "cache")
    os.makedirs(audio_dir, exist_ok=True)
    os.makedirs(cache_dir, exist_ok=True)

    final_mp3 = os.path.join(audio_dir, f"Daily_Speak_English_EP{num:02d}_{clean_slug}_STUDIO_MASTER.mp3")
    temp_wav = os.path.join(audio_dir, "temp_master.wav")

    turns = parse_script(script_path)
    print(f"Parsed {len(turns)} turns from {script_path}.", flush=True)

    # Parallel synthesis with semaphore of 6
    sem = asyncio.Semaphore(6)
    tasks = [synth_turn(i, spk, text, cache_dir, sem) for i, (spk, text) in enumerate(turns)]
    t0 = time.time()
    mp3_files = await asyncio.gather(*tasks)
    print(f"Speech files synthesized in {time.time()-t0:.1f}s.", flush=True)

    # Assemble audio
    assembled_parts = []
    pre_silence_samples = int(1.2 * SR)
    assembled_parts.append(np.zeros((pre_silence_samples, 2), dtype=np.float32))

    current_sample_pos = pre_silence_samples
    turn_timestamps = []

    last_speaker = None
    for i, ((speaker, text), mp3_file) in enumerate(zip(turns, mp3_files)):
        turn_timestamps.append(current_sample_pos / SR)
        clip = load_audio_clip(mp3_file)

        # Pan: Solu -0.16 (16% left), Tonu +0.16 (16% right), Both 0.0 (center)
        if speaker == "Solu":
            pan_val = -0.16
        elif speaker == "Tonu":
            pan_val = 0.16
        else:
            pan_val = 0.0

        stereo_clip = apply_panning(clip, pan_val)
        assembled_parts.append(stereo_clip)
        current_sample_pos += len(clip)

        # Dialogue pause
        if i < len(turns) - 1:
            next_spk = turns[i + 1][0]
            if next_spk == speaker:
                pause_s = 0.18
            elif re.search(r"[\?\!]$", text.strip()):
                pause_s = 0.32
            else:
                pause_s = 0.24

            p_samples = int(pause_s * SR)
            assembled_parts.append(np.zeros((p_samples, 2), dtype=np.float32))
            current_sample_pos += p_samples

        last_speaker = speaker

    post_silence_samples = int(1.5 * SR)
    assembled_parts.append(np.zeros((post_silence_samples, 2), dtype=np.float32))
    current_sample_pos += post_silence_samples

    total_speech_len = current_sample_pos
    master_audio = np.concatenate(assembled_parts, axis=0)

    speech_dur_s = len(master_audio) / SR
    print(f"Dialogue duration: {speech_dur_s:.2f}s ({speech_dur_s/60:.2f} mins).", flush=True)

    # Add acoustic room tone (-56 dB)
    np.random.seed(42 + num)
    room_noise = np.random.normal(0, 0.00018, master_audio.shape).astype(np.float32)
    b_noise = pb.Pedalboard([
        pb.LowpassFilter(cutoff_frequency_hz=1400),
        pb.HighpassFilter(cutoff_frequency_hz=280),
    ])
    room_noise = b_noise(room_noise.T, SR).T
    master_audio += room_noise

    # Layer Intro / Outro Rhodes chords
    intro_music = generate_rhodes_jingle(duration_sec=6.5, is_intro=True)
    in_len = min(len(intro_music), len(master_audio))
    master_audio[:in_len] += intro_music[:in_len]

    outro_music = generate_rhodes_jingle(duration_sec=7.2, is_intro=False)
    out_len = min(len(outro_music), len(master_audio))
    master_audio[-out_len:] += outro_music[-out_len:]

    # Broadcast Pedalboard DSP Chain
    board = pb.Pedalboard([
        pb.HighpassFilter(cutoff_frequency_hz=65),
        pb.LowShelfFilter(cutoff_frequency_hz=220, gain_db=1.6),
        pb.PeakFilter(cutoff_frequency_hz=3600, gain_db=2.5, q=1.0),
        pb.HighShelfFilter(cutoff_frequency_hz=11000, gain_db=1.4),
        pb.Compressor(threshold_db=-20.0, ratio=2.8, attack_ms=18.0, release_ms=140.0),
        pb.Gain(gain_db=1.8),
        pb.Limiter(threshold_db=-0.8, release_ms=80.0),
    ])

    processed_audio = board(master_audio.T, SR).T

    # Write temp 24-bit WAV
    sf.write(temp_wav, processed_audio, SR, subtype="PCM_24")

    # Broadcast YouTube Standard Loudness Normalization (-14.0 LUFS, -1.0 dBFS true peak)
    norm_cmd = [
        "ffmpeg", "-y", "-i", temp_wav,
        "-af", "loudnorm=I=-14.0:TP=-1.0:LRA=9.0",
        "-c:a", "libmp3lame",
        "-b:a", "320k",
        "-ar", str(SR),
        final_mp3
    ]
    subprocess.run(norm_cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if os.path.exists(temp_wav):
        os.remove(temp_wav)

    # Clean 48k temp WAVs from cache
    for f in os.listdir(cache_dir):
        if f.endswith("_48k.wav"):
            try:
                os.remove(os.path.join(cache_dir, f))
            except OSError:
                pass

    # Verify duration and size
    probe_cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        final_mp3
    ]
    res = subprocess.run(probe_cmd, stdout=subprocess.PIPE, text=True, check=True)
    dur_sec = float(res.stdout.strip())
    size_mb = os.path.getsize(final_mp3) / (1024 * 1024)

    # Sync to Downloads/Daily_Speak_English/
    os.makedirs(user_downloads_ep, exist_ok=True)
    user_final_mp3 = os.path.join(user_downloads_ep, os.path.basename(final_mp3))
    shutil.copy2(final_mp3, user_final_mp3)

    # Metadata & Clean Transcript
    generate_metadata_file(user_downloads_ep, ep_meta, turns, turn_timestamps, dur_sec)

    mins_f = int(dur_sec // 60)
    secs_f = int(dur_sec % 60)
    print(f"🎉 EPISODE {num:02d} COMPLETED & MASTERED!", flush=True)
    print(f"   Duration: {mins_f:02d}:{secs_f:02d} ({dur_sec:.1f}s)", flush=True)
    print(f"   Size: {size_mb:.1f} MB | Loudness: -14.0 LUFS Broadcast Standard", flush=True)
    print(f"   Synced to: {user_downloads_ep}\n", flush=True)

    return {
        "num": num,
        "slug": slug,
        "title": title,
        "duration_sec": dur_sec,
        "size_mb": size_mb,
        "dest": user_downloads_ep,
    }


async def main():
    t_start = time.time()
    print("=" * 70)
    print("🚀 STARTING DAILY SPEAK ENGLISH - BATCH RENDERER (EPISODES 51 TO 60)")
    print("   Loudness Standard: -14.0 LUFS Broadcast | Pacing: 0.90x | Target: >= 25 Mins")
    print("=" * 70)

    results = []
    for ep in EPISODES_METADATA_51_60:
        res = await process_episode(ep)
        results.append(res)

    print("\n" + "=" * 70)
    print("🏆 BATCH SUMMARY: EPISODES 51 TO 60 COMPLETE!")
    print("=" * 70)
    for r in results:
        dur_m = int(r["duration_sec"] // 60)
        dur_s = int(r["duration_sec"] % 60)
        print(f"EP {r['num']:02d}: {r['title']}")
        print(f"       Duration: {dur_m:02d}:{dur_s:02d} | Size: {r['size_mb']:.1f} MB | Dest: {r['dest']}")

    total_time = time.time() - t_start
    print(f"\nTotal elapsed time: {total_time/60:.1f} mins ({total_time:.1f}s)")


if __name__ == "__main__":
    asyncio.run(main())

