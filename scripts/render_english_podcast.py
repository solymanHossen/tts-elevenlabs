#!/usr/bin/env python3
"""
Studio Podcast Master Renderer (Solu = Male, Tonu = Female, 0.85x Speed)
========================================================================
Synthesizes and masters "English with Solu & Tonu: Love, Relationships & Understanding Each Other"
into a world-class broadcast-quality podcast episode.

Configuration:
- Solu: Male (en-US-AndrewNeural)
- Tonu: Female (en-US-AvaNeural)
- Speed: 0.85x (rate="-15%" native neural prosody)
- Intro music: Quiet, subtle Rhodes background (lower volume as requested)
- Pacing: Adaptive natural turn-taking dynamics
- Soundstaging: Stereo pan (Solu: -0.16 Left, Tonu: +0.16 Right, Both: Unison stereo)
- DSP Mastering: Sub-bass highpass, warm proximity shelf, presence peak, opto compression
- Loudness: EBU R128 -16.0 LUFS, -1.0 dB True Peak, 48kHz 320kbps MP3
"""

import asyncio
import os
import re
import subprocess
import time
import numpy as np
import soundfile as sf
import pedalboard as pb
import edge_tts

SR = 48000
VOICE_SOLU = "en-US-AndrewNeural"      # Solu = Male (sele)
VOICE_TONU = "en-US-AvaNeural"         # Tonu = Female (meye)
FALLBACK_SOLU = "en-US-BrianNeural"
FALLBACK_TONU = "en-US-EmmaNeural"
RATE = "-10%"                          # 0.90x speed
CACHE_DIR = "outputs/podcast_cache_m_solu_f_tonu_90x"
MASTER_WAV = "outputs/english_podcast_solu_tonu_90x_TEMP.wav"
FINAL_MP3 = "outputs/english_podcast_solu_tonu_90x_STUDIO_MASTER.mp3"

os.makedirs(CACHE_DIR, exist_ok=True)
os.makedirs("outputs", exist_ok=True)


def parse_script(raw_file="scripts/podcast_script_raw.txt"):
    with open(raw_file, "r", encoding="utf-8") as f:
        text = f.read()

    # Clean wrapper tags and metadata
    text = re.sub(r"<\/?USER_REQUEST>", "", text)
    text = re.sub(r"<ADDITIONAL_METADATA>[\s\S]*", "", text)

    lines = text.split("\n")
    turns = []
    current_speaker = None
    current_text = []

    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        m = re.match(r"^\*\*(Solu|Tonu|Both)\:\*\*\s*(.*)$", line)
        if m:
            if current_speaker:
                cleaned = " ".join(current_text).strip()
                cleaned = re.sub(r"\/\/.*$", "", cleaned).strip()
                # Clean emojis
                cleaned = re.sub(r"[\U00010000-\U0010ffff\u2600-\u27bf]", "", cleaned).strip()
                turns.append((current_speaker, cleaned))
                current_text = []
            current_speaker = m.group(1)
            if m.group(2).strip():
                current_text.append(m.group(2).strip())
        elif current_speaker:
            current_text.append(line)

    if current_speaker and current_text:
        cleaned = " ".join(current_text).strip()
        cleaned = re.sub(r"\/\/.*$", "", cleaned).strip()
        cleaned = re.sub(r"[\U00010000-\U0010ffff\u2600-\u27bf]", "", cleaned).strip()
        turns.append((current_speaker, cleaned))

    return turns


