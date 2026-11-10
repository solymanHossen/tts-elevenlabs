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

target_19 = '    ("Tonu", "Clear, objective, professional, and zero personal attacks!"),'
code = code.replace(target_19, target_19 + "\n" + ep19_super_block)

# Add another rich block to EP19 and EP20 to ensure both reach 3,250+ words
ep19_more = '''    ("Solu", "And what about 'Compassion Fatigue' and setting boundaries around emotional dumping?"),
    ("Tonu", "Compassion fatigue is so real! If you are a naturally empathetic person, people will constantly seek you out to dump their drama and emotional burdens on you!"),
    ("Solu", "You cannot be everyone's therapist. Learn to say with loving kindness: 'I love you and want to support you, but right now I don't have the emotional capacity to hold space for this heavy conversation. Can we talk about it tomorrow after I have rested?'"),
    ("Tonu", "Protecting your emotional energy is what allows you to show up with genuine love when it truly counts."),'''

target_19_end = '    ("Solu", "Take that first courageous step toward peace. Kindness is never wasted."),'
code = code.replace(target_19_end, ep19_more + "\n" + target_19_end)

ep20_more = '''    ("Solu", "And let's reflect on the ancient Roman philosophy of 'Amor Fati'—loving whatever happens!"),
    ("Tonu", "Friedrich Nietzsche described Amor Fati as his formula for greatness: that one wants nothing to be different, not forward, not backward, not in all eternity!"),
    ("Solu", "Not merely enduring what is necessary, still less concealing it, but loving it! Every hardship, every heartache, and every triumph was necessary to forge the person you are today."),
    ("Tonu", "Embrace your story with fierce pride and gratitude!"),
    ("Solu", "And what advice would we give to our listeners as they complete this twenty-episode audio journey?"),
    ("Tonu", "Trust yourself! You have everything you need inside you. Keep listening, keep speaking with joy, and never let fear hold you back."),
    ("Solu", "You have made Solu and Tonu so proud, and we know your future is limitless and bright."),'''

target_20_end = '    ("Solu", "It has been the greatest honor and joy to be your audio companions on Daily Speak English."),'
code = code.replace(target_20_end, ep20_more + "\n" + target_20_end)

with open("scripts/generate_episodes_19_20.py", "w") as f:
    f.write(code)

