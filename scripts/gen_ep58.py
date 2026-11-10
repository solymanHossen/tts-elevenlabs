#!/usr/bin/env python3
"""
Daily Speak English - Episode 58
Title: The Philosophy of Aging: Growing Older with Grace, Radiance & Deep Wisdom
Requirements:
- Starts with Tonu: "Hey hey, lovely listeners!..."
- Words >= 3,550 (strict duration >= 25.5 - 28.0 mins)
- High-level engaging, natural conversational English
"""

import gen_common

def build_ep58():
    turns = [
        # SECTION 1: MAGNETIC OPENING & THE ANTI-AGING DELUSION
        ("Tonu", "Hey hey, lovely listeners! Welcome back to Daily Speak English, your favorite place to become fluent, confident, and unstoppable in English! I'm Tonu!"),
        ("Solu", "And I'm Solu! Welcome back, everyone! Today, we are turning our faces toward the light, challenging one of the most toxic, fear-driven obsessions of modern consumer culture, and embracing the profound majesty of our human journey: 'The Philosophy of Aging, Growing Older with Grace, Radiance, and Deep Wisdom'!"),
        ("Tonu", "Solu, think about modern advertising and media! The global anti-aging cosmetic industry is currently worth over sixty billion dollars a year!"),
        ("Solu", "Sixty billion dollars! And what is their core sales pitch? Their pitch is that getting older is an embarrassing medical defect, a humiliating tragedy that must be concealed, injected, dyed, botoxed, and fought at all costs!"),
        ("Tonu", "People dread turning thirty; they panic at forty; they feel invisible at fifty; and they are terrified of sixty!"),
        ("Solu", "Society worships youth—untested, inexperienced, naive youth! Yet throughout thousands of years of human history, from ancient Greece and indigenous tribes to Confucian Asia, the elders were the revered pillars of the community, honored for their judgment, emotional poise, and ancestral wisdom!"),
        ("Tonu", "Today, we are going to explore Erik Erikson's developmental psychology of Ego Integrity, examine the global economic data on the 'U-Bend of Happiness', study Cicero's ancient defense of old age in 'De Senectute', discover the longevity secrets of the global Blue Zones, celebrate neuroplasticity in the mature mind, and master expressive English idioms!"),
        ("Solu", "As the legendary artist Pablo Picasso famously said: 'It takes a long time to become young.' Let's uncover the radiant beauty of every single season of life!"),

        # SECTION 2: ERIK ERIKSON & EGO INTEGRITY VERSUS DESPAIR
        ("Solu", "Let's begin by examining the monumental psychological framework of German-American developmental psychoanalyst Erik Erikson!"),
        ("Tonu", "Erikson outlined eight distinct stages of psychosocial development across the human lifespan, from infancy to late adulthood."),
        ("Solu", "What is the eighth and final stage of human psychological development, Solu?"),
        ("Solu", "The final stage is 'Ego Integrity versus Despair'!"),
        ("Tonu", "What happens in this stage, Tonu?"),
        ("Tonu", "As individuals enter the autumn and winter of their lives, they naturally look back across the entire landscape of their existence!"),
        ("Solu", "If they fall into 'Despair', they are consumed by bitter regret: 'I made the wrong choices, I married the wrong person, I wasted my talents, and now time has run out!'"),
        ("Tonu", "Despair produces bitterness, cynicism, and a terrifying fear of death!"),
        ("Solu", "Now, what is 'Ego Integrity'?"),
        ("Tonu", "Ego Integrity is the serene, triumphant acceptance of your one and only life cycle as something that had to be, that permitted no substitutions!"),
        ("Solu", "You look at your mistakes, your triumphs, your heartbreaks, and your scars, and you say: 'It was messy, it was imperfect, but it was mine, and I lived it with all my heart!'"),
        ("Tonu", "Integrity produces a transcendent, radiant peace that shines like an unshakeable lighthouse for younger generations."),

        # SECTION 3: THE U-BEND OF HAPPINESS: DEMOGRAPHIC PROOF
        ("Solu", "Let's look at one of the most surprising, universally replicated discoveries in modern social science and economics: 'The U-Bend of Happiness'!"),
        ("Tonu", "Economists David Blanchflower and Andrew Oswald analyzed self-reported life satisfaction data across millions of individuals in over one hundred and forty countries!"),
        ("Solu", "What did they discover about human happiness across the lifespan, Solu?"),
        ("Solu", "Everyone assumes that happiness peaks in your carefree twenties and slowly deteriorates downhill into old age! The data proved that assumption is completely WRONG!"),
        ("Tonu", "Human happiness follows a giant, symmetrical U-curve!"),
        ("Solu", "People start out relatively optimistic and cheerful in their late teens and early twenties. Then, happiness steadily declines through the thirties and hits rock bottom in the mid-to-late forties!"),
        ("Tonu", "Why is middle age often the emotional low point? Because of intense competing pressures: paying mortgages, caring for aging parents, raising young children, career burnout, and mourning the death of youthful illusions!"),
        ("Solu", "Now, what happens after age fifty?"),
        ("Tonu", "Happiness surges upward! People in their sixties, seventies, and eighties report significantly higher levels of contentment, gratitude, emotional stability, and day-to-day happiness than people in their twenties!"),
        ("Solu", "The data is conclusive: for the vast majority of human beings, the best, most peaceful, and joyful emotional years of your life are waiting ahead of you in your second half!"),

        # SECTION 4: CICERO'S 'DE SENECTUTE': THE ANCIENT DEFENSE OF AGE
        ("Solu", "Let's travel back to 44 BC in ancient Rome to study one of the greatest essays ever penned: Marcus Tullius Cicero's 'De Senectute'—On Old Age!"),
        ("Tonu", "Cicero was sixty-two years old, facing political turmoil, and wrote this masterpiece through the persona of the revered eighty-four-year-old Roman statesman Cato the Elder."),
        ("Solu", "Cicero systematically addressed and dismantled the four primary complaints people lodge against growing old!"),
        ("Tonu", "Complaint number one: 'Old age withdraws us from active business!' What was Cicero's rebuttal, Solu?"),
        ("Solu", "Cicero used the metaphor of a ship! The young deckhands run up the rigging, climb the masts, and pump out the bilge with brute physical sweat. But the old helmsman sits quietly at the stern, holding the steering rudder with steady hands and wisdom!"),
        ("Tonu", "Great achievements are not won by physical agility, but by counsel, wisdom, and judgment!"),
        ("Solu", "Complaint number two: 'Old age weakens the physical body!' Cicero replied: 'A wise old man no more regrets the loss of youthful brute strength than a young man regrets that he does not have the strength of a bull or an elephant!'"),
        ("Tonu", "Complaint number three: 'Old age deprives us of sensual physical pleasures!' Cicero celebrated this: 'What a magnificent blessing to be liberated from the tyrannical, violent enslavement of lust and youthful impulsive appetites!'"),
        ("Solu", "And complaint number four: 'Old age is close to death!' Cicero argued that a young person hopes to live long, but an old person has ALREADY achieved what the youth only hopes for—a long, full life!"),
        ("Tonu", "Cicero's timeless wisdom reminds us that youth is an apprentice, but maturity is a master."),

        # SECTION 5: THE BLUE ZONES: SECRETS OF CENTENARIANS
        ("Solu", "Let's explore the real-world science of vibrant, active longevity documented by National Geographic explorer Dan Buettner: 'The Blue Zones'!"),
        ("Tonu", "Buettner and a team of demographers, epidemiologists, and medical researchers identified five geographic pockets on Earth where people live active, healthy lives past age one hundred at ten times the global rate!"),
        ("Solu", "Where are these Blue Zones located, Tonu?"),
        ("Solu", "Okinawa in Japan; the mountainous Barbagia region of Sardinia in Italy; the Nicoya Peninsula in Costa Rica; the Aegean island of Ikaria in Greece; and the Seventh-day Adventist community in Loma Linda, California!"),
        ("Tonu", "What are the common lifestyle denominators of ninety- and one-hundred-year-olds who are still gardening, laughing, dancing, and cooking every single day?"),
        ("Solu", "First, 'Natural Movement'! They don't run marathons, pump iron in commercial gyms, or count fitness steps on smartwatches; they walk hilly cobblestone paths, tend terraced vegetable gardens, herd sheep, and knead sourdough bread daily!"),
        ("Tonu", "Second, look at their social structures! In Okinawa, they form 'Moai'—committed social support groups of five friends that meet every single week for seventy, eighty, or ninety years!"),
        ("Solu", "If one member falls ill, suffers a financial setback, or loses a spouse, the Moai is right there to cook meals, provide financial aid, and offer unwavering emotional comfort!"),
        ("Tonu", "Third, look at nutrition and 'Hara Hachi Bu'—the ancient Confucian practice of stopping eating when your stomach is eighty percent full! Their diets are plant-rich, centered on sweet potatoes, wild greens, fava beans, lentils, nuts, and clean water!"),
        ("Solu", "Fourth, 'Ikigai'—having a clear reason to wake up in the morning! In Okinawa, there is no word for 'retirement' in their native language; you simply remain an active, contributing member of the tribe!"),
        ("Tonu", "And fifth, in Ikaria, Greece, people take unhurried afternoon naps, drink herbal mountain tea, and live by a relaxed pace where clocks and deadlines are virtually ignored!"),
        ("Solu", "Aging is not a medical pathology; when supported by love, purposeful contribution, clean food, and human community, aging is a magnificent, radiant harvest."),

        # SECTION 6: CRYSTALLIZED INTELLIGENCE & NEUROSCIENCE OF WISDOM
        ("Solu", "Let's look at what actually happens inside the mature brain according to modern cognitive neuroscience!"),
        ("Tonu", "For decades, obsolete medical textbooks claimed that the human brain stopped developing after age twenty-five and that aging was just a slow, depressing loss of neurons!"),
        ("Solu", "Modern cognitive neuroscience has completely demolished that pessimistic myth!"),
        ("Tonu", "Psychologist Raymond Cattell identified two fundamental types of human intelligence: 'Fluid Intelligence' and 'Crystallized Intelligence'!"),
        ("Solu", "What is Fluid Intelligence, Solu?"),
        ("Solu", "Fluid intelligence is raw cognitive processing speed, working memory capacity, and solving abstract mathematical or logical puzzles quickly! This peaks in your early twenties."),
        ("Tonu", "Now, what is 'Crystallized Intelligence'?"),
        ("Tonu", "Crystallized intelligence is the vast, multidimensional repository of accumulated knowledge, vocabulary depth, semantic nuances, holistic pattern recognition, and social problem-solving!"),
        ("Solu", "Crystallized intelligence increases continuously across your entire life, peaking in your sixties, seventies, and eighties!"),
        ("Tonu", "Neuroimaging shows that older brains naturally utilize 'Bilateralization'—recruiting both the left and right cerebral hemispheres simultaneously to solve complex human, ethical, and organizational challenges!"),
        ("Solu", "And consider this astonishing neurological fact: learning a second language—like practicing English with us right now—builds 'Cognitive Reserve'!"),
        ("Tonu", "Medical studies conducted by Dr. Ellen Bialystok demonstrate that lifelong bilingualism delays the onset of Alzheimer's symptoms and cognitive decline by four to five full years!"),
        ("Solu", "Every new English vocabulary word, every idiom, and every sentence you speak creates fresh synaptic branches in your cerebral cortex, keeping your brain youthful and resilient!"),
        ("Tonu", "A twenty-year-old brain sees details fast; a mature brain sees the entire chessboard, detects emotional subtleties, and resolves human conflicts with profound grace."),

        # SECTION 7: INTERGENERATIONAL MENTORSHIP & THE BURNING LIBRARY
        ("Solu", "Let's explore the sacred relationship between the young and the old: 'Intergenerational Mentorship'!"),
        ("Tonu", "There is a haunting, beautiful West African proverb that states: 'When an old man or woman dies, a library burns to the ground.'"),
        ("Solu", "Think about what is contained inside an eighty-year-old human being! Decades of firsthand historical experience, survival through wars, economic depressions, lost loves, cultural shifts, and hard-earned wisdom that cannot be Googled!"),
        ("Tonu", "In modern society, we tragically segregate generations! We send children to daycare, young adults to offices, and elderly people to nursing homes where they interact only with people of their exact own age!"),
        ("Solu", "This generational apartheid deprives young people of perspective and emotional grounding, while leaving elders isolated and lonely!"),
        ("Tonu", "When young people sit with elders—asking questions, listening to their stories—and when elders offer unconditional encouragement to the young, magic happens!"),
        ("Solu", "The young provide energy, fresh questions, and technological literacy; the elders provide patience, moral compass, and eternal perspective."),

        # SECTION 8: BEFRIENDING MORTALITY & MEMENTO MORI
        ("Solu", "Let's examine how embracing the reality of aging transforms our relationship with mortality through the Stoic practice of 'Memento Mori'!"),
        ("Tonu", "What does 'Memento Mori' mean in Latin, Tonu?"),
        ("Tonu", "It means: 'Remember that you must die.'"),
        ("Solu", "To a naive culture, that sounds morbid and depressing! To a philosopher, it is the ultimate tool for living with fiery gratitude and focus!"),
        ("Tonu", "Steve Jobs, in his famous Stanford commencement address, said: 'Remembering that you are going to die is the best way I know to avoid the trap of thinking you have something to lose. You are already naked. There is no reason not to follow your heart.'"),
        ("Solu", "When you realize that your days on this Earth are numbered, you stop wasting hours arguing on social media!"),
        ("Tonu", "You stop obsessing over what petty critics think of you! You forgive people faster, you hug your children tighter, and you savor every single cup of morning coffee!"),
        ("Solu", "Death is the dark velvet canvas that makes the bright diamond of life sparkle with breathtaking beauty."),

        # SECTION 9: REDEFINING BEAUTY: LINES OF LAUGHTER & DIGNITY
        ("Solu", "Let's reclaim the definition of human physical beauty from superficial magazine covers!"),
        ("Tonu", "What is true beauty in a human face, Solu?"),
        ("Solu", "A completely smooth, frozen face without a single wrinkle reveals a face that has never felt deep sorrow, never laughed until tears rolled down, and never weathered a storm!"),
        ("Tonu", "As the legendary French actress Jeanne Moreau famously said: 'My face is my autobiography! I earned every single line on this face!'"),
        ("Solu", "The crows' feet around the eyes are lines of laughter and radiant smiles!"),
        ("Tonu", "The silver in someone's hair is a crown of dignity, marking decades of perseverance and survival!"),
        ("Solu", "The posture of a seasoned elder carries a grounded, relaxed authority that no twenty-year-old model can ever fake!"),
        ("Tonu", "Stop trying to look eighteen when you are fifty! Eighteen was an awkward, insecure rough draft; fifty is an authentic, confident masterpiece."),

        # SECTION 10: STAYING CURIOUS & YOUNG AT HEART
        ("Solu", "What is the secret to staying perpetually vibrant, energetic, and young at heart even as the calendar turns?"),
        ("Tonu", "CURIOSITY! Unstoppable, child-like curiosity!"),
        ("Solu", "People do not grow old and THEN lose their curiosity; people grow old BECAUSE they abandon their curiosity!"),
        ("Tonu", "Look at Grandma Moses, who didn't start painting her world-famous folk art canvases until she was seventy-eight years old, painting into her hundreds!"),
        ("Solu", "Look at Frank Lloyd Wright, who designed the iconic, revolutionary Guggenheim Museum in New York City in his late eighties!"),
        ("Tonu", "Read new books, learn to play the piano, learn to speak a foreign language like English, travel to unfamiliar cities, plant a garden, and ask questions!"),
        ("Solu", "When your mind is hungry to learn, your spirit remains evergreen, no matter how many candles are on your birthday cake."),

        # SECTION 10B: THE GRANDMOTHER HYPOTHESIS & EVOLUTIONARY PURPOSE
        ("Solu", "Let's explore a fascinating evolutionary anthropology theory known as 'The Grandmother Hypothesis' developed by anthropologist Kristen Hawkes!"),
        ("Tonu", "In almost all mammalian species—from dogs and horses to lions and chimpanzees—females die shortly after their reproductive years end!"),
        ("Solu", "Humans and orca killer whales are the only two species on Earth where females live for decades after their reproductive period! Why did evolution design human women to live into their seventies, eighties, and nineties?"),
        ("Tonu", "Because of the miraculous, irreplaceable power of GRANDMOTHERS!"),
        ("Solu", "Anthropological data shows that in ancestral hunter-gatherer bands, the presence of post-reproductive grandmothers dramatically increased the survival, nutrition, and emotional stability of grandchildren!"),
        ("Tonu", "Grandmothers gathered tough tuber roots, cared for weaned toddlers while mothers worked, mediated tribal conflicts, and transmitted sacred oral history and medicinal plant knowledge across generations!"),
        ("Solu", "Elders are not a burden on human evolution; elders are the evolutionary architects of human civilization, intelligence, and survival!"),

        # SECTION 11: THE ART OF LETTING GO: FROM WARRIOR TO SAGE
        ("Solu", "Let's discuss the graceful psychological transition from the 'Warrior Archetype' to the 'Sage Archetype'!"),
        ("Tonu", "In the first half of life, you must be a warrior: you fight for qualifications, establish a career, conquer challenges, and build a territory for your family."),
        ("Solu", "If you remain an aggressive warrior in the second half of life, you become pathetic—a grasping, controlling tyrant who cannot share power!"),
        ("Tonu", "The wisdom of aging invites you to put down the sword and pick up the staff of the Sage!"),
        ("Solu", "A Sage does not need to win every debate; a Sage listens. A Sage does not hoard wealth; a Sage shares wisdom, mentors others, and plants trees under whose shade they will never sit!"),
        ("Tonu", "Transitioning from accumulation to contribution is the crowning glory of a well-lived life."),

        # SECTION 12: REAL-LIFE ROLEPLAY: THE GRANDMOTHER'S WISDOM
        ("Solu", "Let's bring these principles to life with an intimate, moving conversational roleplay!"),
        ("Tonu", "In this scene, I am Maya, an anxious 29-year-old crying over turning thirty next week, and Solu is her 82-year-old grandmother, Eleanor, having afternoon tea on the porch. Let's listen!"),
        ("Solu", "Maya, darling, you have been staring into your teacup with tears in your eyes for ten minutes. What is troubling that bright head of yours?"),
        ("Tonu", "Oh, Grandma... it's my birthday on Friday. I'm turning thirty! I look in the mirror and I see these tiny lines around my eyes. I'm not married yet, I haven't bought a home, and I feel like my youth is slipping away through my fingers. I feel like it's all downhill from here."),
        ("Solu", "Oh, my sweet girl, come here. Look at my hands. Look at these age spots, these swollen knuckles, and the wrinkles covering my fingers. Do you think I would trade these hands to have my thirty-year-old hands back?"),
        ("Tonu", "Wouldn't you, Grandma? You were so gorgeous in those old photographs."),
        ("Solu", "I was pretty on the outside, Maya, but inside, at thirty, I was terrified! I worried constantly about what neighbors thought, I stayed up all night crying over silly criticisms, and I had no idea who I was!"),
        ("Tonu", "You really felt that way?"),
        ("Solu", "Every young woman does! My forties and fifties were where I found my true voice. My sixties were where I started my travel adventures. And right now, at eighty-two, sitting on this porch with you, I have never felt more free, more confident, or more deeply happy in my entire life!"),
        ("Tonu", "So thirty isn't the end of youth?"),
        ("Solu", "Thirty is when your real life finally begins, darling! It is when you stop living for other people's approval and start living for your own soul. Welcome thirty with a smile!"),
        ("Tonu", "Grandma, hearing you say that makes me feel like a heavy cloud just lifted from my shoulders."),
        ("Solu", "That roleplay reveals how the loving perspective of an elder can instantly heal the anxious illusions of youth!"),

        # SECTION 13: 6 ESSENTIAL ENGLISH IDIOMS & PHRASAL VERBS
        ("Tonu", "Now, let's explore six high-level English idioms, expressions, and phrasal verbs connected to age, wisdom, and time!"),
        ("Solu", "Our first idiom is a celebration of youthful spirit: 'young at heart'. Someone who is 'young at heart' maintains a youthful, playful, energetic, and optimistic attitude toward life, regardless of their chronological age."),
        ("Tonu", "Here is a practical example: 'Even though my grandfather just celebrated his eighty-fifth birthday, he is so young at heart that he still dances with my grandmother every Saturday night.'"),
        ("Solu", "Stay curious and young at heart! What is our second expression, Tonu?"),
        ("Tonu", "Our second idiom describes improving with maturity: 'age like fine wine'. When someone or something 'ages like fine wine', they become more attractive, more talented, more interesting, and more valuable as they grow older."),
        ("Solu", "For example: 'Her acting career has aged like fine wine; her performances in her sixties possess a depth and emotional gravitas that captivates audiences worldwide.'"),
        ("Tonu", "May your wisdom and elegance age like fine wine! What is our third expression, Solu?"),
        ("Solu", "Our third idiom describes the peak season of vitality: 'in the prime of life'. To be 'in the prime of life' means to be in the period of maximum vigor, health, success, and flourishing."),
        ("Tonu", "Let's hear an example: 'At forty-five, with deep experience and excellent fitness, she felt she was truly in the prime of her life.'"),
        ("Solu", "Flourish in the prime of your life! What is our fourth expression, Tonu?"),
        ("Tonu", "Our fourth idiom is a playful, humorous remark about getting older: 'long in the tooth'. When someone or something is described as 'long in the tooth', it means they are getting old, originally referring to horses whose gums recede as they age!"),
        ("Solu", "Here is an example: 'Our vintage sports car is getting a bit long in the tooth, but its engine still purrs like a contented kitten.'"),
        ("Tonu", "Wear your years proudly! What is our fifth idiom, Solu?"),
        ("Solu", "Our fifth idiom describes finding hope in difficulty: 'a silver lining'. A 'silver lining' is a consoling or hopeful aspect of an otherwise gloomy, difficult, or challenging situation, derived from the silver border around dark rain clouds."),
        ("Tonu", "For example: 'Losing my corporate position was painful, but the silver lining was that it gave me the courage to launch my own business.'"),
        ("Solu", "Every dark cloud carries a silver lining! And what is our sixth expression, Tonu?"),
        ("Tonu", "Our sixth idiom describes the rich years of retirement: 'the golden years'. 'The golden years' refers to the later period of adult life, usually following retirement from work, characterized by freedom, leisure, and reflection."),
        ("Solu", "Let's hear an example: 'They spent their golden years traveling through coastal villages and tending their Mediterranean olive grove.'"),

        # SECTION 14: INTERACTIVE SPEAKING PRACTICE
        ("Solu", "Now, it is time for our Interactive Speaking Challenge! This is your turn to speak English out loud with us. Open your chest, pronounce each word with warmth, dignity, and radiant confidence, and repeat each sentence!"),
        ("Tonu", "Sentence number one: 'True elegance and character age like fine wine.' Your turn!"),
        ("Solu", "Speak it with clear articulation: 'True elegance and character age like fine wine.'"),
        ("Tonu", "Superb! Sentence number two: 'No matter my biological age, I remain joyful and young at heart.' Your turn!"),
        ("Solu", "Repeat with vibrant warmth: 'No matter my biological age, I remain joyful and young at heart.'"),
        ("Tonu", "Wonderful! Sentence number three: 'In every difficult storm, we can discover a silver lining.' Your turn!"),
        ("Solu", "Say it out loud: 'In every difficult storm, we can discover a silver lining.'"),
        ("Tonu", "Sentence number four: 'I embrace each new chapter in the golden journey of life.' Your turn!"),
        ("Solu", "Let's say sentence number four together: 'I embrace each new chapter in the golden journey of life.'"),
        ("Tonu", "Phenomenal work, lovely listeners! Speaking these uplifting sentences out loud fills your English voice with wisdom, dignity, and magnetic confidence!"),
        ("Solu", "Every word you practice anchors self-acceptance and emotional maturity into your fluency."),

        # SECTION 15: REFLECTION & FAREWELL
        ("Solu", "And now, it is time for today's Weekly Reflection Question! We want you to practice writing in English down in the comment section below."),
        ("Tonu", "Here is today's question: 'Who is an older person in your family or community whom you deeply admire? What is the single most valuable piece of life advice they ever shared with you? And how will you honor your own aging process with gratitude this year?'"),
        ("Solu", "Take two minutes to write your answer in English in the comments below. Sharing your elder stories weaves an inspiring intergenerational tapestry across our worldwide family!"),
        ("Tonu", "Solu and I read through every single response, and we are moved to tears by your wisdom and love!"),
        ("Solu", "Remember: youth is a gift of nature, but age is a work of art."),
        ("Tonu", "Do not fear the passing of years; celebrate the depth, the grace, and the love you have cultivated along the way."),
        ("Solu", "Every wrinkle is a medal of survival, every gray hair is a crown of experience, and every year is a sacred gift."),
        ("Tonu", "Stand tall in your dignity, stay young at heart, and let your authentic brilliance shine."),
        ("Solu", "Speak with wisdom, live with gratitude, and keep practicing your English every single day."),
        ("Tonu", "Until next time, goodbye from Tonu!"),
        ("Solu", "And goodbye from Solu!"),
        ("Both", "Happy learning, age like fine wine, and goodbye!")
    ]
    return turns

if __name__ == "__main__":
    t = build_ep58()
    gen_common.verify_and_save(58, "scripts/daily_speak_ep58_full.txt",
                              "The Philosophy of Aging: Growing Older with Grace, Radiance & Deep Wisdom",
                              "Daily Speak English | English Listening & Speaking Practice",
                              t)
