with open("scripts/generate_episodes_17_18.py", "r") as f:
    code = f.read()

ep17_block5 = '''    ("Solu", "And what about the testing effect or 'Active Recall' in study sessions?"),
    ("Tonu", "Active recall! Re-reading a textbook passively creates the illusion of competence. Testing yourself—closing the book and trying to remember the phrase—builds deep neural pathways!"),
    ("Solu", "And always celebrate your unique cultural voice! Having a slight accent when speaking English simply proves that you were brave enough to learn a second language!"),
    ("Tonu", "An accent is a badge of honor, courage, and cultural heritage."),'''

target_17 = '    ("Tonu", "People around the world are remarkably kind and supportive when they see someone making a sincere effort to speak their language."),'
code = code.replace(target_17, target_17 + "\n" + ep17_block5)

ep18_block5 = '''    ("Solu", "And what about the sanctuary of independent local bookstores and historic public libraries?"),
    ("Tonu", "Oh, local bookstores! The aroma of printing ink and aged paper, quiet wooden floorboards, and the thrill of serendipitous discovery!"),
    ("Solu", "You walk in without an algorithm telling you what to buy, browse the shelves, pick up a book by a poet from a century ago, and discover a soulmate across time."),
    ("Tonu", "Public libraries are democratic temples of knowledge where everyone, rich or poor, has equal access to all human wisdom."),
    ("Solu", "And throughout history, in times of war, plague, and hardship, it was art, music, and poetry that sustained the human spirit and gave people hope to rebuild tomorrow."),
    ("Tonu", "Art reminds us who we are when the world feels dark."),'''

target_18 = '    ("Tonu", "Winston Churchill famously said: \'We shape our buildings; thereafter, our buildings shape us!\'"),'
code = code.replace(target_18, target_18 + "\n" + ep18_block5)

with open("scripts/generate_episodes_17_18.py", "w") as f:
    f.write(code)

