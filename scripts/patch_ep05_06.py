with open("scripts/generate_episodes_05_06.py", "r") as f:
    code = f.read()

# Additions to EP05:
target_05 = '    ("Solu", "That brings us right into our special English vocabulary section! Let\'s explore seven very common everyday English expressions and idioms related to stress, health, and peace of mind."),'
add_05 = '''    ("Tonu", "Let's also talk about the Japanese concept of Shinrin-yoku, or 'Forest Bathing'!"),
    ("Solu", "Oh, Forest Bathing! It sounds poetic, but there is rigorous biological science behind it."),
    ("Tonu", "Yes! Studies show that spending just thirty minutes immersed in a forest or a park with mature trees reduces cortisol levels by more than twenty percent!"),
    ("Solu", "Trees emit natural organic compounds called phytoncides to protect themselves from insects and rot. When humans inhale phytoncides, our immune systems produce more natural killer cells and our blood pressure drops!"),
    ("Tonu", "Nature is literally preventative medicine for human beings."),
    ("Solu", "And what about the idea of a 'Digital Sabbath'?"),
    ("Tonu", "A Digital Sabbath means choosing one day a week—often Sunday—where you turn off your smartphone, tablet, and laptop for twenty-four full hours!"),
    ("Solu", "Imagine a Sunday with zero notifications, zero news alerts, and zero endless scrolling! You read books, bake bread, go for walks, and have long conversations with your family."),
    ("Tonu", "People who try a Digital Sabbath report feeling like their weekend lasted twice as long!"),
    ("Solu", "That brings us right into our special English vocabulary section! Let's explore seven very common everyday English expressions and idioms related to stress, health, and peace of mind."),'''

code = code.replace(target_05, add_05)

# Additions to EP06:
target_06 = '    ("Solu", "That brings us right into our special English vocabulary section! Let\'s explore seven colorful, practical expressions and idioms about family, friendship, and social relationships."),'
add_06 = '''    ("Tonu", "Let's also talk about the art of being a gracious host and a wonderful dinner guest!"),
    ("Solu", "Oh, dinner party etiquette! When you are invited to a friend or colleague's home for dinner, what is the number one golden rule?"),
    ("Tonu", "Never arrive completely empty-handed! Even a small gesture—a box of fine chocolates, a bouquet of fresh flowers, or a dessert to share—shows immense gratitude and respect for the host's effort."),
    ("Solu", "And when dinner is finished, always offer to help clear the plates or do the dishes! The host will usually say 'Oh, don't worry about it!', but offering shows wonderful manners."),
    ("Tonu", "And know when it's time to head home! When the host starts yawning or clearing the tea cups, that's your cue to say, 'Thank you so much for an unforgettable evening, we should let you get some rest!'"),
    ("Solu", "Now, let's touch upon forgiveness in relationships. Grudges can poison families and friendships for decades."),
    ("Tonu", "They really can. The famous quote says: 'Holding onto anger and resentment is like drinking poison and expecting the other person to die!'"),
    ("Solu", "You are the one suffering from the acidity of that anger, not them!"),
    ("Tonu", "Forgiving someone doesn't mean that what they did was okay, or that you have to let them back into your inner circle. Forgiveness means letting go of the desire for revenge so that your own heart can heal."),
    ("Solu", "And finally, let's celebrate having friends across different generations!"),
    ("Tonu", "Yes! Why limit your friends to people who are your exact age?"),
    ("Solu", "Having an older mentor in their sixties teaches you perspective and timeless wisdom, while having a younger friend keeps you playful, curious, and open to new trends."),
    ("Tonu", "Intergenerational friendships are such a rich tapestry of life!"),
    ("Solu", "That brings us right into our special English vocabulary section! Let's explore seven colorful, practical expressions and idioms about family, friendship, and social relationships."),'''

code = code.replace(target_06, add_06)

with open("scripts/generate_episodes_05_06.py", "w") as f:
    f.write(code)

