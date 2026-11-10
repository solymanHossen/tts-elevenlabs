with open("scripts/generate_episodes_19_20.py", "r") as f:
    code = f.read()

ep19_super_block = '''    ("Solu", "Now let's explore Harvard professor Amy Edmondson's concept of 'Psychological Safety'!"),
    ("Tonu", "Oh, psychological safety! Google conducted a massive multi-year study called Project Aristotle to discover what makes the highest-performing teams in the world."),
    ("Solu", "And they thought the top teams would have the most PhDs, the biggest budgets, or the highest individual IQs!"),
    ("Tonu", "And what did they discover instead, Solu?"),
    ("Solu", "Psychological safety was by far the number one predictor of team success! The belief that you will not be punished, humiliated, or mocked for speaking up with an idea, question, concern, or mistake!"),
    ("Tonu", "When team members feel psychologically safe, innovation explodes because people are not terrified of making a mistake."),
    ("Solu", "And what about the crucial distinction between Intent and Impact in interpersonal communication?"),
    ("Tonu", "We judge ourselves by our good intentions, but other people judge us by the impact of our actions!"),
    ("Solu", "So if you say something that unintentionally hurts a friend or colleague, don't defensively shout: 'That's not what I meant!'"),
    ("Tonu", "Acknowledge the impact first: 'I hear that my words hurt you, and I am deeply sorry for that impact. My intention was not to cause pain, but I take full responsibility for how it landed.'"),
    ("Solu", "And have you heard of 'Rejection Therapy' by entrepreneur Jia Jiang?"),
    ("Tonu", "Rejection therapy! Jia Jiang spent one hundred days intentionally seeking out daily rejections—asking strangers for crazy favors, asking a burger joint for a 'burger refill'—to desensitize his nervous system to the word 'No'!"),
    ("Solu", "And he discovered that rejection is not fatal! In fact, when you ask with warmth, people say yes to the most surprising things!"),
    ("Tonu", "Desensitizing your fear of rejection liberates your social confidence forever."),'''

target_19 = '    ("Solu", "Clear, objective, professional, and zero personal attacks!"),'
code = code.replace(target_19, target_19 + "\n" + ep19_super_block)

ep20_super_block = '''    ("Solu", "Now let's explore the Japanese philosophy of 'Wabi-Sabi'!"),
    ("Tonu", "Oh, Wabi-Sabi! The ancient aesthetic centered on the acceptance of transience and imperfection!"),
    ("Solu", "Wabi-Sabi finds exquisite beauty in things that are imperfect, impermanent, and incomplete: an weathered wooden table, an asymmetric clay bowl, autumn leaves decaying on stone pathways."),
    ("Tonu", "In a modern world obsessed with sterile, airbrushed perfection, Wabi-Sabi is a deep breath of relief! It reminds us that our human lives, our bodies, and our relationships do not need to be flawless to be magnificent."),
    ("Solu", "And what about the ancient Stoic meditation of 'Negative Visualization'—Premeditatio Malorum?"),
    ("Tonu", "Negative visualization! Once a week, take five minutes to imagine losing the things you currently take for granted: imagine your phone breaking, your eyesight failing, or losing your home!"),
    ("Solu", "And then you open your eyes and realize: 'I have my eyesight! I have my warm bed! I have my family!'"),
    ("Tonu", "It completely cures hedonic adaptation and floods your heart with fierce, overwhelming gratitude for your ordinary daily life right now!"),
    ("Solu", "And let's reflect on Viktor Frankl's immortal masterpiece: Man's Search for Meaning!"),
    ("Tonu", "Frankl survived the horrors of Auschwitz by discovering that humans can endure almost any 'how' if they have a 'why'!"),
    ("Solu", "He wrote that everything can be taken from a man but one thing: the last of human freedoms—to choose one's attitude in any given set of circumstances, to choose one's own way!"),
    ("Tonu", "When we cannot change a painful situation, we are challenged to change ourselves."),'''

target_20 = '    ("Tonu", "Virtue is an art of daily balance, discernment, and moderation."),'
code = code.replace(target_20, target_20 + "\n" + ep20_super_block)

with open("scripts/generate_episodes_19_20.py", "w") as f:
    f.write(code)

