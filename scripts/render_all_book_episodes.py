#!/usr/bin/env python3
"""
Daily Speak English — Batch Processor for Episodes 03 to 10 (20+ Minutes Each)
=============================================================================
Renders and masters all remaining episodes from the 10-Episode Script Book.

Specifications:
- Speed: 0.90x (rate="-10%" native neural prosody)
- Solu: Male (en-US-AndrewNeural)
- Tonu: Female (en-US-AvaNeural)
- Stereo soundstaging: Solu Left 16%, Tonu Right 16%
- Subtle Rhodes jingle intro/outro
- Studio room acoustic presence (-56 dB)
- Pedalboard DSP vocal mastering chain
- EBU R128 loudness normalization (-16.0 LUFS, 48kHz, 320kbps MP3)
- YouTube Title, Description with exact Timestamps, and SEO Tags
- Output to podcast_projects/ and synced to ~/Downloads/Daily_Speak_English/
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
RATE = "-10%"  # 0.90x Speed
VOICE_SOLU = "en-US-AndrewNeural"
VOICE_TONU = "en-US-AvaNeural"
FALLBACK_SOLU = "en-US-BrianNeural"
FALLBACK_TONU = "en-US-EmmaNeural"

EPISODES_METADATA = [
    {
        "num": 3,
        "slug": "ep03_money_success_financial_freedom",
        "title": "Money, Success & Financial Freedom",
        "script": "scripts/daily_speak_ep03_full.txt",
        "desc_intro": "In today's 20+ minute conversation practice episode, Solu and Tonu dive deep into money habits, budgeting, saving regularly, building an emergency fund, managing debt, delayed gratification, and defining true personal success.",
        "tags": "daily speak english, money english conversation, learn english, financial freedom, saving money vocabulary, speak english naturally, english listening practice, english speaking practice, solu and tonu"
    },
    {
        "num": 4,
        "slug": "ep04_travel_adventure_exploring_world",
        "title": "Travel, Adventure & Exploring the World",
        "script": "scripts/daily_speak_ep04_full.txt",
        "desc_intro": "In today's 20+ minute conversation practice episode, Solu and Tonu pack their bags to explore the world, discussing cultural discovery, airport communication, overcoming jet lag, travel safety, and sustainable travel.",
        "tags": "daily speak english, travel english conversation, learn english, airport english, travel vocabulary, speak english naturally, english listening practice, english speaking practice, solu and tonu"
    },
    {
        "num": 5,
        "slug": "ep05_stress_mental_wellbeing_happiness",
        "title": "Stress, Mental Well-Being & Happiness",
        "script": "scripts/daily_speak_ep05_full.txt",
        "desc_intro": "In today's 20+ minute thoughtful episode, Solu and Tonu discuss managing everyday stress, box breathing, evening brain dumping, digital sabbaths, forest bathing, and finding genuine mental peace.",
        "tags": "daily speak english, mental health english, stress management english, learn english, speak english naturally, english listening practice, english speaking practice, solu and tonu"
    },
    {
        "num": 6,
        "slug": "ep06_family_friendship_social_life",
        "title": "Family, Friendship & Social Life",
        "script": "scripts/daily_speak_ep06_full.txt",
        "desc_intro": "In today's 20+ minute heartwarming conversation, Solu and Tonu talk about nurturing family bonds, building lifelong friendships, active listening, the five love languages, and dinner party etiquette.",
        "tags": "daily speak english, family and friends english, friendship conversation, learn english, social english, speak english naturally, english listening practice, english speaking practice, solu and tonu"
    },
    {
        "num": 7,
        "slug": "ep07_career_job_interviews_workplace_english",
        "title": "Career, Job Interviews & Workplace English",
        "script": "scripts/daily_speak_ep07_full.txt",
        "desc_intro": "In today's 20+ minute career-focused episode, Solu and Tonu discuss preparing for job interviews with the STAR method, salary negotiations, elevator pitches, email etiquette, and workplace collaboration.",
        "tags": "daily speak english, job interview english, workplace english, business english, career conversation, learn english, speak english naturally, english listening practice, english speaking practice, solu and tonu"
    },
    {
        "num": 8,
        "slug": "ep08_daily_routine_everyday_conversations",
        "title": "Daily Routine & Everyday Conversations",
        "script": "scripts/daily_speak_ep08_full.txt",
        "desc_intro": "In today's 20+ minute practical episode, Solu and Tonu practice everyday English conversations about morning rituals, coffee shop orders, postal errands, transit chats, and evening wind-downs.",
        "tags": "daily speak english, daily routine english, everyday english conversation, learn english, daily english speaking, speak english naturally, english listening practice, english speaking practice, solu and tonu"
    },
    {
        "num": 9,
        "slug": "ep09_dreams_goals_personal_development",
        "title": "Dreams, Goals & Personal Development",
        "script": "scripts/daily_speak_ep09_full.txt",
        "desc_intro": "In today's 20+ minute motivational episode, Solu and Tonu discuss chasing big ambitions, the growth mindset, overcoming procrastination with the 5-second rule, the 20-mile march, and Ikigai.",
        "tags": "daily speak english, dreams and goals english, personal development, motivation english, learn english, speak english naturally, english listening practice, english speaking practice, solu and tonu"
    },
    {
        "num": 10,
        "slug": "ep10_technology_ai_future_of_life",
        "title": "Technology, AI & The Future of Life",
        "script": "scripts/daily_speak_ep10_full.txt",
        "desc_intro": "In today's 20+ minute grand season finale, Solu and Tonu explore artificial intelligence, on-device models, cybersecurity, space exploration, deepfakes, and the irreplaceable power of the human touch.",
        "tags": "daily speak english, technology and ai english, artificial intelligence english conversation, future of life, learn english, speak english naturally, english listening practice, english speaking practice, solu and tonu"
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
        return (s * env).astype(np.float32)

    if not is_outro:
        # Cmaj9 -> Fmaj7
        chords = [
            (0.0, [261.63, 329.63, 392.00, 493.88, 587.33], 2.8),
            (2.2, [174.61, 261.63, 329.63, 392.00, 523.25], 3.8),
        ]
        master_gain = -14.0
    else:
        # Fmaj7 -> Gsus4 -> Cadd9
        chords = [
            (0.0, [174.61, 261.63, 329.63, 392.00, 523.25], 2.5),
            (2.0, [196.00, 261.63, 293.66, 392.00, 587.33], 2.5),
            (4.2, [130.81, 261.63, 329.63, 392.00, 587.33, 659.25], 4.5),
        ]
        master_gain = -12.0

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


def generate_youtube_assets(episode_dir, ep_meta, turns, chapters):
    yt_dir = os.path.join(episode_dir, "youtube")
    os.makedirs(yt_dir, exist_ok=True)
    meta_file = os.path.join(yt_dir, "YOUTUBE_METADATA.txt")

    chapters_text = "\n".join([f"{ts} - {title}" for ts, title in chapters])

    # Extract expressions mentioned in dialogue
    text_blob = "\n".join(t for _, t in turns)
    raw_exprs = re.findall(r"[\'\"‘“]([^\'\"’“”]+)[\'\"’”]\s+means\s+([^.\n]+)", text_blob)
    if raw_exprs:
        expr_list = [f"{i+1}. \"{e.strip()}\" - {m.strip()}." for i, (e, m) in enumerate(raw_exprs)]
        expr_section = "\n".join(expr_list)
    else:
        expr_section = "Refer to the audio for all detailed everyday English expressions and idioms explained by Solu and Tonu!"

    # Extract challenge question
    challenge_match = re.search(r"(?:weekly reflection question|question of the day)[^:]*:\s*([^?]+\?)", text_blob, re.IGNORECASE)
    challenge_q = challenge_match.group(1).strip() if challenge_match else f"How do you apply the concepts of {ep_meta['title']} to your personal life?"

    title = ep_meta["title"]
    num = ep_meta["num"]
    desc_intro = ep_meta["desc_intro"]
    tags = ep_meta["tags"]

    content = f"""================================================================================