async def synth_turn(idx, speaker, text, sem):
    target_mp3 = os.path.join(CACHE_DIR, f"turn_{idx:03d}_{speaker}.mp3")
    if os.path.exists(target_mp3) and os.path.getsize(target_mp3) > 1000:
        return target_mp3

    async with sem:
        for attempt in range(5):
            try:
                voice = VOICE_SOLU if speaker == "Solu" else VOICE_TONU
                if attempt >= 2:
                    voice = FALLBACK_SOLU if speaker == "Solu" else FALLBACK_TONU
                
                if speaker == "Solu" or speaker == "Tonu":
                    c = edge_tts.Communicate(text, voice, rate=RATE)
                    await c.save(target_mp3)
                elif speaker == "Both":
                    f_solu = os.path.join(CACHE_DIR, f"turn_{idx:03d}_Both_solu.mp3")
                    f_tonu = os.path.join(CACHE_DIR, f"turn_{idx:03d}_Both_tonu.mp3")
                    c1 = edge_tts.Communicate(text, VOICE_SOLU, rate=RATE)
                    await c1.save(f_solu)
                    c2 = edge_tts.Communicate(text, VOICE_TONU, rate=RATE)
                    await c2.save(f_tonu)
                    cmd = [
                        "ffmpeg", "-y",
                        "-i", f_solu,
                        "-i", f_tonu,
                        "-filter_complex", "amix=inputs=2:duration=longest:weights=1.0 1.0",
                        target_mp3
                    ]
                    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                return target_mp3
            except Exception as e:
                if attempt == 4:
                    raise RuntimeError(f"Failed to synth turn {idx} [{speaker}]: {e}")
                await asyncio.sleep(1.0 * (attempt + 1))


def create_rhodes_jingle(duration=6.5, is_outro=False):
    """Synthesize warm neo-soul Rhodes electric piano jingle."""
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
        # Intro progression: quiet and subtle bed
        chords = [
            (0.0, [174.61, 220.00, 261.63, 329.63, 392.00]),
            (1.4, [146.83, 220.00, 261.63, 329.63, 349.23]),
            (2.8, [196.00, 233.08, 293.66, 349.23, 440.00]),
            (4.2, [130.81, 196.00, 261.63, 329.63, 392.00, 523.25]),
        ]
        master_gain = -16.0  # Very quiet, subtle intro bed as requested
    else:
        # Outro progression: warm resolution
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
    return processed.T  # (n_samples, 2)


