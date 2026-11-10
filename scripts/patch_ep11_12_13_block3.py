with open("scripts/generate_episodes_11_12_13.py", "r") as f:
    code = f.read()

ep11_block3 = '''    ("Solu", "Let's also talk about kitchen knife safety and essential preparation skills!"),
    ("Tonu", "Oh, knife safety! A famous chef once said: 'A dull knife is far more dangerous than a razor-sharp knife!'"),
    ("Solu", "Why is a dull knife more dangerous, Tonu?"),
    ("Tonu", "Because with a dull knife, you have to press down with excessive force, and the blade slips off slippery tomato skins or onions and cuts your fingers!"),
    ("Solu", "While a sharp knife glides smoothly through food with minimal effort. And always remember the chef's 'claw grip' to protect your fingertips!"),
    ("Tonu", "Curl your guiding fingers inward like a bear claw, with your knuckles resting against the flat of the blade. Your knuckles guide the knife safely without exposing fingertips!"),
    ("Solu", "And what about the magic of making homemade bone broth or vegetable stock from scratch?"),
    ("Tonu", "Never throw away vegetable scraps like carrot peels, celery leaves, and onion skins! Save them in a freezer bag, and at the end of the month, simmer them in a big pot of water with bay leaves and peppercorns for two hours!"),
    ("Solu", "You get rich, aromatic, golden stock packed with nutrients, for practically zero cost!"),
    ("Tonu", "It reduces food waste and elevates every soup, stew, and risotto you cook."),
    ("Solu", "Now, Tonu, let's settle the eternal dessert debate: Are you a sweet person or a savory person?"),
    ("Tonu", "I have an unapologetic sweet tooth! If there is a warm apple pie with a scoop of melting vanilla bean ice cream, or an authentic Italian tiramisu, I cannot say no!"),
    ("Solu", "I appreciate dark chocolate with a hint of sea salt, but I usually prefer savory dishes—a warm cheese board with figs and walnuts!"),
    ("Tonu", "That is the wonderful diversity of human palates; there is room at the culinary table for everyone!"),'''

target_11 = '    ("Solu", "Now, let\'s celebrate street food culture around the world!"),'
code = code.replace(target_11, ep11_block3 + "\n" + target_11)

ep12_block3 = '''    ("Solu", "Let's also discuss posture, desk ergonomics, and the modern epidemic of 'text neck'!"),
    ("Tonu", "Oh, 'text neck'! When we hunch forward looking down at our smartphones, our head tilts forward at a forty-five degree angle!"),
    ("Solu", "And the physics of that tilt puts nearly fifty pounds of extra pressure on our cervical spine and neck muscles!"),
    ("Tonu", "No wonder so many young professionals suffer from chronic tension headaches, tight upper traps, and back pain!"),
    ("Solu", "How can our listeners protect their posture throughout the workday, Tonu?"),
    ("Tonu", "Raise your computer monitor so that the top third of the screen is at eye level! Keep your elbows at ninety degrees, feet flat on the floor, and bring your phone up to eye level instead of craning your neck down."),
    ("Solu", "And what about the restorative power of 'Active Recovery'?"),
    ("Tonu", "Many people think resting from exercise means lying motionless on the sofa all weekend watching television."),
    ("Solu", "While active recovery—like a gentle thirty-minute walk in nature, light foam rolling, or ten minutes of gentle mobility yoga—increases blood flow to repair muscles twice as fast!"),
    ("Tonu", "Movement is lubrication for your joints and nervous system."),
    ("Solu", "And let's touch upon mindful eating: putting your fork down between bites, chewing your food thoroughly, and savoring the textures!"),
    ("Tonu", "When you eat without screens, you enjoy your meal ten times more and naturally stop eating when you are satisfied."),'''

target_12 = '    ("Solu", "Let\'s also talk about the vital difference between nasal breathing and mouth breathing!"),'
code = code.replace(target_12, ep12_block3 + "\n" + target_12)

ep13_block3 = '''    ("Solu", "Now let's explore the Zeigarnik Effect in cognitive psychology!"),
    ("Tonu", "The Zeigarnik Effect, discovered by psychologist Bluma Zeigarnik! Why do unfinished tasks cause so much mental anxiety?"),
    ("Solu", "Our brains naturally obsess over incomplete loops and unfinished projects! If you leave five half-finished tasks lingering in your head, your subconscious keeps pinging you with background stress."),
    ("Tonu", "And the moment you write down a concrete next physical action step on paper, your brain breathes a sigh of relief and lets it go!"),
    ("Solu", "And have you heard of 'Decision Fatigue'?"),
    ("Tonu", "Decision fatigue! The human brain has a finite budget of mental willpower and decision-making energy each day."),
    ("Solu", "Every tiny decision—what socks to wear, what to eat for breakfast, which email to open first—drains that mental battery!"),
    ("Tonu", "That is why visionaries like Steve Jobs or Barack Obama simplified their wardrobe to a signature outfit: it eliminated one trivial morning decision to preserve executive brainpower for high-impact choices!"),
    ("Solu", "Automate or simplify minor daily decisions so you have peak willpower when it counts."),
    ("Tonu", "And what about having a definitive 'Shutdown Ritual' at the end of your workday?"),
    ("Solu", "Cal Newport emphasizes having a conscious shutdown habit! Review your calendar for tomorrow, close your laptop, and say out loud: 'Shutdown Complete!'"),
    ("Tonu", "That vocal declaration creates an airtight psychological barrier between your professional responsibilities and your personal evening peace."),'''

target_13 = '    ("Solu", "Now let\'s explore David Allen\'s famous \'Two-Minute Rule\' from Getting Things Done!"),'
code = code.replace(target_13, ep13_block3 + "\n" + target_13)

with open("scripts/generate_episodes_11_12_13.py", "w") as f:
    f.write(code)

