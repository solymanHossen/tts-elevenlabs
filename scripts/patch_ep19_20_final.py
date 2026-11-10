with open("scripts/generate_episodes_19_20.py", "r") as f:
    code = f.read()

ep19_block3 = '''    ("Solu", "Now let's explore the HEAR framework for active listening during conflicts!"),
    ("Tonu", "H-E-A-R. Let's break down each letter for our listeners!"),
    ("Solu", "H stands for Hear completely without interrupting: let the other person speak without jumping in to defend yourself!"),
    ("Tonu", "E stands for Empathize: acknowledge their emotional reality before debating any logic!"),
    ("Solu", "A stands for Acknowledge: rephrase what they said in your own words to prove you truly understood: 'What I am hearing is that you felt unheard during the project review; is that right?'"),
    ("Tonu", "And R stands for Respond with respect and collaboration!"),
    ("Solu", "And what about Carl Jung's concept of the 'Shadow Self' and emotional triggers?"),
    ("Tonu", "Carl Jung famously wrote: 'Everything that irritates us about others can lead us to an understanding of ourselves!'"),
    ("Solu", "When someone's behavior triggers an intense, explosive reaction in you, pause and reflect! Is that behavior a mirror reflecting a hidden fear, insecurity, or suppressed trait within yourself?"),
    ("Tonu", "Self-inquiry turns anger into personal evolution."),
    ("Solu", "And always practice the 'Twenty-Four-Hour Rule' before sending angry communications!"),
    ("Tonu", "Never hit 'Send' on an angry email or text message late at night! Write it in a private drafts folder, close your laptop, sleep on it for twenty-four hours, and re-read it in the morning light."),
    ("Solu", "Ninety-nine percent of the time, you will delete that harsh email and replace it with a calm, professional message that protects your reputation."),
    ("Tonu", "And what about the SBI framework for delivering constructive feedback?"),
    ("Solu", "Situation, Behavior, Impact! Anchor feedback to a specific Situation: 'Yesterday during our team conference call...'"),
    ("Tonu", "Describe the specific objective Behavior: '...you interrupted the client three times while they were explaining their requirements...'"),
    ("Solu", "And state the concrete Impact: '...which made the client defensive and slowed down the meeting.'"),
    ("Tonu", "Clear, objective, professional, and zero personal attacks!"),'''

target_19 = '    ("Solu", "Now listeners, it is time for our favorite interactive segment: The Speaking Practice Challenge!"),'
code = code.replace(target_19, ep19_block3 + "\n" + target_19)

ep20_block3 = '''    ("Solu", "Now let's explore Aristotle's famous concept of the 'Golden Mean' in virtue ethics!"),
    ("Tonu", "The Golden Mean! Aristotle taught that virtue is always the harmonious middle path between two extreme vices: an excess and a deficiency!"),
    ("Solu", "For example, Courage is the Golden Mean between Cowardice on one extreme and Recklessness on the other!"),
    ("Tonu", "Generosity is the Golden Mean between Stinginess and Wasteful Extravagance!"),
    ("Solu", "Honesty is the Golden Mean between Deceitfulness and Brutal Insensitivity."),
    ("Tonu", "Virtue is an art of daily balance, discernment, and moderation."),
    ("Solu", "And now, Tonu, look at the grand tapestry of our twenty episodes together!"),
    ("Tonu", "Let's walk our listeners through the complete, magnificent curriculum of Daily Speak English!"),
    ("Solu", "In Episodes 1 and 2, we laid the emotional foundation with Love, Relationships, and Building Atomic Daily Habits."),
    ("Tonu", "In Episodes 3 and 4, we empowered your life with Financial Freedom, Money Mindset, and Exploring the World through Travel!"),
    ("Solu", "In Episodes 5 and 6, we nurtured Mental Well-Being, Stress Relief, and Lifelong Family and Friendship Bonds."),
    ("Tonu", "In Episodes 7 and 8, we stepped into Career Mastery, Job Interview English, and the Rhythm of Everyday Conversations!"),
    ("Solu", "In Episodes 9 and 10, we chased Bold Dreams, Personal Growth, and explored Artificial Intelligence and the Future of Humanity!"),
    ("Tonu", "In Episodes 11 and 12, we savored Global Food Traditions and mastered Physical Fitness and Longevity!"),
    ("Solu", "In Episodes 13 and 14, we reclaimed Deep Focus, Time Management, and celebrated Global Cultural Festivities!"),
    ("Tonu", "In Episodes 15 and 16, we championed Environmental Sustainability and unlocked Charismatic Public Speaking and Storytelling!"),
    ("Solu", "And in Episodes 17, 18, 19, and 20, we mastered Language Immersion, Creative Arts and Literature, Emotional Intelligence, and Ancient Philosophical Wisdom!"),
    ("Tonu", "That is an all-encompassing, university-level spoken English education spanning every essential dimension of the human experience!"),
    ("Solu", "You now have the vocabulary, the cultural nuance, the idiom mastery, and the speaking confidence to converse with anyone in the world on any topic."),'''

target_20 = '    ("Tonu", "Now listeners, for the ultimate time in this twentieth episode, it is time for our favorite interactive segment: The Speaking Practice Challenge!"),'
code = code.replace(target_20, ep20_block3 + "\n" + target_20)

with open("scripts/generate_episodes_19_20.py", "w") as f:
    f.write(code)