def load_audio_clip(path):
    """Load audio file and resample to 48kHz mono float32."""
    wav_path = path.replace(".mp3", "_48k.wav")
    if not os.path.exists(wav_path) or os.path.getsize(wav_path) < 1000:
        subprocess.run(
            ["ffmpeg", "-y", "-i", path, "-ar", str(SR), "-ac", "1", wav_path],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    data, sr = sf.read(wav_path, dtype="float32")
    if len(data.shape) > 1:
        data = data[:, 0]
    return data


def apply_panning(mono_clip, pan_val):
    """
    Constant power stereo panning:
    pan_val in [-1.0 (hard left), 1.0 (hard right)]
    0.0 is dead center.
    """
    angle = (pan_val + 1.0) * (np.pi / 4.0)
    left_gain = np.cos(angle)
    right_gain = np.sin(angle)
    return np.column_stack([mono_clip * left_gain, mono_clip * right_gain])


def get_dialogue_pause(prev_text, current_text):
    """Compute adaptive conversational turn-taking pause for 0.85x speech."""
    c_lower = current_text.lower().strip()
    p_lower = prev_text.lower().strip() if prev_text else ""

    quick_starters = (
        "exactly", "i agree", "that's so true", "wow", "oh,", "oh ",
        "right", "yes", "absolutely", "beautifully said", "definitely"
    )
    if any(c_lower.startswith(q) for q in quick_starters):
        return 0.22

    if p_lower.endswith("?"):
        return 0.30

    return 0.32


async def main():
    print("=== Step 1: Parsing dialogue script ===")
    turns = parse_script()
    print(f"Parsed {len(turns)} dialogue turns.")
    print(f"Solu: {VOICE_SOLU} (Male), Tonu: {VOICE_TONU} (Female), Speed: {RATE} (0.85x)")

    print("\n=== Step 2: Parallel Neural Synthesis (0.85x Speed) ===")
    sem = asyncio.Semaphore(6)
    tasks = [synth_turn(i, spk, text, sem) for i, (spk, text) in enumerate(turns)]
    t0 = time.time()
    mp3_files = await asyncio.gather(*tasks)
    print(f"All {len(mp3_files)} speech files ready in {time.time()-t0:.1f}s.")

    print("\n=== Step 3: Studio Soundstaging & Dialogue Assembly ===")
    assembled_parts = []
    
    # 1.2s subtle pre-speech intro head
    pre_silence_samples = int(1.2 * SR)
    assembled_parts.append(np.zeros((pre_silence_samples, 2), dtype=np.float32))

    for i, (spk, text) in enumerate(turns):
        clip_mono = load_audio_clip(mp3_files[i])
        
        # Panning: Solu (Male) left, Tonu (Female) right
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

        assembled_parts.append(clip_stereo)

    dialogue_track = np.concatenate(assembled_parts, axis=0)
    dialogue_duration = len(dialogue_track) / SR
    print(f"Total speech dialogue duration: {dialogue_duration:.2f}s ({dialogue_duration/60:.2f} mins).")

    print("\n=== Step 4: Generating & Mixing Musical Jingles (Subtle Level) ===")
    intro_music = create_rhodes_jingle(duration=6.0, is_outro=False)
    outro_music = create_rhodes_jingle(duration=8.0, is_outro=True)

    outro_padding = int(4.0 * SR)
    total_len = len(dialogue_track) + outro_padding
    master_mix = np.zeros((total_len, 2), dtype=np.float32)

    master_mix[: len(dialogue_track)] += dialogue_track

    # Subtle Intro: quiet bed, ducks out cleanly as Solu starts speaking
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

    print("\n=== Step 5: Adding Studio Room Tone (Acoustic Warmth) ===")
    np.random.seed(42)
    noise = np.random.normal(0, 0.0005, size=(total_len, 2)).astype(np.float32)
    air_board = pb.Pedalboard([
        pb.LowpassFilter(cutoff_frequency_hz=1200),
        pb.HighpassFilter(cutoff_frequency_hz=100),
    ])
    room_tone = air_board(noise.T, SR).T
    master_mix += room_tone

    print("\n=== Step 6: Mastering Chain (Pedalboard DSP) ===")
    mastering_chain = pb.Pedalboard([
        pb.HighpassFilter(cutoff_frequency_hz=75),
        pb.LowShelfFilter(cutoff_frequency_hz=220, gain_db=1.2),
        pb.PeakFilter(cutoff_frequency_hz=3600, gain_db=1.8, q=0.9),
        pb.HighShelfFilter(cutoff_frequency_hz=11000, gain_db=1.0),
        pb.Compressor(threshold_db=-18.0, ratio=2.5, attack_ms=15.0, release_ms=120.0),
        pb.Limiter(threshold_db=-1.0),
    ])

    print("Applying DSP mastering...")
    mastered = mastering_chain(master_mix.T, SR).T

    print(f"Writing raw master WAV: {MASTER_WAV}")
    sf.write(MASTER_WAV, mastered, SR, subtype="PCM_24")

    print("\n=== Step 7: Final EBU R128 Broadcast Normalization & MP3 Encode ===")
    cmd_loudnorm = [
        "ffmpeg", "-y",
        "-i", MASTER_WAV,
        "-af", "loudnorm=I=-16:TP=-1.0:LRA=10",
        "-ar", "48000",
        "-b:a", "320k",
        "-id3v2_version", "3",
        "-metadata", "title=English with Solu & Tonu: Love, Relationships & Understanding Each Other (0.90x)",
        "-metadata", "artist=Solu (Male) & Tonu (Female)",
        "-metadata", "album=English with Solu & Tonu Podcast",
        "-metadata", "genre=Podcast / Education",
        "-metadata", "comment=Mastered at 0.90x Speed with Solu as Male and Tonu as Female",
        FINAL_MP3
    ]
    subprocess.run(cmd_loudnorm, check=True)
    print(f"\n🎉 Successfully created: {FINAL_MP3}")

    cmd_stat = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration,size,bit_rate",
        "-of", "default=noprint_wrappers=1",
        FINAL_MP3
    ]
    stat = subprocess.check_output(cmd_stat, text=True)
    print("Final MP3 Info:\n" + stat)

    if os.path.exists(MASTER_WAV):
        os.remove(MASTER_WAV)


if __name__ == "__main__":
    asyncio.run(main())
