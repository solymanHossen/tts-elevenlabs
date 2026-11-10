with open("scripts/generate_episodes_03_04.py", "r") as f:
    code = f.read()

target = '    ("Solu", "That brings us right into our special section of the episode! Let\'s explore some very useful everyday English expressions and idioms related to money."),'

addition = '''    ("Tonu", "Let's also talk about the difference between being frugal and being cheap, because people frequently confuse these two concepts!"),
    ("Solu", "Oh, that is such a brilliant distinction, Tonu! Being frugal means being mindful, intentional, and resourceful with your money. You spend generously on things that bring true value and joy, while cutting expenses ruthlessly on things that don't matter to you."),
    ("Tonu", "Exactly! Whereas being cheap means sacrificing quality, fairness, or even your own dignity just to save a couple of pennies!"),
    ("Solu", "Yes! A cheap person might leave an insulting tip at a restaurant, buy flimsy products that break after two uses, or refuse to chip in their fair share when dining with friends."),
    ("Tonu", "Being cheap damages relationships and creates unnecessary misery. Frugality, on the other hand, is about respect for your hard-earned money and long-term peace of mind."),
    ("Solu", "And that leads directly to delayed gratification. The ability to resist the temptation of an immediate reward in order to obtain a much greater reward in the future!"),
    ("Tonu", "Psychologists say delayed gratification is one of the strongest predictors of lifelong financial and personal success."),
    ("Solu", "Instead of buying the newest phone model on launch day, you wait a year or invest that money, and five years later you have a solid investment portfolio."),
    ("Tonu", "It is all about patience and perspective!"),
    ("Solu", "That brings us right into our special section of the episode! Let's explore some very useful everyday English expressions and idioms related to money."),'''

code = code.replace(target, addition)
with open("scripts/generate_episodes_03_04.py", "w") as f:
    f.write(code)

