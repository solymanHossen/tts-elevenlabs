#!/usr/bin/env python3
"""
Daily Speak English — Dedicated Batch Processor for Episodes 31 to 40 (25+ Minutes Each)
========================================================================================
Renders and masters Episodes 31 to 40 with LOUDER, PUNCHIER BROADCAST AUDIO:
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

EPISODES_METADATA_31_40 = [
    {
        "num": 31,
        "slug": "ep31_first_impressions_body_language_secrets",
        "title": "The Psychology of First Impressions & Body Language Secrets",
        "script": "scripts/daily_speak_ep31_full.txt",
        "desc_intro": "In today's 25+ minute communication episode, Tonu and Solu decode the psychology of first impressions, the 7-second rule, micro-expressions, posture, power posing, and nonverbal secrets that build instant trust and rapport.",
        "tags": "daily speak english, body language english, first impressions conversation, psychology vocabulary, learn english, speak english naturally, english listening practice, english speaking practice, tonu and solu"
    },
    {
        "num": 32,
        "slug": "ep32_digital_nomad_remote_work_freedom",
        "title": "Digital Nomadism & The Reality of Working From Anywhere",
        "script": "scripts/daily_speak_ep32_full.txt",
        "desc_intro": "In today's 25+ minute lifestyle episode, Tonu and Solu dive into the reality of digital nomadism, remote work freedom, managing loneliness, visa logistics, financial discipline, and staying productive across time zones.",
        "tags": "daily speak english, digital nomad english, remote work conversation, work from anywhere vocabulary, learn english, speak english naturally, english listening practice, english speaking practice, tonu and solu"
    },
    {
        "num": 33,
        "slug": "ep33_mindful_eating_gut_health_food",
        "title": "Mindful Eating, Gut Health & Food Psychology",
        "script": "scripts/daily_speak_ep33_full.txt",
        "desc_intro": "In today's 25+ minute wellness episode, Tonu and Solu explore the gut-brain axis, mindful eating practices, emotional cravings, the Japanese concept of Hara Hachi Bu, and how nourishing your body heals your mind.",
        "tags": "daily speak english, mindful eating english, gut health conversation, food psychology vocabulary, learn english, speak english naturally, english listening practice, english speaking practice, tonu and solu"
    },
    {
        "num": 34,
        "slug": "ep34_difficult_conversations_setting_boundaries",
        "title": "Mastering Difficult Conversations & Setting Firm Boundaries",
        "script": "scripts/daily_speak_ep34_full.txt",
        "desc_intro": "In today's 25+ minute communication episode, Tonu and Solu share master strategies for navigating difficult conversations, setting firm boundaries, Nonviolent Communication (NVC), de-escalating anger, and the Broken Record technique.",
        "tags": "daily speak english, difficult conversations english, setting boundaries conversation, communication vocabulary, learn english, speak english naturally, english listening practice, english speaking practice, tonu and solu"
    },
    {
        "num": 35,
        "slug": "ep35_sleep_architecture_dreams_deep_rest",
        "title": "Sleep Architecture, Dreams & The Neuroscience of Rest",
        "script": "scripts/daily_speak_ep35_full.txt",
        "desc_intro": "In today's 25+ minute neuroscience episode, Tonu and Solu explore sleep architecture, why dreaming heals emotions, the glymphatic brain wash, adenosine and caffeine traps, the 3-2-1 rule, and creating a world-class sleep sanctuary.",
        "tags": "daily speak english, sleep science english, dreams and neuroscience, sleep hygiene conversation, learn english, speak english naturally, english listening practice, english speaking practice, tonu and solu"
    },
    {
        "num": 36,
        "slug": "ep36_power_of_introverts_quiet_strength",
        "title": "The Power of Introverts in an Extroverted World",
        "script": "scripts/daily_speak_ep36_full.txt",
        "desc_intro": "In today's 25+ minute personality episode, Tonu and Solu celebrate the quiet strength and superpowers of introverts, Susan Cain's Quiet revolution, deep listening, managing your social battery, and thriving in noisy environments.",
        "tags": "daily speak english, introvert power english, quiet strength conversation, personality vocabulary, learn english, speak english naturally, english listening practice, english speaking practice, tonu and solu"
    },
    {
        "num": 37,
        "slug": "ep37_overcoming_imposter_syndrome_confidence",
        "title": "Overcoming Imposter Syndrome & Unlocking Quiet Confidence",
        "script": "scripts/daily_speak_ep37_full.txt",
        "desc_intro": "In today's 25+ minute self-mastery episode, Tonu and Solu unpack Imposter Syndrome, the 5 imposter archetypes, Dunning-Kruger contrast, the Evidence Portfolio, shifting to service, and unlocking quiet, unshakeable confidence.",
        "tags": "daily speak english, imposter syndrome english, quiet confidence conversation, self belief vocabulary, learn english, speak english naturally, english listening practice, english speaking practice, tonu and solu"
    },
    {
        "num": 38,
        "slug": "ep38_minimalism_decluttering_simple_living",
        "title": "Minimalism, Clutter-Free Living & Decluttering Your Life",
        "script": "scripts/daily_speak_ep38_full.txt",
        "desc_intro": "In today's 25+ minute intentional living episode, Tonu and Solu investigate the psychology of decluttering, visual clutter and cortisol, the Diderot Effect, Swedish Death Cleaning, digital minimalism, and the liberating 90/90 rule.",
        "tags": "daily speak english, minimalism english, decluttering conversation, simple living vocabulary, learn english, speak english naturally, english listening practice, english speaking practice, tonu and solu"
    },
    {
        "num": 39,
        "slug": "ep39_art_of_travel_slow_vs_tourist",
        "title": "The Art of Travel: Slow Travel vs Tourist Checklists",
        "script": "scripts/daily_speak_ep39_full.txt",
        "desc_intro": "In today's 25+ minute travel episode, Tonu and Solu contrast frantic tourist checklists with the soulful beauty of slow travel, the art of the Flâneur, solo travel self-discovery, culinary immersion, and traveling light.",
        "tags": "daily speak english, slow travel english, travel conversation, adventure vocabulary, learn english, speak english naturally, english listening practice, english speaking practice, tonu and solu"
    },
    {
        "num": 40,
        "slug": "ep40_curiosity_questioning_beginners_mind",
        "title": "Curiosity, Lifelong Questioning & The Beginner's Mind",
        "script": "scripts/daily_speak_ep40_full.txt",
        "desc_intro": "In today's 25+ minute milestone fortieth episode, Tonu and Solu celebrate lifelong curiosity, the Zen concept of Shoshin (Beginner's Mind), Feynman's intellectual honesty, the Socratic method, and staying perpetually young at heart.",
        "tags": "daily speak english, curiosity english, beginners mind conversation, lifelong learning vocabulary, learn english, speak english naturally, english listening practice, english speaking practice, tonu and solu"
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
    if os.path.exists(target_mp3) and os.path.getsize(target_mp3) <= 1000:
        try:
            os.remove(target_mp3)
        except OSError:
            pass

    async with sem:
        for attempt in range(5):
            try:
                voice = VOICE_SOLU if speaker == "Solu" else VOICE_TONU
                if attempt >= 2:
                    voice = FALLBACK_SOLU if speaker == "Solu" else FALLBACK_TONU

                if speaker in ("Solu", "Tonu"):
                    c = edge_tts.Communicate(text, voice, rate=RATE)
                    await asyncio.wait_for(c.save(target_mp3), timeout=25.0)
                elif speaker == "Both":
                    f_solu = os.path.join(cache_dir, f"turn_{idx:03d}_Both_solu.mp3")
                    f_tonu = os.path.join(cache_dir, f"turn_{idx:03d}_Both_tonu.mp3")
                    c1 = edge_tts.Communicate(text, VOICE_SOLU, rate=RATE)
                    await asyncio.wait_for(c1.save(f_solu), timeout=25.0)
                    c2 = edge_tts.Communicate(text, VOICE_TONU, rate=RATE)
                    await asyncio.wait_for(c2.save(f_tonu), timeout=25.0)
                    cmd = [
                        "ffmpeg", "-y",
                        "-i", f_solu,
                        "-i", f_tonu,
                        "-filter_complex", "amix=inputs=2:duration=longest:weights=1.0 1.0",
                        target_mp3,
                    ]
                    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                if os.path.exists(target_mp3) and os.path.getsize(target_mp3) > 1000:
                    return target_mp3
            except Exception as e:
                if os.path.exists(target_mp3) and os.path.getsize(target_mp3) <= 1000:
                    try:
                        os.remove(target_mp3)
                    except OSError:
                        pass
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
        master_gain = -13.0
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

    text_blob = "\n".join(t for _, t in turns)
    raw_exprs = re.findall(r"[\'\"‘“]([^\'\"’“”]+)[\'\"’”]\s+(?:means|is\s+a\s+|refers\s+to|means\s+to)\s+([^.\n]+)", text_blob)
    if raw_exprs:
        expr_list = [f"{i+1}. \"{e.strip()}\" - {m.strip()}." for i, (e, m) in enumerate(raw_exprs[:6])]
        expr_section = "\n".join(expr_list)
    else:
        expr_section = "Refer to the audio for all detailed everyday English expressions and idioms explained by Tonu and Solu!"

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
Improve Your English Speaking & Listening! Ep {num}: {title} (Tonu & Solu)

================================================================================
📝 YOUTUBE VIDEO DESCRIPTION (Copy and paste directly)
================================================================================
Welcome to Episode {num} of Daily Speak English! 🎙️

{desc_intro}

In this episode, Tonu and Solu speak at a calm, natural 0.90x pace—designed specifically to help intermediate and upper-beginner learners improve their English listening comprehension, expand everyday vocabulary, and master natural sentence flow.

⏱️ TIMESTAMPS / CHAPTERS:
{chapters_text}

✨ KEY EVERYDAY ENGLISH EXPRESSIONS COVERED:
{expr_section}

🎯 TODAY'S SPEAKING CHALLENGE:
"{challenge_q}"
Leave your answer in the comments below in English! Tonu and Solu read and reply to your comments! 💬

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
    print(f"Dialogue duration: {dialogue_duration:.2f}s ({dialogue_duration/60:.2f} mins).", flush=True)

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
        elif not added_vocab and ("vocabulary section" in t_low or "first expression" in t_low or "useful everyday" in t_low or "first idiom" in t_low or "signature vocabulary" in t_low or "signature segment" in t_low or "key everyday" in t_low):
            chapters.append((ts_str, "Key Everyday English Expressions"))
            added_vocab = True
        elif not added_speaking and ("speaking practice" in t_low or "sentence number one" in t_low or "interactive speaking" in t_low):
            chapters.append((ts_str, "Interactive Speaking Challenge"))
            added_speaking = True
        elif not added_wrap and (idx >= len(turns) - 5 or "reflection question" in t_low or "weekly reflection" in t_low or "until next time" in t_low):
            chapters.append((ts_str, "Key Takeaways & Wrap Up"))
            added_wrap = True

    # Rhodes Jingle & Room Presence
    intro_music = create_rhodes_jingle(duration=6.0, is_outro=False)
    outro_music = create_rhodes_jingle(duration=8.0, is_outro=True)

    outro_padding = int(4.0 * SR)
    total_len = len(dialogue_track) + outro_padding
    master_mix = np.zeros((total_len, 2), dtype=np.float32)
    master_mix[: len(dialogue_track)] += dialogue_track

    # Intro music ducking
    intro_vol = np.ones(len(intro_music), dtype=np.float32) * 0.35
    duck_start = int(1.0 * SR)
    duck_end = int(4.5 * SR)
    for s in range(duck_start, min(duck_end, len(intro_music))):
        alpha = (s - duck_start) / (duck_end - duck_start)
        intro_vol[s] = (1.0 - alpha) * 0.35
    if len(intro_music) > duck_end:
        intro_vol[duck_end:] = 0.0
    master_mix[: len(intro_music)] += intro_music * intro_vol[:, None]

    # Outro music
    outro_start = max(0, len(dialogue_track) - int(4.5 * SR))
    outro_end = min(total_len, outro_start + len(outro_music))
    actual_outro_len = outro_end - outro_start

    outro_vol = np.ones(actual_outro_len, dtype=np.float32)
    fade_in_samples = int(3.0 * SR)
    for s in range(min(fade_in_samples, actual_outro_len)):
        outro_vol[s] = (s / fade_in_samples) * 0.65
    fade_out_samples = int(2.5 * SR)
    for s in range(actual_outro_len - fade_out_samples, actual_outro_len):
        if s >= 0:
            alpha = (actual_outro_len - s) / fade_out_samples
            outro_vol[s] *= alpha

    master_mix[outro_start:outro_end] += outro_music[:actual_outro_len] * outro_vol[:, None]

    # Studio room tone
    np.random.seed(42 + num)
    noise = np.random.normal(0, 0.0006, size=(total_len, 2)).astype(np.float32)
    air_board = pb.Pedalboard([
        pb.LowpassFilter(cutoff_frequency_hz=1200),
        pb.HighpassFilter(cutoff_frequency_hz=100),
    ])
    room_tone = air_board(noise.T, SR).T
    master_mix += room_tone

    # LOUDER ENHANCED DSP MASTERING CHAIN
    mastering_chain = pb.Pedalboard([
        pb.HighpassFilter(cutoff_frequency_hz=75),
        pb.LowShelfFilter(cutoff_frequency_hz=220, gain_db=1.6), # warm chest resonance
        pb.PeakFilter(cutoff_frequency_hz=3600, gain_db=2.5, q=0.85), # vocal presence & crisp consonants
        pb.HighShelfFilter(cutoff_frequency_hz=11000, gain_db=1.4), # air & sparkle
        pb.Compressor(threshold_db=-20.0, ratio=2.8, attack_ms=12.0, release_ms=100.0), # tight vocal leveling
        pb.Gain(gain_db=1.8), # makeup gain
        pb.Limiter(threshold_db=-0.8), # transparent brickwall limiter
    ])
    mastered = mastering_chain(master_mix.T, SR).T
    sf.write(temp_wav, mastered, SR, subtype="PCM_24")

    # LOUDER EBU R128 NORMALIZATION TARGET: -14.0 LUFS (YouTube Standard)
    cmd_loudnorm = [
        "ffmpeg", "-y",
        "-i", temp_wav,
        "-af", "loudnorm=I=-14:TP=-1.0:LRA=7",
        "-ar", "48000",
        "-b:a", "320k",
        "-id3v2_version", "3",
        "-metadata", f"title=Daily Speak English: Ep {num} — {title} (0.90x)",
        "-metadata", "artist=Tonu (Female) & Solu (Male)",
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

    clean_tx = os.path.join(base_proj_dir, "script", "clean_transcript.txt")
    if os.path.exists(clean_tx):
        shutil.copy2(clean_tx, user_downloads_ep)

    # Read verified duration
    probe_cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        final_mp3
    ]
    res = subprocess.run(probe_cmd, stdout=subprocess.PIPE, text=True, check=True)
    dur_sec = float(res.stdout.strip())
    size_mb = os.path.getsize(final_mp3) / (1024 * 1024)

    print(f"🎉 EPISODE {num:02d} COMPLETED & MASTERED!")
    print(f"   Duration: {int(dur_sec//60):02d}:{int(dur_sec%60):02d} ({dur_sec:.1f}s)")
    print(f"   Size: {size_mb:.1f} MB | Loudness: -14.0 LUFS Broadcast Standard")
    print(f"   Synced to: {user_downloads_ep}\n")
    return {
        "num": num,
        "slug": slug,
        "title": title,
        "duration_sec": dur_sec,
        "size_mb": size_mb,
        "dest": user_downloads_ep,
    }


async def main():
    print("================================================================================")
    print("🚀 BATCH PROCESSING EPISODES 31 TO 40 (25+ MINUTES EACH | -14.0 LUFS)")
    print("================================================================================")

    start_all = time.time()
    results = []
    for ep in EPISODES_METADATA_31_40:
        res = await process_episode(ep)
        results.append(res)

    total_time = time.time() - start_all
    print("\n================================================================================")
    print(f"✅ BATCH 1 (EP31-EP40) COMPLETED IN {total_time/60:.1f} MINUTES!")
    print("================================================================================")
    for r in results:
        m = int(r['duration_sec'] // 60)
        s = int(r['duration_sec'] % 60)
        print(f"EP{r['num']:02d}: {r['title'][:45]:<45} | {m:02d}:{s:02d} | {r['size_mb']:.1f}MB")


if __name__ == "__main__":
    asyncio.run(main())
