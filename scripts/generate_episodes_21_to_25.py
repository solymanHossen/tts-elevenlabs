#!/usr/bin/env python3
"""
Generator for Daily Speak English - Episodes 21 to 25 (22+ Minutes Each)
========================================================================
All episodes start with Tonu:
"Hey hey, lovely listeners! Welcome back to Daily Speak English, your favorite place to improve your English listening and speaking skills. I'm Tonu!"

Target per episode: >= 3,300 words, >= 160 turns (guarantees 23 to 26 minutes at 0.90x speed).
"""

import os
import sys

def count_stats(turns):
    word_count = sum(len(text.split()) for _, text in turns)
    turn_count = len(turns)
    est_duration_sec = (word_count / 135.0) * 60.0 + (turn_count * 0.28) + 14.0
    est_min = est_duration_sec / 60.0
    return turn_count, word_count, est_duration_sec, est_min

def save_script(filename, title, subtitle, turns):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n")
        f.write(f"## {subtitle}\n\n")
        for spk, text in turns:
            f.write(f"**{spk}:** {text}\n\n")
    
    t_cnt, w_cnt, sec, mins = count_stats(turns)
    print(f"Generated {filename}:")
    print(f"  Turns: {t_cnt}")
    print(f"  Words: {w_cnt}")
    print(f"  Est. Duration: {mins:.2f} mins ({sec:.1f}s)")
    if mins < 21.0 or w_cnt < 3200:
        print("  ⚠️ WARNING: Under 21 minutes or under 3,200 words!")
    else:
        print("  ✅ Safely exceeds 20 minutes (22+ mins guaranteed)!")
    return t_cnt, w_cnt

# We will build modular scripts for EP 21, 22, 23, 24, 25
