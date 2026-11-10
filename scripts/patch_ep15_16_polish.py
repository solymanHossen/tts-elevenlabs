with open("scripts/generate_episodes_14_15_16.py", "r") as f:
    code = f.read()

ep15_extra = '''    ("Solu", "Let's also talk about protecting vital pollinators like honeybees, bumblebees, and butterflies!"),
    ("Tonu", "Yes! One out of every three bites of food we eat depends directly on bee pollination—including almonds, apples, berries, and coffee!"),
    ("Solu", "Pesticide use and loss of wild flower meadows have devastated global pollinator populations."),
    ("Tonu", "We can help by planting native wildflowers on our balconies and gardens, leaving patches of lawn uncut, and avoiding toxic chemical insecticides!"),
    ("Solu", "And what about community Tool Libraries?"),
    ("Tonu", "The average household electric drill is used for a total of only thirteen minutes in its entire lifespan!"),
    ("Solu", "Instead of every neighbor buying their own expensive power tools, a community tool library allows everyone to borrow drills, ladders, and lawnmowers for free!"),
    ("Tonu", "It saves money, reduces industrial manufacturing demand, and connects neighbors with trust."),'''

target_15 = '    ("Solu", "Planting a single pot of sweet basil, mint, or cherry tomatoes on a sunny windowsill connects you with the miracle of life. Plucking fresh basil to put on your homemade pizza is unbeatable!"),'
code = code.replace(target_15, target_15 + "\n" + ep15_extra)

ep16_extra = '''    ("Solu", "Now let's explore the famous rhetorical 'Rule of Three'!"),
    ("Tonu", "The Rule of Three! Human brains are biologically wired to recognize and remember triads: three words, three sentences, or three ideas!"),
    ("Solu", "Think about history's most famous phrases: 'Veni, vidi, vici—I came, I saw, I conquered!' Or 'Life, liberty, and the pursuit of happiness!'"),
    ("Tonu", "Or 'Blood, sweat, and tears!' When organizing a speech or presentation, structure your arguments into three main pillars! It feels completely balanced and memorable."),
    ("Solu", "And how should speakers eliminate unconscious nervous physical ticks—like pacing aimlessly, clicking a pen, or jingling keys in their pocket?"),
    ("Tonu", "Record a three-minute video of yourself rehearsing on your phone!"),
    ("Solu", "Watching yourself on video can be slightly uncomfortable, but it reveals unconscious physical habits in ten seconds."),
    ("Tonu", "Once you see your nervous habits, you can consciously replace them with grounded, purposeful stance and intentional gestures."),'''

target_16 = '    ("Tonu", "And finally, end with a powerful Call to Action! Tell the audience exactly what one step you want them to take today when they walk out the auditorium doors."),'
code = code.replace(target_16, target_16 + "\n" + ep16_extra)

with open("scripts/generate_episodes_14_15_16.py", "w") as f:
    f.write(code)

