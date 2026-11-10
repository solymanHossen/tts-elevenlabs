#!/usr/bin/env python3
"""
Daily Speak English - Episode 38
Title: Minimalism, Clutter-Free Living & Decluttering Your Life
Requirements:
- Starts with Tonu: "Hey hey, lovely listeners!..."
- Words >= 3,550 (strict duration >= 25.5 - 28.0 mins)
- High-level engaging, natural conversational English
"""

import gen_common

def build_ep38():
    turns = [
        # SECTION 1: MAGNETIC OPENING
        ("Tonu", "Hey hey, lovely listeners! Welcome back to Daily Speak English, your favorite place to become fluent, confident, and unstoppable in English! I'm Tonu!"),
        ("Solu", "And I'm Solu! Welcome back to another empowering session of Daily Speak English! Today, we are taking a deep breath of fresh air and examining a movement that has transformed millions of overwhelmed modern lives: Minimalism, intentional simplicity, and the liberating psychology of decluttering!"),
        ("Tonu", "Solu, think about the spaces we inhabit every single day! Look inside our closets packed with clothes we haven't worn in three years; look at our desks overflowing with ancient paperwork, tangled cables, and random gadgets; look at our phones buzzing with eighty unread notifications and thousands of unorganized photos!"),
        ("Solu", "It is overwhelming, Tonu! We live in a culture that bombards us twenty-four hours a day with the aggressive marketing message that happiness, status, and security are found by acquiring MORE stuff! More clothes, more shoes, more kitchen appliances, bigger cars, and larger apartments!"),
        ("Tonu", "Yet despite having more material possessions than any previous generation in human history, rates of chronic stress, anxiety, overwhelm, and financial panic have reached historic highs!"),
        ("Solu", "Because the tragic reality is that every single physical item you bring into your home demands a piece of your precious life energy! You have to clean it, store it, organize it, repair it, insure it, protect it, and eventually dispose of it!"),
        ("Tonu", "As author Joshua Becker beautifully said: 'Minimalism isn't about owning less than you need; it's about making room for more of what matters!'"),
        ("Solu", "Today, we are going to explore the scientific connection between clutter and cortisol, examine psychological traps like the Diderot Effect and Sunk Cost Fallacy, share practical decluttering frameworks like Swedish Death Cleaning, and master everyday English that will enrich your vocabulary!"),

        # SECTION 2: THE UCLA STUDY: CLUTTER & CORTISOL
        ("Tonu", "Let's begin by looking at the hard scientific research! Many people assume that having a messy room is just an aesthetic issue, but a landmark nine-year study conducted by researchers at the University of California, Los Angeles, known as the UCLA Center on Everyday Lives of Families, uncovered something alarming!"),
        ("Solu", "What did the UCLA researchers discover when they studied modern households, Tonu?"),
        ("Tonu", "They tracked thirty-two middle-class families and measured their saliva levels of cortisol, the body's primary stress hormone, throughout the day!"),
        ("Solu", "And what was the result?"),
        ("Tonu", "They discovered a direct, undeniable correlation: whenever mothers walked into rooms filled with high concentrations of physical clutter, their cortisol levels spiked dramatically!"),
        ("Solu", "Why does visual clutter elevate stress hormones in our bodies?"),
        ("Tonu", "Because your brain treats physical clutter as unfinished cognitive work! Every pile of unopened mail, every pile of unfolded laundry, and every dusty box in the hallway screams at your subconscious mind: 'Clean me! Organize me! Fix me!'"),
        ("Solu", "Your visual cortex is bombarded with competing stimuli! It prevents your nervous system from relaxing, keeping you trapped in a low-grade state of chronic fight-or-flight!"),
        ("Tonu", "A tidy, clear physical space creates an open, tranquil mental sanctuary. Clearing your physical room is literally clearing your mind!"),

        # SECTION 3: THE DIDEROT EFFECT: THE INFINITE CONSUMPTION SPIRAL
        ("Solu", "Now let's examine a famous psychological trap discovered in the eighteenth century by the French philosopher Denis Diderot: 'The Diderot Effect'!"),
        ("Tonu", "Denis Diderot was a brilliant philosopher and the co-founder of the first modern encyclopedia, but he lived in poverty for most of his life. Then, Catherine the Great, Empress of Russia, heard of his financial struggles and bought his library for a massive fortune!"),
        ("Solu", "Suddenly, Diderot was wealthy! And with his new money, he bought a magnificent, luxurious scarlet dressing gown."),
        ("Tonu", "He was thrilled with his beautiful new robe! But then, he looked around his humble study room. He noticed that his old straw chair looked cheap next to his elegant scarlet robe! So he threw away the chair and bought an expensive leather armchair!"),
        ("Solu", "Then he noticed that his old wooden desk looked ragged next to his leather armchair! So he bought an ornate, expensive mahogany desk!"),
        ("Tonu", "Then his old tapestries and paintings looked dingy, so he replaced all of his art! Within a few months, he had replaced every single item in his apartment, spent all of his fortune, and ended up deeply in debt, miserable, and surrounded by cold luxury!"),
        ("Solu", "In his famous essay, 'Regrets on Parting with My Old Dressing Gown', Diderot wrote: 'I was absolute master of my old robe. I have become the slave of my new one.'"),
        ("Tonu", "Think about how often that happens today! You buy a new pair of shoes, and suddenly you feel you need a new matching jacket, new pants, a new handbag, and a new watch!"),
        ("Solu", "That is the Diderot Effect! The introduction of one new luxury possession creates an artificial spiral of dissatisfaction that drives endless consumption."),

        # SECTION 4: THE SUNK COST FALLACY & CLUTTER GUILT
        ("Solu", "Now, let's address the emotional guilt that prevents people from letting go of items: 'The Sunk Cost Fallacy' and 'Gift Guilt'!"),
        ("Tonu", "Have you ever opened your closet, looked at an expensive leather jacket that doesn't fit you and that you never wear, and thought: 'I spent four hundred dollars on this jacket! I can't possibly give it away or donate it, because that would be wasting four hundred dollars!'"),
        ("Solu", "That is the classic Sunk Cost Fallacy! The money you spent on that jacket is already gone! It vanished the exact moment you swiped your credit card at the store!"),
        ("Tonu", "Keeping that unworn jacket hanging in your closet for five years does NOT bring the four hundred dollars back! In fact, keeping it costs you emotional guilt and valuable closet space every single morning you look at it!"),
        ("Solu", "The money is gone, but keeping the clutter continues the punishment!"),
        ("Tonu", "And what about gifts from friends and family? People say: 'My aunt gave me this hideous porcelain clown statue ten years ago. I hate it, but she gave it to me out of love, so I must keep it forever!'"),
        ("Solu", "Remember this profound truth: The true purpose of a gift is to express love and connection at the moment of giving! Once the gift is received and gratitude is expressed, its mission is fulfilled!"),
        ("Tonu", "The giver wanted you to feel loved; they never intended to burden your living room with a permanent dust collector! You can honor the love while letting go of the physical object."),

        # SECTION 5: MARIE KONDO VS SWEDISH DEATH CLEANING
        ("Solu", "Let's explore two world-famous decluttering philosophies: Marie Kondo's 'KonMari Method' and Margareta Magnusson's 'Swedish Death Cleaning'!"),
        ("Tonu", "Japanese organizing consultant Marie Kondo revolutionized the world with her concept: 'Does it spark joy?'"),
        ("Solu", "Kondo advises taking every single item out of your drawers, holding it with both hands, and feeling your body's visceral response. If it sparks joy, keep it with honor. If it does not, express sincere gratitude for its service and release it!"),
        ("Tonu", "And now, look at the Scandinavian perspective: 'Döstädning' or 'Swedish Death Cleaning', introduced by author Margareta Magnusson!"),
        ("Solu", "The name sounds intense, but Swedish Death Cleaning is an act of deep kindness and practical love!"),
        ("Tonu", "In Swedish culture, as you grow older or transition through life stages, you look at all your accumulated possessions and ask: 'If I were to pass away tomorrow, would my children or loved ones want to spend weeks digging through these boxes of old receipts, broken tools, and useless junk?'"),
        ("Solu", "If the answer is no, you declutter it now so your family doesn't inherit an overwhelming burden of garbage and logistical stress!"),
        ("Tonu", "Whether you use Spark Joy or Swedish Death Cleaning, the goal is the same: to surround yourself only with items that serve an active purpose or bring authentic joy to your heart."),

        # SECTION 6: THE 90/90 RULE & THE PACKING PARTY
        ("Solu", "Let's share two phenomenal tactical tools from Joshua Fields Millburn and Ryan Nicodemus, famously known as 'The Minimalists'!"),
        ("Tonu", "Tool number one is 'The 90/90 Rule'! When you are looking at an item in your home and debating whether to keep it, ask yourself two honest questions:"),
        ("Solu", "Question one: Have I used this item in the past ninety days?"),
        ("Tonu", "And Question two: If not, will I definitely use it in the next ninety days?"),
        ("Solu", "If the answer to both questions is no, you don't need it! Let it go! Donate it to someone who can actually use it today!"),
        ("Tonu", "And tool number two is the radical experiment known as 'The Packing Party'!"),
        ("Solu", "Ryan Nicodemus was depressed and surrounded by expensive gadgets. So his best friend helped him pack every single item in his entire apartment into brown cardboard moving boxes, as if he were moving away!"),
        ("Tonu", "His clothes, his dishes, his books, his electronics—everything was in taped boxes!"),
        ("Solu", "Over the next twenty-one days, Ryan only unpacked an item when he specifically needed to use it: a toothbrush, a frying pan, two work shirts, a pair of jeans, a towel."),
        ("Tonu", "And do you know what happened after twenty-one days, Solu?"),
        ("Solu", "Eighty percent of his possessions were still sitting untouched inside the cardboard boxes! He realized that eighty percent of what he owned didn't contribute to his daily life at all!"),
        ("Tonu", "He sold and donated those boxes, and said he had never felt lighter, freer, or more at peace!"),

        # SECTION 7: THE CAPSULE WARDROBE & DECISION FATIGUE
        ("Solu", "Now let's step into the bedroom and examine the concept of 'The Capsule Wardrobe'!"),
        ("Tonu", "How many times have you stood in front of a closet crammed with sixty shirts and thirty pairs of pants, and groaned: 'I have literally nothing to wear!'"),
        ("Solu", "Psychologists call this 'The Paradox of Choice'! When you have too many mismatched, ill-fitting options, your brain experiences decision fatigue before your day even starts!"),
        ("Tonu", "A Capsule Wardrobe is a curated collection of thirty to forty versatile, high-quality, timeless clothing pieces that all coordinate effortlessly with each other!"),
        ("Solu", "Think of visionary leaders like Steve Jobs with his iconic black turtleneck, Mark Zuckerberg with his gray t-shirts, or Barack Obama who only wore navy or gray suits!"),
        ("Tonu", "Obama said in an interview: 'You will see I wear only gray or blue suits. I'm trying to pare down decisions. I don't want to make decisions about what I'm eating or wearing. Because I have too many other decisions to make!'"),
        ("Solu", "When you pare down your wardrobe to clothes that fit you impeccably, feel comfortable, and look sharp, getting dressed takes two minutes, and you step out the door looking elegant every day!"),

        # SECTION 8: DIGITAL MINIMALISM & ATTENTION SANCTUARY
        ("Tonu", "We cannot talk about decluttering without addressing our digital environments: what professor Cal Newport calls 'Digital Minimalism'!"),
        ("Solu", "Physical clutter is in your living room, but digital clutter lives inside your pocket, vibrating and buzzing against your body twenty-four hours a day!"),
        ("Tonu", "Look at the average smartphone: eighty downloaded apps, six thousand unorganized screenshots, five email accounts with twelve thousand unread newsletters, and seventy-five browser tabs open!"),
        ("Solu", "How do we practice digital decluttering, Tonu?"),
        ("Tonu", "Step one: Turn off all push notifications except direct personal phone calls and text messages from real human beings! No app should interrupt your train of thought with a sale on sneakers!"),
        ("Solu", "Step two: Delete apps you haven't opened in thirty days! If you need to use an airline or banking service once a year, you can use their website!"),
        ("Tonu", "Step three: Practice 'Inbox Zero'! Unsubscribe aggressively from marketing emails using the search word 'unsubscribe'. If a newsletter doesn't educate or inspire you, send it to the digital trash bin!"),
        ("Solu", "Reclaiming your digital attention gives you back four to five hours of deep focus every single day."),

        # SECTION 9: SENTIMENTAL OBJECTS & PRESERVING MEMORIES
        ("Tonu", "Let's tackle the hardest category of decluttering: sentimental items, childhood trophies, inherited porcelain, and letters from old friends."),
        ("Solu", "People cling to sentimental objects because they mistakenly believe that discarding the physical object means erasing the memory or dishonoring the person!"),
        ("Tonu", "Always remember: The memory does not live inside the ceramic teacup; the memory lives inside your soul!"),
        ("Solu", "Here is a brilliant modern solution: Take a high-resolution photograph of the sentimental object!"),
        ("Tonu", "Create a digital scrapbook titled 'Treasured Memories'. Photograph your high school trophy, your grandmother's vintage sewing basket, or your child's kindergarten painting, and write a three-sentence caption about why it was special!"),
        ("Solu", "Then, donate or release the physical item! Whenever you want to reminisce, you can flip through your beautiful photo album without letting boxes of dusty objects consume your living space."),

        # SECTION 10: MINDFUL CONSUMPTION & THE 30-DAY RULE
        ("Solu", "Decluttering your home is only half the battle. If you clean out your house on Saturday, but go to the shopping mall on Sunday and buy ten new bags of items, the clutter returns within a month!"),
        ("Tonu", "How do we stop the flow of clutter at the front door? By adopting 'The 30-Day Purchase Rule'!"),
        ("Solu", "How does the 30-Day Rule work, Tonu?"),
        ("Tonu", "Whenever you feel a sudden impulse to buy a non-essential item—a new gadget, a pair of designer boots, a decorative vase—write the item, price, and date down on a wishlist."),
        ("Solu", "Then, wait thirty days! Do not buy it immediately!"),
        ("Tonu", "Ninety percent of the time, when thirty days pass, the emotional dopamine rush has faded, and you realize: 'I don't actually need or want this at all! I was just bored or stressed!'"),
        ("Solu", "And if you still genuinely desire it after thirty days, you can buy it with intentionality and joy!"),

        # SECTION 11: FAST FASHION & THE 'COST PER WEAR' METRIC
        ("Tonu", "Let's also look at the massive environmental and financial trap known as 'Fast Fashion'!"),
        ("Solu", "In recent years, giant fast-fashion retail websites have made it possible to buy a trendy top for five dollars or a jacket for twelve dollars with two taps on a screen!"),
        ("Tonu", "People buy entire hauls of thirty garments, wear them once for an Instagram photograph, and then throw them away or shove them to the back of the closet!"),
        ("Solu", "And billions of tons of cheap synthetic polyester clothing end up rotting in landfills in the Atacama Desert in Chile or floating down rivers in West Africa, shedding toxic microplastics into our drinking water!"),
        ("Tonu", "How do we escape this cycle? By calculating what smart shoppers call 'Cost Per Wear'!"),
        ("Solu", "Explain the Cost Per Wear calculation, Tonu!"),
        ("Tonu", "Imagine you buy a cheap, poorly made twenty-dollar dress. The fabric is itchy, the seams rip, and you only wear it two times before throwing it out. What was the cost per wear? Ten dollars per wear!"),
        ("Solu", "Now imagine you invest in a classic, beautifully tailored eighty-dollar wool sweater. It feels incredible against your skin, looks elegant, and you wear it eighty times across three winters. What was the cost per wear? Only one dollar per wear!"),
        ("Tonu", "Buy fewer things, but buy pieces made with craftsmanship, natural fabrics, and durability! You save thousands of dollars, protect the planet, and always look impeccable!"),

        # SECTION 12: THE 'ONE IN, ONE OUT' RULE & CONTAINER PRINCIPLE
        ("Solu", "To keep your home permanently organized and prevent clutter from creeping back in, let's share two golden rules: 'The One In, One Out Rule' and 'The Container Principle'!"),
        ("Tonu", "The One In, One Out Rule is simple: whenever a new item enters your house, an equivalent old item must leave!"),
        ("Solu", "If you buy a new pair of running shoes, an old pair must be donated or recycled! If you bring home a new coffee mug, one old mug gets gifted!"),
        ("Tonu", "This creates an equilibrium where your inventory never expands uncontrollably!"),
        ("Solu", "And pairing that with 'The Container Principle' is pure genius! A container—whether it is a bookshelf, a spice rack, a shoe cabinet, or a wardrobe—sets the physical boundary of your life!"),
        ("Tonu", "Instead of buying a larger bookshelf when your books overflow, recognize that the bookshelf is full! That container boundary tells you it is time to donate five books you have already read to make room for the new ones!"),
        ("Solu", "Let your physical containers dictate your limits, not the other way around!"),
        ("Tonu", "When you treat your home as a sanctuary with fixed boundaries rather than an infinite storage warehouse, cleaning becomes effortless and your environment remains peaceful."),
        ("Solu", "It creates a beautiful rhythm of living where maintenance takes ten minutes a day instead of stealing your entire weekend."),

        # SECTION 13: LIVE ROLEPLAY: DECLINING FREE PROMOTIONAL MERCHANDISE & SETTING INTENTIONAL BOUNDARIES
        ("Solu", "Now let's demonstrate a realistic real-world roleplay! Imagine you are attending a conference, exhibition, or corporate event, and people are handing out free promotional bags, cheap plastic water bottles, pens, and branded t-shirts."),
        ("Tonu", "Most people accept every free item because it is 'free', only to take it home and shove it into an overflowing drawer!"),
        ("Solu", "Let's demonstrate how to politely and gracefully decline free junk without feeling awkward! Tonu, hand me some swag."),
        ("Tonu", "Here you go, sir! Take this complimentary promotional tote bag filled with branded keychains, pens, and our company water bottle!"),
        ("Solu", "Here is how you respond with warmth and minimalism: 'Thank you so much for the generous offer! Those look really cool, but I am currently practicing a clutter-free lifestyle and keeping my bags light. Please save them for someone who will get great use out of them! Have a wonderful event!'"),
        ("Tonu", "Notice how polite and refreshing that is! You expressed genuine gratitude, set your boundary, and freed yourself from dragging home useless plastic clutter!"),
        ("Solu", "Just because something is free does not mean it has zero cost to your mental peace!"),

        # SECTION 12: VOCABULARY & IDIOM SPOTLIGHT (6 KEY IDIOMS)
        ("Tonu", "Now, let's step into our signature vocabulary segment: Key Everyday English Idioms and Phrases! Today, we have selected six colorful, essential expressions about minimalism, tidiness, and simplicity!"),
        ("Solu", "Let's master them together! Tonu, what is our very first idiom for today?"),
        ("Tonu", "Our first expression is 'clear out'. To 'clear out' means to remove unwanted things, trash, or clutter from a room, container, or space to make it clean and organized."),
        ("Solu", "Let's listen to a natural conversational example: 'This Saturday, we are going to clear out the garage and donate all our old camping gear to the local shelter.'"),
        ("Tonu", "Perfect! What is our second expression, Solu?"),
        ("Solu", "Our second expression is 'part with'. To 'part with something' means to give away, sell, or discard a possession, often when it is emotionally difficult or reluctant to do so."),
        ("Tonu", "Here is how you can use it: 'It was hard for Marcus to part with his childhood comic book collection, but selling it helped him furnish his new apartment.'"),
        ("Solu", "Letting go creates space for new beginnings! Tonu, introduce our third expression."),
        ("Tonu", "Our third expression is 'tidy up'. To 'tidy up' means to make a room or space neat, orderly, and organized by putting things in their proper places."),
        ("Solu", "Let's hear an example: 'Before our evening guests arrived, we spent fifteen minutes tidying up the kitchen and living room.'"),
        ("Tonu", "A quick tidy up brings instant clarity! What is our fourth expression, Solu?"),
        ("Solu", "Our fourth expression describes heavy emotional or physical burdens: 'weigh down'. To 'weigh someone down' means to make someone feel burdened, exhausted, or restricted by too many responsibilities, worries, or physical possessions."),
        ("Tonu", "For example: 'Living in a huge suburban mansion with endless maintenance weighed him down, so he downsized to a simple seaside cottage.'"),
        ("Solu", "Lightness is true wealth! Tonu, take us to our fifth idiom."),
        ("Tonu", "Our fifth expression is a legendary design philosophy: 'less is more'. 'Less is more' means that simplicity, restraint, and minimalism often produce greater elegance, beauty, and effectiveness than complexity and excess."),
        ("Solu", "Here is an inspiring example: 'When designing our modern living room, the architect adopted the philosophy that less is more, using clean lines and minimal furniture.'"),
        ("Tonu", "And what is our sixth and final expression for today, Solu?"),
        ("Solu", "Our sixth expression describes genuine mental relief: 'breathe easy'. To 'breathe easy' means to feel deeply relieved, calm, and free from stress, pressure, or worry."),
        ("Tonu", "Let's hear an example: 'Once all the clutter was cleared out and the house was completely clean, she could finally sit on her couch and breathe easy.'"),

        # SECTION 13: INTERACTIVE SPEAKING PRACTICE
        ("Solu", "Now, it is time for our Interactive Speaking Challenge! This is your turn to speak English out loud along with us. Open your chest, pronounce each syllable clearly, and repeat each sentence with confidence and cadence!"),
        ("Tonu", "Sentence number one: 'Minimalism is not about deprivation; it is about making room for peace, purpose, and joy.' Your turn!"),
        ("Solu", "Speak it out loud with clear cadence: 'Minimalism is not about deprivation; it is about making room for peace, purpose, and joy.'"),
        ("Tonu", "Beautiful rhythm! Sentence number two: 'When you embrace the truth that less is more, your life becomes remarkably light and free.' Your turn!"),
        ("Solu", "Repeat with steady conviction: 'When you embrace the truth that less is more, your life becomes remarkably light and free.'"),
        ("Tonu", "Wonderful! Sentence number three: 'Clearing out physical clutter gives your mind the space to focus and breathe easy.' Your turn!"),
        ("Solu", "Say it clearly: 'Clearing out physical clutter gives your mind the space to focus and breathe easy.'"),
        ("Tonu", "Sentence number four: 'The best things in life are never things; they are memories, relationships, and moments of peace.' Your turn!"),
        ("Solu", "Let's say sentence number four together: 'The best things in life are never things; they are memories, relationships, and moments of peace.'"),
        ("Tonu", "Outstanding work! Your spoken English is sounding crisper, more fluent, and filled with authentic presence!"),

        # SECTION 14: REFLECTION & FAREWELL
        ("Solu", "And now, it is time for today's Weekly Reflection Question! We want you to practice writing in English down in the comment section below."),
        ("Tonu", "Here is today's question: 'Look around your bedroom or workspace right now. What is one physical or digital item that is creating visual clutter or stress in your life? What will you clear out or donate this weekend to create more peace?'"),
        ("Solu", "Writing your reflection in English strengthens your vocabulary and gives you the accountability to take action. Leave your comment below!"),
        ("Tonu", "Solu and I read through every single comment, and we love hearing your personal stories and transformations!"),
        ("Solu", "Remember that true abundance is not having a house stuffed with possessions, but having a heart full of gratitude and a mind free of clutter."),
        ("Tonu", "Live simply, cherish what matters, and keep speaking English with joy and confidence every day!"),
        ("Solu", "Until next time, goodbye from Solu!"),
        ("Tonu", "And goodbye from Tonu!"),
        ("Both", "Happy learning, live lightly, and goodbye!")
    ]
    return turns

if __name__ == "__main__":
    t = build_ep38()
    gen_common.verify_and_save(38, "scripts/daily_speak_ep38_full.txt",
                              "Minimalism, Clutter-Free Living & Decluttering Your Life",
                              "Daily Speak English | English Listening & Speaking Practice",
                              t)
