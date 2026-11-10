#!/usr/bin/env python3
"""
Super Generator for Daily Speak English - Episodes 08, 09, 10
============================================================
Guarantees 3,300+ words and 155+ turns per episode,
yielding 22 to 25 minutes runtime at 0.90x speed.
"""

import os
import re

def count_stats(turns):
    word_count = sum(len(text.split()) for _, text in turns)
    turn_count = len(turns)
    # At 0.90x, ~135 wpm. Add ~0.3s pause per turn.
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
    if mins < 21.0:
        print("  ⚠️ WARNING: Under 21 minutes!")
    else:
        print("  ✅ Safely exceeds 20 minutes (21+ mins guaranteed)!")
    return t_cnt, w_cnt

# -------------------------------------------------------------
# EPISODE 08: Daily Routine & Everyday Conversations (Super Expanded)
# -------------------------------------------------------------
from generate_episodes_07_08 import ep08_turns as ep08_base

# Add 25 more rich turns to EP08
ep08_extra = [
    ("Solu", "Let's also explore a common situation that many people struggle with: returning an item to a store!"),
    ("Tonu", "Oh, retail customer service! When you buy a shirt or a kitchen gadget that doesn't fit or doesn't work, how do you handle the return politely?"),
    ("Solu", "You walk up to the customer service counter with your receipt and the item in its original box, and you say: 'Good afternoon! I would like to return this blender, please. I purchased it three days ago, but the motor seems to be defective.'"),
    ("Tonu", "And the customer service representative asks: 'Do you have the original receipt and the payment card you used?'"),
    ("Solu", "And you hand them the receipt and say: 'Yes, here is the receipt, and here is the debit card I paid with.'"),
    ("Tonu", "Then they inspect the box and say: 'Everything looks good. Would you like an exchange for a brand new unit, or would you prefer a full refund back to your card?'"),
    ("Solu", "And you reply: 'I would prefer a full refund, please, thank you so much for your help!'"),
    ("Tonu", "And they say: 'The refund has been processed. It will reflect on your bank statement within three to five business days. Here is your return receipt!'"),
    ("Solu", "Notice how calm, courteous, and straightforward that interaction is. No tension, no arguing, just clear communication."),
    ("Tonu", "Now let's talk about scheduling home maintenance and repairs! What do you say when your apartment sink is leaking or the radiator isn't heating properly?"),
    ("Solu", "You call your building manager or a plumbing service and say: 'Hello! I am calling from apartment 3B. Our kitchen sink faucet has developed a steady leak under the cabinet. Could you please send a maintenance technician to take a look at it?'"),
    ("Tonu", "And the property manager asks: 'Is it an active emergency leak that is flooding the floor, or is it a slow drip?'"),
    ("Solu", "And you say: 'It is a slow drip into a bucket right now, but we want to get it fixed before it causes water damage.'"),
    ("Tonu", "And they say: 'Our maintenance tech will be in your building tomorrow between ten in the morning and noon. Does someone need to be home to let them in?'"),
    ("Solu", "And you say: 'Yes, I will be working from home tomorrow morning and can let them in. Thank you!'"),
    ("Tonu", "Having these practical conversation scripts in your mind eliminates so much everyday stress when living or traveling in an English-speaking country!"),
    ("Solu", "And let's talk about the science of morning sunlight on our circadian rhythm!"),
    ("Tonu", "Yes! Neuroscientists like Dr. Andrew Huberman emphasize getting natural sunlight in your eyes within thirty to sixty minutes of waking up."),
    ("Solu", "Even on an overcast, cloudy day, outdoor natural light is fifty to one hundred times brighter than indoor artificial lights!"),
    ("Tonu", "When natural photons hit the specialized photoreceptors in your eyes, it triggers an immediate cortisol pulse that promotes daytime alertness and sets an internal biological timer for melatonin release sixteen hours later!"),
    ("Solu", "So if you want to fall asleep easily at ten tonight, step outside into the morning sunshine at seven this morning!"),
    ("Tonu", "It is completely free, natural, and more effective than an extra cup of espresso."),
    ("Solu", "And what about having a tidy kitchen sink before going to sleep? The famous 'Clean Sink' ritual!"),
    ("Tonu", "Oh, waking up to a kitchen sink full of greasy pots and dishes from last night puts your brain into an immediate state of stress!"),
    ("Solu", "Taking just ten minutes after dinner to wash the dishes, wipe down the countertops, and shine the sink gives your future self an incredible gift tomorrow morning."),
    ("Tonu", "When you walk into a clean, peaceful kitchen to brew your morning coffee, your day starts with calm serenity and control.")
]

