#!/usr/bin/env python3
"""
Daily Speak English - Episode 48
Title: The Art of Apology: Forgiveness, Repair & Letting Go of Resentment
Requirements:
- Starts with Tonu: "Hey hey, lovely listeners!..."
- Words >= 3,550 (strict duration >= 25.5 - 28.0 mins)
- High-level engaging, natural conversational English
"""

import gen_common

def build_ep48():
    turns = [
        # SECTION 1: MAGNETIC OPENING
        ("Tonu", "Hey hey, lovely listeners! Welcome back to Daily Speak English, your favorite place to become fluent, confident, and unstoppable in English! I'm Tonu!"),
        ("Solu", "And I'm Solu! Welcome back, everyone! Today, we are mastering an emotional and linguistic superpower that has the miraculous power to heal fractured families, resurrect broken friendships, restore professional trust, and liberate your soul: 'The Art of Apology', the psychology of relational repair, and the courage to release resentment!"),
        ("Tonu", "Solu, why is it that three tiny words—'I was wrong'—are often the hardest, most agonizing words for a human tongue to utter?"),
        ("Solu", "Because to an insecure human ego, admitting a mistake feels like an existential execution! People will argue for three hours, invent fifty convoluted excuses, twist historical facts, and burn down a ten-year relationship just to protect their stubborn pride!"),
        ("Tonu", "And look at the terrible fake apologies people give every single day! They say: 'I'm sorry IF you were offended!' or 'I'm sorry, BUT you provoked me!' or 'Mistakes were made!'"),
        ("Solu", "Those are not apologies; those are disguised verbal attacks that inflict even deeper insult on the person who was hurt!"),
        ("Tonu", "Today, we are going to explore Dr. Harriet Lerner's clinical framework for genuine apology, analyze the neurobiology of defensiveness, examine why holding a grudge physically damages your cardiovascular heart tissue, share how to forgive people who never apologize, and master empathetic English!"),
        ("Solu", "A sincere apology is not a sign of weakness; a sincere apology is the highest demonstration of emotional maturity, strength of character, and respect."),

        # SECTION 2: THE TOXIC ANATOMY OF FAKE APOLOGIES
        ("Solu", "Let's begin by exposing the five most common counterfeit apologies that poison human relationships!"),
        ("Tonu", "Counterfeit apology number one is 'The 'IF' Apology'!"),
        ("Solu", "'I am sorry IF you felt hurt by what I said.' Notice how insidious that is! The word 'IF' shifts the blame onto the other person's sensitivity!"),
        ("Tonu", "It implies: 'What I said was completely fine, but you are overly fragile and sensitive!'"),
        ("Solu", "Counterfeit apology number two is 'The 'BUT' Apology' or The Eraser!"),
        ("Tonu", "'I am sorry I shouted at you, BUT you were being completely unreasonable and made me late!'"),
        ("Solu", "The word 'BUT' acts like a giant eraser that wipes away everything that came before it! Everything before the 'but' is a lie; everything after the 'but' is the real excuse!"),
        ("Tonu", "Counterfeit apology number three is 'The Passive Bureaucratic Apology'—popularized by politicians and corporate spokespeople: 'Mistakes were made!'"),
        ("Solu", "Notice the passive voice! Who made the mistakes? Aliens from Mars? A ghost? The passive voice completely avoids personal agency and accountability!"),
        ("Tonu", "Counterfeit apology number four is 'The Theatrical Over-Apology'!"),
        ("Solu", "When you tell someone they hurt you, they burst into hysterical tears: 'Oh, I am the worst human being on Earth! I ruin everything! You should hate me!'"),
        ("Tonu", "Suddenly, YOU have to comfort THEM! They flipped the script, making themselves the victim while evading all responsibility!"),
        ("Solu", "And Counterfeit apology number five is 'The Demand Apology'—demanding immediate forgiveness: 'I said I'm sorry, why are you still upset? You need to get over it right now!'"),
        ("Tonu", "An apology is an offering of repair; an apology is never a demand for instant pardon!"),

        # SECTION 3: DR. HARRIET LERNER'S 6 LAWS OF A GENUINE APOLOGY
        ("Solu", "Now let's examine the gold standard: renowned psychologist Dr. Harriet Lerner's landmark book, 'Why Won't You Apologize?'!"),
        ("Tonu", "Dr. Lerner outlines six essential pillars of a genuine, healing apology. What is pillar number one, Solu?"),
        ("Solu", "Pillar number one: 'Zero Excuses, Zero Ifs, and Zero Buts'! Keep the spotlight of accountability entirely on your own behavior!"),
        ("Tonu", "Pillar number two: 'Acknowledge the Specific Impact on the Other Person'! Don't just say 'I'm sorry.' Say: 'I understand that when I canceled our plans at the last minute, you had prepared dinner, and it made you feel dismissed and undervalued.'"),
        ("Solu", "Demonstrate that you viscerally understand the emotional hurt your actions caused!"),
        ("Tonu", "Pillar number three: 'Offer Tangible Amends and Restitution'! What can you do to fix what was broken, repair the damage, or restore equity?"),
        ("Solu", "Pillar number four: 'Commit to Genuine Behavioral Change'! An apology without changed behavior is mere manipulation! Explain what concrete steps you are taking to ensure this never happens again."),
        ("Tonu", "Pillar number five: 'Do Not Get Defensive if the Person Does Not Immediately Forgive You'! Forgiveness takes time; give them space to process their feelings."),
        ("Solu", "And Pillar number six: 'Never Ask Them to Comfort You'! Carry the emotional weight of your own accountability like a mature adult."),

        # SECTION 4: THE NEUROBIOLOGY OF DEFENSIVENESS & EGO THREAT
        ("Tonu", "Why is it so excruciatingly painful for our brains to admit we made a mistake?"),
        ("Solu", "Because of what cognitive psychologists call 'Ego Threat' and 'Cognitive Dissonance'!"),
        ("Tonu", "Most people have an internal identity story: 'I am a good, kind, competent, fair, and intelligent human being.'"),
        ("Solu", "When evidence arises showing that you acted unfairly, lied, hurt someone, or made a blunder, your brain experiences acute cognitive dissonance!"),
        ("Tonu", "Your brain perceives two contradictory realities: 'I am a good person' versus 'I just did something hurtful and terrible!'"),
        ("Solu", "To resolve that agonizing dissonance, an insecure ego either denies reality, blames the victim, or attacks!"),
        ("Tonu", "A truly confident person understands that making a bad decision does not make you a bad human being!"),
        ("Solu", "You can have a noble heart while still having made a clumsy, thoughtless, or hurtful mistake. Separating your core worth from your behavior allows you to apologize freely without shame."),

        # SECTION 5: THE EMOTIONAL BALANCE SHEET & RESTITUTION
        ("Solu", "Let's explore the concept of the 'Emotional Balance Sheet' in human relationships!"),
        ("Tonu", "Every relationship is like an emotional bank account. Kindness, active listening, honesty, and loyalty are deposits."),
        ("Solu", "Broken promises, harsh insults, and neglect are massive withdrawals!"),
        ("Tonu", "When you inflict a severe emotional injury on someone, you create a massive deficit on the balance sheet!"),
        ("Solu", "Simply saying: 'Sorry about that, let's move on!' does not balance the ledger!"),
        ("Tonu", "You must make deliberate, intentional deposits of care, reliability, and restitution over a sustained period to rebuild the reservoir of trust!"),
        ("Solu", "Trust is like a mirror: once broken, you can glue it back together, but you can still see the cracks unless you patiently polish and heal the surface with consistent integrity."),

        # SECTION 6: FORGIVENESS VS RECONCILIATION: PROTECTING YOUR BOUNDARIES
        ("Tonu", "Now, let's address the receiver of an apology: the vital difference between Forgiveness and Reconciliation!"),
        ("Solu", "Many people refuse to forgive because they believe that forgiving someone means you MUST welcome them right back into your living room, your business, or your heart!"),
        ("Tonu", "That is a dangerous misunderstanding! Let's separate the two concepts clearly, Solu."),
        ("Solu", "Forgiveness is internal emotional surgery! It is between you and your own soul! It means choosing to let go of the burning poison of hatred and resentment so that it no longer destroys your peace!"),
        ("Tonu", "Reconciliation, however, is a relational contract! It requires mutual respect, safety, verified honesty, and changed behavior!"),
        ("Solu", "You can forgive an unfaithful partner or an abusive family member completely—wishing them peace from afar—while still maintaining an absolute boundary: 'I forgive you, but you no longer have access to my life.'"),
        ("Tonu", "You can forgive from a safe distance! Wisdom and mercy walk hand in hand."),

        # SECTION 7: RADICAL FORGIVENESS: WHEN NO APOLOGY EVER ARRIVES
        ("Solu", "What if the person who deeply injured you never apologized? What if they died, or what if they are so arrogant that they boast about hurting you?"),
        ("Tonu", "Must you wait for their apology to be free from your pain?"),
        ("Solu", "Never! If your healing depends on the person who broke you saying 'I'm sorry', then you are handing the remote control of your emotional freedom to your tormentor!"),
        ("Tonu", "Why would you give the person who hurt you the power to keep you in emotional chains forever?"),
        ("Solu", "Practice 'Radical Acceptance' and self-liberation! Acknowledge: 'They may never possess the emotional maturity or courage to apologize. But my life is too precious to spend twenty years waiting for words that will never come. I release the debt today, not for them, but for ME!'"),
        ("Tonu", "Cancel the debt in your heart! When you cancel the debt, the debtor loses all power over your peace."),

        # SECTION 8: THE SOMATIC COST OF RESENTMENT: CARDIAC HEALTH
        ("Solu", "Let's look at the hard medical science of holding grudges: Dr. Charlotte van Oyen Witvliet's clinical research at Hope College!"),
        ("Tonu", "What did researchers discover when they hooked participants up to cardiac monitors, blood pressure cuffs, and electromyography sensors, Solu?"),
        ("Solu", "When participants mentally replayed old grievances, betrayals, and grudges, their physiological response was catastrophic!"),
        ("Tonu", "Their systolic and diastolic blood pressure skyrocketed! Their heart rate variability crashed! Cortisol and stress hormones flooded their veins!"),
        ("Solu", "And the facial electromyography showed that their facial frowning muscles contracted involuntarily into patterns of chronic distress!"),
        ("Tonu", "And what happened when those same participants were guided through exercises of empathetic forgiveness?"),
        ("Solu", "Their blood pressure plunged back to normal! Their cardiovascular tension vanished, and their immune markers normalized!"),
        ("Tonu", "Carrying a grudge is literal cardiovascular poison! Every time you hate someone, your own physical heart pays the price!"),
        ("Solu", "Forgiveness is preventive cardiovascular medicine!"),

        # SECTION 9: SELF-FORGIVENESS: SILENCING THE GHOSTS OF REGRET
        ("Tonu", "Let's speak to the deepest, most agonizing apology of all: apologizing to YOURSELF and practicing Self-Forgiveness!"),
        ("Solu", "How many of our listeners carry heavy guilt over past mistakes: staying in a toxic relationship too long, wasting money, failing an exam, or hurting a loved one five years ago?"),
        ("Tonu", "You look back at your younger self with shame and disgust: 'How could I have been so foolish? Why didn't I see the red flags?'"),
        ("Solu", "Remember the golden law of human development: You did the best you could with the emotional maturity, knowledge, and tools you possessed at that time!"),
        ("Tonu", "Judging your twenty-year-old self with the thirty-year-old wisdom you acquired THROUGH that exact mistake is an act of chronological cruelty!"),
        ("Solu", "Look back at that younger version of you with compassion! Wrap your arms around them and say: 'You were hurting, you were confused, and you made a blunder. But look at the wisdom and character that grew from that scar. I forgive you. Let's walk forward together.'"),

        # SECTION 10: CULTURAL PERSPECTIVES ON APOLOGY
        ("Tonu", "Let's also look at how cultures around the world approach apologies: the fascinating contrast between Eastern and Western traditions!"),
        ("Solu", "In Japan, the art of apology, known as 'Ojigi' and 'Shazai', is deeply woven into the moral fabric of society!"),
        ("Tonu", "Japanese corporate CEOs, politicians, and railway directors will bow at a ninety-degree angle for two full minutes in front of cameras, taking collective responsibility for a train arriving two minutes late or a mechanical defect!"),
        ("Solu", "In collectivist cultures, an apology restores social harmony, humility, and trust in the collective web of society."),
        ("Tonu", "In Western legalistic individualist cultures, people are often terrified to apologize because lawyers warn that saying 'I'm sorry' can be construed as an admission of legal liability!"),
        ("Solu", "We must reclaim the human sacredness of apology beyond legalism! In personal relationships, an apology is an act of spiritual communion and relational rebirth."),
        ("Tonu", "When two people apologize with total vulnerability, the fractured relationship often becomes far stronger, deeper, and more resilient than it ever was before the crack occurred."),
        ("Solu", "Just like the Japanese art of Kintsugi, where broken pottery is repaired with shimmering gold lacquer, a healed relationship carries a golden beauty that makes its history sacred."),

        # SECTION 11: DR. GARY CHAPMAN'S 5 APOLOGY LANGUAGES
        ("Solu", "Let's explore a brilliant psychological framework from Dr. Gary Chapman and Dr. Jennifer Thomas: 'The 5 Languages of Apology'!"),
        ("Tonu", "Just like people have different Love Languages, different human beings need to hear different elements to feel that an apology is genuine!"),
        ("Solu", "What are the five apology languages, Tonu?"),
        ("Tonu", "Language number one is 'Expressing Regret'—simply hearing the sincere emotional words: 'I am so sorry for the pain I caused you.'"),
        ("Solu", "Language number two is 'Accepting Responsibility'—owning up without excuses: 'I was completely wrong. It was my fault.'"),
        ("Tonu", "Language number three is 'Making Restitution'—asking: 'What can I do to make this right? How can I fix what was damaged?'"),
        ("Solu", "Language number four is 'Genuinely Repenting'—presenting a concrete plan of behavioral change: 'Here are the steps I am taking so this never happens again.'"),
        ("Tonu", "And Language number five is 'Requesting Forgiveness'—humbly asking: 'Will you please forgive me?'"),
        ("Solu", "Notice how often partners clash because they speak different apology languages! One person desperately needs to hear 'I was wrong', but the other partner just buys flowers or says 'I'm sorry!'"),
        ("Tonu", "Ask your loved ones: 'When someone hurts you, what do you need to hear most to feel that they are genuinely remorseful?' Learning their apology language heals relationships fast!"),

        # SECTION 12: THE TRAP OF FORCED CHILDHOOD APOLOGIES
        ("Solu", "Let's examine how our childhood conditioning often ruined our ability to apologize as adults!"),
        ("Tonu", "Think about what parents and teachers do on the playground when two children fight!"),
        ("Solu", "The parent grabs the crying child by the arm, drags them in front of the other kid, and sternly orders: 'Say you are sorry right this second, or you are grounded!'"),
        ("Tonu", "And what does the child do? They look at their shoes, cross their arms, and mumble with bitter resentment: 'Sorry.'"),
        ("Solu", "What does that teach a developing child's brain, Tonu?"),
        ("Tonu", "It teaches the child that an apology is a humiliating, forced public punishment where you submit to an authority figure, rather than an act of authentic empathy and repair!"),
        ("Solu", "So as adults, people treat apologizing as a terrifying submission!"),
        ("Tonu", "Instead of forcing words, wise parents teach empathy: 'Look at your sister's face; she is crying because the tower fell. How can we help her rebuild it?' Focus on empathy and restitution, not forced humiliation!"),

        # SECTION 13: HO'OPONOPONO: THE HAWAIIAN HEALING MANTRA
        ("Solu", "Let's explore an ancient Hawaiian reconciliation practice that has brought profound peace to millions worldwide: 'Ho'oponopono'!"),
        ("Tonu", "In traditional Hawaiian culture, when interpersonal conflict or illness arose in a village, the community gathered for Ho'oponopono—a sacred process of spiritual and emotional alignment!"),
        ("Solu", "Ho'oponopono centers on four simple, immortal phrases that you can whisper in your heart toward anyone you hold resentment against:"),
        ("Tonu", "'I am sorry. Please forgive me. Thank you. I love you.'"),
        ("Solu", "Notice how complete that prayer is! 'I am sorry' acknowledges shared human frailty. 'Please forgive me' asks for release. 'Thank you' expresses gratitude for the lesson. 'I love you' restores divine connection!"),
        ("Tonu", "Repeating those four sentences dissolves the tight, icy knot of bitterness in your chest and opens your heart to unconditional peace."),
        ("Solu", "And here is a revolutionary insight: you can say those four phrases to YOURSELF in front of a mirror!"),
        ("Tonu", "Look into your own eyes in the bathroom mirror: 'I am sorry for doubting you. Please forgive me for being so harsh on you. Thank you for your resilience. I love you.'"),
        ("Solu", "That five-minute self-apology in the mirror has healed lifelong wounds of low self-esteem and self-loathing in thousands of people."),
        ("Tonu", "When you make peace with the person in the mirror, making peace with the outside world becomes natural and effortless."),

        # SECTION 14: LIVE ROLEPLAY: DELIVERING A SOULFUL, FLAWLESS APOLOGY
        ("Solu", "Now let's demonstrate a realistic real-world roleplay! Imagine you forgot to show up for an important dinner with a dear friend who needed your support, because you got wrapped up in work."),
        ("Tonu", "Most people make excuses: 'Traffic was terrible, work was crazy, you know how busy I am!'"),
        ("Solu", "Let's demonstrate how to deliver a flawless, healing apology using Dr. Lerner's principles! Tonu, play the hurt friend."),
        ("Tonu", "Solu, I waited at the restaurant for forty-five minutes on Friday evening. You didn't even text me until 9 PM. I was going through a really hard week, and I felt like our friendship didn't matter to you at all."),
        ("Solu", "Here is the master apology: 'Tonu, you are completely right, and I am so deeply sorry. There is no excuse for my thoughtlessness. I allowed myself to get consumed by work deadlines, and in doing so, I completely failed to show up for someone I love dearly. Seeing you sit at that restaurant alone breaks my heart, and I understand why it made you feel dismissed and undervalued. Your friendship is one of the greatest treasures of my life. I have already set alarms in my calendar, and I am committed to prioritizing our time with total reliability. I know this hurt our trust, and I don't expect you to brush it aside, but I would love the chance to make it up to you and cook dinner for you this weekend if you are open to it.'"),
        ("Tonu", "Look at how profound that is! Zero excuses, acknowledged the specific hurt, validated her pain, took full responsibility, and offered loving amends!"),
        ("Solu", "That kind of apology dissolves hurt and cements a friendship for decades."),

        # SECTION 12: VOCABULARY & IDIOM SPOTLIGHT (6 KEY IDIOMS)
        ("Tonu", "Now, let's step into our signature segment: Key Everyday English Idioms and Phrases! Today, we have selected six colorful, essential expressions about apology, forgiveness, and peace!"),
        ("Solu", "Let's master them together! Tonu, what is our very first idiom for today?"),
        ("Tonu", "Our first expression describes overcoming pride: 'swallow one's pride'. To 'swallow your pride' means to set aside your arrogance, ego, or embarrassment and do what is humble, necessary, and right."),
        ("Solu", "Let's listen to a natural conversational example: 'Although it was uncomfortable, Marcus swallowed his pride and admitted to his business partner that his marketing calculation was wrong.'"),
        ("Tonu", "Humility is true greatness! What is our second expression, Solu?"),
        ("Solu", "Our second expression describes restorative action: 'make amends'. To 'make amends' means to do something positive, corrective, or restorative to compensate for a hurt, mistake, or injustice you caused."),
        ("Tonu", "Here is how you can use it: 'To make amends for missing her daughter's violin recital, Elena took the entire following Friday off to spend quality time together.'"),
        ("Solu", "Actions speak louder than words! Tonu, introduce our third idiom."),
        ("Tonu", "Our third expression describes personal moral relief: 'clear one's conscience'. To 'clear your conscience' means to confess a truth, apologize, or right a wrong so you no longer feel guilty or tormented inside."),
        ("Solu", "Let's hear an example: 'He called his former colleague to apologize for taking credit for the project, finally clearing his conscience after three years.'"),
        ("Tonu", "A clear conscience is the softest pillow! What is our fourth expression, Solu?"),
        ("Solu", "Our fourth expression is an ancient proverb for letting go: 'let bygones be bygones'. To 'let bygones be bygones' means to agree to forget past disagreements, insults, or grievances and move forward in peace."),
        ("Tonu", "For example: 'After years of cold silence between the two neighbors, they shook hands over the garden fence and decided to let bygones be bygones.'"),
        ("Solu", "Let the past remain in the past! Tonu, take us to our fifth idiom."),
        ("Tonu", "Our fifth expression describes bold accountability: 'own up to something'. To 'own up to something' means to admit, confess, and take full responsibility for a mistake, wrongdoing, or fault."),
        ("Solu", "Here is an inspiring example: 'When the server crashed, Daniel immediately owned up to the coding error instead of trying to blame his junior teammates.'"),
        ("Tonu", "And what is our sixth and final expression for today, Solu?"),
        ("Solu", "Our sixth expression describes forgiving what cannot be undone: 'water under the bridge'. 'Water under the bridge' refers to past problems, arguments, or grievances that are completely forgiven, forgotten, and no longer matter."),
        ("Tonu", "Let's hear an example: 'We had some heated arguments during the merger last year, but that is all water under the bridge now; we are excited to collaborate.'"),

        # SECTION 16: INTERACTIVE SPEAKING PRACTICE
        ("Solu", "Now, it is time for our Interactive Speaking Challenge! This is your turn to speak English out loud along with us. Open your chest, pronounce each syllable with warmth, sincerity, and dignity, and repeat each sentence with steady cadence!"),
        ("Tonu", "Sentence number one: 'A sincere apology is not weakness; it is the ultimate mark of character and courage.' Your turn!"),
        ("Solu", "Speak it out loud with clear cadence: 'A sincere apology is not weakness; it is the ultimate mark of character and courage.'"),
        ("Tonu", "Beautiful rhythm! Sentence number two: 'When you swallow your pride and own up to your mistakes, healing naturally begins.' Your turn!"),
        ("Solu", "Repeat with steady conviction: 'When you swallow your pride and own up to your mistakes, healing naturally begins.'"),
        ("Tonu", "Wonderful! Sentence number three: 'Forgiving past grievances is the greatest gift of freedom you can give to your own heart.' Your turn!"),
        ("Solu", "Say it clearly: 'Forgiving past grievances is the greatest gift of freedom you can give to your own heart.'"),
        ("Tonu", "Sentence number four: 'Letting bygones be bygones opens the doorway to a future filled with peace and grace.' Your turn!"),
        ("Solu", "Let's say sentence number four together: 'Letting bygones be bygones opens the doorway to a future filled with peace and grace.'"),
        ("Tonu", "Outstanding work! Notice how compassionate, mature, and deeply resonant your spoken English sounds when you speak with genuine vulnerability!"),
        ("Solu", "Every sentence you practice out loud rewires your brain for emotional bravery and profound relational connection."),

        # SECTION 17: REFLECTION & FAREWELL
        ("Solu", "And now, it is time for today's Weekly Reflection Question! We want you to practice writing in English down in the comment section below."),
        ("Tonu", "Here is today's question: 'Is there an apology you need to deliver to someone in your life—or perhaps an apology you need to offer to yourself for past mistakes? What is one grudge you are ready to let go of this week to free your heart?'"),
        ("Solu", "Writing your personal reflections in English deepens your emotional courage and connects you to our supportive global community. Share your thoughts in the comments below!"),
        ("Tonu", "Solu and I read through every single comment, and we are so inspired by your bravery and dedication!"),
        ("Solu", "When you have the courage to apologize and forgive, you heal not only your own soul, but generations of generational pain around you."),
        ("Tonu", "A gentle, forgiving heart is the most powerful and revolutionary force in a world often blinded by pride."),
        ("Solu", "It frees your energy to love completely, to create boldly, and to experience the boundless beauty of every single day."),
        ("Tonu", "Let peace be your compass, let kindness be your voice, and let forgiveness be your sacred armor."),
        ("Solu", "Remember: life is too short to carry the heavy stones of bitterness and pride. Forgive generously, apologize humbly, and love fiercely."),
        ("Tonu", "Walk in grace, heal what is broken, and keep speaking English with bold confidence every single day!"),
        ("Solu", "Until next time, goodbye from Solu!"),
        ("Tonu", "And goodbye from Tonu!"),
        ("Both", "Happy learning, forgive freely, and goodbye!")
    ]
    return turns

if __name__ == "__main__":
    t = build_ep48()
    gen_common.verify_and_save(48, "scripts/daily_speak_ep48_full.txt",
                              "The Art of Apology: Forgiveness, Repair & Letting Go of Resentment",
                              "Daily Speak English | English Listening & Speaking Practice",
                              t)
