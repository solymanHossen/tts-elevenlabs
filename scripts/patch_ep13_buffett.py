with open("scripts/generate_episodes_11_12_13.py", "r") as f:
    code = f.read()

ep13_buffett = '''    ("Solu", "Now, let's explore Warren Buffett's famous 5/25 Rule for extreme focus!"),
    ("Tonu", "Oh, the 5/25 Rule! How did Warren Buffett teach this to his personal airplane pilot, Solu?"),
    ("Solu", "Buffett told his pilot to write down his top twenty-five career and personal goals on a sheet of paper."),
    ("Tonu", "Then he told him to circle his top five most important goals that meant everything to him."),
    ("Solu", "And the pilot thought: 'Great, I will focus primarily on my top five, and work on the other twenty whenever I have spare time!'"),
    ("Tonu", "And Buffett looked at him sternly and said: 'No! You have misunderstood. The other twenty goals are now your Avoid-At-All-Cost list! They are the secret dream-killers that will distract you from your top five!'"),
    ("Solu", "Because those secondary goals are interesting enough to seduce your attention, but not important enough to change your life!"),
    ("Tonu", "And have you heard of Parkinson's Law?"),
    ("Solu", "Parkinson's Law: 'Work expands to fill the time available for its completion!'"),
    ("Tonu", "If you give yourself two weeks to write a four-page essay, it will take two full weeks of stress. But if you give yourself twenty-four hours, you will finish it in twenty-four hours!"),
    ("Solu", "Setting artificial, aggressive mini-deadlines forces extreme clarity and eliminates unnecessary fluff."),'''

target_13 = '    ("Tonu", "And eighty percent of the time, once you overcome that initial hurdle of starting, you keep going naturally!"),'
code = code.replace(target_13, target_13 + "\n" + ep13_buffett)

with open("scripts/generate_episodes_11_12_13.py", "w") as f:
    f.write(code)

