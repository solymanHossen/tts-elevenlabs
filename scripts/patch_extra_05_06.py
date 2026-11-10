with open("scripts/generate_episodes_05_06.py", "r") as f:
    code = f.read()

target_05 = '    ("Tonu", "Releasing physical tension immediately calms your mental state."),'
add_05 = '''    ("Tonu", "Releasing physical tension immediately calms your mental state."),
    ("Solu", "Have you ever tried Progressive Muscle Relaxation before sleeping?"),
    ("Tonu", "Oh, Progressive Muscle Relaxation is incredible for insomnia!"),
    ("Solu", "You start at your toes, squeeze them tightly for five seconds, and release. Then your calves, squeeze and release. Then your thighs, stomach, chest, shoulders, and finally your facial muscles!"),
    ("Tonu", "By the time you finish releasing tension from your forehead, your whole body feels heavy, warm, and ready to melt right into dreamland."),
    ("Solu", "It is so much more effective than counting sheep!"),'''

code = code.replace(target_05, add_05)

target_06 = '    ("Solu", "And finally, let\'s celebrate having friends across different generations!"),'
add_06 = '''    ("Solu", "Now, let's talk about the five love languages in families and friendships!"),
    ("Tonu", "Oh, Dr. Gary Chapman's famous concept: Words of Affirmation, Quality Time, Acts of Service, Receiving Gifts, and Physical Touch!"),
    ("Solu", "Most people think love languages are only for romantic couples, but they apply equally to friends and family members."),
    ("Tonu", "For example, if your friend's primary love language is Quality Time, sending them an expensive gift won't mean as much as spending an uninterrupted afternoon walking in the park together!"),
    ("Solu", "And if your parent's love language is Acts of Service, helping them clean the garage or fixing their computer will make them feel deeply loved and appreciated."),
    ("Tonu", "Understanding how your loved ones perceive love prevents so much accidental misunderstanding!"),
    ("Solu", "And finally, let's celebrate having friends across different generations!"),'''

code = code.replace(target_06, add_06)

with open("scripts/generate_episodes_05_06.py", "w") as f:
    f.write(code)

