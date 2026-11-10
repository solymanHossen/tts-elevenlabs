#!/usr/bin/env python3
"""
Dedicated Renderer for Episodes 08, 09, 10 (22+ Minutes Each)
============================================================
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

TARGET_EPISODES = [
    ep for ep in rabe.EPISODES_METADATA if ep["num"] in (8, 9, 10)
]

async def main():
    print("=" * 60)
    print("🚀 STARTING RENDERING FOR EPISODES 08, 09, 10 (22+ MINS EACH)")
    print("=" * 60)
    
    t0_total = time.time()
    for ep in TARGET_EPISODES:
        num = ep["num"]
        slug = ep["slug"]
        # Wipe cache to ensure fresh synthesis of all turns
        cache_dir = os.path.join("podcast_projects", slug, "cache")
        if os.path.exists(cache_dir):
            shutil.rmtree(cache_dir)
        os.makedirs(cache_dir, exist_ok=True)
        
        await rabe.process_episode(ep)
        
    print(f"\n🎉 ALL 3 EPISODES (EP08, EP09, EP10) RENDERED SUCCESSFULLY IN {time.time()-t0_total:.1f}s!")

if __name__ == "__main__":
    asyncio.run(main())

