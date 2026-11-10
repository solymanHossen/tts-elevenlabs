#!/usr/bin/env python3
"""
Daily Speak English - Episode 57
Title: The Sanctuary of Quiet Spaces: Public Libraries, Independent Bookstores & Slow Thought
Requirements:
- Starts with Tonu: "Hey hey, lovely listeners!..."
- Words >= 3,550 (strict duration >= 25.5 - 28.0 mins)
- High-level engaging, natural conversational English
"""

import gen_common

def build_ep57():
    turns = [
        # SECTION 1: MAGNETIC OPENING & THE SANCTUARY OF SILENCE
        ("Tonu", "Hey hey, lovely listeners! Welcome back to Daily Speak English, your favorite place to become fluent, confident, and unstoppable in English! I'm Tonu!"),
        ("Solu", "And I'm Solu! Welcome back, everyone! Today, we are stepping through heavy wooden doors, leaving behind the screaming traffic, flashing digital billboards, and ringing smartphones, into one of the most sacred, peaceful, and endangered realms on Earth: 'The Sanctuary of Quiet Spaces, Public Libraries, Independent Bookstores, and the Lost Art of Slow Thought'!"),
        ("Tonu", "Solu, think about modern commercial cities! Almost every single indoor space you enter in a 21st-century city demands your money!"),
        ("Solu", "Yes! If you sit in a café, a restaurant, a shopping mall, or a movie theater, you are a CONSUMER! You are expected to purchase coffee, buy clothes, swipe a credit card, and consume!"),
        ("Tonu", "There is only one major public institution left in the modern world where you can walk in, sit down for eight hours in a comfortable chair, read the greatest minds in human history, use the internet, ask questions to research scholars, and never be asked to pay a single penny!"),
        ("Solu", "THE PUBLIC LIBRARY! It is an absolute democratic miracle that would be impossible to invent today if it didn't already exist!"),
        ("Tonu", "And alongside libraries are independent bookstores—those warm, dusty, labyrinthine sanctuaries with wooden floorboards that creak, the intoxicating scent of aged paper, and handwritten recommendation notes tucked into novels!"),
        ("Solu", "Today, we are going to explore sociologist Ray Oldenburg's 'Third Place' theory, examine how quiet spaces heal sensory overstimulation, discover Maryanne Wolf's neuroscience of deep reading, unpack the charming Japanese concept of 'Tsundoku', explore Andrew Carnegie's library legacy, and master literary English expressions!"),
        ("Tonu", "As author Jorge Luis Borges famously wrote: 'I have always imagined that Paradise will be a kind of library.' Let's step together into that paradise!"),

        # SECTION 2: RAY OLDENBURG & THE CRISIS OF THE 'THIRD PLACE'
        ("Solu", "Let's begin by examining an influential sociological framework developed by Professor Ray Oldenburg in his classic book 'The Great Good Place': 'The Third Place'!"),
        ("Tonu", "What are the three places in human life according to Oldenburg, Solu?"),
        ("Solu", "Your 'First Place' is your HOME—where you sleep, eat, and live with your family!"),
        ("Tonu", "Your 'Second Place' is your WORKPLACE or school—where you earn your living or build your career!"),
        ("Solu", "And your 'Third Place' is the public, informal social anchor of community life! It is a neutral, accessible ground where people gather to converse, relax, read, and connect across social classes!"),
        ("Tonu", "Historically, third places were village greens, English pubs, French cafés, barbershops, public plazas, and neighborhood libraries!"),
        ("Solu", "What has happened to third places in the twenty-first century?"),
        ("Tonu", "They have been ruthlessly commercialized, privatized, or replaced by social media algorithms! People spend all day moving from home office to kitchen, trapped in a solitary digital bubble!"),
        ("Solu", "This collapse of physical third places is the root driver of the global loneliness epidemic!"),
        ("Tonu", "Public libraries and cozy independent bookshops remain the purest surviving third places—warm, welcoming, non-judgmental community living rooms open to all human beings."),

        # SECTION 3: THE ARCHITECTURE OF SILENCE & ACOUSTIC HEALING
        ("Solu", "Let's explore the restorative physical impact of stepping into a library reading room: 'The Architecture of Silence'!"),
        ("Tonu", "Think about what happens the moment you push open the heavy double doors of a grand public library—like the New York Public Library on Fifth Avenue, the British Library in London, or the Bibliothèque Nationale in Paris!"),
        ("Solu", "You walk under soaring fifty-foot arched ceilings, surrounded by warm oak tables, glowing green banker's lamps, and thousands of leather-bound books absorbing acoustic noise!"),
        ("Tonu", "Instantly, your speaking voice drops to an involuntary whisper!"),
        ("Solu", "Why does that happen, Tonu?"),
        ("Tonu", "Because silence in a library is NOT an awkward, tense void; it is a shared, collective reverent hush!"),
        ("Solu", "Acoustic ecology research shows that modern urban ambient noise—traffic sirens, subway rumbles, construction jackhammers—chronically elevates cortisol, increases cardiovascular stress, and impairs cognitive processing!"),
        ("Tonu", "When you immerse yourself in a quiet reading sanctuary, your nervous system experiences profound relief!"),
        ("Solu", "Your amygdala calms, your breathing deepens, and your working memory expands. Silence is acoustic oxygen for a suffocated mind."),

        # SECTION 4: THE DEMOCRATIC MIRACLE: FROM ALEXANDRIA TO CARNEGIE
        ("Solu", "Let's look at the fascinating history of libraries, from the ancient wonders of the world to the modern public lending systems!"),
        ("Tonu", "In the ancient world, the Great Library of Alexandria in Egypt was the intellectual capital of the Mediterranean, housing hundreds of thousands of papyrus scrolls containing the philosophy, astronomy, and mathematics of civilization!"),
        ("Solu", "When Alexandria was destroyed, an unfathomable ocean of ancient wisdom was lost to humanity forever!"),
        ("Tonu", "In the eighteenth century, books were still luxury items accessible only to wealthy aristocrats, monarchs, and private subscription clubs!"),
        ("Solu", "In 1731, Benjamin Franklin and his circle of mutual-improvement tradesmen, known as the 'Junto', pooled their money to establish the Library Company of Philadelphia—the very first successful public lending library in America!"),
        ("Tonu", "Franklin recognized that an informed, educated citizenry was the essential bedrock of a functioning democracy!"),
        ("Solu", "Then, in the late nineteenth and early twentieth centuries, came Andrew Carnegie—a Scottish immigrant boy who arrived in Pennsylvania penniless, worked as a bobbin boy in a cotton mill for $1.20 a week, and eventually built Carnegie Steel, becoming the richest industrialist on Earth!"),
        ("Tonu", "What did Carnegie do with his colossal fortune, Solu?"),
        ("Solu", "Carnegie remembered that as a poor, hungry working boy, a generous man named Colonel James Anderson opened his personal 400-volume library on Saturday afternoons to working youths. That access changed Carnegie's entire life and destiny!"),
        ("Tonu", "Carnegie declared that immense personal wealth should be treated as a sacred trust for the upliftment of humanity. He funded the construction of over 2,500 free public libraries across the United States, Britain, Canada, Australia, and New Zealand!"),
        ("Solu", "Carnegie insisted that over the grand entrance of every single library, carved into stone above the doorway, were the immortal words: 'FREE TO THE PEOPLE'!"),
        ("Tonu", "Whether you were a penniless immigrant orphan or a wealthy railroad baron, you walked through those double doors as an absolute equal citizen of the global republic of letters!"),
        ("Solu", "Every public library standing today is a living monument to human dignity, equality, and the infinite potential of an educated mind."),

        # SECTION 5: SERENDIPITY VS THE ALGORITHMIC BUBBLE
        ("Solu", "Let's contrast the experience of browsing physical library shelves with browsing Amazon or social media: 'Serendipity versus Algorithms'!"),
        ("Tonu", "When you search for something online, predictive machine learning algorithms analyze your browsing history, past purchases, and clicks, showing you things you ALREADY like!"),
        ("Solu", "If you search for science fiction, it shows you more science fiction; if you search for political opinions, it confirms your existing biases!"),
        ("Tonu", "The algorithm traps you inside a narrow, digital echo chamber, shrinking your intellectual horizon!"),
        ("Solu", "Now, compare that to physical library stacks! What happens when you walk down an aisle looking for a book on 20th-century history, Tonu?"),
        ("Tonu", "You find the book you were looking for; but right next to it on the shelf, your eyes catch an intriguing spine about deep-sea marine biology, or a translation of ancient Persian poetry, or a memoir of an Arctic explorer!"),
        ("Solu", "You pull it down, flip through the pages, and fall head-over-heels in love with a subject you never knew existed!"),
        ("Tonu", "That is SERENDIPITY—the delightful art of finding valuable things you weren't looking for!"),
        ("Solu", "Physical bookstores and libraries are engines of serendipity, breaking us out of narrow algorithmic cages and expanding our curiosity in unexpected directions."),

        # SECTION 6: INDEPENDENT BOOKSTORES & THE LEGACY OF SHAKESPEARE AND COMPANY
        ("Solu", "Let's celebrate the magic and resilience of independent neighborhood bookstores!"),
        ("Tonu", "Twenty years ago, when online mega-retailers and e-books emerged, industry analysts predicted that independent bookstores would go completely extinct within a decade!"),
        ("Solu", "And yet, independent bookstores have experienced an astonishing, defiant renaissance! Why did they survive and flourish, Tonu?"),
        ("Tonu", "Because an algorithm cannot give you what an independent bookseller gives you: HUMANITY, community curation, and literary soul!"),
        ("Solu", "Look at legendary bookstores throughout history! Think of 'Shakespeare and Company' in Paris, founded in 1919 by Sylvia Beach!"),
        ("Tonu", "Sylvia Beach's little shop on the Left Bank of the Seine was the haven and sanctuary for the entire 'Lost Generation' of writers: Ernest Hemingway, F. Scott Fitzgerald, Gertrude Stein, and James Joyce!"),
        ("Solu", "When James Joyce's masterpiece 'Ulysses' was banned in Britain and the United States, Sylvia Beach personally published it at enormous financial risk because she believed in the power of art!"),
        ("Tonu", "Look at 'City Lights Bookstore' in San Francisco, founded in 1953 by poet Lawrence Ferlinghetti, which became the spiritual home of the Beat generation and fought historic battles for free speech!"),
        ("Solu", "And consider your own local neighborhood bookstore today: the passionate staff members read hundreds of titles, writing small handwritten paper cards tucked beneath books: 'If you loved Donna Tartt, this haunting mystery will keep you up all night!'"),
        ("Tonu", "Indie bookstores host open mic poetry readings, children's story hours, local author signings, and passionate philosophical book clubs!"),
        ("Solu", "Buying a book at an independent bookstore is an act of civic love—a vote for human culture, local community, and authentic spaces."),

        # SECTION 6B: BIBLIOSMIA: THE CHEMISTRY OF THE SCENT OF OLD BOOKS
        ("Tonu", "Solu, have you ever opened an old, vintage book, buried your nose in the pages, and taken a deep, intoxicating breath?"),
        ("Solu", "Yes! It is one of the most comforting, nostalgic smells in the world! There is actually a scientific name for that scent: 'Bibliosmia'—the smell of old books!"),
        ("Tonu", "What causes that wonderful aroma scientifically, Tonu?"),
        ("Tonu", "Paper is made from wood pulp, which contains cellulose and 'Lignin'—the organic polymer that gives trees their structural rigidity!"),
        ("Solu", "As paper ages over decades, the lignin and wood chemicals slowly break down through chemical oxidation, releasing volatile organic compounds into the air!"),
        ("Tonu", "One of the primary compounds released is 'Vanillin'—the exact same chemical compound that produces the fragrance of vanilla!"),
        ("Solu", "Another compound is 'Benzaldehyde', which smells like sweet almonds, alongside floral and grassy chemical notes!"),
        ("Tonu", "So when you smell an old book, you are literally smelling a warm, subtle symphony of vanilla, sweet almonds, and grassy notes!"),
        ("Solu", "No digital e-reader or glowing screen will ever reproduce the tactile, aromatic majesty of aged paper and ink."),

        # SECTION 7: MARYANNE WOLF & THE NEUROSCIENCE OF DEEP READING
        ("Solu", "Let's examine the fascinating cognitive neuroscience of reading researched by Dr. Maryanne Wolf, Director of the Center for Dyslexia, Diverse Learners, and Social Justice at UCLA!"),
        ("Tonu", "In her bestselling book 'Reader, Come Home: The Reading Brain in a Digital World', Dr. Wolf analyzed how screen reading is rewiring our neural circuitry!"),
        ("Solu", "What happens to the human brain when we read on smartphones and tablets, Solu?"),
        ("Solu", "The brain adopts an 'F-shaped' skimming pattern! Our eyes dart across the top, down the middle, hunting for keywords, bullet points, and quick answers!"),
        ("Tonu", "We develop what Dr. Wolf calls the 'Skim-Reading Circuit'! We process vast quantities of information, but we sacrifice the deep reading processes: critical analysis, analogical thinking, deductive reasoning, and empathetic perspective-taking!"),
        ("Solu", "When you hold a physical paper book, your brain forms a spatial, tactile cognitive map!"),
        ("Tonu", "You feel the weight of the pages shifting from your right hand to your left hand as you progress; you smell the paper, you see the fixed typography!"),
        ("Solu", "That sensory grounding anchors sustained attention, allowing you to enter deep cognitive immersion where new neural connections are forged."),
        ("Tonu", "Reading a physical book is not outdated technology; it is the ultimate cognitive gym for your brain in a distracting world."),

        # SECTION 8: 'TSUNDOKU': THE JAPANESE ART OF THE UNREAD BOOK
        ("Solu", "Let's travel to Japan to explore one of the most charming, liberating cultural words in the literary world: 'Tsundoku'!"),
        ("Tonu", "What is Tsundoku, Tonu?"),
        ("Tonu", "Tsundoku is the Japanese slang term for acquiring reading materials, stacking them up in beautiful piles on your desk, nightstand, or shelves, and letting them accumulate unread!"),
        ("Solu", "Many people feel intense guilt about Tsundoku! They look at the twenty unread books on their bedside table and say: 'I'm so undisciplined! I keep buying books and never finishing them!'"),
        ("Tonu", "Nassim Nicholas Taleb, in his brilliant book 'The Black Swan', dismantled this guilt by analyzing the legendary private library of Italian novelist Umberto Eco!"),
        ("Solu", "Eco owned over thirty thousand books in his personal library! When visitors came, they would foolishly ask: 'Professor Eco, have you read all of these?'"),
        ("Tonu", "Eco would smile and say: 'No! The unread books are far more valuable than the read ones!'"),
        ("Solu", "Taleb calls this the 'Antilibrary'! An antilibrary is a collection of books you have NOT read!"),
        ("Tonu", "Read books stroke your ego, reminding you of what you know. Unread books keep you humble, curious, and constantly aware of the vast ocean of wisdom you have yet to explore!"),
        ("Solu", "Never feel guilty about buying books! A stack of unread books is an altar to curiosity and future intellectual adventures."),

        # SECTION 9: LIBRARIES IN THE 21ST CENTURY: HUBS OF EQUITY
        ("Solu", "Let's update our understanding of what modern public libraries actually do today!"),
        ("Tonu", "Many people mistakenly think libraries are just dusty warehouses of 19th-century encyclopedias!"),
        ("Solu", "In reality, the modern public library is a cutting-edge civic innovation hub!"),
        ("Tonu", "What services do modern libraries offer for free, Solu?"),
        ("Solu", "They offer high-speed internet and computer terminals for unemployed workers applying for jobs; they lend out 3D printers, podcast recording studios, and digital audio workstations!"),
        ("Tonu", "They provide free English language classes for newly arrived immigrants, citizenship tutoring, resume workshops, and free access to academic journals and expensive software!"),
        ("Solu", "Many libraries even offer 'Libraries of Things'—where you can check out gardening tools, sewing machines, musical instruments, and camping gear!"),
        ("Tonu", "During extreme weather heatwaves or freezing blizzards, public libraries open their doors as climate warming and cooling sanctuaries for vulnerable community members."),
        ("Solu", "Libraries are the beating heart of social equity, ensuring that technological progress does not leave the vulnerable behind."),

        # SECTION 10: READING AS AN EMPATHY MACHINE
        ("Solu", "Let's explore a stunning finding from social psychology: reading literary fiction makes human beings dramatically more empathetic!"),
        ("Tonu", "Drs. David Comer Kidd and Emanuele Castano published landmark studies in the journal 'Science' demonstrating that reading literary fiction directly improves 'Theory of Mind'!"),
        ("Solu", "What is Theory of Mind, Solu?"),
        ("Solu", "Theory of Mind is the psychological capacity to comprehend that other people possess beliefs, desires, emotions, and perspectives entirely different from your own!"),
        ("Tonu", "When you read a great novel—whether by Charles Dickens, Chinua Achebe, Jane Austen, or Haruki Murakami—you live inside another human being's consciousness for three hundred pages!"),
        ("Solu", "You experience life as an 18th-century orphan in London, a Nigerian village elder, a 19th-century woman navigating social rigidities, or an astronaut stranded in deep space!"),
        ("Tonu", "You feel their triumphs, their heartbreak, their fears, and their moral dilemmas!"),
        ("Solu", "No other medium on Earth matches the intimate empathy engine of the written word. Reading dissolves the walls of prejudice and reveals our shared humanity."),

        # SECTION 11: CREATING A READING NOOK & SLOW CULTURE AT HOME
        ("Solu", "How can our listeners bring the sanctuary of the library into their own busy homes and apartments?"),
        ("Tonu", "You don't need a massive Victorian mansion with mahogany bookshelves; you just need to carve out a dedicated 'Sanctuary Corner'!"),
        ("Solu", "Pick a corner of your bedroom or living room: a comfortable chair, a warm lamp with soft amber light, a cozy throw blanket, and a small side table!"),
        ("Tonu", "Establish the 'Sacred Phone-Free Zone'! When you sit in that chair, your smartphone remains in another room!"),
        ("Solu", "Dedicate twenty minutes every morning or evening to this quiet corner. Brew a warm cup of herbal tea, open a physical book, and let the outside world fade away."),
        ("Tonu", "This daily ritual of slow thought anchors your mental peace, protecting you against the hurried frenzy of modern life."),

        # SECTION 12: REAL-LIFE ROLEPLAY: THE DISCOVERY IN THE ARCHIVES
        ("Solu", "Let's illustrate these principles with an inspiring, realistic conversational roleplay!"),
        ("Tonu", "In this scene, I am Nora, a stressed university student overwhelmed by online finals, and Solu is Arthur, an elderly head librarian at an ancient city library. Let's listen!"),
        ("Solu", "Good afternoon, young lady. You look like you're carrying the weight of the entire digital universe in that heavy backpack. May I help you find something?"),
        ("Tonu", "Hello, sir. Honestly... I don't even know what I'm looking for. I've been staring at a computer screen in my dorm for three days, my eyes are throbbing with a migraine, and I just needed to escape the noise. I haven't stepped inside a public library since I was twelve."),
        ("Solu", "Ah, you're suffering from screen exhaustion! Well, Nora, you have arrived at the best hospital in the city! Follow me down this hallway to the north reading room."),
        ("Tonu", "Oh... wow. Look at this room! The tall arched windows, the smell of aged cedar... and it is so completely quiet! People are actually sitting and reading without phones!"),
        ("Solu", "Here is table fourteen, right by the sunlit window. And take a look at this shelf here: this is our collection of 19th-century botanical sketches and nature journals. No exams, no notifications, no deadlines. Just sit, breathe, and let your eyes rest."),
        ("Tonu", "Arthur, thank you. Just walking into this room feels like my racing heart finally slowed down to a peaceful tempo."),
        ("Solu", "That is the magic of these walls, Nora. Books never demand your rush; they wait patiently for you to be ready. Enjoy your quiet sanctuary."),
        ("Tonu", "That roleplay reveals how the sanctuary of quiet spaces offers restorative refuge for overstimulated modern souls!"),

        # SECTION 13: 6 ESSENTIAL ENGLISH IDIOMS & PHRASAL VERBS
        ("Tonu", "Now, let's explore six high-level English idioms, expressions, and phrasal verbs connected to books, reading, and learning!"),
        ("Solu", "Our first idiom is a classic academic expression: 'hit the books'. To 'hit the books' is an informal idiom that means to begin studying hard and seriously, especially for an exam or project."),
        ("Tonu", "Here is a practical example: 'Final exams start next Monday, so I need to clear my schedule this weekend and hit the books.'"),
        ("Solu", "Hit the books with focus and enthusiasm! What is our second expression, Tonu?"),
        ("Tonu", "Our second expression describes cozy relaxation: 'curl up with a book'. To 'curl up with a book' means to settle comfortably into a warm, relaxed position—often in an armchair or bed with a blanket—to read for pleasure."),
        ("Solu", "For example: 'On rainy Sunday afternoons, there is nothing I love more than curling up with a book and a hot cup of chamomile tea.'"),
        ("Tonu", "What a comforting image! What is our third expression, Solu?"),
        ("Solu", "Our third idiom describes strict adherence to rules: 'by the book'. To do something 'by the book' means to follow all official rules, procedures, and regulations strictly and precisely without bending them."),
        ("Tonu", "Let's hear an example: 'The financial auditor investigated every transaction by the book to ensure complete regulatory compliance.'"),
        ("Solu", "Integrity means doing things by the book! What is our fourth expression, Tonu?"),
        ("Tonu", "Our fourth idiom describes transparency versus mystery: 'an open book' versus 'a closed book'. Someone who is 'an open book' is honest, transparent, and easy to understand with no hidden secrets. Conversely, 'a closed book' is mysterious and hard to read."),
        ("Solu", "Here is an example: 'Maria is an open book; you always know exactly what she is feeling from her expressive smile.'"),
        ("Tonu", "Be open and authentic! What is our fifth idiom, Solu?"),
        ("Solu", "Our fifth idiom describes learning from someone's positive example: 'take a leaf out of someone's book'. To 'take a leaf out of someone's book' means to imitate or adopt someone's successful behavior, good habit, or wise approach."),
        ("Tonu", "For example: 'You should take a leaf out of his book and start organizing your workspace every evening before going to bed.'"),
        ("Solu", "Take a leaf out of the wise books of great mentors! And what is our sixth expression, Tonu?"),
        ("Tonu", "Our sixth idiom describes deep perceptive insight: 'read someone like a book'. To 'read someone like a book' means to understand someone's hidden thoughts, motives, or feelings easily, usually because their expressions are transparent."),
        ("Solu", "Let's hear an example: 'My mother can read me like a book; the moment I walked through the door, she knew something was troubling me.'"),

        # SECTION 14: INTERACTIVE SPEAKING PRACTICE
        ("Solu", "Now, it is time for our Interactive Speaking Challenge! This is your opportunity to speak English out loud with us. Open your chest, pronounce each syllable with warmth and poise, and repeat each sentence with steady cadence!"),
        ("Tonu", "Sentence number one: 'Public libraries are democratic sanctuaries open freely to all people.' Your turn!"),
        ("Solu", "Speak it with clear articulation: 'Public libraries are democratic sanctuaries open freely to all people.'"),
        ("Tonu", "Superb! Sentence number two: 'On rainy weekends, I love to curl up with a book in my quiet corner.' Your turn!"),
        ("Solu", "Repeat with gentle warmth: 'On rainy weekends, I love to curl up with a book in my quiet corner.'"),
        ("Tonu", "Wonderful! Sentence number three: 'Let us take a leaf out of their book and embrace lifelong curiosity.' Your turn!"),
        ("Solu", "Say it out loud: 'Let us take a leaf out of their book and embrace lifelong curiosity.'"),
        ("Tonu", "Sentence number four: 'True wisdom is cultivated through the patience of slow thought.' Your turn!"),
        ("Solu", "Let's say sentence number four together: 'True wisdom is cultivated through the patience of slow thought.'"),
        ("Tonu", "Phenomenal work, lovely listeners! Practicing these elegant phrases out loud enriches your conversational vocabulary and connects your speaking voice with literary elegance!"),
        ("Solu", "Every sentence spoken out loud strengthens your neurological pathways for fluent English."),

        # SECTION 15: REFLECTION & FAREWELL
        ("Solu", "And now, it is time for today's Weekly Reflection Question! We want you to practice writing in English down in the comment section below."),
        ("Tonu", "Here is today's question: 'What is your favorite book of all time that touched your soul or changed your worldview? And when was the last time you visited a public library or independent bookstore in your town?'"),
        ("Solu", "Take two minutes to write your answer in English in the comments below. Sharing your literary loves creates a global library of wisdom among our listeners!"),
        ("Tonu", "Solu and I read through every single comment, and we are constantly adding your recommendations to our personal reading lists!"),
        ("Solu", "Remember: in a noisy world screaming for your attention, silence is your greatest sanctuary."),
        ("Tonu", "Visit your local library, support your independent bookstore, and give your mind the unhurried gift of slow thought."),
        ("Solu", "Turn off the notifications, open a physical book, and let your imagination soar across the horizons of human history."),
        ("Tonu", "Stand tall in your curiosity, keep learning with passion, and let your authentic light shine."),
        ("Solu", "Speak with eloquence, think with depth, and keep practicing your English every single day."),
        ("Tonu", "Until next time, goodbye from Tonu!"),
        ("Solu", "And goodbye from Solu!"),
        ("Both", "Happy learning, curl up with a great book, and goodbye!")
    ]
    return turns

if __name__ == "__main__":
    t = build_ep57()
    gen_common.verify_and_save(57, "scripts/daily_speak_ep57_full.txt",
                              "The Sanctuary of Quiet Spaces: Public Libraries, Independent Bookstores & Slow Thought",
                              "Daily Speak English | English Listening & Speaking Practice",
                              t)
