with open("scripts/generate_episodes_17_18.py", "r") as f:
    code = f.read()

ep17_block3 = '''    ("Solu", "Now let's talk about the incredible diversity of global English accents!"),
    ("Tonu", "Yes! Many English learners mistakenly believe that there is only one 'correct' accent—like standard American or British Received Pronunciation."),
    ("Solu", "In reality, non-native English speakers outnumber native speakers by three to one worldwide! English belongs to the entire globe."),
    ("Tonu", "From the melodic cadence of Indian and Nigerian English, to the crisp rhythm of Australian and Irish accents, to Canadian and Scottish dialects!"),
    ("Solu", "The goal of speaking English is not to erase your beautiful cultural accent; the goal is clear pronunciation, natural rhythm, and mutual comprehension!"),
    ("Tonu", "And what about the technique of recording yourself speaking?"),
    ("Solu", "Record a two-minute voice note on your phone once a week discussing your day in English!"),
    ("Tonu", "Save those recordings in a dedicated folder. In six months, go back and listen to your very first recording!"),
    ("Solu", "The contrast will take your breath away! You will see proof of your exponential growth, giving you immense confidence."),
    ("Tonu", "And remember: over sixty percent of all information on the internet is in English!"),
    ("Solu", "Mastering English opens the doors to the world's greatest libraries, scientific research, international universities, and global remote careers!"),'''

target_17 = '    ("Solu", "Now listeners, it is time for our favorite interactive segment: The Speaking Practice Challenge!"),'
code = code.replace(target_17, ep17_block3 + "\n" + target_17)

ep18_block3 = '''    ("Solu", "Now let's explore the Japanese philosophy of 'Kintsugi' in pottery and life!"),
    ("Tonu", "Oh, Kintsugi! Kintsugi translates as 'golden joinery'. When a ceramic bowl or tea cup cracks or shatters, Japanese craftsmen do not throw it away!"),
    ("Solu", "Instead, they repair the broken pieces using Japanese lacquer dusted with real, powdered twenty-four-karat gold!"),
    ("Tonu", "The cracks are not hidden; they are illuminated with gold! The repaired bowl is considered more valuable and beautiful than the original unbroken bowl, because its fractures tell an authentic history of resilience."),
    ("Solu", "What a magnificent metaphor for the human condition! Our scars, mistakes, heartbreaks, and hardships are not things to be ashamed of; when healed with wisdom, they become our greatest golden beauty."),
    ("Tonu", "And what about Photography as visual storytelling? Henri Cartier-Bresson's famous concept of 'The Decisive Moment'!"),
    ("Solu", "The Decisive Moment! Photography is not about owning a ten-thousand-dollar camera; it is about having eyes that see!"),
    ("Tonu", "Waiting patiently with your camera until composition, human emotion, and golden sunlight align in a single split-second of perfection."),
    ("Solu", "And the Rule of Thirds in visual composition: dividing your frame into a three-by-three grid and placing your subject along the intersecting grid lines!"),
    ("Tonu", "It creates dynamic tension and visual interest, drawing the viewer's eye across the entire canvas."),'''

target_18 = '    ("Solu", "Now listeners, it is time for our favorite interactive segment: The Speaking Practice Challenge!"),'
code = code.replace(target_18, ep18_block3 + "\n" + target_18)

with open("scripts/generate_episodes_17_18.py", "w") as f:
    f.write(code)

