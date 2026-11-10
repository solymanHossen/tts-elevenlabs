#!/usr/bin/env python3
"""
Daily Speak English - Episode 35
Title: Sleep Architecture, Dreams & The Neuroscience of Rest
Requirements:
- Starts with Tonu: "Hey hey, lovely listeners!..."
- Words >= 3,550 (strict duration >= 25.5 - 28.0 mins)
- High-level engaging, natural conversational English
"""

import gen_common

def build_ep35():
    turns = [
        # SECTION 1: MAGNETIC OPENING
        ("Tonu", "Hey hey, lovely listeners! Welcome back to Daily Speak English, your favorite place to become fluent, confident, and unstoppable in English! I'm Tonu!"),
        ("Solu", "And I'm Solu! Welcome back, everyone! Today, we are exploring a breathtaking topic that directly controls your mood, your intelligence, your physical energy, and your longevity: sleep architecture, the neuroscience of deep rest, and the incredible world of dreams!"),
        ("Tonu", "Solu, did you know that human beings are the only species on planet Earth that deliberately deprive themselves of sleep for no apparent survival reason?"),
        ("Solu", "That is unbelievable when you think about it! A lion won't stay awake watching Netflix; a horse won't scroll through social media until 2 AM! Only humans wear exhaustion like a badge of honor!"),
        ("Tonu", "In modern culture, people brag about sleeping only four or five hours a night, saying things like 'I will sleep when I am dead!' But modern neuroscience has proven that if you don't sleep enough now, that day might arrive much sooner than you think!"),
        ("Solu", "Exactly right, Tonu. Today, you are going to learn how sleep actually works inside your brain, why dreams are nature's emotional therapy, and how to build a world-class sleep sanctuary while expanding your advanced English vocabulary!"),

        # SECTION 2: THE FOUR STAGES OF SLEEP
        ("Tonu", "Let's begin by unlocking what scientists call 'Sleep Architecture'! Many people think that falling asleep is like flipping an electrical switch off, as if your brain just shuts down into darkness."),
        ("Solu", "In reality, sleep is an incredibly active, coordinated symphony of four distinct stages cycling every ninety minutes throughout the night!"),
        ("Tonu", "What is stage one, Solu?"),
        ("Solu", "Stage one is 'NREM Stage 1', or light sleep. This is the drifting twilight zone between wakefulness and slumber. Your heartbeat slows down, your muscles begin to relax, and you might experience sudden twitching, known as a hypnic jerk!"),
        ("Tonu", "Have you ever felt like you were suddenly falling off a tall curb or dropping from the sky right as you doze off? That is a hypnic jerk! Your brain checks if your muscles are still responsive."),
        ("Solu", "Then we descend into 'Stage 2 NREM sleep'. During stage two, your core body temperature drops, and your brain generates sudden bursts of rapid electrical activity called 'sleep spindles' and 'K-complexes'!"),
        ("Tonu", "Sleep spindles act like a tranquilizer shield, protecting your brain from outside noises like passing cars or distant dogs barking, so you stay asleep!"),
        ("Solu", "And sleep spindles also transfer freshly learned memories from your temporary short-term storage, the hippocampus, into the permanent long-term library of your cortex!"),
        ("Tonu", "That means every English word, phrase, and pronunciation pattern you practice during the day is physically etched into your brain during stage two sleep!"),

        # SECTION 3: DEEP SLOW-WAVE SLEEP & THE GLYMPHATIC DISHWASHER
        ("Solu", "Now let's talk about the holy grail of physical restoration: 'Stage 3 NREM sleep', also known as Deep Slow-Wave Sleep!"),
        ("Tonu", "In deep slow-wave sleep, your brain waves slow down to majestic, synchronized delta waves. Your blood pressure plunges, human growth hormone surges through your veins to repair damaged muscle fibers, and your immune system reloads its weapons!"),
        ("Solu", "And something truly miraculous happens inside your brain cells during deep sleep that scientists only discovered recently: 'The Glymphatic System' activates!"),
        ("Tonu", "The glymphatic system is like a nightly neurological dishwasher! Dr. Maiken Nedergaard and neuroscientists discovered that during deep slow-wave sleep, your brain cells literally shrink by sixty percent!"),
        ("Solu", "Why do the brain cells shrink, Tonu?"),
        ("Tonu", "They shrink to open up wide microscopic channels between the cells! Then, cerebrospinal fluid rushes through your brain tissues like soapy water, washing away metabolic waste and toxic proteins called beta-amyloid and tau proteins!"),
        ("Solu", "And beta-amyloid is the exact toxic protein that accumulates into poisonous plaques in Alzheimer's disease and cognitive dementia!"),
        ("Tonu", "When you sacrifice your deep sleep, your brain misses its nightly cleansing bath. The toxic waste remains trapped inside your neural pathways, leaving you foggy, irritable, forgetful, and mentally exhausted the next morning!"),
        ("Solu", "Deep sleep is literally your brain taking out its cellular garbage!"),

        # SECTION 4: REM SLEEP & EMOTIONAL FIRST AID
        ("Tonu", "After deep sleep, the cycle shifts into the most cinematic stage of all: 'REM sleep', or Rapid Eye Movement sleep!"),
        ("Solu", "REM sleep is when your most vivid, emotional, and bizarre dreams occur! Your eyelids flutter rapidly, your respiration speeds up, but your large voluntary muscles become completely paralyzed!"),
        ("Tonu", "Why does our body paralyze our muscles during REM sleep, Solu?"),
        ("Solu", "It is an evolutionary safety mechanism called 'REM Atonia'! If your body wasn't temporarily paralyzed, you would physically act out your dreams: you might jump out of bed, kick your bedroom wall, or run down the stairs while dreaming that you are chasing a cheetah!"),
        ("Tonu", "Fascinating! And renowned neuroscientist Dr. Matthew Walker, author of the bestselling book 'Why We Sleep', calls REM dreaming 'overnight emotional therapy' or 'nocturnal soothing balm'!"),
        ("Solu", "Explain that concept to our listeners, Tonu. How does dreaming heal our emotional wounds?"),
        ("Tonu", "During REM sleep, the neurochemical noradrenaline, which is the brain's stress and anxiety chemical, is completely switched off! It is the only time in twenty-four hours when your brain is completely free of stress neurochemicals!"),
        ("Solu", "So your brain can replay difficult memories, heartbreaks, embarrassing mistakes, and emotional conflicts from the previous day in a neurochemically safe, calm atmosphere!"),
        ("Tonu", "It divorces the factual memory from the painful emotional charge! You remember the event, but the emotional sting and terror are softened and healed!"),
        ("Solu", "Dreaming is emotional first aid! Without enough REM sleep, every minor irritation feels like a catastrophic emotional emergency."),

        # SECTION 5: ADENOSINE, SLEEP PRESSURE & THE CAFFEINE TRAP
        ("Tonu", "Now let's examine the biological engine that makes you feel sleepy in the first place: 'Sleep Pressure' and a chemical called Adenosine!"),
        ("Solu", "From the very second you open your eyes in the morning, your brain begins burning energy and producing a chemical byproduct called Adenosine!"),
        ("Tonu", "Think of Adenosine like sand falling through an hourglass! The longer you stay awake, the more Adenosine accumulates in your brain receptors!"),
        ("Solu", "By the time twelve, fourteen, or sixteen hours have passed, your brain is filled with heavy Adenosine pressure! Your eyelids feel heavy, your head nods, and your brain signals an overwhelming urge to sleep!"),
        ("Tonu", "Now, what do millions of modern people do when they feel that natural Adenosine tiredness at 3 PM in the office?"),
        ("Solu", "They run straight to the espresso machine and chug a double shot of dark roast coffee or an energy drink!"),
        ("Tonu", "And what does caffeine actually do to Adenosine, Solu? Does caffeine remove tiredness?"),
        ("Solu", "No! Caffeine does NOT destroy or reduce Adenosine at all! Caffeine is a molecular imposter! Its chemical shape looks almost identical to Adenosine, so it rushes into your brain and docks into the Adenosine receptor seats, locking them shut!"),
        ("Tonu", "It puts a piece of black tape over the fuel gauge! The fuel tank is still completely empty, but you can no longer see the warning light!"),
        ("Solu", "And while caffeine blocks the receptors, your brain continues producing even more Adenosine behind the scenes!"),
        ("Tonu", "And when the caffeine finally wears off four, five, or six hours later, all that accumulated Adenosine floods into the receptors simultaneously!"),
        ("Solu", "And that causes the dreaded 'Caffeine Crash'! You suddenly feel twice as exhausted, irritable, and sluggish as you were before!"),
        ("Tonu", "And let's look at the half-life of caffeine! Caffeine has an average half-life of five to seven hours, and a quarter-life of up to twelve hours!"),
        ("Solu", "What does that mean in real life? If you drink a cup of coffee at 4 PM in the afternoon, half of that caffeine is still buzzing in your bloodstream at 10 PM, and twenty-five percent is still active at 4 AM in the morning!"),
        ("Tonu", "Even if you are able to fall asleep after late-afternoon caffeine, sleep monitors show that caffeine slashes your deep slow-wave sleep by twenty to thirty percent! You wake up unrefreshed, reach for another cup of coffee, and enter a vicious cycle!"),

        # SECTION 6: CIRCADIAN RHYTHMS & ANDREW HUBERMAN'S LIGHT PROTOCOL
        ("Solu", "Now let's talk about the master internal clock in your brain: 'The Suprachiasmatic Nucleus' and your Circadian Rhythm!"),
        ("Tonu", "Your circadian rhythm is an ancient, twenty-four-hour biological schedule that regulates hormone release, body temperature, digestion, and alertness!"),
        ("Solu", "And what is the primary signal that synchronizes this master clock, Tonu?"),
        ("Tonu", "Natural sunlight! Neurobiologist Dr. Andrew Huberman from Stanford University has popularized the profound science of morning light exposure!"),
        ("Solu", "Within thirty to sixty minutes of waking up, step outside into natural sunlight for ten to twenty minutes without wearing sunglasses!"),
        ("Tonu", "Special photoreceptor cells in your eyes, called intrinsically photosensitive retinal ganglion cells, detect the specific wavelength of morning blue light and send an electrical signal straight to your suprachiasmatic nucleus!"),
        ("Solu", "This triggers a healthy morning spike of cortisol, boosting your alertness, immune system, and mental clarity for the day!"),
        ("Tonu", "And here is the magic: that morning sunlight exposure sets a biological timer in your brain that dictates when melatonin—the hormone of darkness—will be released sixteen hours later in the evening!"),
        ("Solu", "So if you want to fall asleep effortlessly at 10:30 PM, your preparation doesn't start at 10 PM; your preparation started with sunlight at 7 AM this morning!"),
        ("Tonu", "And just as morning light wakes you up, artificial blue light from smartphones, iPads, and LED screens late at night destroys your evening melatonin!"),
        ("Solu", "When you hold a bright smartphone two inches from your face at 11 PM in a dark bedroom, your prehistoric brain thinks the sun is rising in the sky! It halts melatonin production, confusing your body and delaying restorative sleep for hours!"),

        # SECTION 7: THE 3-2-1 SLEEP RULE & BEDROOM SANCTUARY
        ("Tonu", "Let's share a practical, life-changing framework that our listeners can implement tonight: 'The 3-2-1 Rule for Deep Rest'!"),
        ("Solu", "The 3-2-1 Rule is simple, memorable, and immensely powerful! Tonu, break down the numbers!"),
        ("Tonu", "Number 3: Three hours before bedtime, stop eating heavy meals!"),
        ("Solu", "Digesting a heavy, greasy dinner requires enormous cardiovascular effort. Your stomach draws blood flow away from your brain, raises your core body temperature, and triggers acid reflux and micro-awakenings throughout the night!"),
        ("Tonu", "Number 2: Two hours before bedtime, stop working and stop drinking large amounts of water!"),
        ("Solu", "Closing your work laptop stops stressful cortisol from racing through your thoughts, and limiting fluids ensures you don't wake up three times to run to the restroom in the middle of the night!"),
        ("Tonu", "And Number 1: One hour before bedtime, turn off all screens and dim the overhead house lights!"),
        ("Solu", "Replace social media scrolling with a warm shower, reading a physical paper book, stretching, or listening to a soothing English podcast like Daily Speak English!"),
        ("Tonu", "And let's talk about bedroom temperature! Did you know that your body must drop its core temperature by about one to two degrees Fahrenheit to initiate and sustain deep sleep?"),
        ("Solu", "Yes! A bedroom that is too hot is one of the most common causes of insomnia and restless tossing and turning!"),
        ("Tonu", "Keep your bedroom cool—around sixty-five to sixty-eight degrees Fahrenheit, or eighteen to twenty degrees Celsius! When your room is cool, your body relaxes, melatonin releases smoothly, and you sink effortlessly into deep slow-wave slumber!"),

        # SECTION 8: NON-SLEEP DEEP REST (NSDR) & YOGA NIDRA
        ("Solu", "Now, what if you had a terrible night of sleep? What if your baby cried, you traveled across time zones, or work kept you up? How can you recover without taking long, groggy daytime naps?"),
        ("Tonu", "Science has a magnificent answer: 'Non-Sleep Deep Rest', or NSDR, also known historically as 'Yoga Nidra'!"),
        ("Solu", "What is NSDR, Tonu?"),
        ("Tonu", "NSDR is a guided relaxation protocol lasting ten to thirty minutes where you lie down, close your eyes, practice slow diaphragmatic breathing with extended exhalations, and conduct a mental body scan from head to toe!"),
        ("Solu", "Brain imaging studies show that during NSDR, your brain wave frequency slows down from active beta waves into calm alpha and theta waves, mimicking the early restorative stages of natural sleep!"),
        ("Tonu", "A twenty-minute NSDR session can restore depleted dopamine levels, clear brain fog, and dramatically boost cognitive stamina without causing sleep inertia or ruining your nighttime sleep drive!"),
        ("Solu", "It is an incredible tool for busy professionals, students, and anyone needing a quick neurological reset during a demanding afternoon."),

        # SECTION 9: THE SNOOZE BUTTON TRAP & SLEEP INERTIA
        ("Tonu", "Now let's tackle a morning habit that millions of people do every single day: hitting the dreaded alarm snooze button!"),
        ("Solu", "Oh, the snooze button is pure psychological poison! Why is hitting snooze so damaging to our brain, Tonu?"),
        ("Tonu", "When your alarm blares at 6:30 AM, your brain is jolted out of a sleep state. If you smack the snooze button and fall back asleep for nine minutes, your brain initiates a brand-new ninety-minute sleep cycle!"),
        ("Solu", "And when the alarm screams again nine minutes later, it rips you out of the deepest, most vulnerable part of that new cycle!"),
        ("Tonu", "That plunges you into severe 'Sleep Inertia'! Sleep inertia is that groggy, disoriented, zombie-like brain fog where you can barely remember your own name!"),
        ("Solu", "If you wake up when your first alarm rings, that initial grogginess disappears within ten to fifteen minutes. But if you hit snooze three times, sleep inertia can cripple your cognitive abilities for up to three or four hours!"),
        ("Tonu", "Put your alarm clock across the room so you have to physically get out of bed to silence it! When your feet hit the floor, your day has begun!"),

        # SECTION 10: DREAMS, CREATIVITY & HISTORICAL BREAKTHROUGHS
        ("Solu", "Tonu, let's explore how dreams have fueled some of the greatest scientific discoveries and artistic masterpieces in human history!"),
        ("Tonu", "It is astonishing how many breakthroughs were born in dreams! Take Dmitri Mendeleev, the Russian chemist who created the Periodic Table of Elements!"),
        ("Solu", "Mendeleev had been struggling for months to arrange the chemical elements by atomic weight. Exhausted, he collapsed onto his desk and fell into a deep dream!"),
        ("Tonu", "In his dream, he saw a vision where all the chemical elements fell into precise rows and columns like a celestial puzzle! When he awoke, he immediately wrote it down on a piece of paper, and the modern Periodic Table was born!"),
        ("Solu", "And what about Paul McCartney of The Beatles? He woke up one morning with the complete melody of 'Yesterday' fully orchestrated in his head! He leaped out of bed and played it on the piano right away!"),
        ("Tonu", "And Mary Shelley dreamed the fundamental concept of 'Frankenstein' during a vivid, terrifying nightmare by Lake Geneva!"),
        ("Solu", "Why are dreams such fertile soil for creative genius, Tonu?"),
        ("Tonu", "Because during waking hours, your prefrontal cortex acts like a strict logical censor, rejecting unusual ideas. But during REM sleep, that logical censor shuts down, allowing your brain to connect distant, bizarre concepts and form brilliant innovative insights!"),

        # SECTION 11: EVENING BRAIN DUMPING & THE DIGITAL SUNSET
        ("Solu", "Let's share another transformative practical tool for our listeners who suffer from 'racing mind syndrome' when trying to sleep."),
        ("Tonu", "You know that agonizing feeling when you lie in bed, close your eyes, and suddenly your brain starts replaying every single task you forgot to finish, an awkward comment from five years ago, and tomorrow's endless to-do list!"),
        ("Solu", "Psychologists call this 'Cognitive Rumination'. How do we silence the racing mind, Tonu?"),
        ("Tonu", "Use a technique called 'The Evening Brain Dump'! Keep a physical paper notebook and a pen on your nightstand."),
        ("Solu", "Thirty minutes before bed, open the notebook and write down everything swirling in your mind: tomorrow's meetings, grocery items, unwritten emails, and lingering worries!"),
        ("Tonu", "A study from Baylor University showed that participants who spent five minutes writing out a specific to-do list of tomorrow's tasks fell asleep significantly faster than those who wrote about completed tasks!"),
        ("Solu", "When your brain sees that the tasks are safely preserved on paper, it relaxes its vigilance! It stops whispering 'Don't forget this!' because it knows the paper will remember for you."),
        ("Tonu", "Pair that with a 'Digital Sunset'—putting your phone to sleep in another room—and you will sleep like an infant!"),

        # SECTION 12: LIVE ROLEPLAY: DECLINING LATE-NIGHT TEXTS & PRIORITIZING REST
        ("Solu", "Now let's demonstrate a realistic real-world roleplay! Imagine a colleague or friend who constantly calls or messages you with non-urgent gossip or work tasks at 10:45 PM."),
        ("Tonu", "And they send a message: 'Hey, are you awake? Did you see what our manager posted on LinkedIn? Also, can you look over this slide deck before tomorrow morning?'"),
        ("Solu", "Most people feel pressured to respond immediately, sacrificing their precious sleep window!"),
        ("Tonu", "Now let's show how to establish an elegant, respectful evening boundary! Solu, how would you address this?"),
        ("Solu", "The best move is often not replying until morning! But if they call or require an explicit boundary, you can send a calm, courteous text the next morning: 'Good morning! I wind down and turn off my phone by 10 PM to protect my sleep and health. I am reviewing the slide deck now and will have feedback for you by 9:30 AM!'"),
        ("Tonu", "Notice the brilliance of that response! You didn't apologize for sleeping, you didn't act annoyed, and you clearly trained them that late-night messages will simply wait until morning hours!"),
        ("Solu", "Clear, healthy, professional boundaries safeguard your health and command immense respect."),

        # SECTION 13: VOCABULARY & IDIOM SPOTLIGHT (6 KEY IDIOMS)
        ("Tonu", "Now, let's step into our signature vocabulary segment: Key Everyday English Idioms and Phrases! Today, we have selected six colorful, essential expressions related to sleep, rest, and energy!"),
        ("Solu", "Let's master them together! Tonu, what is our very first sleep idiom for today?"),
        ("Tonu", "Our first expression is 'hit the sack' or 'hit the hay'. To 'hit the sack' is an informal, natural way of saying to go to bed or fall asleep."),
        ("Solu", "Let's hear a natural conversational example: 'I have been studying for my English exam all evening, so I am going to hit the sack early tonight.'"),
        ("Tonu", "Perfect! What is our second expression, Solu?"),
        ("Solu", "Our second expression is a wise decision-making tool: 'sleep on it'. To 'sleep on something' means to delay making an important decision until the next day, giving yourself time and sleep to think clearly."),
        ("Tonu", "Here is how you can use it: 'Before you sign that expensive apartment lease, why don't you sleep on it and see how you feel in the morning?'"),
        ("Solu", "Letting your subconscious process the decision overnight is brilliant advice! Tonu, introduce our third idiom."),
        ("Tonu", "Our third expression is 'burn the candle at both ends'. To 'burn the candle at both ends' means to work excessively hard from early morning until late at night, exhausting your physical and mental stamina."),
        ("Solu", "Let's hear an example: 'Between working a demanding corporate job and launching a side business, David has been burning the candle at both ends and looks completely depleted.'"),
        ("Tonu", "You cannot burn the candle at both ends without melting down! What is our fourth expression, Solu?"),
        ("Solu", "Our fourth expression is playful and casual: 'catch some Z's'. To 'catch some Z's' means to get some sleep or take a brief, restful nap."),
        ("Tonu", "For example: 'I have a one-hour flight layover, so I am going to find a quiet gate and catch some Z's before my next connection.'"),
        ("Solu", "Always take an opportunity to rest! Tonu, take us to our fifth idiom."),
        ("Tonu", "Our fifth expression describes extreme exhaustion: 'dead on one's feet'. To be 'dead on your feet' means to be physically and mentally exhausted to the point where you can barely stand or keep your eyes open."),
        ("Solu", "Here is a great example: 'After running a full marathon and driving three hours back home, Samantha was completely dead on her feet.'"),
        ("Tonu", "And what is our sixth and final expression for today, Solu?"),
        ("Solu", "Our sixth expression is 'a wake-up call'. A 'wake-up call' is an alarming event, health scare, or warning that forces you to realize that you need to change your habits, attitude, or behavior immediately!"),
        ("Tonu", "Let's hear an example: 'Fainting during the morning team meeting was a severe wake-up call for Julian to start prioritizing his sleep and nutrition.'"),

        # SECTION 14: INTERACTIVE SPEAKING PRACTICE
        ("Solu", "Now, it is time for our Interactive Speaking Challenge! This is your turn to speak English out loud along with us. Sit up tall, fill your lungs with air, and repeat each sentence with confidence, rhythm, and clear pronunciation!"),
        ("Tonu", "Sentence number one: 'Prioritizing eight hours of restful sleep is not a luxury; it is the foundation of high performance and vitality.' Your turn!"),
        ("Solu", "Speak it out loud with conviction: 'Prioritizing eight hours of restful sleep is not a luxury; it is the foundation of high performance and vitality.'"),
        ("Tonu", "Wonderful pacing! Sentence number two: 'Before making that major life decision, I always make sure to sleep on it.' Your turn!"),
        ("Solu", "Repeat with natural English melody: 'Before making that major life decision, I always make sure to sleep on it.'"),
        ("Tonu", "Fantastic! Sentence number three: 'Stepping into morning sunlight sets your internal clock and gives you steady energy all day long.' Your turn!"),
        ("Solu", "Say it clearly: 'Stepping into morning sunlight sets your internal clock and gives you steady energy all day long.'"),
        ("Tonu", "Sentence number four: 'When you take care of your sleep, you take care of your brain, your mood, and your future.' Your turn!"),
        ("Solu", "Let's say sentence number four together: 'When you take care of your sleep, you take care of your brain, your mood, and your future.'"),
        ("Tonu", "Outstanding job! Your pronunciation is crisp, your spoken confidence is blossoming, and your vocal cadence is sounding more and more like a native speaker!"),

        # SECTION 15: REFLECTION & FAREWELL
        ("Solu", "And now, it is time for today's Weekly Reflection Question! We want you to practice writing in English down in the comment section below."),
        ("Tonu", "Here is today's question: 'What is your current sleep routine like? Do you struggle with late-night screen scrolling, or do you have a peaceful wind-down ritual? What is one habit from today's episode that you will try tonight to improve your rest?'"),
        ("Solu", "Writing your thoughts down in English helps solidify your vocabulary and gives you accountability to create healthier habits. Leave your comment below!"),
        ("Tonu", "Solu and I read through every single comment, and we love cheering on your progress and interacting with our wonderful global community."),
        ("Solu", "Remember that true strength is knowing when to work hard and when to surrender to deep, healing rest."),
        ("Tonu", "Sleep deeply, dream boldly, and keep practicing your spoken English with joy every single day!"),
        ("Solu", "Until next time, goodbye from Solu!"),
        ("Tonu", "And goodbye from Tonu!"),
        ("Both", "Happy learning, sleep well, and goodbye!")
    ]
    return turns

if __name__ == "__main__":
    t = build_ep35()
    gen_common.verify_and_save(35, "scripts/daily_speak_ep35_full.txt",
                              "Sleep Architecture, Dreams & The Neuroscience of Rest",
                              "Daily Speak English | English Listening & Speaking Practice",
                              t)

