#!/usr/bin/env python3
"""
Daily Speak English - Episode 60 (Grand Finale)
Title: The Grand Finale: Crafting a Remarkable, Unforgettable Life & The Journey Ahead
Requirements:
- Starts with Tonu: "Hey hey, lovely listeners!..."
- Words >= 3,550 (strict duration >= 25.5 - 28.0 mins)
- High-level engaging, natural conversational English
"""

import gen_common

def build_ep60():
    turns = [
        # SECTION 1: MAGNETIC OPENING & THE MILESTONE CELEBRATION
        ("Tonu", "Hey hey, lovely listeners! Welcome back to Daily Speak English, your favorite place to become fluent, confident, and unstoppable in English! I'm Tonu!"),
        ("Solu", "And I'm Solu! Welcome back, everyone! Today is an extraordinary, breathtaking milestone in our journey together: this is EPISODE SIXTY! Sixty monumental masterclasses of philosophy, psychology, neuroscience, emotional mastery, and spoken English fluency!"),
        ("Tonu", "Solu, can you believe how far our worldwide family has traveled together? From our very first conversations to this grand milestone, hundreds of thousands of listeners across Asia, Europe, the Americas, Africa, and the Middle East have tuned in every week to learn, grow, and transform their voices!"),
        ("Solu", "It is deeply humbling and inspiring! And for this landmark sixtieth episode, we have chosen the ultimate theme that weaves every single lesson we have ever taught into one magnificent tapestry: 'Crafting a Remarkable, Unforgettable Life and the Journey Ahead'!"),
        ("Tonu", "What does it truly mean to craft a remarkable life? Society tells us that a successful life is measured by bank account balances, luxury cars, corporate titles, and social media followers!"),
        ("Solu", "And yet, modern palliative psychology reveals that when people reach the final days of their lives, not a single human being wishes they had spent more time at the office, bought a more expensive watch, or collected more vanity metrics!"),
        ("Tonu", "They care about love, deep human connection, authentic courage, and whether their presence made this Earth a kinder, warmer place!"),
        ("Solu", "Today, we are going to explore Australian nurse Bronnie Ware's famous study 'The Top 5 Regrets of the Dying', contemplate poet Mary Oliver's immortal question about our one wild and precious life, examine the compounding mathematics of daily character, explore the profound legacy of small kindnesses, celebrate English as a global bridge to human freedom, and master triumphant English idioms!"),
        ("Solu", "As author Mark Twain wrote: 'Twenty years from now you will be more disappointed by the things that you didn't do than by the ones you did do. So throw off the bowlines. Sail away from the safe harbor. Catch the trade winds in your sails. Explore. Dream. Discover.' Let's set sail together into this grand finale!"),

        # SECTION 2: WHAT DOES IT MEAN TO LIVE A REMARKABLE LIFE?
        ("Solu", "Let's begin by dismantling the shallow commercial definitions of success and defining what actually makes a human life 'remarkable'!"),
        ("Tonu", "If you look at the word 'remarkable', it literally means worthy of being remarked upon, remembered, and noticed!"),
        ("Solu", "Does that mean you have to be a billionaire tech mogul, an Olympic gold medalist, or a Hollywood celebrity to have a remarkable life?"),
        ("Tonu", "ABSOLUTELY NOT! Some of the most hollow, miserable, lonely individuals on Earth have billions of dollars and millions of followers!"),
        ("Solu", "A truly remarkable life is measured by DEPTH, not breadth; by AUTHENTICITY, not popularity; and by LOVE, not accumulation!"),
        ("Tonu", "A remarkable life is lived by a dedicated schoolteacher who inspires generations of underprivileged children to believe in their dreams!"),
        ("Solu", "A remarkable life is lived by a loving parent who breaks cycles of generational trauma and creates a home of unconditional safety and laughter!"),
        ("Tonu", "A remarkable life is lived by an honest craftsman who takes sublime pride in building furniture that outlasts generations!"),
        ("Solu", "A remarkable life is lived by YOU, lovely listener, waking up every single morning, facing your fears, expanding your mind, mastering a new language, and bringing kindness into an often harsh world."),
        ("Tonu", "Remarkable is not what you own; remarkable is who you become and how deeply you love."),

        # SECTION 3: BRONNIE WARE & THE TOP 5 REGRETS OF THE DYING
        ("Solu", "Let's examine one of the most powerful, perspective-shifting psychological studies of our era: Australian palliative care nurse Bronnie Ware's international bestseller 'The Top Five Regrets of the Dying'!"),
        ("Tonu", "Bronnie Ware spent years counseling and holding the hands of terminally ill patients during the final twelve weeks of their lives, listening to their rawest, most unfiltered deathbed confessions."),
        ("Solu", "What was the number one, most common regret articulated by dying human beings, Solu?"),
        ("Solu", "Regret Number One was: 'I wish I'd had the courage to live a life true to myself, not the life others expected of me!'"),
        ("Tonu", "When people realize that their life is almost over and look back clearly, it is shocking how many unfulfilled dreams they left on the table because they were terrified of what family, neighbors, or society would think! They wore masks to please others, while burying their authentic passions."),
        ("Solu", "What was Regret Number Two, Tonu?"),
        ("Tonu", "Regret Number Two was: 'I wish I hadn't worked so hard!' Every single male patient Ware nursed, and many women, deeply regretted spending their precious youth on the endless corporate treadmill, missing their children growing up and missing the deep companionship of their partner!"),
        ("Solu", "They realized too late that no one remembers your overtime hours, but your children remember when you were absent for their bedtime stories!"),
        ("Tonu", "Regret Number Three was: 'I wish I'd had the courage to express my feelings!' People suppressed their anger, their truth, and their romantic love just to avoid temporary conflict, settling for a mediocre, emotionally stifled existence!"),
        ("Solu", "Regret Number Four was: 'I wish I had stayed in touch with my friends!' In the busy, frantic rush of careers and mortgages, people let golden friendships slip away through negligence, realizing too late that love and friendship are all that remain at the end!"),
        ("Tonu", "And Regret Number Five was: 'I wish that I had let myself be happier!' People realized too late that happiness is a daily conscious choice, a habit of gratitude, not a distant destination that arrives after achieving wealth!"),
        ("Solu", "Listen to these five regrets today while your heart is beating, your mind is sharp, and your lungs are full of fresh air! You have the sovereign power right now to live so that none of these regrets will ever be yours."),

        # SECTION 4: MARY OLIVER'S QUESTION: YOUR ONE WILD AND PRECIOUS LIFE
        ("Solu", "Let's turn to the Pulitzer Prize-winning American poet Mary Oliver and her iconic poem 'The Summer Day'!"),
        ("Tonu", "In that breathtaking poem, Oliver observes a simple grasshopper eating sugar out of her hand, gazes at the clouds, and asks what prayer truly is."),
        ("Solu", "And she closes the poem with a question that echoes like a clarion bell across human consciousness!"),
        ("Tonu", "She asks: 'Doesn't everything die at last, and too soon? Tell me, what is it you plan to do with your one wild and precious life?'"),
        ("Solu", "Let those words sink into your spirit: YOUR ONE WILD AND PRECIOUS LIFE!"),
        ("Tonu", "Notice the adjectives she chose: WILD—because life is untamed, unpredictable, and full of raw wonder; and PRECIOUS—because life is fragile, fleeting, and irreplaceable!"),
        ("Solu", "You do not get a rehearsal! You do not get a second practice run! Today is not a dress rehearsal for your real life; TODAY IS YOUR LIFE!"),
        ("Tonu", "Stop living on autopilot! Wake up to the sacred privilege of being alive, conscious, and capable of creating beauty."),

        # SECTION 5: CRAFTING A PERSONAL CODE OF HONOR & VALUES
        ("Solu", "To navigate the storms of life without losing your way, you must develop a personal compass: 'A Code of Honor and Core Values'!"),
        ("Tonu", "What is the difference between having goals and having core values, Solu?"),
        ("Solu", "Goals are external destinations that you achieve and check off: 'buy an apartment, get a promotion, run a marathon!' Once you achieve a goal, the excitement fades in forty-eight hours!"),
        ("Tonu", "Core values, on the other hand, are the guiding principles of HOW you navigate reality every single day: Integrity, Courage, Empathy, Generosity, Curiosity, and Loyalty!"),
        ("Solu", "A goal can be stolen from you by a market crash or an injury; but your core values can NEVER be compromised unless you surrender them yourself!"),
        ("Tonu", "Sit down this week with a pen and write down your three non-negotiable core values!"),
        ("Solu", "When tough decisions arrive—whether in business ethics, romantic relationships, or personal integrity—run every choice through your three core values!"),
        ("Tonu", "When your daily behavior aligns with your deepest values, an unshakeable sense of self-respect and peace settles into your soul."),

        # SECTION 6: THE BUTTERFLY EFFECT OF SMALL KINDNESSES
        ("Solu", "Let's explore the physics of human impact: 'The Butterfly Effect and the Legacy of Small Acts'!"),
        ("Tonu", "In chaos theory and meteorology, the butterfly effect posits that the delicate flap of a butterfly's wings in Brazil can set off a tornado in Texas weeks later!"),
        ("Solu", "In human relationships, the ripple effect of small acts of kindness and encouragement is literally infinite!"),
        ("Tonu", "Think about a kind, affirming word someone spoke to you ten or fifteen years ago! A teacher who saw your hidden talent, a stranger who smiled when you were feeling invisible, a mentor who looked into your eyes and said 'I believe in you!'"),
        ("Solu", "That person probably forgot that sentence five minutes later! But that single sentence became a burning torch of courage that guided you through decades of self-doubt!"),
        ("Tonu", "You never know who is standing on the edge of giving up today! A warm greeting, a listening ear, a generous compliment, holding a door open, or a cup of coffee bought for a stressed coworker can literally save a human life!"),
        ("Solu", "You do not need to build monuments of marble or bronze to leave an immortal legacy. Your legacy is the love, courage, and hope you plant in the hearts of every human being you encounter."),

        # SECTION 7: JAMES CLEAR, ARISTOTLE & COMPOUNDING HABITS
        ("Solu", "Let's revisit a timeless philosophical and mathematical principle that governs both financial wealth and personal destiny: 'The Law of 1% Compounding'!"),
        ("Tonu", "James Clear, author of the international phenomenon 'Atomic Habits', demonstrated that if you improve by just one percent every single day for one year, you end up thirty-seven times better by the end of twelve months!"),
        ("Solu", "And conversely, if you decline by one percent every day, you degrade almost down to absolute zero!"),
        ("Tonu", "Greek philosopher Aristotle declared twenty-four hundred years ago: 'We are what we repeatedly do. Excellence, then, is not an single act, but a habit!'"),
        ("Solu", "Character is not forged in rare, dramatic, cinematic moments on a battlefield! Character is sculpted in the quiet, microscopic choices you make every single hour of the day!"),
        ("Tonu", "Reading ten pages of a wise book instead of scrolling social media; going for a twenty-minute walk in nature instead of sitting on the couch; speaking an encouraging word instead of toxic gossip!"),
        ("Solu", "Practicing twenty minutes of spoken English out loud every morning instead of procrastinating!"),
        ("Tonu", "Small, positive choices compound like interest in a bank account! Over five, ten, and twenty years, those microscopic daily habits transform you into an intellectual, physical, and emotional powerhouse."),

        # SECTION 8: EMBRACING THE SPIRIT OF ADVENTURE & THE UNKNOWN
        ("Solu", "Let's talk about the courage to step off the paved road and embrace the thrilling mystery of the unknown!"),
        ("Tonu", "Most people spend their entire lives trying to eliminate all risk, uncertainty, and unpredictability! They want a five-year guarantee for everything!"),
        ("Solu", "And in doing so, they eliminate all adventure, all discovery, all growth, and all spontaneous wonder from their existence!"),
        ("Tonu", "A ship in a harbor is completely safe, anchored securely to the wooden dock. But that is NOT what ships were built for!"),
        ("Solu", "Ships were built to brave the high seas, ride the towering ocean swells, navigate by the midnight constellations, and discover brand-new continents!"),
        ("Tonu", "Say yes to the adventure! Travel to a country where you don't speak the native tongue; start the creative business that scares you; invite the person you admire for coffee; move to the city that excites your soul!"),
        ("Solu", "Life begins at the very outer edge of your comfort zone. When you leap, the net appears."),

        # SECTION 9: ENGLISH AS A PASSPORT TO GLOBAL CITIZENSHIP
        ("Solu", "Now, let's reflect on the transformative role that spoken English plays in crafting your remarkable, limitless life!"),
        ("Tonu", "To many students in school, English was taught as a dry, intimidating, punitive academic subject: memorizing irregular verb tables, filling in grammar bubbles with pencils, and taking stressful exams!"),
        ("Solu", "And that was an educational tragedy, because ENGLISH IS NOT A SUBJECT; ENGLISH IS A SUPERPOWER!"),
        ("Tonu", "Holy Roman Emperor Charlemagne famously proclaimed over a thousand years ago: 'To have another language is to possess a second soul!'"),
        ("Solu", "Think about that! When you learn English, you are not just memorizing words; you are acquiring a second soul, a second perspective, and a second worldview!"),
        ("Tonu", "English is the modern global lingua franca—the universal bridge connecting two billion human beings across every continent, country, and culture on Earth!"),
        ("Solu", "English allows you to read breakthrough scientific research before it is translated, access global remote careers, negotiate international contracts, travel anywhere on Earth with sovereign confidence, and build lifelong friendships with people across the globe!"),
        ("Tonu", "Every time you practice English with Solu and me, you are expanding your cognitive universe and claiming your rightful seat as an empowered global citizen!"),
        ("Solu", "Speak English with pride, speak with your authentic native accent, speak with unshakeable joy, and let your voice be heard across the world."),

        # SECTION 10: THE 60-EPISODE JOURNEY: A CELEBRATION OF GROWTH
        ("Solu", "Let's pause and take a magnificent look back across our sixty-episode voyage on Daily Speak English!"),
        ("Tonu", "Think about the incredible landscapes of human knowledge we have explored together!"),
        ("Solu", "We decoded first impressions and body language; we tackled the realities of digital nomadism and remote work freedom; we explored gut health and mindful nutrition!"),
        ("Tonu", "We mastered difficult conversations and boundary setting; we unlocked sleep architecture and the neuroscience of rest; we celebrated the quiet superpowers of introverts!"),
        ("Solu", "We dismantled imposter syndrome; embraced minimalism and clutter-free living; traveled slowly across cultures; cultivated the beginner's mind of curiosity!"),
        ("Tonu", "We explored mental toughness with Navy SEALs and Stoics; bathed our senses in wild forests; savored the bittersweet warmth of nostalgia; unlocked the sanctuary of libraries; celebrated growing older with grace; and ignited post-traumatic growth and hope!"),
        ("Solu", "Every single episode was a stone laid in the cathedral of your personal growth and linguistic mastery!"),
        ("Tonu", "We are so extraordinarily proud of your dedication, your consistency, and your brilliant courage!"),

        # SECTION 10B: THE TORCHBEARERS: PASSING THE FLAME TO OTHERS
        ("Solu", "What is the ultimate responsibility of someone who has acquired wisdom, fluency, and inner strength?"),
        ("Tonu", "To pass the torch! To illuminate the path for others!"),
        ("Solu", "The Roman philosopher Seneca wrote: 'If wisdom were given to me on the condition that I must keep it shut up and not impart it to others, I would reject it!'"),
        ("Tonu", "True greatness is never selfish! When you become confident in English, mentor someone who is struggling!"),
        ("Solu", "When you achieve success in your career, reach your hand down and pull someone up behind you!"),
        ("Tonu", "Be an encourager, be a mentor, and be a light in your community. A candle loses nothing by lighting another candle; it simply makes the whole room brighter!"),

        # SECTION 11: REAL-LIFE ROLEPLAY: THE STUDIO REFLECTION & TOAST
        ("Solu", "Let's bring this landmark episode to life with an intimate, heartfelt conversation between Tonu and me, right here in the Daily Speak English studio!"),
        ("Tonu", "Solu, look at the microphone in front of us, look at our studio notebooks, and look at the warm amber soundboard lights. It feels like just yesterday we stepped into this studio for Episode One!"),
        ("Solu", "I know, Tonu! We were full of nervous excitement, wondering if anyone out there in the world would connect with our vision of combining deep human philosophy with natural spoken English fluency."),
        ("Tonu", "And today, reading the thousands of heartfelt comments from listeners in Tokyo, Berlin, São Paulo, Cairo, Dhaka, Seoul, London, Nairobi, Paris, and Toronto... it brings tears of pure gratitude to my eyes!"),
        ("Solu", "Think about what our listeners have accomplished over these sixty episodes! People who were terrified to speak a single sentence of English in public are now confidently leading international boardroom meetings, traveling solo across foreign continents, making new friends, and expressing their deepest ideas with poise!"),
        ("Tonu", "That is the greatest reward we could ever dream of! English is no longer their barrier; English has become their wings to soar across the globe."),
        ("Solu", "Here is to our incredible global family! Let's raise our studio mugs of warm tea in a heartfelt toast: to every listener who believed in themselves, practiced in their cars on the way to work, listened while jogging, repeated sentences in their kitchens, and refused to let fear silence their voice!"),
        ("Tonu", "To your bravery, your relentless consistency, your radiant brilliance, and the magnificent, unforgettable life you are crafting every single day!"),
        ("Solu", "Cheers to our listeners, cheers to sixty masterclasses together, and cheers to the limitless horizons waiting ahead!"),

        # SECTION 12: 6 ESSENTIAL ENGLISH IDIOMS & PHRASAL VERBS
        ("Tonu", "Now, let's explore six high-level, triumphant English idioms, expressions, and phrasal verbs connected to legacy, ambition, and living a remarkable life!"),
        ("Solu", "Our first idiom is a powerful declaration of purposeful impact: 'make one's mark'. To 'make one's mark' means to achieve significant success, distinction, or recognition, leaving a lasting and positive impression on the world or an industry."),
        ("Tonu", "Here is a practical example: 'Through her groundbreaking research in clean solar energy, Dr. Chen truly made her mark on the scientific community.'"),
        ("Solu", "Go out and make your mark on the world! What is our second expression, Tonu?"),
        ("Tonu", "Our second expression is the timeless Latin imperative of living fully: 'seize the day', translated from the ancient Roman poet Horace's 'Carpe Diem'! To 'seize the day' means to make the most of the present moment, taking advantage of opportunities with enthusiasm and zero delay."),
        ("Solu", "For example: 'Instead of putting off her travel dreams for retirement, she seized the day and booked a hiking expedition across the Andes mountains.'"),
        ("Tonu", "Seize the day while the sunshine is warm! What is our third expression, Solu?"),
        ("Solu", "Our third idiom describes creating an enduring positive impact: 'leave a legacy'. To 'leave a legacy' means to provide or accomplish something meaningful that will benefit, inspire, and continue to exist for future generations long after you are gone."),
        ("Tonu", "Let's hear an example: 'The founder's true legacy was not the profits of his company, but the charitable education foundation that sent ten thousand orphans to college.'"),
        ("Solu", "Live your life to leave a proud legacy! What is our fourth expression, Tonu?"),
        ("Tonu", "Our fourth idiom describes boundless potential: 'the sky is the limit'. When someone says 'the sky is the limit', it means there is virtually no limit to what someone can achieve, earn, or experience if they set their mind to it."),
        ("Solu", "Here is an example: 'With your deep work ethic, emotional intelligence, and English fluency, the sky is the limit for your international career!'"),
        ("Tonu", "Remember that always: the sky is the limit! What is our fifth idiom, Solu?"),
        ("Solu", "Our fifth idiom describes pioneering positive change for others: 'pave the way'. To 'pave the way' means to create conditions, opportunities, or smooth paths that make it easier for others to follow, succeed, or make progress in the future."),
        ("Tonu", "For example: 'Pioneering female scientists paved the way for generations of young girls to pursue careers in aerospace engineering and medicine.'"),
        ("Solu", "Pave the way for those who come behind you! And what is our sixth expression, Tonu?"),
        ("Tonu", "Our sixth idiom describes trusting your inner wisdom: 'go with one's gut'. To 'go with one's gut' means to trust your intuition, internal instincts, and deepest feelings when making an important choice, rather than over-analyzing logical details."),
        ("Solu", "Let's hear an example: 'The data seemed neutral, but he went with his gut and invested in the renewable startup, which proved to be the best decision of his career.'"),

        # SECTION 13: INTERACTIVE SPEAKING PRACTICE
        ("Solu", "Now, it is time for our Interactive Speaking Challenge! For this landmark sixtieth episode, stand up, open your chest, project your voice with supreme triumph, radiant warmth, and unstoppable confidence, and repeat each sentence!"),
        ("Tonu", "Sentence number one: 'I seize the day, trust my inner compass, and make my mark on the world.' Your turn!"),
        ("Solu", "Speak it with commanding power: 'I seize the day, trust my inner compass, and make my mark on the world.'"),
        ("Tonu", "Outstanding! Sentence number two: 'When I speak with courage and authentic truth, the sky is the limit.' Your turn!"),
        ("Solu", "Repeat with vibrant clarity: 'When I speak with courage and authentic truth, the sky is the limit.'"),
        ("Tonu", "Wonderful! Sentence number three: 'Through kindness and excellence, I pave the way for future generations.' Your turn!"),
        ("Solu", "Say it out loud: 'Through kindness and excellence, I pave the way for future generations.'"),
        ("Tonu", "Sentence number four: 'I am crafting a remarkable, wild, and precious life filled with love and purpose.' Your turn!"),
        ("Solu", "Let's say sentence number four together with all our hearts: 'I am crafting a remarkable, wild, and precious life filled with love and purpose.'"),
        ("Tonu", "BRAVO! BRAVO, LOVELY LISTENERS! That was absolutely magnificent! Hear the resonance, the strength, and the unshakeable confidence in your speaking voice!"),
        ("Solu", "You are not the same person who started this journey. You have expanded your mind, your heart, and your linguistic power."),

        # SECTION 14: GRAND FINALE REFLECTION & FAREWELL
        ("Solu", "And now, it is time for our Grand Finale Reflection Question! We want you to celebrate your growth and write your manifesto in English down in the comment section below."),
        ("Tonu", "Here is today's milestone question: 'Looking back across this entire series, how has your English confidence and personal mindset transformed? What was your favorite episode that touched your soul? And what is the single biggest dream you will courageously pursue this year to make your mark on the world?'"),
        ("Solu", "Write your manifesto in English in the comments below! Share your heart, cheer for your fellow listeners, and celebrate your victory with our global community!"),
        ("Tonu", "Solu and I read through every single comment, and we will be right there in the comments cheering, clapping, and celebrating your incredible journey!"),
        ("Solu", "Remember: your voice is your unique, sacred gift to humanity. Never let fear, doubt, criticism, or perfectionism silence the song inside your soul."),
        ("Tonu", "Step boldly into the world. Speak with radiance, love without reservation, forgive quickly, and live with fiery, unquenchable passion."),
        ("Solu", "The journey of learning never ends; it simply opens wider into new, magnificent horizons. Keep reading, keep listening, and keep speaking every single day."),
        ("Tonu", "Stand tall, shine your brilliant light, seize every single day, and know that you are capable of extraordinary greatness."),
        ("Solu", "Until our next grand adventure, goodbye from Solu!"),
        ("Tonu", "And goodbye from Tonu!"),
        ("Both", "Happy learning, seize the day, make your mark, and goodbye!")
    ]
    return turns

if __name__ == "__main__":
    t = build_ep60()
    gen_common.verify_and_save(60, "scripts/daily_speak_ep60_full.txt",
                              "The Grand Finale: Crafting a Remarkable, Unforgettable Life & The Journey Ahead",
                              "Daily Speak English | English Listening & Speaking Practice",
                              t)
