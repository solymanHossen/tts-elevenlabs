with open("scripts/generate_episodes_19_20.py", "r") as f:
    code = f.read()

ep19_add = '''    ("Solu", "Now let's explore neuroscientist Dr. Lisa Feldman Barrett's groundbreaking concept: 'Emotional Granularity'!"),
    ("Tonu", "Oh, emotional granularity! What does that mean in simple English, Solu?"),
    ("Solu", "Most people have very low emotional vocabulary: when they feel uncomfortable, they simply say 'I feel bad' or 'I feel stressed!'"),
    ("Tonu", "While high emotional granularity means pinpointing your precise emotional state with rich nuance!"),
    ("Solu", "Are you feeling 'resentful', 'unappreciated', 'insecure', 'overwhelmed', 'envious', 'lonely', or 'fatigued'?"),
    ("Tonu", "And fMRI brain scans show that the moment you identify and name your precise emotion with specific language, activity in your amygdala decreases immediately! Psychologists call it 'Name it to tame it!'"),
    ("Solu", "Naming an emotion gives your rational brain conscious power over it."),
    ("Tonu", "Now let's examine Dr. Stephen Karpman's famous 'Drama Triangle' in interpersonal conflicts!"),
    ("Solu", "The Drama Triangle! In unhealthy relationships and family arguments, people constantly rotate between three toxic roles: The Victim, The Persecutor, and The Rescuer!"),
    ("Tonu", "The Victim says: 'Poor me! Everything is unfair and everyone takes advantage of me!'"),
    ("Solu", "The Persecutor blames and attacks: 'It is all your fault, you always ruin everything!'"),
    ("Tonu", "And the Rescuer tries to fix everyone else's problems without being asked, creating dependency and secret resentment!"),
    ("Solu", "How do emotionally mature people escape the Drama Triangle, Tonu?"),
    ("Tonu", "Shift to the Empowerment Dynamic! The Victim transforms into the Creator—taking active ownership of solutions."),
    ("Solu", "The Persecutor transforms into the Challenger—offering honest, constructive truth with respect."),
    ("Tonu", "And the Rescuer transforms into the Coach—asking empowering questions instead of solving problems for others!"),
    ("Solu", "And what about setting firm boundaries with grace and kindness?"),
    ("Tonu", "A healthy boundary does not require an essay of defensive excuses!"),
    ("Solu", "Never over-apologize or invent fake sickness when saying no! A calm, polite boundary sounds like: 'Thank you so much for the invitation, but I won't be able to make it this time. I hope you all have a wonderful time!'"),
    ("Tonu", "Clean, respectful, and zero guilt!"),
    ("Solu", "And let's touch upon self-forgiveness. Many people are quick to forgive others, but carry bitter shame over their own past mistakes for decades."),
    ("Tonu", "You did the best you could with the emotional tools and wisdom you had back then. Forgive yourself for who you were, so you can be who you are meant to be today!"),'''

target_19 = '    ("Solu", "Now listeners, it is time for our favorite interactive segment: The Speaking Practice Challenge!"),'
code = code.replace(target_19, ep19_add + "\n" + target_19)

ep20_add = '''    ("Solu", "Now let's explore the timeless Eastern philosophy of Taoism and the concept of 'Wu Wei'!"),
    ("Tonu", "Oh, Wu Wei! Translated from the Tao Te Ching as 'effortless action' or 'acting in harmony with the natural flow of life'!"),
    ("Solu", "Lao Tzu used the metaphor of water: water is the softest, gentlest substance in the world, yet it carves through solid mountain granite by flowing patiently around obstacles!"),
    ("Tonu", "When we fight reality, try to force outcomes, and resist natural transitions, we exhaust ourselves. Practicing Wu Wei means adapting like water—yielding when appropriate, persevering quietly, and trusting the timing of life!"),
    ("Solu", "And what about Zen Buddhism's concept of 'Shoshin'—The Beginner's Mind?"),
    ("Tonu", "Zen master Shunryu Suzuki wrote: 'In the beginner's mind there are many possibilities; in the expert's mind there are few.'"),
    ("Solu", "When you think you know everything, your mind closes into arrogance and rigidity. Approaching every conversation, every book, and every day with a humble beginner's curiosity keeps you forever young and wise."),
    ("Tonu", "Now let's talk about Bronnie Ware's famous book: The Top Five Regrets of the Dying!"),
    ("Solu", "Bronnie Ware spent years working as a palliative hospice caregiver, caring for patients during the final twelve weeks of their lives."),
    ("Tonu", "And she asked them what they regretted most when looking back across their entire lifespan."),
    ("Solu", "What was the number one, most common regret of all, Tonu?"),
    ("Tonu", "Regret number one was: 'I wish I'd had the courage to live a life true to myself, not the life others expected of me!'"),
    ("Solu", "Think about that! Millions of people spend their entire lives living to please their parents, their neighbors, or societal expectations, burying their true dreams!"),
    ("Tonu", "And regret number two was: 'I wish I hadn't worked so hard, and spent more time with the people I love.'"),
    ("Solu", "And regret number three was: 'I wish I had stayed in touch with my true friends.'"),
    ("Tonu", "These deathbed regrets are the ultimate roadmap for how to live wisely today! Live authentically, love deeply, work with purpose, and cherish your friendships."),
    ("Solu", "And think about what kind of ancestor you want to be! The Greek proverb says: 'A civilization flourishes when elders plant trees under whose shade they know they will never sit.'"),
    ("Tonu", "Planting seeds of kindness, education, and love that will bear fruit for generations long after we are gone."),'''

target_20 = '    ("Tonu", "Now listeners, for the ultimate time in this twentieth episode, it is time for our favorite interactive segment: The Speaking Practice Challenge!"),'
code = code.replace(target_20, ep20_add + "\n" + target_20)

with open("scripts/generate_episodes_19_20.py", "w") as f:
    f.write(code)

