#!/usr/bin/env python3
"""
Daily Speak English — Batch Processor for Episodes 11 to 20 (22+ Minutes Each)
=============================================================================
Renders and masters the 10 brand-new episodes (Episodes 11 to 20).

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

import render_all_book_episodes as rabe

EPISODES_METADATA_11_20 = [
    {
        "num": 11,
        "slug": "ep11_food_cooking_culinary_traditions",
        "title": "Food, Cooking & Culinary Traditions",
        "script": "scripts/daily_speak_ep11_full.txt",
        "desc_intro": "In today's 20+ minute culinary episode, Solu and Tonu explore global food traditions, restaurant ordering etiquette, cooking vs baking, street food culture, spices, and the emotional connection to home-cooked meals.",
        "tags": "daily speak english, food english conversation, cooking vocabulary, restaurant english, learn english, speak english naturally, english listening practice, english speaking practice, solu and tonu"
    },
    {
        "num": 12,
        "slug": "ep12_health_fitness_longevity",
        "title": "Health, Fitness & Longevity",
        "script": "scripts/daily_speak_ep12_full.txt",
        "desc_intro": "In today's 20+ minute health and vitality episode, Solu and Tonu discuss functional fitness, strength vs cardio, nasal breathing, thermal stress, Blue Zone habits, and the foundational power of restorative sleep.",
        "tags": "daily speak english, health english conversation, fitness vocabulary, longevity habits, learn english, speak english naturally, english listening practice, english speaking practice, solu and tonu"
    },
    {
        "num": 13,
        "slug": "ep13_time_management_focus_productivity",
        "title": "Time Management, Focus & Productivity",
        "script": "scripts/daily_speak_ep13_full.txt",
        "desc_intro": "In today's 20+ minute productivity episode, Solu and Tonu master the art of deep focus, time blocking, overcoming digital distractions, the Pomodoro technique, Parkinson's law, and Warren Buffett's 5/25 rule.",
        "tags": "daily speak english, time management english, productivity conversation, deep work english, learn english, speak english naturally, english listening practice, english speaking practice, solu and tonu"
    },
    {
        "num": 14,
        "slug": "ep14_culture_traditions_global_festivities",
        "title": "Culture, Traditions & Global Festivities",
        "script": "scripts/daily_speak_ep14_full.txt",
        "desc_intro": "In today's 20+ minute vibrant festive episode, Solu and Tonu celebrate world festivals—from Eid and Diwali to Lunar New Year and Christmas—exploring traditional attire, folk dances, and cultural hospitality etiquette.",
        "tags": "daily speak english, culture english conversation, global festivals, holiday english vocabulary, learn english, speak english naturally, english listening practice, english speaking practice, solu and tonu"
    },
    {
        "num": 15,
        "slug": "ep15_environmental_awareness_sustainable_living",
        "title": "Environmental Awareness & Sustainable Living",
        "script": "scripts/daily_speak_ep15_full.txt",
        "desc_intro": "In today's 20+ minute eco-conscious episode, Solu and Tonu discuss sustainable living, zero-waste principles, renewable clean energy, ocean protection, circular economy, and reconnecting with nature.",
        "tags": "daily speak english, environmental english, sustainability conversation, green living vocabulary, learn english, speak english naturally, english listening practice, english speaking practice, solu and tonu"
    },
    {
        "num": 16,
        "slug": "ep16_public_speaking_storytelling_confidence",
        "title": "Public Speaking, Storytelling & Communication Confidence",
        "script": "scripts/daily_speak_ep16_full.txt",
        "desc_intro": "In today's 20+ minute empowering communication episode, Solu and Tonu unlock public speaking mastery, conquering stage fright, the 4-part storytelling framework, vocal variety, and persuasive rhetoric.",
        "tags": "daily speak english, public speaking english, storytelling conversation, communication skills, learn english, speak english naturally, english listening practice, english speaking practice, solu and tonu"
    },
    {
        "num": 17,
        "slug": "ep17_learning_languages_lifelong_learning",
        "title": "Learning New Languages & Lifelong Learning",
        "script": "scripts/daily_speak_ep17_full.txt",
        "desc_intro": "In today's 20+ minute language acquisition episode, Solu and Tonu reveal polyglot secrets, breaking the intermediate plateau, comprehensible input, active recall, collocations, and overcoming language anxiety.",
        "tags": "daily speak english, language learning english, polyglot tips, english fluency secrets, learn english, speak english naturally, english listening practice, english speaking practice, solu and tonu"
    },
    {
        "num": 18,
        "slug": "ep18_art_music_literature_creativity",
        "title": "Art, Music, Literature & Creativity",
        "script": "scripts/daily_speak_ep18_full.txt",
        "desc_intro": "In today's 20+ minute artistic episode, Solu and Tonu explore creative expression, the healing power of music, reading fiction, Japanese Kintsugi, color psychology, and overcoming the creative resistance.",
        "tags": "daily speak english, art and music english, literature conversation, creative writing english, learn english, speak english naturally, english listening practice, english speaking practice, solu and tonu"
    },
    {
        "num": 19,
        "slug": "ep19_emotional_intelligence_empathy_conflict",
        "title": "Emotional Intelligence, Empathy & Conflict Resolution",
        "script": "scripts/daily_speak_ep19_full.txt",
        "desc_intro": "In today's 20+ minute emotional intelligence episode, Solu and Tonu discuss Daniel Goleman's 5 EQ pillars, nonviolent communication, de-escalating arguments, psychological safety, and the art of setting healthy boundaries.",
        "tags": "daily speak english, emotional intelligence english, empathy conversation, conflict resolution, learn english, speak english naturally, english listening practice, english speaking practice, solu and tonu"
    },
    {
        "num": 20,
        "slug": "ep20_wisdom_philosophy_meaning_of_life",
        "title": "Wisdom, Philosophy & The Meaning of a Good Life",
        "script": "scripts/daily_speak_ep20_full.txt",
        "desc_intro": "In today's 20+ minute grand milestone episode, Solu and Tonu explore Stoic philosophy, Aristotle's Eudaimonia, the 85-year Harvard happiness study, Wabi-Sabi, and celebrate the complete 20-episode journey.",
        "tags": "daily speak english, philosophy english conversation, wisdom vocabulary, stoicism english, learn english, speak english naturally, english listening practice, english speaking practice, solu and tonu"
    }
]

async def main():
    print("=" * 65)
    print("🚀 BATCH PROCESSING EPISODES 11 TO 20 (22+ MINUTES EACH)")
    print("=" * 65)

    start_total = time.time()
    for ep_meta in EPISODES_METADATA_11_20:
        num = ep_meta["num"]
        slug = ep_meta["slug"]
        clean_slug = re.sub(r"^ep\d+_", "", slug, flags=re.IGNORECASE).upper()
        folder_name = f"EP{num:02d}_{clean_slug}"
        user_downloads_ep = os.path.expanduser(f"~/Downloads/Daily_Speak_English/{folder_name}")
        expected_mp3 = os.path.join(user_downloads_ep, f"Daily_Speak_English_EP{num:02d}_{clean_slug}_STUDIO_MASTER.mp3")

        # Skip if already rendered and >= 20 mins
        if os.path.exists(expected_mp3):
            try:
                cmd_p = ["ffprobe", "-i", expected_mp3, "-show_entries", "format=duration", "-v", "quiet", "-of", "csv=p=0"]
                d = float(subprocess.check_output(cmd_p).decode().strip())
                if d >= 1200:
                    print(f"⏩ Episode {num:02d} already completed ({d/60:.2f} mins). Skipping.")
                    continue
            except Exception:
                pass

        # Clear cache for fresh synthesis
        cache_dir = os.path.join("podcast_projects", slug, "cache")
        if os.path.exists(cache_dir):
            shutil.rmtree(cache_dir)
        os.makedirs(cache_dir, exist_ok=True)

        await rabe.process_episode(ep_meta)

    print(f"\n🎉 ALL 10 NEW EPISODES (EP11 TO EP20) RENDERED AND MASTERED in {time.time()-start_total:.1f}s!")

if __name__ == "__main__":
    asyncio.run(main())

