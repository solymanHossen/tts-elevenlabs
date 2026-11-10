with open("scripts/generate_episodes_14_15_16.py", "r") as f:
    code = f.read()

ep14_add = '''    ("Solu", "Let's also talk about traditional garments and ethnic attire around the globe!"),
    ("Tonu", "Traditional clothing is such a breathtaking visual art form! Think about the exquisite silk Japanese Kimono with its wide obi sash, dyed with centuries-old botanical techniques."),
    ("Solu", "Or South Asian Sarees and Kurtas—six yards of handwoven silk or cotton draped with grace, embroidered with gold and silver zari threads!"),
    ("Tonu", "Or West African Kente cloth from Ghana, with its bold geometric patterns in vibrant gold, green, and red, where every single color and symbol represents a proverb or ancestral blessing!"),
    ("Solu", "And the Scottish Kilt, where each distinct tartan pattern represents a proud historic Highland clan."),
    ("Tonu", "Wearing traditional attire connects generations. It tells the story of your ancestors' craftsmanship, climate, and geography."),
    ("Solu", "Now let's explore traditional dances and folk music!"),
    ("Tonu", "From the fiery, passionate footwork of Flamenco in the caves of Andalusia, Spain, to the dramatic, elegant Tango in the cafes of Buenos Aires, Argentina!"),
    ("Solu", "And the rhythmic, lightning-fast footwork of Irish step dancing, or the sacred, earth-thumping drums of Native American Powwow dances."),
    ("Tonu", "Dance is a universal human language that requires zero translation. Your body becomes the instrument!"),
    ("Solu", "And what about coming-of-age rituals marking the transition from childhood to adulthood?"),
    ("Tonu", "In Latin American culture, the Quinceañera marks a young woman's fifteenth birthday with a grand ball, a ceremonial waltz with her father, and receiving her first pair of high heels."),
    ("Solu", "In Jewish tradition, the Bar Mitzvah for boys at thirteen and Bat Mitzvah for girls at twelve marks the age of religious maturity and community responsibility."),
    ("Tonu", "And in Japan, Coming of Age Day—Seijin no Hi—is celebrated on the second Monday of January, where twenty-year-olds dress in formal kimonos and suits to receive municipal blessings."),
    ("Solu", "And let's talk about body language and hand gestures that have completely opposite meanings in different countries!"),
    ("Tonu", "Oh, this is such a critical travel tip! For example, the common 'thumbs up' gesture, which means 'great job' in English-speaking countries, is considered an offensive insult in parts of the Middle East and West Africa!"),
    ("Solu", "And making a circle with your thumb and index finger—the 'OK' sign—is considered extremely vulgar in Brazil!"),
    ("Tonu", "And in Bulgaria and parts of southern India, nodding your head up and down means 'No', while shaking your head from side to side means 'Yes'!"),
    ("Solu", "Imagine asking for a table at a restaurant, the host shakes their head, and you walk away disappointed, while they were actually saying 'Yes, right this way!'"),
    ("Tonu", "That is why curiosity, patience, and a humble smile are your greatest travel companions!"),'''

target_14 = '    ("Solu", "Now, let\'s explore our special English vocabulary section! Let\'s examine seven colorful everyday idioms and expressions inspired by culture, celebrations, and traditions."),'
code = code.replace(target_14, ep14_add + "\n" + target_14)

