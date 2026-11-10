#!/usr/bin/env python3
"""
Daily Speak English - Episode 45
Title: Managing Anger, Reactivity & The 90-Second Emotional Wave
Requirements:
- Starts with Tonu: "Hey hey, lovely listeners!..."
- Words >= 3,550 (strict duration >= 25.5 - 28.0 mins)
- High-level engaging, natural conversational English
"""

import gen_common

def build_ep45():
    turns = [
        # SECTION 1: MAGNETIC OPENING
        ("Tonu", "Hey hey, lovely listeners! Welcome back to Daily Speak English, your favorite place to become fluent, confident, and unstoppable in English! I'm Tonu!"),
        ("Solu", "And I'm Solu! Welcome back, everyone! Today, we are mastering an emotional fire that can either forge you into an unshakeable leader or burn down your most precious relationships in ten seconds of madness: the neuroscience of Anger, emotional reactivity, and the miraculous secret known as 'The 90-Second Emotional Wave'!"),
        ("Tonu", "Solu, think about how quickly human anger erupts! Someone cuts you off in highway traffic; a coworker sends a sarcastic, passive-aggressive email; or your partner makes an unfair comment about your habits!"),
        ("Solu", "Within half a second, your blood boils! Your heart hammers against your ribs like a war drum, your vision tunnels, your fists clench, and your throat tightens with furious adrenaline!"),
        ("Tonu", "And in that blind rush of rage, people scream words they regret for the next twenty years! They send furious messages that destroy marriages, ruin careers, fracture lifelong friendships, and shatter trust!"),
        ("Solu", "And five minutes later, as the red mist clears, a wave of sickening guilt and shame crashes down, and they wonder: 'Why did I say that? What came over me? That wasn't even me!'"),
        ("Tonu", "Today, we are going to unpack the cutting-edge brain science behind the Amygdala Hijack, discover Dr. Jill Bolte Taylor's 90-Second Rule, reveal why 'venting' actually makes anger worse, share physical nervous system resets, and master emotional regulation English!"),
        ("Solu", "As the ancient Stoic philosopher Seneca wrote two thousand years ago in his famous treatise 'On Anger': 'Anger is a temporary madness. For it is equally lustful of harm, and cares not for itself so long as it may hurt another.'"),

        # SECTION 2: THE 90-SECOND CHEMICAL RULE (DR. JILL BOLTE TAYLOR)
        ("Tonu", "Let's begin with one of the most astonishing discoveries in modern neuroscience: Harvard neuroanatomist Dr. Jill Bolte Taylor's '90-Second Rule'!"),
        ("Solu", "Explain this biological miracle to our listeners, Tonu! What happens during those ninety seconds?"),
        ("Tonu", "Dr. Taylor discovered that when a human being perceives an emotional trigger, a chemical surge of stress hormones—adrenaline, noradrenaline, and cortisol—floods into the bloodstream!"),
        ("Solu", "Your heart rate spikes, your blood vessels constrict, and your muscles tense up for physical combat!"),
        ("Tonu", "And do you know how long that biological chemical reaction physically lasts in your body from start to finish?"),
        ("Solu", "Less than ninety seconds! Exactly one and a half minutes!"),
        ("Tonu", "Within ninety seconds, the chemicals are filtered, metabolized, and completely flushed out of your bloodstream!"),
        ("Solu", "Now, wait a minute, Solu! If the chemical reaction is completely over in ninety seconds, why do people stay furious for four hours, three days, or twenty years?"),
        ("Tonu", "Because of the STORY their conscious mind tells! The ninety seconds is biology; everything after ninety seconds is psychology!"),
        ("Solu", "After the chemical wave passes, your brain loops: 'How dare he disrespect me! Did you see how she looked at me? I will never forgive them! Next time I see them, I am going to tell them off!'"),
        ("Tonu", "Every time you replay that angry thought in your head, your brain triggers a brand-new ninety-second surge of adrenaline! You are personally reigniting the fire over and over again!"),
        ("Solu", "If you can simply watch the chemical wave wash over you for ninety seconds without speaking, typing, or reacting, the physiological rage will naturally dissolve!"),

        # SECTION 3: THE AMYGDALA HIJACK & EVOLUTIONARY SURVIVAL
        ("Solu", "Now let's examine the brain structure responsible for this explosion: what Dr. Daniel Goleman coined as 'The Amygdala Hijack'!"),
        ("Tonu", "Your amygdala is an ancient, almond-shaped cluster of nuclei nestled deep in the primitive limbic system of your brain!"),
        ("Solu", "Its job is survival! Hundreds of thousands of years ago, if a saber-toothed tiger leaped from the bushes, your amygdala didn't want you to stop and write a philosophical essay about the tiger's fur pattern!"),
        ("Tonu", "It bypassed your logical prefrontal cortex completely! It triggered instant physical fight-or-flight within twenty milliseconds!"),
        ("Solu", "The problem is that your ancient amygdala cannot tell the difference between a real saber-toothed tiger and an insulting email from your boss!"),
        ("Tonu", "It reacts to social disrespect, perceived unfairness, and emotional criticism with the exact same violent survival emergency!"),
        ("Solu", "When your amygdala hijacks your brain, blood flow is literally diverted AWAY from your logical prefrontal cortex! You are functioning with the cognitive capacity of a terrified prehistoric caveman!"),
        ("Tonu", "Never try to solve a problem, negotiate a contract, or have a serious conversation during an Amygdala Hijack! Step away until your prefrontal cortex comes back online!"),

        # SECTION 4: VIKTOR FRANKL'S SACRED SPACE
        ("Solu", "Let's reflect on one of the most sublime philosophical insights of the twentieth century: Austrian neurologist and Holocaust survivor Viktor Frankl's famous principle!"),
        ("Tonu", "Viktor Frankl wrote: 'Between stimulus and response there is a space. In that space is our power to choose our response. In our response lies our growth and our freedom.'"),
        ("Solu", "Think about what reactive people do! A stimulus happens: someone says something rude. Zero space! Boom: immediate explosive insult!"),
        ("Tonu", "They are like a pinball machine! Hit a button, and they make a loud noise! They have zero internal sovereignty; anyone on the street can push their buttons and control their emotional state!"),
        ("Solu", "A wise, emotionally mature person creates SPACE between the stimulus and the response!"),
        ("Tonu", "When an insult or provocation arrives, they pause. They breathe. They observe their internal surge of heat without becoming the heat!"),
        ("Solu", "In that sacred space of two seconds, ten seconds, or an hour, they choose a response grounded in dignity, wisdom, and strategic poise!"),

        # SECTION 5: ANGER AS A SECONDARY EMOTION: UNMASKING THE TRUTH
        ("Tonu", "Let's explore a fundamental psychological truth taught in psychotherapy: Anger is almost ALWAYS a 'Secondary Emotion'!"),
        ("Solu", "What does it mean that anger is a secondary emotion, Tonu?"),
        ("Tonu", "Imagine an iceberg floating in the frozen North Atlantic! The jagged, menacing ice visible above the water line is Anger!"),
        ("Solu", "It looks aggressive, intimidating, loud, and powerful!"),
        ("Tonu", "But ninety percent of the iceberg is submerged underwater! And what is hiding under the surface of anger?"),
        ("Solu", "Primary emotions! Fear, heartbreak, feeling betrayed, feeling disrespected, grief, shame, physical exhaustion, and vulnerability!"),
        ("Tonu", "Think about a father whose six-year-old child runs into a busy street. The father sprints, grabs the child by the arm, pulls them to safety, and immediately shouts furiously: 'What is wrong with you? Don't you ever do that again!'"),
        ("Solu", "Is the father truly angry? No! The primary emotion was sheer, paralyzing TERROR of losing his precious child! But terror feels helpless, so the brain converts it into the active armor of anger!"),
        ("Tonu", "Whenever you feel blinding rage, ask yourself: 'What is the tender, vulnerable hurt hiding beneath this armor? Am I afraid? Am I feeling unappreciated? Did someone break my heart?'"),
        ("Solu", "Naming the primary emotion instantly disarms the rage and allows you to communicate your real truth."),

        # SECTION 6: THE DESTRUCTIVE MYTH OF 'VENTING'
        ("Solu", "Let's debunk a massive psychological myth that has circulated for decades: the belief in 'Catharsis' or 'Venting' your rage!"),
        ("Tonu", "For years, pop psychology told people: 'If you are angry, don't hold it in! Punch a pillow, smash plates in a rage room, scream into your mattress, or rant to your friend!'"),
        ("Solu", "People assumed that anger was like steam building up in a pressure cooker, and that venting releases the pressure!"),
        ("Tonu", "Modern clinical psychology has thoroughly tested this, and the results are unanimous: VENTING DOES NOT REDUCE ANGER! VENTING MAKES ANGER SIGNIFICANTLY WORSE!"),
        ("Solu", "Dr. Brad Bushman, a leading psychologist at Ohio State University, conducted extensive experiments with angry participants. One group hit punching bags while thinking about the person who angered them, while the other group sat quietly in a chair."),
        ("Tonu", "And what happened, Solu?"),
        ("Solu", "The participants who hit the punching bag became significantly MORE aggressive, hostile, and vengeful toward others than the group who sat quietly!"),
        ("Tonu", "Why? Because practicing aggression trains and reinforces neural pathways for aggression! By shouting and punching, you are rehearsing rage in your brain circuits!"),
        ("Solu", "Do not feed the fire! Venting fans the flames; stillness, deep breathing, and cognitive reframing starve the fire of oxygen."),

        # SECTION 7: SOMATIC NERVOUS SYSTEM RESETS
        ("Solu", "Now, when that physical chemical wave hits you, what concrete physiological tools can you use in real time to down-regulate your nervous system?"),
        ("Tonu", "Tool number one is 'The Physiological Sigh', popularized by Stanford neurobiologist Dr. Andrew Huberman!"),
        ("Solu", "How do you perform a Physiological Sigh, Tonu?"),
        ("Tonu", "Take two rapid inhalations through your nose: one deep breath, followed immediately by a quick second sip of air to maximally inflate the alveoli sacs in your lungs!"),
        ("Solu", "And then, release a long, slow, unforced exhalation through your mouth: 'Ahhhhh...'!"),
        ("Tonu", "Doing two or three physiological sighs immediately slows your heart rate down within ten seconds through the vagus nerve!"),
        ("Solu", "Tool number two is 'The Mammalian Dive Reflex'!"),
        ("Tonu", "If you feel blinding, uncontrollable rage, walk to the restroom and splash ice-cold water directly onto your forehead, nose, and upper cheeks!"),
        ("Solu", "Cold water on those facial trigeminal nerves triggers an ancient aquatic biological reflex that instantly drops your heart rate and forces your central nervous system out of panic!"),

        # SECTION 8: THE 24-HOUR RULE FOR DIGITAL REACTIVITY
        ("Tonu", "Let's establish a golden digital boundary that will save your career and your relationships: 'The 24-Hour Draft Rule'!"),
        ("Solu", "How many times have you received an infuriating email or message at 9 PM and immediately typed a blistering, venomous reply with smoking fingers?"),
        ("Tonu", "If you feel angry while writing a message, NEVER press send!"),
        ("Solu", "Open a blank text file or notes app—NOT your email client where you might accidentally hit send—and type out everything you honestly want to say! Get all your frustration onto the page!"),
        ("Tonu", "Then, close the laptop, walk away, and wait twenty-four hours! Sleep on it! Let the chemicals flush out!"),
        ("Solu", "Ninety-nine percent of the time, when you re-read that angry draft the next morning, your stomach will churn in horror, and you will say: 'Thank heavens I didn't send that!'"),
        ("Tonu", "You delete ninety percent of the emotional venom, extract the three factual business points, and send a calm, professional response that commands respect."),

        # SECTION 9: MARCUS AURELIUS & THE STOIC MORNING MEDITATION
        ("Solu", "Let's draw timeless wisdom from Roman Emperor Marcus Aurelius, the most powerful man in the ancient world!"),
        ("Tonu", "Every single morning in his military tent, Marcus opened his private journal, 'Meditations', and wrote these famous words to himself:"),
        ("Solu", "'When you wake up in the morning, tell yourself: The people I deal with today will be meddling, ungrateful, arrogant, dishonest, jealous, and surly.'"),
        ("Tonu", "Why did a Roman emperor remind himself of that every morning?"),
        ("Solu", "Because anger is born from breached expectations! If you walk into your day expecting everyone to be angelic, polite, reasonable, and perfectly considerate, you will be enraged by 8:30 AM!"),
        ("Tonu", "Marcus prepared his mind in advance! He wrote: 'They are like this because they cannot distinguish good from evil. But I have seen the beauty of good, and I cannot be injured by any of them, nor can I be angry with my kinsman.'"),
        ("Solu", "Expect people to be flawed, imperfect, and stressed. When you inoculate yourself against surprise, their rudeness cannot disturb your sovereign peace."),

        # SECTION 10: NONVIOLENT ASSERTIVENESS: SPEAKING YOUR TRUTH WITHOUT SHOUTING
        ("Tonu", "Managing anger does NOT mean being a passive, spineless doormat who allows people to mistreat them!"),
        ("Solu", "Suppressing your anger into silent resentment is just as toxic as exploding!"),
        ("Tonu", "The goal is 'Assertive Calm'! You don't shout, you don't insult, and you don't attack; but you speak your boundary with icy, unyielding clarity!"),
        ("Solu", "A whisper spoken with absolute moral conviction is infinitely more terrifying and authoritative than a scream!"),
        ("Tonu", "When you scream, people focus on your bad behavior rather than their original offense. But when you remain utterly calm and state the boundary firmly, the spotlight of responsibility remains entirely on them!"),

        # SECTION 11: PASSIVE AGGRESSION: THE COLD WAR OF ANGER
        ("Solu", "Let's also examine a deceptive, toxic form of anger that destroys relationships from the inside out: 'Passive Aggression'!"),
        ("Tonu", "Passive aggression is anger that lacks the courage to speak directly!"),
        ("Solu", "What does passive aggression look like in daily life, Tonu?"),
        ("Tonu", "It looks like the 'Silent Treatment'—refusing to look at someone or speak for three days! It looks like heavy, theatrical sighing, slamming kitchen cabinet doors, sarcastic eye-rolling, and deliberate 'weaponized incompetence'!"),
        ("Solu", "And when you ask them: 'Are you upset? What's wrong?', they say with cold, frozen lips: 'Nothing. I am completely fine!'"),
        ("Tonu", "That is emotional cowardice and psychological manipulation! It forces the other person to walk on eggshells, guessing your thoughts!"),
        ("Solu", "If you have an issue, have the adult maturity to state it with clarity: 'When you arrived forty minutes late without texting me, it made me feel disrespected. In the future, please notify me in advance so I can plan my time.'"),
        ("Tonu", "Direct, compassionate honesty is the only antidote to the toxic smog of passive aggression!"),

        # SECTION 12: THE 'HALT' PROTOCOL: BIOLOGY MASQUERADING AS RAGE
        ("Solu", "Let's share a practical four-letter diagnostic acronym used in crisis counseling: 'HALT'!"),
        ("Tonu", "HALT stands for Hungry, Angry, Lonely, and Tired!"),
        ("Solu", "Whenever you find yourself filled with sudden, uncontrollable irritability or fury, stop and ask yourself: 'Am I Hungry? Am I Lonely? Am I physically Tired?'"),
        ("Tonu", "Eighty percent of the time, that 'deep philosophical problem' with your spouse or coworker is actually low blood sugar and sleep deprivation!"),
        ("Solu", "Your brain has run out of glucose, and your cortisol is elevated from exhaustion!"),
        ("Tonu", "Never make a major life decision, never evaluate your relationships, and never initiate a heavy argument when your body is in HALT mode!"),
        ("Solu", "Drink a large glass of water, eat a nutritious meal with protein, take a twenty-minute rest, and then see if the problem still feels like a catastrophic emergency!"),

        # SECTION 13: NELSON MANDELA & FORGIVENESS AS SELF-PRESERVATION
        ("Tonu", "Let's reflect on the ultimate master of emotional transcendence: Nelson Mandela!"),
        ("Solu", "Mandela was imprisoned for twenty-seven grueling years on Robben Island, breaking limestone rocks in a tiny concrete cell by an apartheid regime!"),
        ("Tonu", "Yet when he was finally released, he invited his former prison guard to sit in the front row of his presidential inauguration, and worked closely with the very leaders who had locked him away!"),
        ("Solu", "When asked by an American journalist: 'Mr. Mandela, do you not feel burning hatred and resentment for what they did to you for twenty-seven years?'"),
        ("Tonu", "Mandela gave one of the most immortal answers in human history: 'As I walked out the door toward the gate that would lead to my freedom, I knew if I didn't leave my bitterness and hatred behind, I'd still be in prison.'"),
        ("Solu", "And Mandela famously said: 'Resentment is like drinking poison and then hoping it will kill your enemies!'"),
        ("Tonu", "Forgiveness is NOT saying that what the other person did was okay; forgiveness is not excusing abuse! Forgiveness is simply putting down the hot coal that is burning YOUR own hand."),
        ("Solu", "Releasing hatred sets the prisoner free—and then you discover that the prisoner was YOU all along."),
        ("Tonu", "And remember the crucial difference between Forgiveness and Reconciliation!"),
        ("Solu", "Forgiveness happens entirely inside your own heart; it is unconditional and does not require the other person to apologize or even be alive!"),
        ("Tonu", "Reconciliation, however, requires TWO people! It requires that the other person genuinely acknowledges the harm, changes their behavior, and rebuilds trust over time."),
        ("Solu", "You can forgive someone completely so that you are free from bitterness, while still keeping a firm boundary that prevents them from ever hurting you again."),

        # SECTION 14: LIVE ROLEPLAY: DE-ESCALATING AN UNFAIR WORKPLACE ACCUSATION
        ("Solu", "Now let's demonstrate a realistic real-world roleplay! Imagine a manager or client accuses you in a meeting: 'You completely botched the quarterly data presentation! It was an absolute mess!'"),
        ("Tonu", "An untrained person either shrinks into tears or explodes: 'You don't know what you are talking about! You never gave me the files!'"),
        ("Solu", "Let's demonstrate how a master of emotional regulation handles this with poise! Tonu, play the angry manager."),
        ("Tonu", "Solu! What was that presentation this morning? The numbers were confusing, and the client was unimpressed! Did you even prepare for this?"),
        ("Solu", "Here is how you respond with calm, grounded authority: 'I hear your frustration, Tonu, and I take our client relationships very seriously. The revised dataset arrived from accounting thirty minutes before the call, which did not allow time for our usual cross-checking. I have already audited the discrepancy and prepared a revised, clean executive summary. Let's sit down for fifteen minutes this afternoon, review the corrections together, and send the updated deck to the client. How does 2 PM work for you?'"),
        ("Tonu", "Look at the mastery of that response! You didn't become defensive, you didn't match her high emotional pitch, you stated the objective operational fact, presented a solution, and led the interaction toward a professional outcome!"),
        ("Solu", "When someone throws fire, you don't throw gasoline back; you bring water, clarity, and leadership."),

        # SECTION 12: VOCABULARY & IDIOM SPOTLIGHT (6 KEY IDIOMS)
        ("Tonu", "Now, let's step into our signature segment: Key Everyday English Idioms and Phrases! Today, we have selected six colorful, essential expressions about anger, emotional regulation, and conflict!"),
        ("Solu", "Let's master them together! Tonu, what is our very first anger idiom for today?"),
        ("Tonu", "Our first expression describes sudden, uncontrolled rage: 'fly off the handle'. To 'fly off the handle' means to lose your temper suddenly, unexpectedly, and violently over something minor."),
        ("Solu", "Let's listen to a natural conversational example: 'Whenever traffic was delayed, our old supervisor would fly off the handle and scream at everyone in the car.'"),
        ("Tonu", "Never fly off the handle! What is our second expression, Solu?"),
        ("Solu", "Our second expression describes the pinnacle of emotional self-mastery: 'keep one's cool'. To 'keep your cool' means to remain calm, composed, and rational in a stressful, provocative, or chaotic situation."),
        ("Tonu", "Here is how you can use it: 'Despite the hostile questions from journalists, the diplomat kept her cool and answered with poised elegance.'"),
        ("Solu", "Keep your cool, protect your peace! Tonu, introduce our third idiom."),
        ("Tonu", "Our third expression describes restraint: 'bite one's tongue'. To 'bite your tongue' means to deliberately stop yourself from saying something angry, sarcastic, or offensive, even though you desperately want to say it!"),
        ("Solu", "Let's hear an example: 'When his mother-in-law criticized his cooking, Marcus bit his tongue and simply smiled politely to keep the peace.'"),
        ("Tonu", "Biting your tongue saves countless relationships! What is our fourth expression, Solu?"),
        ("Solu", "Our fourth expression describes blinding fury: 'see red'. To 'see red' means to become intensely, uncontrollably angry and enraged."),
        ("Tonu", "For example: 'When he saw the vandal scratching the paint on his vintage car, he completely saw red.'"),
        ("Solu", "Recognize when you are seeing red, and pause! Tonu, take us to our fifth idiom."),
        ("Tonu", "Our fifth expression is 'clear the air'. To 'clear the air' means to discuss a tense misunderstanding, resentment, or disagreement openly and honestly so that bad feelings are resolved."),
        ("Solu", "Here is a wonderful example: 'The tension in our design team was palpable, so we had an open Friday morning meeting to clear the air.'"),
        ("Tonu", "And what is our sixth and final expression for today, Solu?"),
        ("Solu", "Our sixth expression describes a healthy release: 'blow off steam'. To 'blow off steam' means to release pent-up stress, frustration, or nervous energy through harmless physical exercise, sports, or creative hobbies."),
        ("Tonu", "Let's hear an example: 'After an intense twelve-hour day dealing with difficult customer complaints, Elena went for a five-mile run to blow off steam.'"),

        # SECTION 16: INTERACTIVE SPEAKING PRACTICE
        ("Solu", "Now, it is time for our Interactive Speaking Challenge! This is your turn to speak English out loud along with us. Open your chest, drop your shoulders, breathe deeply, and repeat each sentence with calm authority and steady cadence!"),
        ("Tonu", "Sentence number one: 'Between stimulus and response, I choose the power of calm reflection.' Your turn!"),
        ("Solu", "Speak it out loud with clear cadence: 'Between stimulus and response, I choose the power of calm reflection.'"),
        ("Tonu", "Beautiful rhythm! Sentence number two: 'No matter how chaotic the storm, I have the self-mastery to keep my cool.' Your turn!"),
        ("Solu", "Repeat with steady conviction: 'No matter how chaotic the storm, I have the self-mastery to keep my cool.'"),
        ("Tonu", "Wonderful! Sentence number three: 'Pausing for ninety seconds gives my logical brain the space to lead with wisdom.' Your turn!"),
        ("Solu", "Say it clearly: 'Pausing for ninety seconds gives my logical brain the space to lead with wisdom.'"),
        ("Tonu", "Sentence number four: 'When you respond with calm dignity, you command respect in any room.' Your turn!"),
        ("Solu", "Let's say sentence number four together: 'When you respond with calm dignity, you command respect in any room.'"),
        ("Tonu", "Outstanding work! Notice how grounded, commanding, and serene your spoken English sounds when you speak from emotional self-mastery!"),
        ("Solu", "Every time you practice speaking with calm self-restraint, you wire your brain for unshakable peace and authority."),

        # SECTION 17: REFLECTION & FAREWELL
        ("Solu", "And now, it is time for today's Weekly Reflection Question! We want you to practice writing in English down in the comment section below."),
        ("Tonu", "Here is today's question: 'What is a specific trigger that usually makes you lose your temper or feel defensive? What is one strategy from today's episode—like the 90-second pause or the physiological sigh—that you will use the next time you feel that heat rising?'"),
        ("Solu", "Writing your reflection in English anchors emotional self-mastery into your daily awareness. Share your thoughts in the comments below!"),
        ("Tonu", "Solu and I read through every single comment, and we are so proud of your dedication to emotional maturity and English fluency!"),
        ("Solu", "Every insight you write down reminds thousands of other listeners that we all share the same human struggles, and that we can master our minds together."),
        ("Tonu", "True strength is never about overpowering someone with screams; true strength is mastering your own impulses with grace."),
        ("Solu", "When you master your emotions, you master your destiny, turning every provocation into an opportunity to demonstrate your highest character."),
        ("Tonu", "You become an unshakeable, majestic mountain that remains completely peaceful regardless of how fiercely the outside winds blow."),
        ("Solu", "Remember: anyone can become angry—that is easy. But to be angry with the right person, to the right degree, at the right time, for the right purpose—that is true mastery."),
        ("Tonu", "Breathe deeply, hold your peace, and keep speaking English with bold confidence every single day!"),
        ("Solu", "Until next time, goodbye from Solu!"),
        ("Tonu", "And goodbye from Tonu!"),
        ("Both", "Happy learning, keep your cool, and goodbye!")
    ]
    return turns

if __name__ == "__main__":
    t = build_ep45()
    gen_common.verify_and_save(45, "scripts/daily_speak_ep45_full.txt",
                              "Managing Anger, Reactivity & The 90-Second Emotional Wave",
                              "Daily Speak English | English Listening & Speaking Practice",
                              t)