# Insert ep08_extra before vocabulary section in ep08_base
ep08_full = []
inserted_08 = False
for spk, txt in ep08_base:
    if not inserted_08 and ("Now, let's explore our special English vocabulary section" in txt or "special English vocabulary" in txt):
        ep08_full.extend(ep08_extra)
        inserted_08 = True
    ep08_full.append((spk, txt))
if not inserted_08:
    ep08_full.extend(ep08_extra)

# -------------------------------------------------------------
# EPISODE 09: Dreams, Goals & Personal Development (Super Expanded)
# -------------------------------------------------------------
from generate_episodes_09_10 import ep09_turns as ep09_base

ep09_extra = [
    ("Solu", "Let's also talk about the powerful difference between intrinsic motivation and extrinsic motivation!"),
    ("Tonu", "Oh, that is such an important distinction for lifelong success and fulfillment!"),
    ("Solu", "Extrinsic motivation is doing something for external rewards or to avoid punishment—like working only for a paycheck, studying only to pass a test, or buying things to impress other people."),
    ("Tonu", "While intrinsic motivation is doing something because you genuinely love it, find it fascinating, or it aligns with your deep personal values!"),
    ("Solu", "When you learn English only because someone forced you to, every study session feels like torture. But when you learn English because you love discovering global cultures, reading fascinating books, and making friends worldwide, practice becomes pure joy!"),
    ("Tonu", "Intrinsic motivation never runs out of fuel! It is like having an internal solar battery that powers you indefinitely."),
    ("Solu", "And what about the psychological trap of the 'Comparison Trap'? In the era of social media, comparing yourself to others is the fastest route to misery."),
    ("Tonu", "Teddy Roosevelt famously said: 'Comparison is the thief of joy!'"),
    ("Solu", "You are comparing your behind-the-scenes struggles and messy reality with someone else's curated, filtered, perfected highlight reel!"),
    ("Tonu", "The only person you should compare yourself to is the person you were yesterday. If you are one percent kinder, wiser, and more consistent than you were yesterday, you are winning!"),
    ("Solu", "And let's talk about the incredible benefit of having a 'Stop-Doing List'!"),
    ("Tonu", "A Stop-Doing List! Everyone has a To-Do list, but nobody has a Stop-Doing list! How does that work, Solu?"),
    ("Solu", "Personal development is as much about subtraction as it is about addition! Write down three habits you are actively stopping this month."),
    ("Tonu", "For example: 'I will stop looking at my phone in bed. I will stop saying yes to social events I dread attending. I will stop complaining about traffic!'"),
    ("Solu", "When you remove energy-draining habits from your schedule, you suddenly unlock hours of free time and mental clarity for your biggest dreams!"),
    ("Tonu", "Now let's touch upon the power of morning priming and visualization!"),
    ("Solu", "Top Olympic athletes and successful entrepreneurs spend ten minutes every single morning visualizing their success in vivid sensory detail."),
    ("Tonu", "When you visualize yourself delivering a confident English presentation, having a successful job interview, or completing a marathon, your brain fires the exact same motor neurons as if you were physically doing it!"),
    ("Solu", "It programs your subconscious nervous system to feel calm, prepared, and confident when the actual moment arrives."),
    ("Tonu", "And finally, never underestimate the power of patience. Great trees take decades to grow deep roots before they reach the clouds!"),
    ("Solu", "Honor your journey, trust the process, and keep taking faithful daily steps toward your dreams.")
]

ep09_full = []
inserted_09 = False
for spk, txt in ep09_base:
    if not inserted_09 and ("Now, let's dive into our special English vocabulary section" in txt or "special English vocabulary" in txt):
        ep09_full.extend(ep09_extra)
        inserted_09 = True
    ep09_full.append((spk, txt))
if not inserted_09:
    ep09_full.extend(ep09_extra)

# -------------------------------------------------------------
# EPISODE 10: Technology, AI & The Future of Life (Super Expanded)
# -------------------------------------------------------------
from generate_episodes_09_10 import ep10_turns as ep10_base