📺 YOUTUBE VIDEO TITLE OPTIONS (Choose one)
================================================================================
Option 1 (Recommended):
Daily Speak English | Ep {num}: {title} | Full English Conversation Practice (0.90x Speed)

Option 2 (Search / SEO Optimized):
Learn English Through Conversation: {title} | Daily Speak English Ep {num}

Option 3 (Catchy / Click-Worthy):
Improve Your English Speaking & Listening! Ep {num}: {title} (Solu & Tonu)

================================================================================
📝 YOUTUBE VIDEO DESCRIPTION (Copy and paste directly)
================================================================================
Welcome to Episode {num} of Daily Speak English! 🎙️

{desc_intro}

In this episode, Solu and Tonu speak at a calm, natural 0.90x pace—designed specifically to help intermediate and upper-beginner learners improve their English listening comprehension, expand everyday vocabulary, and master natural sentence flow.

⏱️ TIMESTAMPS / CHAPTERS:
{chapters_text}

✨ KEY EVERYDAY ENGLISH EXPRESSIONS COVERED:
{expr_section}

🎯 TODAY'S SPEAKING CHALLENGE:
"{challenge_q}"
Leave your answer in the comments below in English! Solu and Tonu read and reply to your comments! 💬

💡 HOW TO GET THE MOST OUT OF THIS EPISODE:
1. Listen once without reading to test your comprehension.
2. Listen a second time and repeat the phrases out loud during the Speaking Practice section.
3. Write down 2 new expressions from today's episode and use them in your own sentences.