ep15_add = '''    ("Solu", "Let's also talk about the incredible global transition to Renewable Clean Energy!"),
    ("Tonu", "Oh, renewable energy is revolutionizing power generation! Look at Iceland, where nearly one hundred percent of electricity and home heating comes from geothermal volcanic energy and hydropower!"),
    ("Solu", "Or Denmark and the United Kingdom, where massive offshore wind turbines standing in the open North Sea generate enough electricity to power millions of homes!"),
    ("Tonu", "And solar panel technology has become so affordable and efficient that millions of families are installing rooftop solar arrays and battery storage, generating their own clean electricity!"),
    ("Solu", "And what about water conservation? Fresh water is one of the most precious and vulnerable resources on Earth."),
    ("Tonu", "Less than one percent of all water on Earth is accessible fresh water! Taking shorter five-minute showers, fixing dripping faucets, and turning off the tap while brushing your teeth saves thousands of gallons a year."),
    ("Solu", "And rainwater harvesting! Collecting rainwater from gutters in rain barrels provides free, mineral-rich water for gardens and lawns without straining municipal supplies."),
    ("Tonu", "Now let's talk about the 'Right to Repair' movement and community Repair Cafes!"),
    ("Solu", "The Right to Repair! In our throwaway consumer culture, manufacturers intentionally glue electronics shut and refuse to sell replacement parts, forcing consumers to buy a brand new phone or toaster when a tiny wire snaps!"),
    ("Tonu", "Repair Cafes are community gatherings where volunteer electricians, carpenters, and tailors help neighbors fix their broken lamps, bicycles, toys, and jackets for free!"),
    ("Solu", "It keeps tons of electronic waste out of landfills, teaches valuable practical repair skills, and fosters vibrant community friendships."),
    ("Tonu", "And what about the cooling power of urban trees and urban forests?"),
    ("Solu", "Cities suffer from the 'Urban Heat Island' effect—asphalt roads and concrete buildings absorb solar heat, making cities five to ten degrees hotter than surrounding countryside!"),
    ("Tonu", "Planting leafy tree canopies along city sidewalks provides shade, absorbs carbon dioxide, filters particulate air pollution, and dramatically lowers air conditioning energy demands."),
    ("Solu", "And let's touch upon sustainable travel and ecotourism!"),
    ("Tonu", "Whenever possible, take high-speed electric trains instead of domestic short-haul flights! Rail travel produces up to eighty percent fewer carbon emissions per passenger kilometer."),
    ("Solu", "And stay in locally-owned eco-guesthouses, support indigenous wildlife conservation guides, and leave zero trash behind."),'''

target_15 = '    ("Tonu", "Now, let\'s explore our special English vocabulary section! Let\'s examine seven very common everyday English expressions and idioms inspired by nature, the environment, and weather."),'
code = code.replace(target_15, ep15_add + "\n" + target_15)

ep16_add = '''    ("Solu", "Let's also explore vocal warm-up exercises that professional actors and keynote speakers use before stepping on stage!"),
    ("Tonu", "Oh, vocal warm-ups! Your voice is a physical instrument powered by vocal cords, the diaphragm, and facial articulators."),
    ("Solu", "What is a great vocal warm-up exercise our listeners can practice right now, Tonu?"),
    ("Tonu", "Start with lip trills! Relax your lips and blow air through them making a motorboat sound: 'Brrrrrr!' It relaxes tension in your lips and jaw!"),
    ("Solu", "And practice vocal humming on an 'Mmm' sound, sliding your pitch gently up and down like a siren to wake up your vocal resonance chambers!"),
    ("Tonu", "And tongue twisters for crisp diction! Let's try a famous one: 'Unique New York, unique New York, you know you need unique New York!'"),
    ("Solu", "Or: 'Red leather, yellow leather, red leather, yellow leather!' Repeating tongue twisters trains your tongue, teeth, and lips to articulate consonants cleanly!"),
    ("Tonu", "Now let's talk about Impromptu Speaking—speaking off the cuff when you are suddenly put on the spot in a meeting or social gathering!"),
    ("Solu", "Many people freeze when a manager says: 'Solu, what is your opinion on this marketing campaign?'"),
    ("Tonu", "What is the secret framework to deliver a brilliant impromptu answer on the spot?"),
    ("Solu", "Use the PREP framework! P-R-E-P. Point, Reason, Example, Point!"),
    ("Tonu", "Let's walk our listeners through PREP!"),
    ("Solu", "P: State your main Point clearly in one sentence: 'I believe we should focus our marketing on short-form video content.'"),
    ("Tonu", "R: Give the Reason: 'Because our primary audience of young professionals consumes seventy percent of their media on mobile video.'"),
    ("Solu", "E: Share a concrete Example: 'For example, our competitor increased their lead conversion by forty percent after launching their video series last month.'"),
    ("Tonu", "P: Reiterate your main Point: 'Therefore, investing in video will deliver the highest return on our marketing budget!'"),
    ("Solu", "In sixty seconds, you have delivered a structured, persuasive, and completely coherent executive answer with zero preparation!"),
    ("Tonu", "And what should a speaker do when technical glitches happen—the microphone dies or the projector screen goes completely black?"),
    ("Solu", "Never panic or apologize repeatedly! Smile, project your voice naturally, and say with humor: 'It looks like the technology wanted to take a coffee break, but luckily my voice works without Wi-Fi!'"),
    ("Tonu", "Audiences love authentic, unflappable speakers who can laugh at unexpected hiccups."),'''

target_16 = '    ("Tonu", "Now, let\'s explore our special English vocabulary section! Let\'s examine seven colorful idioms and expressions related to public speaking, performing, and communication."),'
code = code.replace(target_16, ep16_add + "\n" + target_16)

with open("scripts/generate_episodes_14_15_16.py", "w") as f:
    f.write(code)

