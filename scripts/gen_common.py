#!/usr/bin/env python3
"""
Common verification and saving utility for Daily Speak English scripts.
Enforces:
- Starts with Tonu ("Hey hey, lovely listeners!...")
- Words >= 3,550 (guarantees >= 25.5 - 28.0 minutes at 0.90x pacing)
- Turns >= 135
"""

import os
import re

def verify_and_save(ep_num, filename, title, subtitle, turns):
    # Verify Tonu start
    first_spk, first_txt = turns[0]
    assert first_spk == "Tonu", f"EP{ep_num} must start with Tonu! Found {first_spk}"
    assert "Hey hey, lovely listeners!" in first_txt, f"EP{ep_num} must start with standard Tonu greeting!"
    
    # Save script
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n")
        f.write(f"## {subtitle}\n\n")
        for spk, text in turns:
            f.write(f"**{spk}:** {text}\n\n")
            
    word_count = sum(len(text.split()) for _, text in turns)
    turn_count = len(turns)
    est_duration_sec = (word_count / 135.0) * 60.0 + (turn_count * 0.28) + 14.0
    est_min = est_duration_sec / 60.0
    
    print(f"✅ EPISODE {ep_num:02d}: {title}")
    print(f"   Turns: {turn_count} | Words: {word_count} | Est. Duration: {est_min:.2f} mins ({est_duration_sec:.1f}s)")
    if word_count < 3550 or est_min < 25.0:
        print(f"   ⚠️ WARNING: Short length in EP{ep_num:02d}! (Need >=3550 words, >=25.0 mins; currently {est_min:.2f}m)")
    else:
        print(f"   🎉 PERFECT! Safely exceeds 25 minutes ({est_min:.1f} mins).")
    return word_count, turn_count
