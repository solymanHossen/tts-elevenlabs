#!/usr/bin/env python3
"""
Daily Speak English - Episode 42
Title: Friendship Breakups, Outgrowing People & Moving On
Requirements:
- Starts with Tonu: "Hey hey, lovely listeners!..."
- Words >= 3,550 (strict duration >= 25.5 - 28.0 mins)
- High-level engaging, natural conversational English
"""

import gen_common

def build_ep42():
    turns = [
        # SECTION 1: MAGNETIC OPENING
        ("Tonu", "Hey hey, lovely listeners! Welcome back to Daily Speak English, your favorite place to become fluent, confident, and unstoppable in English! I'm Tonu!"),
        ("Solu", "And I'm Solu! Welcome back, everyone! Today, we are exploring one of the most painful, confusing, and unspoken emotional experiences of adult human life: 'Friendship Breakups', outgrowing old companions, and the delicate art of moving forward with grace and compassion!"),
        ("Tonu", "Solu, think about how our society handles romance versus friendship! When a romantic relationship ends, there are thousands of songs, books, movies, and breakup guides! Your family brings you ice cream, your colleagues give you space to grieve, and everyone understands that your heart is broken!"),
        ("Solu", "Yes! Society has clear cultural rituals for romantic breakups. But what happens when you lose a best friend of ten years? When the person you shared every secret, every triumph, and every late-night phone call with slowly drifts away, stops calling, or betrays your trust?"),
        ("Tonu", "There are no Hallmark sympathy cards for a friendship breakup! There is no official closure ceremony! Psychologists call this 'Disenfranchised Grief'—grief that society does not openly acknowledge, validate, or support!"),
        ("Solu", "And because people don't talk about it openly, you end up feeling completely alone, wondering: 'What did I do wrong? Did I become a bad person? Why did we grow so far apart?'"),
        ("Tonu", "Today, we are going to dive deep into Aristotle's three types of friendship, examine Robin Dunbar's famous social circle limits, analyze why outgrowing people is a natural law of personal growth, share scripts for closure, and master heart-to-heart conversational English!"),

        # SECTION 2: ARISTOTLE'S THREE TYPES OF FRIENDSHIP
        ("Solu", "Let's travel back two thousand three hundred years to ancient Greece to study one of the greatest philosophical analyses of human connection ever written: Aristotle's 'Nicomachean Ethics'!"),
        ("Tonu", "Aristotle identified that all human friendships fall into three distinct categories! What is type number one, Solu?"),
        ("Solu", "Type number one is 'Friendships of Utility'! These are relationships based on mutual practical benefit or convenience!"),
        ("Tonu", "Think about coworkers at an office, business partners, study buddies in university, or neighbors who water your plants when you travel!"),
        ("Solu", "You like each other, you collaborate smoothly, but the bond is tied to the shared circumstance! The moment one of you changes companies, graduates, or moves across town, the utility disappears, and the friendship naturally dissolves!"),
        ("Tonu", "And that is completely normal and healthy! What is type number two, Solu?"),
        ("Solu", "Type number two is 'Friendships of Pleasure'! These are friends based purely on shared entertainment, hobbies, and having fun together!"),
        ("Tonu", "Your weekend tennis partner, your nightclub dancing crew, your fantasy football buddies, or the group you play video games with online!"),
        ("Solu", "You laugh together, you enjoy great wine, but the connection remains on the surface! If you suffer a severe family tragedy or enter a serious philosophical depression, these friends don't know how to support you!"),
        ("Tonu", "And when your tastes, hobbies, or energy levels change, these friendships often fade away. And what is type number three—the holy grail of friendship, Solu?"),
        ("Solu", "Type number three is 'Friendships of Character' or 'Virtue Friendships'!"),
        ("Tonu", "In a Virtue Friendship, you love the person not for what they do for you, and not for the entertainment they provide, but for WHO THEY ARE at their moral core!"),
        ("Solu", "You admire their integrity, their compassion, their courage, and their spirit! These are the rare, soulmate friendships where you want the other person to flourish for their own sake!"),
        ("Tonu", "Aristotle said that true friendships of virtue are rare because noble character takes years to cultivate. If you have even two or three virtue friends in your entire lifetime, you are extraordinarily rich!"),

        # SECTION 3: THE DUNBAR NUMBER & SOCIAL CAPACITY
        ("Solu", "Now let's examine the hard biological limits of human social capacity: British anthropologist Robin Dunbar's famous 'Dunbar Number'!"),
        ("Tonu", "Dr. Robin Dunbar studied the neocortex size of primates and humans and discovered that our brains physically cannot maintain meaningful social relationships with more than roughly one hundred and fifty people!"),
        ("Solu", "And within that one hundred and fifty, Dunbar mapped concentric emotional circles that dictate our capacity for intimacy!"),
        ("Tonu", "At the very outer layer are one hundred and fifty casual acquaintances: people you recognize and would greet if you bumped into them at a wedding."),
        ("Solu", "Inside that circle are roughly fifty good friends: people you might invite to a large birthday barbecue."),
        ("Tonu", "Inside that are fifteen close friends: people you confide in regularly and can rely on for practical support."),
        ("Solu", "And at the absolute center of your social universe is your 'Support Clique'—a tiny circle of roughly THREE to FIVE intimate people!"),
        ("Tonu", "These three to five people receive sixty percent of all your social time, emotional energy, and vulnerable presence!"),
        ("Solu", "Why is this biological reality so liberating to understand? Because in the era of Instagram, Facebook, and LinkedIn, people feel pressured to maintain friendships with five hundred people simultaneously!"),
        ("Tonu", "You cannot pour deep water into five hundred cups! Your emotional pitcher is finite. Trying to be everyone's best friend leaves you emotionally bankrupt and chronically shallow!"),

        # SECTION 4: THE SILENT DRIFT VS THE EXPLOSIVE FALLOUT
        ("Solu", "Let's examine how friendship endings actually happen: the difference between 'The Silent Drift' and 'The Explosive Fallout'!"),
        ("Tonu", "Most friendship breakups do not happen because of a giant screaming fight, an unforgivable betrayal, or a dramatic movie scene!"),
        ("Solu", "Eighty percent of friendship breakups happen through 'The Silent Drift'!"),
        ("Tonu", "Explain what the silent drift looks like, Solu."),
        ("Solu", "You used to talk every day after school or university. Then, one person gets a demanding eighty-hour-a-week corporate job, gets married, or has twin babies!"),
        ("Tonu", "The other person is single, pursuing freelance travel, or going through a creative renaissance. Suddenly, your daily schedules, financial realities, and priorities are completely out of sync!"),
        ("Solu", "Text messages become shorter: 'Hey, miss you, let's catch up soon!' Then replies take two days, then two weeks, and eventually, six months pass without a word!"),
        ("Tonu", "You bump into each other at a supermarket, hug warmly, promise to grab coffee next week, but deep down, both of you know that the season of your shared journey has quietly closed."),
        ("Solu", "And there doesn't have to be any anger or bitterness! People are like tectonic plates: sometimes they drift together to form majestic mountain peaks, and sometimes they slowly drift apart across vast oceans."),

        # SECTION 5: OUTGROWING VALUES: THE PAIN OF DIVERGING PATHS
        ("Tonu", "Now let's address the more agonizing scenario: outgrowing someone because your core values, maturity, and lifestyles have diverged!"),
        ("Solu", "Think about friendships formed in high school or university! Many of those bonds were forged purely through proximity, alcohol, complaining about professors, or mutual boredom!"),
        ("Tonu", "Now imagine you spend five years working on yourself: you start reading books, quit destructive habits, focus on mental health, learn English, and build a purposeful career."),
        ("Solu", "And you go back to hang out with your old friendship crew, hoping for warmth and celebration!"),
        ("Tonu", "And what happens? You sit at the table and realize they are still telling the exact same high school jokes from ten years ago, gossiping viciously about old classmates, complaining about their lives, and mocking your ambitions!"),
        ("Solu", "When you tell them you are studying or pursuing a new dream, they make cynical comments: 'Oh, look who thinks they are too good for us now! Mr. Big Shot!'"),
        ("Tonu", "That hurts down to your bones! They don't want you to grow, because your growth is an uncomfortable mirror that exposes their stagnation!"),
        ("Solu", "You cannot heal in the same environment that made you sick, and you cannot soar if you remain tied to people who refuse to leave the ground."),

        # SECTION 6: TOXIC DYNAMICS: ENERGY VAMPIRES & COMPETITIVE FRIENDS
        ("Solu", "Let's identify the warning signs of friendships that have become genuinely toxic and destructive to your well-being!"),
        ("Tonu", "Warning sign number one is 'The One-Way Street' or 'The Emotional Dump Truck'!"),
        ("Solu", "Every time they call you, they talk nonstop for forty-five minutes about their boyfriend drama, their annoying boss, their landlord, and their aches and pains!"),
        ("Tonu", "You listen with compassion, offering guidance and comfort. But the minute they finish complaining and you say: 'Actually, I had a really hard week too,' they suddenly say: 'Oh, that's crazy! Anyway, I have to run!'"),
        ("Solu", "They don't want a friend; they want an unpaid therapist and an emotional garbage dump!"),
        ("Tonu", "Warning sign number two is 'The Frenemy' or 'The Competitive Underminer'!"),
        ("Solu", "When something terrible happens to you, they are right there giving you hugs because it makes them feel superior! But when you achieve a major promotion, pass an exam, or fall in love, their smile tightens, and they deliver backhanded compliments!"),
        ("Tonu", "They say things like: 'Congratulations on your new job! I guess they weren't looking for someone with advanced qualifications this time, haha!'"),
        ("Solu", "A true friend celebrates your victories as if they were their own! If someone's energy feels like a poison cloud whenever you win, they are not your friend."),

        # SECTION 7: TO CONFRONT OR SLOW-FADE?
        ("Tonu", "Now, here is the big dilemma that our listeners constantly ask: 'When a friendship is no longer healthy, should I have an explicit breakup conversation, or should I do the Slow Fade?'"),
        ("Solu", "Psychologists and relationship experts say that the choice depends entirely on two factors: the depth of history, and whether emotional safety exists!"),
        ("Tonu", "If this is a friend of ten years with deep shared history who simply drifted or had a misunderstanding, you owe them the honor of an honest, vulnerable conversation!"),
        ("Solu", "Call them or meet for coffee and say: 'I value our history deeply, and I've felt some distance and tension between us lately. I wanted to talk about where we stand because you have meant so much to my life.'"),
        ("Tonu", "Now, what if the person is high-conflict, narcissistic, manipulative, or emotionally abusive?"),
        ("Solu", "If someone has proven that they twist your words, scream, or weaponize vulnerability, having a confrontation is like pouring gasoline on fire! In those cases, 'The Slow Fade' or polite distance is the safest, wisest move!"),
        ("Tonu", "Reply to texts with polite, delayed, boring brevity. Don't engage in debates, don't initiate hangouts, and let the connection gently wither without drama."),

        # SECTION 8: GRIEVING THE LOSS & RELEASING GUILT
        ("Solu", "Let's speak to anyone listening right now who carries a heavy stone of guilt over an ended friendship."),
        ("Tonu", "You look at old photographs, remember the laughter you shared, and you wonder: 'Was I too selfish? Should I have tried harder? Am I disloyal?'"),
        ("Solu", "Hear this truth clearly: You can deeply cherish the memories of who someone was to you in your past, while acknowledging that they cannot be part of your future!"),
        ("Tonu", "Not every friendship is designed to last until you are ninety years old sitting in rocking chairs on a porch!"),
        ("Solu", "Some people are 'Season Friends'—they were brought into your life for a specific season: to help you survive college, to teach you how to open your heart, or to help you discover your humor!"),
        ("Tonu", "When that season ends, the gift of the friendship remains forever etched into your character! You don't have to erase the past to honor your present growth."),

        # SECTION 9: MAKING DEEP ADULT FRIENDSHIPS: PROXIMITY & VULNERABILITY
        ("Solu", "Now, how do we make new, authentic adult friends when our old circle has shifted?"),
        ("Tonu", "Sociologist Rebecca G. Adams discovered that making close friends requires three specific conditions: proximity, repeated unplanned interactions, and a setting that encourages vulnerability!"),
        ("Solu", "That is why making friends in childhood and college was so effortless: you saw the same people in hallways, dorms, and cafeterias five days a week without planning!"),
        ("Tonu", "As adults, you must engineer those conditions deliberately! Join a running club, a pottery studio, an English conversation circle, a community garden, or volunteer for a local charity!"),
        ("Solu", "Show up to the same class or coffee shop at the same time every single week! Consistency breeds familiarity, and familiarity breeds trust."),
        ("Tonu", "And take the first step! Don't wait for other people to invite you; be the courageous person who says: 'Hey, I really enjoyed our conversation today, would you like to grab a coffee next Tuesday?'"),

        # SECTION 10: HONORING THE SACRED VESSEL OF CHARACTER FRIENDSHIP
        ("Solu", "When you are blessed to find those rare virtue friends who celebrate your soul, cherish and protect them like priceless treasure!"),
        ("Tonu", "Water the garden of your true friendships! Send a thoughtful voice note just to say: 'I was thinking about you today and how much I appreciate your kindness.'"),
        ("Solu", "Remember their birthdays, show up when their parents are sick, celebrate their promotions, and give them the gift of your undivided, screen-free presence."),
        ("Tonu", "Quality over quantity is the eternal law of human connection. Three true friends will carry you through a lifetime of storms."),

        # SECTION 11: THE CRUELTY OF GHOSTING & AMBIGUOUS LOSS
        ("Solu", "Now, let's address a widespread modern habit that causes immense psychological damage: 'Ghosting' in long-term friendships!"),
        ("Tonu", "Ghosting isn't just ignoring someone on a dating app after one coffee date; thousands of people experience being ghosted by friends they knew for five or ten years!"),
        ("Solu", "You send a message, see the blue read receipts, and then silence! Days turn into months, and they simply vanish into thin air!"),
        ("Tonu", "Psychologists call the emotional fallout of ghosting 'Ambiguous Loss'! Because there is no formal ending or clear explanation, your brain cannot complete the natural cycle of grief!"),
        ("Solu", "You replay every single conversation in your head: 'Did I say something offensive? Did their mother get sick? Did I fail them?' It inflicts deep psychological torture!"),
        ("Tonu", "Ghosting in a long-standing friendship is emotional cowardice! If you need to step back, send a two-sentence message: 'I need to take space to focus on personal matters, but I want you to know I wish you well.' That simple gesture grants dignity and peace!"),

        # SECTION 12: THE 'REFRIGERATOR TEST' FOR TRUE INTIMACY
        ("Solu", "Let's share a lighthearted yet profound relationship test: 'The Refrigerator Test'!"),
        ("Tonu", "What is the Refrigerator Test, Solu?"),
        ("Solu", "Think about the people in your life! With casual friends, when you visit their house, you sit formally on the couch, wait for them to offer you a glass of water, and use a coaster!"),
        ("Tonu", "That is a performative, polite friendship! Now, what is a Refrigerator Friend?"),
        ("Solu", "A Refrigerator Friend is someone whose house you can walk into, kick off your shoes, walk straight into their kitchen, open their refrigerator, grab an apple, and sit on their floor without asking permission or feeling self-conscious!"),
        ("Tonu", "You don't have to tidy your house before they visit; they can see you in your sweatpants with messy hair and unwashed dishes in the sink, and you feel zero shame!"),
        ("Solu", "Those 'refrigerator friendships' where all masks and social pretenses are dropped are the true sanctuaries of our adult lives."),

        # SECTION 13: DIGITAL TETHERING VS FLESH-AND-BLOOD COMMUNITY
        ("Tonu", "Let's also look at the illusion of digital friendship on social media!"),
        ("Solu", "You might have four thousand followers on Instagram and exchange heart emojis and meme reels with fifty people every day."),
        ("Tonu", "Yet studies show that young adults are reporting higher rates of chronic loneliness than any generation in human history!"),
        ("Solu", "Because reacting to an Instagram story is not the same as sharing a pot of tea across a wooden table!"),
        ("Tonu", "A laughing emoji cannot replace hearing your friend's authentic belly laugh in real life, seeing the crinkles around their eyes, and feeling the warmth of a long embrace!"),
        ("Solu", "Step away from the screen! Pick up the phone, hear their vocal tone, meet in physical reality, and let your mirror neurons connect in three-dimensional presence!"),
        ("Tonu", "And notice the magical power of shared silence! In superficial relationships, silence feels awkward and terrifying, so people scramble to fill it with nervous gossip."),
        ("Solu", "In a true virtue friendship, you can sit side by side on a park bench or drive along a highway for thirty minutes without saying a single word, feeling completely peaceful, understood, and connected."),
        ("Tonu", "Comfortable shared silence is the ultimate litmus test of soulful human connection."),

        # SECTION 14: LIVE ROLEPLAY: A GENTLE, HONEST FRIENDSHIP CLOSURE
        ("Solu", "Now let's demonstrate a realistic real-world roleplay! Imagine an old friend whom you have outgrown calls you and demands to know why you haven't been hanging out every weekend like you used to."),
        ("Tonu", "Most people make cowardly excuses or get defensive! Let's show how to communicate with profound maturity, warmth, and firm boundary! Tonu, play the old friend."),
        ("Tonu", "Hey Solu! You've been dodging my calls for weeks! Are you blowing me off? What happened to our Friday night drinking sessions? You've changed, man!"),
        ("Solu", "Here is how you answer with truth and grace: 'Hey Tonu, I really appreciate you reaching out directly instead of holding it inside. You're right: I have changed, and my life and priorities are in a very different place right now. I'm focusing intensely on my health, my studies, and my career, which means I don't go out partying anymore. I will always treasure the incredible memories and laughter we shared, but my daily lifestyle is quite different now. I truly wish you nothing but the best, and I hope you understand.'"),
        ("Tonu", "Look at how magnificent that is! You didn't insult their lifestyle, you didn't apologize for your growth, and you held your ground with unwavering respect!"),
        ("Solu", "Clear honesty honors both you and them, allowing both people to move forward in peace."),

        # SECTION 12: VOCABULARY & IDIOM SPOTLIGHT (6 KEY IDIOMS)
        ("Tonu", "Now, let's step into our signature segment: Key Everyday English Idioms and Phrases! Today, we have selected six colorful, essential expressions about friendship, loyalty, and relationships!"),
        ("Solu", "Let's master them together! Tonu, what is our very first friendship idiom for today?"),
        ("Tonu", "Our first expression is 'drift apart'. To 'drift apart' means to gradually become less friendly, close, or intimate with someone over time as your interests, lives, or locations change."),
        ("Solu", "Let's listen to a natural conversational example: 'After university graduation, Marcus and Daniel drifted apart as they pursued careers in different cities.'"),
        ("Tonu", "A very natural part of life! What is our second expression, Solu?"),
        ("Solu", "Our second expression describes overcoming turbulence: 'hit a rough patch'. To 'hit a rough patch' means to experience a difficult, stressful, or challenging period in a relationship or life."),
        ("Tonu", "Here is how you can use it: 'Their long-standing friendship hit a rough patch after a business disagreement, but they managed to talk it through.'"),
        ("Solu", "Honest dialogue heals rough patches! Tonu, introduce our third expression."),
        ("Tonu", "Our third expression describes chance encounters: 'cross paths'. To 'cross paths with someone' means to meet or encounter someone, often unexpectedly or by chance."),
        ("Solu", "Let's hear an example: 'Ten years after finishing high school, I crossed paths with my childhood best friend at an international airport in Tokyo.'"),
        ("Tonu", "What a magical surprise! What is our fourth expression, Solu?"),
        ("Solu", "Our fourth expression describes making peace: 'bury the hatchet'. To 'bury the hatchet' means to end a conflict, forgive past grievances, and make peace after a long feud or disagreement."),
        ("Tonu", "For example: 'After years of cold silence, the two estranged brothers decided to bury the hatchet and celebrate Thanksgiving together.'"),
        ("Solu", "Forgiveness is freedom! Tonu, take us to our fifth idiom."),
        ("Tonu", "Our fifth expression describes true emotional comfort: 'a shoulder to cry on'. A 'shoulder to cry on' is someone who listens sympathetically, compassionately, and lovingly to your grief and troubles."),
        ("Solu", "Here is a touching example: 'During the agonizing months following her mother's illness, Clara was an unwavering shoulder to cry on.'"),
        ("Tonu", "And what is our sixth and final expression for today, Solu?"),
        ("Solu", "Our sixth expression describes legendary loyalty: 'through thick and thin'. To support someone 'through thick and thin' means to remain loyal, committed, and supportive through all hardships, setbacks, and triumphs."),
        ("Tonu", "Let's hear an inspiring example: 'True friends are those rare souls who stand by your side through thick and thin, never wavering when storms arrive.'"),

        # SECTION 13: INTERACTIVE SPEAKING PRACTICE
        ("Solu", "Now, it is time for our Interactive Speaking Challenge! This is your turn to speak English out loud along with us. Open your chest, pronounce each syllable with warmth and emotional maturity, and repeat each sentence with steady cadence!"),
        ("Tonu", "Sentence number one: 'Outgrowing people is not betrayal; it is the natural evidence of personal growth and evolving values.' Your turn!"),
        ("Solu", "Speak it out loud with clear cadence: 'Outgrowing people is not betrayal; it is the natural evidence of personal growth and evolving values.'"),
        ("Tonu", "Beautiful rhythm! Sentence number two: 'I am learning to honor the memories of past friendships while giving myself permission to move forward.' Your turn!"),
        ("Solu", "Repeat with steady conviction: 'I am learning to honor the memories of past friendships while giving myself permission to move forward.'"),
        ("Tonu", "Wonderful! Sentence number three: 'True friends are those precious souls who stand by you through thick and thin.' Your turn!"),
        ("Solu", "Say it clearly: 'True friends are those precious souls who stand by you through thick and thin.'"),
        ("Tonu", "Sentence number four: 'When you surround yourself with people who inspire your soul, your life expands with joy and purpose.' Your turn!"),
        ("Solu", "Let's say sentence number four together: 'When you surround yourself with people who inspire your soul, your life expands with joy and purpose.'"),
        ("Tonu", "Outstanding work! Your spoken English is sounding compassionate, authoritative, and deeply resonant!"),

        # SECTION 16: REFLECTION & FAREWELL
        ("Solu", "And now, it is time for today's Weekly Reflection Question! We want you to practice writing in English down in the comment section below."),
        ("Tonu", "Here is today's question: 'Have you ever experienced a painful friendship breakup or drifted away from someone you used to love? How did that loss shape your maturity, and what qualities do you value most in true friends today?'"),
        ("Solu", "Writing your personal experiences in English connects you with thousands of fellow learners worldwide who have walked the same path. Share your story in the comments below!"),
        ("Tonu", "Solu and I read through every single comment, and we are so honored to share this meaningful journey of language and life with you."),
        ("Solu", "Every story you share reminds us that healing, growth, and forgiveness are universal human experiences that unite us all across every language and border."),
        ("Tonu", "Remember that life is too short to spend with people who extinguish your light. Surround yourself with souls who fan your flames."),
        ("Tonu", "Love deeply, let go with grace, and keep speaking English with bold courage every single day!"),
        ("Solu", "Until next time, goodbye from Solu!"),
        ("Tonu", "And goodbye from Tonu!"),
        ("Both", "Happy learning, cherish true friends, and goodbye!")
    ]
    return turns

if __name__ == "__main__":
    t = build_ep42()
    gen_common.verify_and_save(42, "scripts/daily_speak_ep42_full.txt",
                              "Friendship Breakups, Outgrowing People & Moving On",
                              "Daily Speak English | English Listening & Speaking Practice",
                              t)
