with open("scripts/generate_episodes_09_10.py", "r") as f:
    code = f.read()

# Additions to EP09
target_09 = '    ("Solu", "Whatever your English or career goal is, commit to your daily twenty-mile march. Practice for fifteen or twenty minutes every single day, rain or shine!"),'
add_09 = '''    ("Solu", "Whatever your English or career goal is, commit to your daily twenty-mile march. Practice for fifteen or twenty minutes every single day, rain or shine!"),
    ("Tonu", "Now, let's talk about the Japanese philosophy of Ikigai: finding your purpose and reason for being!"),
    ("Solu", "Oh, Ikigai! It translates beautifully to 'the reason you wake up in the morning.'"),
    ("Tonu", "Ikigai is found at the intersection of four circles: What you love, what you are good at, what the world needs, and what you can be paid for!"),
    ("Solu", "When those four circles overlap, work ceases to feel like a tedious grind and transforms into meaningful, fulfilling service."),
    ("Tonu", "And you don't have to find your complete Ikigai overnight! It reveals itself gradually as you try new projects, explore hobbies, and follow your curiosity."),
    ("Solu", "And consider creating your own 'Personal Board of Advisors'!"),
    ("Tonu", "Just like a successful corporation has a board of directors, you can have three or four trusted mentors—one for career guidance, one for financial wisdom, and one for emotional well-being."),
    ("Solu", "Whenever you face a major life crossroads, consult your personal board. Their combined perspective prevents blind spots and impulsive decisions."),'''

code = code.replace(target_09, add_09)

# Additions to EP10
target_10 = '    ("Tonu", "Use technology to bring you closer to human beings in the real physical world, not to isolate you from them."),'
add_10 = '''    ("Tonu", "Use technology to bring you closer to human beings in the real physical world, not to isolate you from them."),
    ("Solu", "Let's also discuss the ethics of intellectual property and AI training data."),
    ("Tonu", "Yes! Modern AI models are trained on millions of articles, books, paintings, and songs created by talented human authors and artists."),
    ("Solu", "It is so important that creators receive proper credit, consent, and fair compensation for their life's work!"),
    ("Tonu", "Without human culture and human creativity, AI would have nothing to learn from in the first place! Respecting original human creators is vital for a thriving creative future."),
    ("Solu", "And what about space exploration? How does AI help humanity reach the cosmos?"),
    ("Tonu", "Space telescopes like the James Webb Space Telescope use AI to process petabytes of cosmic data, identifying distant exoplanets and mapping galaxies from billions of years ago!"),
    ("Solu", "And autonomous rovers exploring the surface of Mars use computer vision to navigate rocks and craters, because radio signals from Earth take up to twenty minutes to arrive!"),
    ("Tonu", "And what new careers will emerge in the future, Solu?"),
    ("Solu", "Just as the internet created jobs like web designers, app developers, and cloud architects that didn't exist thirty years ago, the future will bring AI ethics directors, prompt engineers, and human-machine collaboration consultants!"),
    ("Tonu", "The future is full of limitless possibility for those who stay adaptable, curious, and eager to learn."),'''

code = code.replace(target_10, add_10)

with open("scripts/generate_episodes_09_10.py", "w") as f:
    f.write(code)

