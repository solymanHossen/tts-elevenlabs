with open("scripts/generate_episodes_17_18.py", "r") as f:
    code = f.read()

ep17_block4 = '''    ("Solu", "Now let's explore the secret of 'Collocations' and 'Lexical Chunks' in language acquisition!"),
    ("Tonu", "Oh, collocations! This is the number one difference between someone who sounds like a translated dictionary and someone who speaks natural, effortless English!"),
    ("Solu", "What is a collocation, Tonu?"),
    ("Tonu", "Collocations are words that naturally go together like old friends! For example, in English, we say 'heavy rain', never 'strong rain'!"),
    ("Solu", "We say 'make a decision', never 'do a decision'! We say 'commit a crime', 'catch a cold', and 'take a break'!"),
    ("Tonu", "If you memorize isolated individual vocabulary words, your brain has to constantly think about which words fit together mathematically."),
    ("Solu", "While if you learn words in natural chunks and complete phrases, they roll off your tongue as a single cohesive unit!"),
    ("Tonu", "Phrases like: 'As far as I am concerned...', 'To be completely honest with you...', 'If I remember correctly...', or 'It goes without saying that...'!"),
    ("Solu", "Memorizing twenty of these conversational sentence starters gives you instant fluency and buys your brain time to form your main idea."),
    ("Tonu", "And what should someone do when they feel their heart race with language anxiety before ordering at a cafe abroad?"),
    ("Solu", "Take one deep physiological sigh, remind yourself that the waiter just wants to take your order, rehearse your phrase once in your head, smile, and speak!"),
    ("Tonu", "People around the world are remarkably kind and supportive when they see someone making a sincere effort to speak their language."),'''

target_17 = '    ("Solu", "Mastering English opens the doors to the world\'s greatest libraries, scientific research, international universities, and global remote careers!"),'
code = code.replace(target_17, target_17 + "\n" + ep17_block4)

ep18_block4 = '''    ("Solu", "Now let's explore the Golden Ratio and Sacred Geometry in art and architecture!"),
    ("Tonu", "The Golden Ratio—represented by the Greek letter Phi, approximately 1.618!"),
    ("Solu", "Why has the Golden Ratio captivated artists, mathematicians, and architects for over two thousand years?"),
    ("Tonu", "Because the Golden Ratio appears everywhere in the natural universe! The spiral of a nautilus seashell, the arrangement of seeds in a sunflower head, the spiral arms of distant galaxies, and even the proportions of the human face and body!"),
    ("Solu", "Ancient Greek architects used the Golden Ratio to design the Parthenon in Athens, creating buildings with timeless visual harmony."),
    ("Tonu", "And Renaissance master Leonardo da Vinci used it in the Vitruvian Man and the Mona Lisa, creating compositions that feel innately pleasing to human perception!"),
    ("Solu", "And what about the tactile, therapeutic joy of tactile crafts—like woodworking, knitting, leathercraft, or pottery?"),
    ("Tonu", "In our digital world where we spend twelve hours a day tapping cold glass screens, our hands crave physical creation!"),
    ("Solu", "Working with fragrant wood, smelling cedar shavings, molding cool clay on a potter's wheel, or knitting wool with bamboo needles grounds you in physical reality."),
    ("Tonu", "And when you finish, you hold a tangible physical object in your hands that will outlive you. That brings deep fulfillment that no digital app can match."),
    ("Solu", "And how about architectural spaces? The height of ceilings, natural daylight from arched windows, and acoustic warmth shape how human beings feel and think."),
    ("Tonu", "Winston Churchill famously said: 'We shape our buildings; thereafter, our buildings shape us!'"),'''

target_18 = '    ("Tonu", "It creates dynamic tension and visual interest, drawing the viewer\'s eye across the entire canvas."),'
code = code.replace(target_18, target_18 + "\n" + ep18_block4)

with open("scripts/generate_episodes_17_18.py", "w") as f:
    f.write(code)

