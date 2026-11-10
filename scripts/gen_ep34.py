#!/usr/bin/env python3
"""
Generator for Daily Speak English - Episode 34 (26+ Minutes Each)
=================================================================
Mastering Difficult Conversations & Setting Firm Boundaries
Target: >= 3,550 words, >= 140 turns (guarantees 26 to 28 minutes at 0.90x speed).
"""

import gen_common

def build_ep34():
    turns = [
        # SECTION 1: WARM MAGNETIC HOOK
        ("Tonu", "Hey hey, lovely listeners! Welcome back to Daily Speak English, your favorite place to become fluent, confident, and unstoppable in English! I'm Tonu!"),
        ("Solu", "And I'm Solu! It is an absolute privilege to welcome you back for another deeply empowering, practical, and courage-building English conversation."),
        ("Tonu", "Solu, have you ever felt that sick, heavy knot in the pit of your stomach when you knew you had to have a serious, uncomfortable confrontation with someone?"),
        ("Solu", "Oh Tonu, that feeling is unforgettable! Your heart pounds against your ribs, your palms sweat, your throat tightens up, and your brain screams: 'Maybe if I just ignore this, it will magically disappear on its own!'"),
        ("Tonu", "Whether it is telling a pushy coworker that their demands are unreasonable, telling a family member that they cannot cross your personal boundaries, asking a roommate to clean up their mess, or asking your manager for fair compensation."),
        ("Solu", "Most people spend days or even months agonizing in silent anxiety, swallowing their resentment, smiling politely on the outside while burning with anger on the inside!"),
        ("Tonu", "And that brings us directly into today's vital, life-transforming topic: Mastering Difficult Conversations, Setting Unshakeable Boundaries, and Speaking Your Truth with Grace!"),
        ("Solu", "Conflict is not a sign that a relationship is broken; conflict is the doorway to true intimacy, respect, and mutual understanding!"),
        ("Tonu", "If you cannot have difficult conversations, your relationships remain shallow, fragile, and full of hidden resentment."),
        ("Solu", "Today, we are going to unlock the legendary Harvard Negotiation Project framework on Difficult Conversations, teach you how to separate intent from impact, give you battle-tested scripts to say 'No' without guilt, and arm you with powerful everyday English vocabulary to stand up for yourself with poise and confidence!"),

        # SECTION 2: THE PEOPLE-PLEASER'S TRAP: BEING NICE VS BEING KIND
        ("Tonu", "Let's begin by dismantling a dangerous cultural myth: The People-Pleaser's Trap! Solu, what is the difference between being 'Nice' versus being truly 'Kind'?"),
        ("Solu", "This distinction changed my entire life, Tonu! 'Being Nice' is often rooted in fear, insecurity, and conflict avoidance!"),
        ("Tonu", "Explain what you mean by that, Solu!"),
        ("Solu", "A 'nice' person says 'yes' to everything, smiles when they are hurt, and agrees with opinions they secretly despise—not because they love the other person, but because they are terrified of rejection, disapproval, or anger!"),
        ("Tonu", "And what is the hidden cost of constantly saying 'yes' to everyone else?"),
        ("Solu", "Every time you say 'yes' to an unreasonable request that violates your boundaries, you are saying 'NO' to your own mental health, your own family time, your own rest, and your own self-respect!"),
        ("Tonu", "And eventually, that unexpressed anger doesn't disappear; it ferments into toxic bitterness and passive-aggressive resentment!"),
        ("Solu", "Whereas 'True Kindness' requires honesty, courage, and clear boundaries!"),
        ("Tonu", "As the celebrated researcher Dr. Brené Brown famously said: 'Clear is kind. Unclear is unkind!'"),
        ("Solu", "When you tell someone clearly and politely: 'I love you, but I cannot take on this extra project this weekend,' you are honoring them with the truth rather than pretending and resenting them later."),

        # SECTION 3: THE HARVARD THREE-CONVERSATION FRAMEWORK
        ("Tonu", "Now let's explore the groundbreaking communication framework developed by Douglas Stone, Bruce Patton, and Sheila Heen at the Harvard Law School: 'Difficult Conversations'!"),
        ("Solu", "The Harvard team discovered that in every difficult conversation, there are actually THREE separate conversations happening at the exact same time!"),
        ("Tonu", "What are those three hidden layers, Solu?"),
        ("Solu", "Layer number one is 'The What-Happened Conversation'! This is where people argue about facts, details, and blame: 'You said this! No, I never said that! You made this mistake! No, it was your fault!'"),
        ("Tonu", "Layer number two is 'The Feelings Conversation'! Are my feelings valid? Does the other person care that I am hurt, exhausted, or angry? If emotions are unexpressed, they leak out through tone of voice and sarcasm!"),
        ("Solu", "And Layer number three is the deepest and most vulnerable layer of all: 'The Identity Conversation'!"),
        ("Tonu", "The Identity Conversation! What does that mean?"),
        ("Solu", "The Identity Conversation is the internal panic inside your own soul: 'What does this conflict say about ME? Does this mean I am a bad friend? Does this mean I am incompetent at my job? Does this mean I am unlovable?'"),
        ("Tonu", "When your core identity feels threatened, your nervous system triggers fight-or-flight! You become defensive, defensive, and aggressive."),
        ("Solu", "When you realize that a disagreement does NOT threaten your fundamental worth as a good human being, you can enter difficult conversations with grounded calm."),

        # SECTION 4: INTENT VERSUS IMPACT
        ("Solu", "Now let's examine the single biggest communication trap that destroys relationships: Confusing INTENT with IMPACT!"),
        ("Tonu", "This happens in every marriage, workplace, and friendship on Earth! Solu, explain the difference between Intent and Impact!"),
        ("Solu", "We judge OURSELVES by our good intentions, but we judge OTHER PEOPLE by their external impact on us!"),
        ("Tonu", "Give us a vivid real-life example of this!"),
        ("Solu", "Imagine a husband arrives home from work forty-five minutes late without calling his wife. The wife was waiting with a hot dinner, and she feels hurt, neglected, and disrespected."),
        ("Tonu", "When she confronts him, she assumes his INTENT was malicious: 'You don't care about me; you are selfish and thoughtless!'"),
        ("Solu", "And the husband immediately gets defensive about his INTENT: 'How can you call me selfish? My boss called an emergency meeting; I was working hard to earn money for this family! You are so unfair!'"),
        ("Tonu", "Notice what happened! They are having two completely different arguments! He is defending his good intentions, while she is crying over the painful impact on her evening!"),
        ("Solu", "How do you solve this communication deadlock?"),
        ("Tonu", "Separate intent from impact! Acknowledge the impact first: 'I hear that arriving late made you feel hurt and unvalued, and I am so sorry my actions caused you that pain. My intention was never to neglect you; I was stuck in a meeting, but I understand why it felt that way.'"),
        ("Solu", "The moment someone feels that their emotional pain is validated and heard, their defensiveness melts away immediately."),

        # SECTION 5: THE ANATOMY OF A CLEAN BOUNDARY: NO IS A COMPLETE SENTENCE
        ("Solu", "Now let's talk about setting boundaries: What is the Anatomy of a Clean Boundary, Tonu?"),
        ("Tonu", "Most people set what communication therapists call 'Leaky Boundaries'! When asked to do something they don't want to do, they panic and offer a five-minute rambling excuse!"),
        ("Solu", "Haha! 'Oh, I would love to help you move apartments this Saturday, but my cousin's dog is sick, and my car might have an oil leak, and I have a headache, so maybe if I finish early I can stop by...'"),
        ("Tonu", "And what does the other person hear? They hear: 'Oh, so your schedule is negotiable! If I help you with your car, then you can help me move!'"),
        ("Solu", "When you over-explain and make up elaborate excuses, you give the other person ammunition to negotiate your boundaries away!"),
        ("Tonu", "Remember this liberating truth: 'NO' is a complete sentence!"),
        ("Solu", "You do not owe anyone a legal deposition explaining why you are choosing to protect your weekend!"),
        ("Tonu", "A clean boundary is warm, brief, and unambiguous: 'Thank you so much for thinking of me, but I am unable to take that on right now.' Period!"),
        ("Solu", "You don't apologize excessively, you don't make up lies, and you don't leave false hope."),

        # SECTION 6: THE BROKEN RECORD TECHNIQUE FOR PUSHY PEOPLE
        ("Tonu", "What should you do when you state a clean boundary, but the person is aggressive, pushy, or tries to guilt-trip you into submission?"),
        ("Solu", "Use the classic psychological tool known as 'The Broken Record Technique'!"),
        ("Tonu", "What is the Broken Record Technique, Solu?"),
        ("Solu", "The Broken Record Technique means choosing ONE calm, polite sentence, and repeating that exact sentence with an even, neutral tone, no matter what dramatic argument the other person throws at you!"),
        ("Tonu", "Demonstrate how that works in real life!"),
        ("Solu", "Imagine a pushy colleague says: 'Come on, Solu, everyone else stayed late to finish the report; if you leave at five, the boss will think you aren't a team player!'"),
        ("Tonu", "And you calmly reply: 'I understand it is a busy week, but I am unable to stay past five today.'"),
        ("Solu", "Then the colleague pushes harder: 'You are letting the whole team down! It will only take two hours!'"),
        ("Tonu", "And you repeat with identical calm: 'I hear your concern, but I am unable to stay past five today.'"),
        ("Solu", "They try a third time: 'You are being so difficult!'"),
        ("Tonu", "And you smile warmly: 'I appreciate your perspective, but I am unable to stay past five today.'"),
        ("Solu", "You don't take the bait, you don't get angry, you don't defend yourself. After three repetitions, the pushy person runs out of conversational leverage and backs down!"),

        # SECTION 7: DE-ESCALATING DEFENSIVE CONFLICT
        ("Solu", "Now, let's explore how to de-escalate a conversation when the other person becomes furious, defensive, or starts shouting!"),
        ("Tonu", "Rule number one: Lower your vocal volume and slow down your speaking cadence!"),
        ("Solu", "When someone raises their voice, human instinct wants to shout even louder to overpower them!"),
        ("Tonu", "If you scream back, you pour gasoline onto a roaring bonfire. But if you drop your voice to a quiet, calm, deliberate murmur, they have to stop shouting just to hear what you are saying!"),
        ("Solu", "And use the magical phrase: 'Help me understand where you are coming from.'"),
        ("Tonu", "That shifts the energy from a courtroom battle into a collaborative investigation! It signals that you are not trying to win an argument; you are trying to understand the human heart in front of you."),

        # SECTION 8: MARSHALL ROSENBERG'S NONVIOLENT COMMUNICATION (NVC)
        ("Solu", "Let's explore the world-famous four-step formula developed by Dr. Marshall Rosenberg: 'Nonviolent Communication' or NVC!"),
        ("Tonu", "NVC has been used to resolve armed civil wars and heal marriages on the brink of divorce! What are the four steps, Solu?"),
        ("Solu", "Step number one is 'Observation without Evaluation'! State the objective, factual camera evidence without adding insults or generalizations like 'always' or 'never'."),
        ("Tonu", "Instead of saying 'You always ignore me!', say: 'When I spoke to you yesterday evening and you continued typing on your laptop without looking up...'"),
        ("Solu", "Step number two is 'Expressing Feelings'! State how you felt using emotional words, not thoughts. Say 'I felt lonely and overlooked,' not 'I felt like you don't care.'"),
        ("Tonu", "Step number three is 'Identifying Unmet Needs'! Why did you feel that way? Because all human anger stems from an unmet core need: 'Because I need connection and shared presence after a long workday.'"),
        ("Solu", "And Step number four is 'Making a Concrete, Actionable Request'! Not a demand! Say: 'Would you be willing to close your laptop for twenty minutes when I arrive home so we can share a cup of tea together?'"),
        ("Tonu", "Notice how beautiful and impossible to argue with that is! You didn't attack their character; you expressed an honest observation, a vulnerable feeling, a human need, and a simple request!"),

        # SECTION 9: THE KARPMAN DRAMA TRIANGLE
        ("Solu", "Now let's examine a psychological trap discovered by Dr. Stephen Karpman: 'The Drama Triangle'!"),
        ("Tonu", "The Drama Triangle maps the three toxic roles people subconsciously adopt during conflicts: The Victim, The Rescuer, and The Persecutor!"),
        ("Solu", "The 'Rescuer' is often the chronic people-pleaser who tries to save everyone, solve everyone's problems, and manage everyone's feelings without being asked!"),
        ("Tonu", "And what happens when the Rescuer gets exhausted and nobody appreciates them?"),
        ("Solu", "They flip into the 'Victim'! They cry: 'After everything I sacrificed for you, look how terribly you treat me!'"),
        ("Tonu", "And then they flip into the 'Persecutor' and lash out with bitter rage!"),
        ("Solu", "How do you break free from the Drama Triangle, Tonu?"),
        ("Tonu", "Step into what psychologists call 'The Empowerment Dynamic'! Stop trying to rescue adults from their own responsibilities. Let people experience the natural consequences of their choices, while you remain a compassionate supporter rather than a savior."),

        # SECTION 10: THE GRAY ROCK METHOD FOR TOXIC INDIVIDUALS
        ("Solu", "What should our listeners do when dealing with a truly toxic, manipulative, or narcissistic boss or family member who feeds on drama?"),
        ("Tonu", "Psychologists recommend a technique known as 'The Gray Rock Method'!"),
        ("Solu", "What is the Gray Rock Method, Tonu?"),
        ("Tonu", "Imagine a dull, plain, uninteresting gray rock sitting on the side of a gravel road. Does anyone look at it twice? No! It is completely boring!"),
        ("Solu", "When dealing with a manipulative person, become a Gray Rock! Do not show anger, do not show hurt, do not give emotional reactions!"),
        ("Tonu", "Give short, bland, factual answers: 'Yes, I received your email. Thank you for the update. Understood.'"),
        ("Solu", "Toxic manipulators are addicted to emotional drama and reactivity. When you deprive them of that emotional fuel, they get bored and look elsewhere!"),
        ("Tonu", "And put them on an 'Information Diet'! Stop sharing your private dreams, financial details, or personal vulnerabilities with people who have proven they cannot be trusted with your heart."),

        # SECTION 11: WORKPLACE & DIGITAL BOUNDARIES
        ("Solu", "Let's also talk about setting boundaries with our digital technology and workplace messaging apps!"),
        ("Tonu", "In our hyper-connected world, bosses and clients send WhatsApp messages on Saturday morning and Slack pings at 10 PM!"),
        ("Solu", "If you reply to a work email at eleven at night, you are training your employer that your time belongs to them twenty-four hours a day!"),
        ("Tonu", "Set an automatic out-of-office schedule. Communicate clearly: 'My working hours are 9 AM to 6 PM. For any emergencies outside these hours, our team lead can reach me by phone, but otherwise, I will respond first thing tomorrow morning.'"),
        ("Solu", "True professionals respect people who have clear, professional boundaries."),

        # SECTION 12: GABOR MATÉ: WHEN THE BODY SAYS NO
        ("Tonu", "Let's also explore the somatic, physical reality of boundary violations: Dr. Gabor Maté's landmark book, 'When the Body Says No'!"),
        ("Solu", "What does Dr. Gabor Maté reveal about people who suppress their boundaries, Tonu?"),
        ("Tonu", "Dr. Maté studied hundreds of patients with chronic autoimmune diseases, rheumatoid arthritis, fibromyalgia, and migraines."),
        ("Solu", "And what did he discover in their psychological profiles?"),
        ("Tonu", "He discovered a striking pattern: almost all of them were chronic people-pleasers who spent decades repressing their anger, swallowing their own needs, and feeling responsible for everyone else's emotional comfort!"),
        ("Solu", "When your mouth is afraid to say 'NO', your physical body will eventually say 'NO' for you through autoimmune illness, ulcers, high blood pressure, and chronic exhaustion!"),
        ("Tonu", "Boundary setting is not just a communication skill; boundary setting is physical preventive medicine!"),

        # SECTION 13: LIVE ROLEPLAY: SAYING NO TO A FRIDAY 5 PM DEADLINE
        ("Solu", "Now, let's give our listeners a real-world, scripted roleplay! Imagine your manager walks to your desk on Friday afternoon at 4:30 PM with a stack of files."),
        ("Tonu", "And the manager says: 'Solu, I need this complete client market analysis on my desk by Monday morning at 8 AM!'"),
        ("Solu", "How do most people react? They panic, feel furious inside, but meekly mumble: 'Okay, I guess I will cancel my anniversary dinner and work all weekend.'"),
        ("Tonu", "Now, let's demonstrate the professional, boundaried response! Solu, how would you respond?"),
        ("Solu", "I would take a calm breath, look the manager in the eye, and say: 'I understand this client analysis is high priority for the team. However, my weekend is fully committed, and to produce the thorough, high-quality work this client expects will require about ten focused hours.'"),
        ("Tonu", "And then what do you offer, Solu?"),
        ("Solu", "I offer two clear choices: 'I can either shift my Monday morning project to deliver this by Tuesday at noon, or we can look at delegating the data gathering to an assistant so I can finish the executive summary on Monday afternoon. Which of those two options serves the client best?'"),
        ("Tonu", "Notice what Solu did! He didn't whine, he didn't apologize, and he didn't get angry! He acknowledged the priority, held his weekend boundary firmly, and offered two constructive business solutions!"),
        ("Solu", "That is how you earn genuine professional respect."),

        # SECTION 14: THE BROKEN RECORD TECHNIQUE & FAMILY FOG (FEAR, OBLIGATION, GUILT)
        ("Tonu", "Now, what happens when people push back, argue, or try to guilt-trip you after you state a boundary?"),
        ("Solu", "Psychotherapist Dr. Susan Forward coined a famous acronym for emotional manipulation: 'FOG', which stands for Fear, Obligation, and Guilt!"),
        ("Tonu", "Family members or friends who are used to walking all over your boundaries will say: 'If you really loved us, you would come to dinner every single Sunday!' or 'How can you be so selfish after all we did for you?'"),
        ("Solu", "When caught in the FOG, do not defend yourself, do not make lengthy excuses, and do not over-explain! The moment you give five reasons why you cannot come, they will argue with all five reasons!"),
        ("Tonu", "Instead, use the classic psychological tool called 'The Broken Record Technique'!"),
        ("Solu", "How does The Broken Record Technique work in practice, Tonu?"),
        ("Tonu", "You select one short, polite, immovable sentence and repeat it calmly like a broken vinyl record, no matter what dramatic argument the other person makes!"),
        ("Solu", "For example, they say: 'You must host the entire holiday dinner at your house!'"),
        ("Tonu", "You reply: 'I won't be able to host this year, but I'm looking forward to bringing a salad to whoever hosts.'"),
        ("Solu", "They say: 'You are ruining our family tradition! Don't you care about us?'"),
        ("Tonu", "You calmly repeat without raising your voice: 'I understand you are disappointed, but I won't be able to host this year.'"),
        ("Solu", "They push again: 'Can't you at least clean the house and let us bring food?'"),
        ("Tonu", "You repeat: 'I won't be able to host this year, but I am excited to see everyone.'"),
        ("Solu", "Notice how powerful that is! You don't take the bait, you don't enter an emotional shouting match, and within three repetitions, the manipulator realizes there is no door to kick open!"),
        ("Tonu", "A boundary is not a debate; a boundary is a calm decision about where your personal energy begins and ends."),

        # SECTION 15: VOCABULARY & IDIOM SPOTLIGHT (6 KEY IDIOMS)
        ("Tonu", "Now, let's step into our signature segment: Key Everyday English Vocabulary and Idioms! Today, we have selected six colorful, essential expressions about boundaries, courage, and difficult conversations."),
        ("Solu", "Let's master them together! Tonu, what is our very first boundary expression for today?"),
        ("Tonu", "Our first expression is 'set boundaries'. To 'set boundaries' means to establish clear personal limits regarding what behavior, demands, or treatment you will and will not accept from other people."),
        ("Solu", "Let's listen to a natural conversational example: 'After experiencing severe burnout, Elena set firm boundaries by turning off her work email after six in the evening.'"),
        ("Tonu", "That protected her sanity! What is our second expression, Solu?"),
        ("Solu", "Our second expression is 'clear the air'. To 'clear the air' means to discuss a tense, awkward, or unresolved disagreement openly and honestly in order to remove bad feelings and restore harmony."),
        ("Tonu", "Here is an everyday example: 'The tension between the two business partners was obvious, so they scheduled a private lunch to clear the air.'"),
        ("Solu", "Brilliant! Tonu, introduce our third expression."),
        ("Tonu", "Our third expression is 'nip something in the bud'. To 'nip something in the bud' means to stop a problem, bad behavior, or misunderstanding at an early stage before it grows larger and harder to manage."),
        ("Solu", "Let's hear an example: 'When the new employee started arriving thirty minutes late every day, the manager nipped it in the bud with a private, gentle conversation.'"),
        ("Tonu", "Address small problems before they become giant crises! What is our fourth expression, Solu?"),
        ("Solu", "Our fourth expression describes chronic social anxiety: 'walk on eggshells'. To 'walk on eggshells' means to be overly cautious, nervous, and anxious around someone because they are easily angered, offended, or unpredictable."),
        ("Tonu", "For example: 'Living with an unpredictable, short-tempered roommate made him feel like he was constantly walking on eggshells in his own apartment.'"),
        ("Solu", "No one should have to live like that. Tonu, take us to our fifth expression."),
        ("Tonu", "Our fifth expression is 'put one's foot down'. To 'put your foot down' means to take a firm, resolute stand against something unacceptable, refusing to yield or allow it to continue."),
        ("Solu", "Here is how you can use it: 'When the contractor demanded another unexpected payment without explaining the costs, Marcus put his foot down and demanded a full audit.'"),
        ("Tonu", "And what is our sixth and final expression for today, Solu?"),
        ("Solu", "Our sixth expression describes genuine emotional connection: 'have a heart-to-heart'. To 'have a heart-to-heart' means to have an intimate, deeply honest, and compassionate conversation about personal feelings and truths."),
        ("Tonu", "Let's hear an example: 'After months of growing apart, the two childhood best friends sat down by the fireplace and had a long, tearful heart-to-heart.'"),

        # SECTION 9: INTERACTIVE SPEAKING PRACTICE
        ("Solu", "Now, it is time for our Interactive Speaking Challenge! This is your turn to speak English out loud along with us. Stand tall, relax your shoulders, open your chest, and repeat each sentence with steady courage and clear pronunciation!"),
        ("Tonu", "Sentence number one: 'Setting clear boundaries is not selfish; it is the foundation of self-respect and healthy love.' Your turn!"),
        ("Solu", "Say it out loud with clear conviction: 'Setting clear boundaries is not selfish; it is the foundation of self-respect and healthy love.'"),
        ("Tonu", "Great cadence! Sentence number two: 'Having a calm heart-to-heart helped us clear the air and rebuild our trust.' Your turn!"),
        ("Solu", "Repeat with steady confidence: 'Having a calm heart-to-heart helped us clear the air and rebuild our trust.'"),
        ("Tonu", "Wonderful! Sentence number three: 'It is so much kinder to be honest upfront than to say yes and resent people later.' Your turn!"),
        ("Solu", "Speak it clearly: 'It is so much kinder to be honest upfront than to say yes and resent people later.'"),
        ("Tonu", "Sentence number four: 'When you speak your truth with warmth and grace, you invite others to do the same.' Your turn!"),
        ("Solu", "Let's say sentence number four together: 'When you speak your truth with warmth and grace, you invite others to do the same.'"),
        ("Tonu", "Outstanding work! Your spoken English is sounding more authoritative, grounded, and emotionally mature with every single lesson."),

        # SECTION 10: REFLECTION & FAREWELL
        ("Solu", "And now, it is time for today's Weekly Reflection Question! We want you to practice writing in English down in the comment section below."),
        ("Tonu", "Here is today's question: 'Is there a difficult conversation or a personal boundary you have been avoiding because of fear or discomfort? What is one gentle, firm boundary you need to set this week to protect your peace of mind?'"),
        ("Solu", "Writing your thoughts down in English takes the fear out of your mind and gives you the courage to act with dignity. Share your reflection in the comments below!"),
        ("Tonu", "Solu and I read through every single comment, and we will be right there in the comments cheering on your bravery."),
        ("Solu", "Remember that peace is not the absence of conflict; peace is the presence of honesty, respect, and clear boundaries."),
        ("Tonu", "Keep practicing your spoken English with courage, joy, and consistency. Take wonderful care of yourself, and stand firm in your worth!"),
        ("Solu", "Until next time, goodbye from Solu!"),
        ("Tonu", "And goodbye from Tonu!"),
        ("Both", "Happy learning, speak your truth, and goodbye!")
    ]
    return turns

if __name__ == "__main__":
    t = build_ep34()
    gen_common.verify_and_save(34, "scripts/daily_speak_ep34_full.txt",
                              "Mastering Difficult Conversations & Setting Firm Boundaries",
                              "Daily Speak English | English Listening & Speaking Practice",
                              t)