👍 Like this video if you learned something new today.
📤 Share this with a friend who is learning English!

#DailySpeakEnglish #LearnEnglish #EnglishConversation #EnglishSpeakingPractice #EnglishListeningPractice #SpeakEnglish #{title.replace(' ', '').replace('&', 'And').replace(',', '')}

================================================================================
🏷️ YOUTUBE SEO TAGS (Copy and paste into the Tags box)
================================================================================
{tags}
"""

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
    
    base_proj_dir = os.path.join("podcast_projects", slug)
    audio_dir = os.path.join(base_proj_dir, "audio")
    cache_dir = os.path.join(base_proj_dir, "cache")
    os.makedirs(audio_dir, exist_ok=True)
    os.makedirs(cache_dir, exist_ok=True)

    final_mp3 = os.path.join(audio_dir, f"Daily_Speak_English_EP{num:02d}_{clean_slug}_STUDIO_MASTER.mp3")
    temp_wav = os.path.join(audio_dir, "temp_master.wav")

    turns = parse_script(script_path)
    print(f"Parsed {len(turns)} turns from {script_path}.")

    # Parallel synthesis with semaphore of 6
    sem = asyncio.Semaphore(6)
    tasks = [synth_turn(i, spk, text, cache_dir, sem) for i, (spk, text) in enumerate(turns)]
    t0 = time.time()
    mp3_files = await asyncio.gather(*tasks)
    print(f"Speech files synthesized in {time.time()-t0:.1f}s.")

    # Assemble audio
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

    # Generate dynamic chapters
    chapters = [("00:00", f"Introduction: {title}")]
    added_concepts = False
    added_scenarios = False
    added_vocab = False
    added_speaking = False
    added_wrap = False

    for idx, (spk, text) in enumerate(turns):
        if idx == 0:
            continue
        ts_sec = int(turn_timestamps[idx])
        ts_str = f"{ts_sec//60:02d}:{ts_sec%60:02d}"
        t_low = text.lower()

        if not added_concepts and idx >= int(len(turns) * 0.20):
            chapters.append((ts_str, "Deep Dive & Core Concepts"))
            added_concepts = True
        elif not added_scenarios and idx >= int(len(turns) * 0.45):
            chapters.append((ts_str, "Everyday Scenarios & Real Insights"))
            added_scenarios = True
        elif not added_vocab and ("vocabulary section" in t_low or "first expression" in t_low or "useful everyday" in t_low):
            chapters.append((ts_str, "Key Everyday English Expressions"))
            added_vocab = True
        elif not added_speaking and ("speaking practice" in t_low or "sentence number one" in t_low):
            chapters.append((ts_str, "Interactive Speaking Challenge"))
            added_speaking = True
        elif not added_wrap and (idx >= len(turns) - 5 or "reflection question" in t_low or "grand finale" in t_low or "until next time" in t_low):
            chapters.append((ts_str, "Key Takeaways & Wrap Up"))
            added_wrap = True

    # Jingle & room tone
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

    # Studio room tone
    np.random.seed(42 + num)
    noise = np.random.normal(0, 0.0005, size=(total_len, 2)).astype(np.float32)
    air_board = pb.Pedalboard([
        pb.LowpassFilter(cutoff_frequency_hz=1200),
        pb.HighpassFilter(cutoff_frequency_hz=100),
    ])
    room_tone = air_board(noise.T, SR).T
    master_mix += room_tone

    # DSP Mastering
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

    # EBU R128 encode
    cmd_loudnorm = [
        "ffmpeg", "-y",
        "-i", temp_wav,
        "-af", "loudnorm=I=-16:TP=-1.0:LRA=10",
        "-ar", "48000",
        "-b:a", "320k",
        "-id3v2_version", "3",
        "-metadata", f"title=Daily Speak English: Ep {num} — {title} (0.90x)",
        "-metadata", "artist=Solu (Male) & Tonu (Female)",
        "-metadata", "album=Daily Speak English",
        "-metadata", "genre=Podcast / Education",
        final_mp3,
    ]
    subprocess.run(cmd_loudnorm, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if os.path.exists(temp_wav):
        os.remove(temp_wav)

    # Generate metadata
    yt_meta_path = generate_youtube_assets(base_proj_dir, ep_meta, turns, chapters)

    # Sync to Downloads
    user_downloads_ep = os.path.expanduser(f"~/Downloads/Daily_Speak_English/{folder_name}")
    os.makedirs(user_downloads_ep, exist_ok=True)
    shutil.copy2(final_mp3, user_downloads_ep)
    shutil.copy2(yt_meta_path, user_downloads_ep)
    clean_script_file = os.path.join(base_proj_dir, "script", "clean_transcript.txt")
    if os.path.exists(clean_script_file):
        shutil.copy2(clean_script_file, user_downloads_ep)

    # Check ffprobe final duration
    cmd_probe = ["ffprobe", "-i", final_mp3, "-show_entries", "format=duration", "-v", "quiet", "-of", "csv=p=0"]
    probe_out = subprocess.check_output(cmd_probe).decode().strip()
    final_dur = float(probe_out)
    mins = int(final_dur // 60)
    secs = int(final_dur % 60)

    print(f"✅ Finished Episode {num:02d}: {title}")
    print(f"   Duration: {mins:02d}:{secs:02d} ({final_dur:.2f}s) {'[>= 20 mins!]' if final_dur >= 1200 else '[WARNING: < 20 mins]'}")
    print(f"   Audio Master: {final_mp3}")
    print(f"   Synced to: {user_downloads_ep}")


async def main():
    start_total = time.time()
    for ep_meta in EPISODES_METADATA:
        num = ep_meta["num"]
        slug = ep_meta["slug"]
        clean_slug = re.sub(r"^ep\d+_", "", slug, flags=re.IGNORECASE).upper()
        folder_name = f"EP{num:02d}_{clean_slug}"
        user_downloads_ep = os.path.expanduser(f"~/Downloads/Daily_Speak_English/{folder_name}")
        expected_mp3 = os.path.join(user_downloads_ep, f"Daily_Speak_English_EP{num:02d}_{clean_slug}_STUDIO_MASTER.mp3")
        if os.path.exists(expected_mp3):
            try:
                cmd_p = ["ffprobe", "-i", expected_mp3, "-show_entries", "format=duration", "-v", "quiet", "-of", "csv=p=0"]
                d = float(subprocess.check_output(cmd_p).decode().strip())
                if d >= 1200:
                    print(f"⏩ Episode {num:02d} already completed ({d/60:.2f} mins). Skipping.")
                    continue
            except Exception:
                pass
        await process_episode(ep_meta)

    print(f"\n🎉 ALL REMAINING EPISODES RENDERED AND MASTERED SUCCESSFULLY in {time.time()-start_total:.1f}s!")


if __name__ == "__main__":
    asyncio.run(main())
