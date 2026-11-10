with open("scripts/generate_episodes_07_08.py", "r") as f:
    code = f.read()

target_07 = '    ("Solu", "Spend at least thirty minutes a day upskilling: reading industry publications, taking online courses, and networking with peers."),'
add_07 = '''    ("Solu", "Spend at least thirty minutes a day upskilling: reading industry publications, taking online courses, and networking with peers."),
    ("Tonu", "And find a professional mentor! Having a mentor who has already walked the path you are on can save you years of trial and error."),
    ("Solu", "How do you approach a potential mentor respectfully?"),
    ("Tonu", "Ask for a twenty-minute virtual coffee chat to ask about a specific challenge they solved, rather than broadly asking 'Will you be my mentor?' People are eager to share specific wisdom when asked thoughtfully!"),'''

code = code.replace(target_07, add_07)

target_08 = '    ("Solu", "Switch to warm bedside lamps, drink a cup of chamomile tea, read a physical book, or have a relaxed chat with your partner or family."),'
add_08 = '''    ("Solu", "Switch to warm bedside lamps, drink a cup of chamomile tea, read a physical book, or have a relaxed chat with your partner or family."),
    ("Tonu", "And buy a simple, traditional alarm clock for your bedroom instead of using your smartphone!"),
    ("Solu", "That is such a genius life hack! If your phone is charging in the kitchen or living room overnight, you eliminate the temptation of late-night scrolling and morning screen addiction instantly."),
    ("Tonu", "You sleep so much deeper when your bedroom is a sacred tech-free sanctuary!"),'''

code = code.replace(target_08, add_08)

with open("scripts/generate_episodes_07_08.py", "w") as f:
    f.write(code)

