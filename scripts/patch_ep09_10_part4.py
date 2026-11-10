with open("scripts/generate_episodes_09_10.py", "r") as f:
    code = f.read()

target_09 = '    ("Tonu", "And celebrate your small wins along the way! Don\'t wait until you reach the final mountaintop to feel happy. Reward yourself for staying disciplined today."),'
add_09 = '''    ("Tonu", "And celebrate your small wins along the way! Don't wait until you reach the final mountaintop to feel happy. Reward yourself for staying disciplined today."),
    ("Solu", "How do you celebrate small wins, Tonu?"),
    ("Tonu", "When I finish a major chapter or complete a thirty-day challenge, I treat myself to a delicious dessert, buy that book I've been eyeing, or spend a guilt-free afternoon watching my favorite movie!"),
    ("Solu", "Rewarding your brain releases dopamine, which reinforces the desire to keep pursuing future goals!"),
    ("Tonu", "It creates positive emotional momentum that pulls you forward effortlessly."),'''

code = code.replace(target_09, add_09)

target_10 = '    ("Tonu", "From relationships and habits, to money, travel, mental health, friendship, careers, routines, dreams, and technology—you have practiced hundreds of real English conversations!"),'
add_10 = '''    ("Tonu", "From relationships and habits, to money, travel, mental health, friendship, careers, routines, dreams, and technology—you have practiced hundreds of real English conversations!"),
    ("Solu", "Think about where you started in Episode One, talking about love and deep communication, through building atomic habits in Episode Two, understanding your finances in Episode Three, and packing your bags for travel in Episode Four."),
    ("Tonu", "Then learning how to handle stress and mental peace in Episode Five, nurturing family and lifelong friendships in Episode Six, preparing for your dream career and salary negotiation in Episode Seven, and mastering your daily routines and grocery chats in Episode Eight."),
    ("Solu", "And in Episode Nine, stepping out of your comfort zone to chase your biggest life ambitions, leading all the way to our deep look at technology and AI today!"),
    ("Tonu", "That is an extraordinary foundation of over twenty-five hundred everyday English sentences, seventy idioms and phrasal verbs, and dozens of speaking challenges!"),'''

code = code.replace(target_10, add_10)

with open("scripts/generate_episodes_09_10.py", "w") as f:
    f.write(code)

