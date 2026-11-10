with open("scripts/generate_episodes_09_10.py", "r") as f:
    code = f.read()

# Additions to EP09
target_09 = '    ("Tonu", "Recognizing that self-sabotage allows you to consciously expand your capacity for joy, abundance, and success."),'
add_09 = '''    ("Tonu", "Recognizing that self-sabotage allows you to consciously expand your capacity for joy, abundance, and success."),
    ("Solu", "Now, let's explore a brilliant exercise: Designing your Ideal Ordinary Day!"),
    ("Tonu", "Oh, I love this visualization exercise! How does it work?"),
    ("Solu", "Instead of imagining winning a hundred million dollars in the lottery and lounging on a yacht forever, imagine an ideal ordinary Tuesday five years from now!"),
    ("Tonu", "What time do you wake up? What does the morning light look like in your room? What kind of work are you doing? Who are you having lunch with?"),
    ("Solu", "When you get crystal clear on what an ideal ordinary day looks and feels like, you can start reverse engineering your life right now!"),
    ("Tonu", "You realize that eighty percent of your ideal ordinary day doesn't require millions of dollars; it requires intentional choices, healthy boundaries, and daily discipline today."),
    ("Solu", "And have you heard of the 'Twenty-Mile March' concept from business author Jim Collins?"),
    ("Tonu", "The Twenty-Mile March! In the historic race to the South Pole between explorers Amundsen and Scott, Amundsen's team committed to marching exactly twenty miles every single day, whether the weather was clear and sunny or a blinding blizzard!"),
    ("Solu", "While Scott's team rested during storms and marched forty miles on sunny days until they collapsed from exhaustion."),
    ("Tonu", "And Amundsen's steady, disciplined twenty-mile march won the race safely!"),
    ("Solu", "Whatever your English or career goal is, commit to your daily twenty-mile march. Practice for fifteen or twenty minutes every single day, rain or shine!"),'''

code = code.replace(target_09, add_09)

# Additions to EP10
target_10 = '    ("Tonu", "Now, let\'s explore our special English vocabulary section! Let\'s examine seven essential, cutting-edge expressions and idioms related to technology, innovation, and modern life."),'
add_10 = '''    ("Solu", "Let's also talk about the evolution of synthetic speech and voice technology, because it has advanced by leaps and bounds!"),
    ("Tonu", "Oh, absolutely! Think back to computer voices twenty years ago. They sounded completely metallic, robotic, and monotone, like a malfunctioning microwave!"),
    ("Solu", "And today, neural speech synthesis can capture emotional warmth, subtle breathing pauses, natural laughter, and beautiful human intonation!"),
    ("Tonu", "It enables people who lost their voice due to illness to speak again with their own digital voice, and makes audiobooks and educational podcasts accessible to millions of people worldwide."),
    ("Solu", "And what about running AI models locally and on mobile phones?"),
    ("Tonu", "That is such an exciting frontier! In the past, all heavy AI calculations had to happen on giant corporate server farms in the cloud."),
    ("Solu", "Which raised huge privacy concerns because your personal data and audio had to travel across the internet."),
    ("Tonu", "Now, with efficient compact models and neural processing chips, we can run voice cloning, translation, and dictation directly on your own personal device or smartphone, completely offline without any internet connection!"),
    ("Solu", "Local-first computing means absolute privacy: your thoughts, voice recordings, and personal documents never leave your hands!"),
    ("Tonu", "And let's touch upon the environmental footprint of modern technology."),
    ("Solu", "Yes! Data centers consume massive amounts of electricity and millions of gallons of water for cooling server racks."),
    ("Tonu", "That is why the race toward green computing, renewable solar and wind powered data centers, and algorithmic efficiency is one of the most critical engineering missions of our generation."),
    ("Solu", "Technology must be in harmony with our planet, not at war with it."),
    ("Tonu", "And finally, what about AI companions and emotional chatbots?"),
    ("Solu", "Many people are turning to AI chatbots for friendship and comfort when they feel lonely."),
    ("Tonu", "While an AI can be a helpful sounding board, we must be careful never to let a machine replace real human beings!"),
    ("Solu", "A digital screen can never replace a warm hug from your mother, sharing a laugh with an old friend over pizza, or holding hands with someone you love."),
    ("Tonu", "Use technology to bring you closer to human beings in the real physical world, not to isolate you from them."),
    ("Tonu", "Now, let's explore our special English vocabulary section! Let's examine seven essential, cutting-edge expressions and idioms related to technology, innovation, and modern life."),'''

code = code.replace(target_10, add_10)

with open("scripts/generate_episodes_09_10.py", "w") as f:
    f.write(code)

