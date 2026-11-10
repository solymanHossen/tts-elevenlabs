with open("scripts/generate_episodes_17_18.py", "r") as f:
    code = f.read()

ep17_add = '''    ("Solu", "Now let's address a major hurdle that almost every language learner encounters: The Dreaded Intermediate Plateau!"),
    ("Tonu", "Oh, the intermediate plateau! In the beginning, when you are a complete beginner, progress is explosive! You learn greetings, food vocabulary, and basic phrases, and you feel like a linguistic genius!"),
    ("Solu", "And then you reach the intermediate B1 or B2 level, and suddenly progress seems to grind to a complete halt! You can survive everyday conversations, but you feel stuck!"),
    ("Tonu", "Why does the intermediate plateau happen, and how do learners break through it, Solu?"),
    ("Solu", "It happens because beginner textbooks and apps no longer challenge your brain! To break through the intermediate plateau, you must transition to authentic, native-level materials!"),
    ("Tonu", "Start reading full English novels, listening to native-speed investigative podcasts, watching British and American documentaries, and writing personal essays in English!"),
    ("Solu", "And let's talk about connected speech, reductions, and the famous 'Schwa' sound!"),
    ("Tonu", "Oh, the Schwa sound—the upside-down 'e' symbol in the phonetic alphabet! The schwa /ə/ is the most common vowel sound in the entire English language!"),
    ("Solu", "In unstressed syllables, English vowels naturally reduce to a relaxed, neutral 'uh' sound—like the 'a' in 'about', or the 'o' in 'harmony', or the 'e' in 'problem'!"),
    ("Tonu", "And words link together smoothly: 'want to' naturally becomes 'wanna', 'going to' becomes 'gonna', and 'could have' becomes 'could've'!"),
    ("Solu", "When non-native speakers pronounce every single syllable with equal, heavy stress, it sounds robotic and exhausts their facial muscles. Embracing the relaxed schwa and linking sounds makes your English flow like water!"),
    ("Tonu", "Now let's talk about language exchange partnerships!"),
    ("Solu", "Language exchange apps like Tandem or HelloTalk allow you to partner with native English speakers who want to learn your native tongue!"),
    ("Tonu", "The golden rule of language exchange: split your time strictly fifty-fifty! Spend thirty minutes speaking entirely in English, and thirty minutes speaking in your native language."),
    ("Solu", "And did you know that being multilingual physically delays the onset of cognitive decline and dementia?"),
    ("Tonu", "Yes! Studies published in neurobiology journals show that bilingual and multilingual individuals develop symptoms of Alzheimer's disease four to five years later than monolinguals!"),
    ("Solu", "Constantly switching between two linguistic operating systems builds immense 'Cognitive Reserve' in the brain's prefrontal cortex."),
    ("Tonu", "And many polyglots report feeling like they have slightly different personalities in each language!"),
    ("Solu", "That is so true! Speaking English might make you feel more direct and expressive, while speaking your native tongue connects you with deep ancestral warmth."),'''

target_17 = '    ("Solu", "Now, let\'s explore our special English vocabulary section! Let\'s examine seven colorful idioms and expressions related to learning, language, and knowledge."),'
code = code.replace(target_17, ep17_add + "\n" + target_17)

ep18_add = '''    ("Solu", "Let's also explore the fascinating world of Color Psychology in art and marketing!"),
    ("Tonu", "Color has an immediate, subconscious physiological effect on the human body! For example, warm colors like vibrant red and orange stimulate appetite and increase heart rate."),
    ("Solu", "Which is why nearly every major global fast-food brand uses red and yellow in their logos!"),
    ("Tonu", "While cool colors like deep ocean blue and forest green lower blood pressure, promote mental calm, and evoke feelings of trust, stability, and security."),
    ("Solu", "Artists like Claude Monet and Vincent van Gogh understood color harmony intuitively, using complementary colors to make canvas surfaces vibrate with visual energy!"),
    ("Tonu", "And what about the magic of Poetry and Spoken Word?"),
    ("Solu", "Poetry is the distillation of human language into pure concentrated emotion! In ancient Greek, 'poiesis' literally means 'to create or bring into existence'."),
    ("Tonu", "Think about the rhythmic pulse of Shakespeare's iambic pentameter—da-DUM, da-DUM, da-DUM, da-DUM, da-DUM—which mimics the exact biological rhythm of the human heartbeat!"),
    ("Solu", "Or Japanese Haiku—three brief lines of five, seven, and five syllables—capturing a fleeting moment of natural beauty, like a frog leaping into an ancient pond!"),
    ("Tonu", "And today, modern spoken-word slam poetry blends lyrical storytelling with raw vulnerability, performing poetry that moves stadiums of young people to tears!"),
    ("Solu", "Now let's address 'Creative Blocks' and how artists overcome Resistance, described by author Steven Pressfield in The War of Art!"),
    ("Tonu", "The Resistance! That internal psychological force that whispers: 'Don't paint today, don't write that chapter, clean the kitchen instead, you're not talented anyway!'"),
    ("Solu", "Amateurs wait for magical inspiration before they create. Professionals know that inspiration comes AFTER you sit down at the desk!"),
    ("Tonu", "Picasso famously said: 'Inspiration exists, but it has to find you working!'"),
    ("Solu", "Show up every day at the appointed time, sit down with your instrument, pen, or canvas, and treat creativity with the professional respect of a sacred vocation."),
    ("Tonu", "And what about the collaborative harmony of a full symphony orchestra?"),
    ("Solu", "Eighty individual musicians playing violins, cellos, oboes, trumpets, and timpani drums, all watching the silent baton of the conductor!"),
    ("Tonu", "Each musician plays their unique part, creating a tapestry of sound that no solo instrument could ever produce alone. It is the pinnacle of human collaboration."),'''

target_18 = '    ("Tonu", "Now, let\'s explore our special English vocabulary section! Let\'s examine seven colorful idioms and expressions inspired by art, music, literature, and creativity."),'
code = code.replace(target_18, ep18_add + "\n" + target_18)

with open("scripts/generate_episodes_17_18.py", "w") as f:
    f.write(code)

