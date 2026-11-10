with open("scripts/generate_episodes_19_20.py", "r") as f:
    code = f.read()

ep19_extra2 = '''    ("Solu", "And what about the practice of 'Emotional Decompression' after a stressful day?"),
    ("Tonu", "Yes! Don't carry workplace conflicts and emotional tension into your family dinner table."),
    ("Solu", "Take ten minutes in your parked car or on your walk home to breathe, shake out physical tension, and mentally transition into home peace."),
    ("Tonu", "Your loved ones deserve the best of you, not the stressed leftovers of your day!"),'''

target_19 = '    ("Tonu", "Protecting your emotional energy is what allows you to show up with genuine love when it truly counts."),'
code = code.replace(target_19, target_19 + "\n" + ep19_extra2)

ep20_extra2 = '''    ("Solu", "And what about the Stoic practice of 'Sympatheia'—the mutual interdependence of everything in the universe?"),
    ("Tonu", "Marcus Aurelius reminded himself daily: 'We are made for cooperation, like feet, like hands, like the rows of the upper and lower teeth!'"),
    ("Solu", "To act against one another, to be cynical and bitter, is contrary to nature!"),
    ("Tonu", "When you help another human being, you are helping yourself. When you injure another, you are injuring yourself."),
    ("Solu", "Compassion and unity are the highest expressions of human wisdom."),
    ("Tonu", "Live gently, love generously, and walk with humility on this earth."),'''

target_20 = '    ("Solu", "Every laugh with your family, every evening walk, every cup of tea with an old friend is a once-in-a-lifetime experience."),'
code = code.replace(target_20, target_20 + "\n" + ep20_extra2)

with open("scripts/generate_episodes_19_20.py", "w") as f:
    f.write(code)