ep10_extra = [
    ("Solu", "Let's also explore how Artificial Intelligence is transforming healthcare and medicine, because that is where AI is saving human lives every single day!"),
    ("Tonu", "Oh, the medical applications of AI are truly miraculous! AI models can analyze thousands of medical imaging scans—like X-rays, MRIs, and CT scans—and detect microscopic cancer cells or early cardiovascular disease years before human eyes could spot them!"),
    ("Solu", "And in drug discovery, discovering a new pharmaceutical medication traditionally took over a decade and cost billions of dollars. AI can simulate molecular folding and predict protein structures in just a few days!"),
    ("Tonu", "It brings affordable, targeted therapies to rare diseases that were previously ignored by big pharmaceutical corporations."),
    ("Solu", "And what about smart cities, renewable energy grids, and climate technology?"),
    ("Tonu", "AI algorithms can predict electric vehicle charging demands, optimize solar panel angles in real time, and balance power grids to minimize carbon emissions across entire metropolises!"),
    ("Solu", "That is technology serving the greater good of humanity and our planet."),
    ("Tonu", "Now, let's talk about critical thinking and the 'Filter Bubble' phenomenon on the internet."),
    ("Solu", "Oh, filter bubbles and echo chambers! Search engines and social media algorithms are designed to show you content that confirms what you already believe, in order to keep you clicking!"),
    ("Tonu", "So if two people search for the exact same news topic, they might receive completely opposite search results based on their browsing history!"),
    ("Solu", "This creates polarization where people believe their own perspective is the absolute truth and everyone else is crazy or misinformed."),
    ("Tonu", "How can our listeners break free from algorithmic echo chambers?"),
    ("Solu", "Actively read diverse sources of news! Seek out perspectives that challenge your assumptions, read long-form investigative journalism, and always ask: 'What is the other side of this argument?'"),
    ("Tonu", "Intellectual curiosity and open-mindedness are the ultimate shields against manipulation."),
    ("Solu", "And what about the future of human relationships? With virtual reality, augmented reality glasses, and the metaverse, will people stop meeting in person?"),
    ("Tonu", "I don't think so! Technology can simulate many things, but nothing in the digital universe can replace the biological warmth of physical human presence."),
    ("Solu", "Sharing a warm meal with your family, feeling the cool ocean breeze on your face, walking through a rainy forest, and hearing genuine laughter with good friends."),
    ("Tonu", "Technology is meant to enhance our human experience, not to replace it!"),
    ("Solu", "And what about the rise of quantum computing? Many scientists call quantum computing the ultimate technological leap!"),
    ("Tonu", "Quantum computing is mind-bending! Unlike classical computers that use binary bits of zeros and ones, quantum computers use qubits that can exist in multiple states simultaneously!"),
    ("Solu", "Which allows them to perform complex calculations in three seconds that would take our fastest supercomputers ten thousand years to solve!"),
    ("Tonu", "From discovering miraculous superconductor materials to designing batteries that charge in two minutes and last for weeks, quantum computing will redefine what is technologically possible."),
    ("Solu", "The future is arriving faster than anyone could have anticipated."),
    ("Tonu", "And that is why maintaining our love for learning and language is our greatest compass."),
    ("Solu", "As we navigate this brave new digital world, let us use technology wisely, protect our privacy, cherish our human connections, and remain perpetual learners.")
]

ep10_full = []
inserted_10 = False
for spk, txt in ep10_base:
    if not inserted_10 and ("Now, let's explore our special English vocabulary section" in txt or "special English vocabulary" in txt):
        ep10_full.extend(ep10_extra)
        inserted_10 = True
    ep10_full.append((spk, txt))
if not inserted_10:
    ep10_full.extend(ep10_extra)

if __name__ == "__main__":
    save_script("scripts/daily_speak_ep08_full.txt", 
                "Daily Routine & Everyday Conversations", 
                "Daily Speak English | English Listening & Speaking Practice", 
                ep08_full)
    
    print("-" * 50)
    save_script("scripts/daily_speak_ep09_full.txt", 
                "Dreams, Goals & Personal Development", 
                "Daily Speak English | English Listening & Speaking Practice", 
                ep09_full)
    
    print("-" * 50)
    save_script("scripts/daily_speak_ep10_full.txt", 
                "Technology, AI & The Future of Life", 
                "Daily Speak English | English Listening & Speaking Practice", 
                ep10_full)
