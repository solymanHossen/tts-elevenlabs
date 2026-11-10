with open("scripts/generate_episodes_19_20.py", "r") as f:
    code = f.read()

ep19_buf = '''    ("Solu", "Now let's examine the difference between Passive, Aggressive, Passive-Aggressive, and Assertive communication!"),
    ("Tonu", "Oh, the four communication styles! Most conflicts stem from passive-aggressive or aggressive behavior."),
    ("Solu", "Passive communicators swallow their needs and say 'Whatever you want is fine', leading to deep internal resentment."),
    ("Tonu", "Aggressive communicators bully and demand: 'It's my way or the highway!'"),
    ("Solu", "Passive-aggressive communicators use sarcasm, silent treatment, and subtle sabotage because they are afraid of direct honesty."),
    ("Tonu", "While Assertive communicators speak with calm honesty: 'Here is what I need, here is my boundary, and I respect your perspective equally.'"),
    ("Solu", "Assertiveness is the golden standard of emotional intelligence!"),'''

target_19 = '    ("Tonu", "Clean, respectful, and zero guilt!"),'
code = code.replace(target_19, target_19 + "\n" + ep19_buf)

ep20_buf = '''    ("Solu", "Now let's explore the Japanese concept of 'Mono no Aware'—the gentle pathos of things!"),
    ("Tonu", "Oh, Mono no Aware! The deep, empathetic awareness of the impermanence of all things in life."),
    ("Solu", "Think about cherry blossoms in spring: cherry blossoms bloom brilliantly for only one short week, and then petals drift gently to the earth."),
    ("Tonu", "If cherry blossoms stayed on the branches made of plastic all year long, nobody would travel across the world to see them!"),
    ("Solu", "It is their very impermanence and fragility that makes them so intensely, heartbreakingly beautiful!"),
    ("Tonu", "And the same is true for human life: our moments are precious precisely because they cannot be repeated."),
    ("Solu", "Every laugh with your family, every evening walk, every cup of tea with an old friend is a once-in-a-lifetime experience."),'''

target_20 = '    ("Tonu", "When we cannot change a painful situation, we are challenged to change ourselves."),'
code = code.replace(target_20, target_20 + "\n" + ep20_buf)

with open("scripts/generate_episodes_19_20.py", "w") as f:
    f.write(code)

