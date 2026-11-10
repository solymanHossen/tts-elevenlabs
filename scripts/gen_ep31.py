#!/usr/bin/env python3
"""
Generator for Daily Speak English - Episodes 31 to 35 (26+ Minutes Each)
========================================================================
All episodes start with Tonu:
"Hey hey, lovely listeners! Welcome back to Daily Speak English, your favorite place to become fluent, confident, and unstoppable in English! I'm Tonu!"

Target per episode: >= 3,600 words, >= 140 turns (guarantees 26 to 28 minutes at 0.90x speed).
"""

import gen_common

def build_ep31():
    # EPISODE 31: The Psychology of First Impressions & Body Language Secrets
    turns = [
        # SECTION 1: WARM MAGNETIC HOOK
        ("Tonu", "Hey hey, lovely listeners! Welcome back to Daily Speak English, your favorite place to become fluent, confident, and unstoppable in English! I'm Tonu!"),
        ("Solu", "And I'm Solu! It is so electrifying to welcome you back as we kick off our brand-new season of Daily Speak English!"),
        ("Tonu", "Solu, think about this shocking scientific fact: When you walk into a room and meet a stranger for the very first time, how many seconds do you think it takes for their subconscious brain to form a lasting opinion about you?"),
        ("Solu", "Most people would guess a few minutes, or maybe after having a five-minute polite conversation over coffee."),
        ("Tonu", "Not even close! Princeton University psychologists discovered that human beings form judgments about your trustworthiness, competence, warmth, and likability within one-tenth of a second—just one hundred milliseconds!"),
        ("Solu", "One hundred milliseconds! That is faster than the blink of an eye! Before you even open your mouth to say 'Hello', the other person's ancient evolutionary brain has already categorized you."),
        ("Tonu", "And that brings us directly into today's captivating, life-changing topic: The Psychology of First Impressions, Unspoken Body Language Secrets, and Mastering Charisma in Spoken English!"),
        ("Solu", "Whether you are walking into an important job interview, going on a first date, meeting international clients, or simply introducing yourself at a party, first impressions set the invisible thermostat for the entire relationship."),
        ("Tonu", "And here is the good news: Charisma and positive body language are not genetic gifts reserved for movie stars. They are trainable, physical skills that anyone can master."),
        ("Solu", "Today, we are going to unpack the science of nonverbal communication, reveal the micro-expressions that build instant trust, teach you how to project relaxed authority, and arm you with fantastic everyday English vocabulary to talk about human behavior with natural fluency!"),
        ("Tonu", "Because when you feel confident in your nonverbal presence, your spoken English flows with ten times more natural charisma, freedom, and emotional connection."),
        ("Solu", "Your words and your physical presence work in perfect harmony to touch human hearts and inspire trust."),

        # SECTION 2: THE EVOLUTIONARY ORIGINS OF FIRST IMPRESSIONS
        ("Tonu", "Let's start by understanding why human beings are so obsessed with rapid snap judgments. What is the evolutionary purpose of first impressions, Solu?"),
        ("Solu", "For our prehistoric ancestors living on the open plains, encountering an unfamiliar stranger was literally a matter of life or death!"),
        ("Tonu", "Exactly! If an unknown person emerged from the trees carrying a spear, our ancestors didn't have thirty minutes to sit down and analyze their philosophy!"),
        ("Solu", "The brain had to answer two immediate survival questions in a fraction of a second: Question number one: What are this person's intentions toward me? Are they friend or foe? Warm or hostile?"),
        ("Tonu", "And Question number two: Can this person act on those intentions? In other words, are they strong or weak? Competent or incompetent?"),
        ("Solu", "Harvard social psychologist Amy Cuddy calls these two fundamental dimensions 'Warmth' and 'Competence'!"),
        ("Tonu", "And which dimension does the brain evaluate first, Tonu?"),
        ("Tonu", "Brain scans show that people evaluate WARMTH first! Before anyone cares how smart, talented, or wealthy you are, they need to know that you care about them and pose no threat."),
        ("Solu", "If you walk into a room trying to look impressively smart, stern, and intimidating, people subconsciously put up their emotional guards. But if you lead with genuine warmth, open posture, and a welcoming smile, people open their hearts to you instantly."),

        # SECTION 3: THE SECRET POWER OF OPEN HANDS & EYE CONTACT
        ("Solu", "Now let's examine specific body language signals: The incredible, overlooked power of your HANDS!"),
        ("Tonu", "Oh Solu, hands are the ultimate truth-tellers of the human body! Why are hands so psychologically powerful?"),
        ("Solu", "Because in human evolution, visible hands meant: 'I am not concealing a rock, a dagger, or a weapon!'"),
        ("Tonu", "When you keep your hands hidden in your jacket pockets, under the table, or behind your back, the other person's subconscious brain experiences a subtle spike in cortisol—the stress hormone! They feel an instinctual unease because they cannot see your hands."),
        ("Solu", "Whereas, if you keep your hands visible, relaxed, and open with palms visible, you project honesty, transparency, and safety!"),
        ("Tonu", "And what about the handshake, Solu? In many cultures, the physical handshake is the opening ritual."),
        ("Solu", "A great handshake should be firm, warm, and dry! Avoid the limp, lifeless 'dead fish' handshake that communicates insecurity and disinterest."),
        ("Tonu", "And also avoid the aggressive 'bone-crusher' handshake where someone tries to squeeze your fingers off to prove their dominance!"),
        ("Solu", "A warm, natural, two-second web-to-web grip combined with steady eye contact communicates grounded self-respect and mutual honor."),
        ("Tonu", "And what about eye contact? How much eye contact is healthy without looking like an intense, unblinking serial killer?"),
        ("Solu", "Haha! That is a very important distinction! Psychologists recommend the '60/70 Rule': maintain eye contact about sixty to seventy percent of the time during a conversation."),
        ("Tonu", "Hold eye contact long enough to notice the color of the other person's eyes, and then naturally break it to look away for a moment when you are reflecting on a thought. That feels completely natural, warm, and relaxed."),

        # SECTION 4: POSTURE, SPATIAL OCCUPATION & THE POWER POSE
        ("Solu", "Now let's talk about posture and how we occupy space in a room: Standing Tall versus Slouching!"),
        ("Tonu", "Think about what happens to your body when you feel stressed, insecure, or defensive! Your shoulders cave inward, your neck pulls down like a turtle hiding in its shell, and you make your physical footprint as small as possible!"),
        ("Solu", "And think about what that signals to everyone in the room: 'I feel small, I lack confidence, please don't look at me!'"),
        ("Tonu", "In contrast, confident leaders practice what posture coaches call 'Expanding Your Space'! Roll your shoulders back and down, keep your chin parallel to the floor, open your chest, and stand with your feet shoulder-width apart."),
        ("Solu", "Amy Cuddy's famous research on 'Power Posing' showed that standing in an expansive posture for just two minutes before an interview actually increases testosterone—the confidence hormone—and decreases cortisol!"),
        ("Tonu", "Even more importantly, it physically changes your breathing. When your chest is open, your diaphragm can expand fully, allowing you to breathe deeply into your belly."),
        ("Solu", "And when your breathing is deep and steady, your spoken voice resonates from your chest with rich, authoritative warmth, rather than coming out as a shallow, squeaky squeak from your throat!"),

        # SECTION 5: THE ART OF THE DUAL-SPEED SMILE & VOCAL WARMTH
        ("Tonu", "Let's explore facial expressions: The difference between a fake, polite smile and an authentic, magnetic smile!"),
        ("Solu", "Most people flash what communication experts call the 'Instant Plastic Smile'! The moment they meet someone, their mouth snaps into an immediate grin, but their eyes remain completely dead and cold."),
        ("Tonu", "People sense that fakeness instantly! In psychology, an authentic smile is called a 'Duchenne Smile'—named after the French neurologist Guillaume Duchenne."),
        ("Solu", "What makes a Duchenne smile so irresistible, Tonu?"),
        ("Tonu", "A Duchenne smile engages the orbicularis oculi muscles around the eyes! The corners of the mouth lift gently, the cheeks rise, and tiny, joyful crinkles appear around the eyes!"),
        ("Solu", "And use communication coach Leil Lowndes's technique called 'The Flooding Smile'! When you meet someone, don't flash an instant grin. Look into their eyes for a split second, pause, and then let a warm, radiant smile slowly flood across your entire face as if that smile were created exclusively for them!"),
        ("Tonu", "It makes the other person feel uniquely special, cherished, and acknowledged. It melts social awkwardness like warm butter."),
        ("Solu", "And what about the vocal tone of your voice? Your voice carries fifty percent of the emotional impression!"),
        ("Tonu", "Avoid what linguists call 'uptalk'—ending positive statements with an upward question mark, like: 'My name is Tonu? And I am a marketing manager?'"),
        ("Solu", "Uptalk sounds like you are asking for permission to exist! Use downward inflection at the end of sentences to convey calm, steady certainty."),

        # SECTION 6: THE FORGOTTEN ART OF REMEMBERING NAMES
        ("Solu", "Now, let's talk about the single sweetest sound in any language: The sound of a person's own NAME!"),
        ("Tonu", "Dale Carnegie wrote in his timeless book 'How to Win Friends and Influence People': 'Remember that a person's name is to that person the sweetest and most important sound in any language!'"),
        ("Solu", "And yet, ninety percent of people say: 'Oh, I am terrible with names; I forget someone's name five seconds after they introduce themselves!'"),
        ("Tonu", "Why do we forget names so quickly, Tonu?"),
        ("Tonu", "Because we weren't actually listening! When the other person was speaking their name, our brain was too busy worrying about what WE were going to say next!"),
        ("Solu", "How can our listeners become masters at remembering names effortlessly?"),
        ("Tonu", "Use the 'Three-Times Name Rule'! The moment someone introduces themselves—say, 'Hi, I'm Julian'—repeat their name out loud immediately: 'It is a pleasure to meet you, Julian!'"),
        ("Solu", "Then, connect their name mentally with a visual image or another famous Julian you know. And during the conversation, use their name naturally once: 'So Julian, how long have you lived in Dublin?'"),
        ("Tonu", "And when parting ways, say: 'Julian, it was wonderful speaking with you today; have a fantastic evening!'"),
        ("Solu", "By repeating their name three times, you cement the neural memory in your long-term storage, and you leave them feeling deeply respected and valued."),

        # SECTION 7: CULTURAL VARIATIONS IN FIRST IMPRESSIONS
        ("Solu", "Now let's explore a fascinating dimension: Cultural Variations in First Impressions! Body language is not completely universal across the planet, is it, Tonu?"),
        ("Tonu", "Not at all, Solu! What signals confidence and respect in one culture might be considered rude or aggressive in another!"),
        ("Solu", "Give our listeners an example of how gestures and space differ across borders."),
        ("Tonu", "In North America and Western Europe, direct, firm eye contact is seen as a sign of honesty, competence, and forthrightness. But in several East Asian cultures, prolonged direct eye contact with an elder or senior manager can be interpreted as confrontational and disrespectful!"),
        ("Solu", "And look at physical proximity and personal space! Anthropologist Edward T. Hall coined the term 'Proxemics' to study how cultures use personal space."),
        ("Tonu", "In Latin American, Mediterranean, and Middle Eastern cultures, people stand much closer together during conversation and touch arms frequently to express warmth!"),
        ("Solu", "Whereas in Scandinavian or Germanic cultures, people maintain a much wider personal bubble—sometimes an entire arm's length! If you step too close, they instinctively step back to preserve their comfort."),
        ("Tonu", "And bowing in Japan! A bow is not just bending at the waist; the depth and duration of the bow communicate precise levels of social deference, gratitude, and respect."),
        ("Solu", "When meeting international colleagues or friends, cultural intelligence means being observant, adaptable, and not judging their warmth by your own local cultural norms."),

        # SECTION 8: PAUL EKMAN & THE SCIENCE OF MICRO-EXPRESSIONS
        ("Tonu", "Let's explore the groundbreaking work of Dr. Paul Ekman on 'Micro-Expressions'—the science that inspired the famous television show 'Lie to Me'!"),
        ("Solu", "What are Micro-Expressions, Tonu?"),
        ("Tonu", "A micro-expression is an involuntary, ultra-rapid facial expression that flashes across the human face in one twenty-fifth of a second!"),
        ("Solu", "One twenty-fifth of a second! That is too fast for conscious control!"),
        ("Tonu", "Ekman studied isolated tribes in Papua New Guinea and proved that seven core human emotions produce the exact same universal facial movements across all human cultures: Anger, Fear, Disgust, Sadness, Happiness, Surprise, and Contempt!"),
        ("Solu", "Even individuals born blind who have never seen another human face make the exact same micro-expressions of pride or grief!"),
        ("Tonu", "And what is the most dangerous micro-expression in relationships and negotiations, Solu?"),
        ("Solu", "Without a doubt: CONTEMPT! Contempt is signaled by a unilateral, asymmetrical sneer—one corner of the lip tightening and pulling slightly upward."),
        ("Tonu", "When you see that asymmetrical smirk on someone's face, their subconscious is communicating superiority, dismissal, and disrespect."),
        ("Solu", "Being attuned to subtle micro-expressions allows you to read the emotional climate of a room before conflicts escalate."),

        # SECTION 9: THE PSYCHOLOGY OF CLOTHING & COLOR COMMUNICATION
        ("Solu", "Now, let's talk about what we wear: The Psychology of Enclothed Cognition and Color Theory!"),
        ("Tonu", "Psychologists Hajo Adam and Adam Galinsky coined the term 'Enclothed Cognition' to describe how the clothes we wear systematically influence our own psychological processes!"),
        ("Solu", "Tell our listeners about their famous white lab coat experiment, Tonu!"),
        ("Tonu", "In their study, participants were divided into two groups to take a difficult attention test. The first group wore a white coat told it was a doctor's lab coat; the second group wore the identical coat told it was an artist's smock!"),
        ("Solu", "And the group who believed they were wearing a doctor's coat made half as many errors! Their brain subconsciously adopted the precision, focus, and rigor associated with medical professionals!"),
        ("Tonu", "What you wear doesn't just influence how others perceive you; it directly changes how you think and carry yourself!"),
        ("Solu", "And what about color psychology in first impressions, Tonu?"),
        ("Tonu", "Navy blue is the world's most trusted color in business! It communicates stability, intelligence, calm, and integrity."),
        ("Solu", "While wearing pure black conveys authority, power, and elegance, but too much black can sometimes feel distant or intimidating."),
        ("Tonu", "And accents of warm burgundy, emerald green, or soft earth tones invite approachable warmth and creativity."),

        # SECTION 10: DIGITAL FIRST IMPRESSIONS: MASTERING ZOOM & VIDEO CALLS
        ("Solu", "In our modern remote work era, over fifty percent of first impressions happen through a tiny glass camera lens on a laptop screen!"),
        ("Tonu", "Yes! The 'Digital First Impression'! And so many brilliant professionals make catastrophic mistakes on video calls without realizing it!"),
        ("Solu", "What are the biggest video call mistakes, Tonu?"),
        ("Tonu", "Mistake number one: The 'Nose-Cam' angle! Placing your laptop flat on your desk so the camera points directly up your nose, showing your ceiling fan!"),
        ("Solu", "Haha! It makes you look like a giant looming down threateningly on the other person!"),
        ("Tonu", "Elevate your laptop on a stand or a stack of thick books so the camera lens is exactly level with your eyes! Eye-level camera placement simulates natural human eye contact."),
        ("Solu", "Mistake number two: Backlighting! Sitting with a bright window behind you, which turns you into an ominous dark silhouette in a witness protection program!"),
        ("Tonu", "Always have soft, natural light facing you from in front of your face. When people can clearly see your eyes, your facial expressions, and your smile, their brain feels relaxed and builds trust."),
        ("Solu", "And look directly into the camera lens when you are speaking, rather than staring at your own image in the corner of the screen!"),

        # SECTION 11: PERSONAL ANECDOTES: OUR BIGGEST FIRST IMPRESSION DISASTERS
        ("Solu", "Tonu, have you ever had an embarrassing first impression disaster that you still laugh about today?"),
        ("Tonu", "Oh Solu, I have the ultimate disaster story! During my first semester at university, I had to give a presentation to eighty students and four senior professors!"),
        ("Solu", "What happened, Tonu?"),
        ("Tonu", "I was so petrified with stage fright that my knees started knocking together like wooden castanets! My hands were trembling so violently that the note cards I was holding went flying into the front row!"),
        ("Solu", "Oh no! That is every student's worst nightmare!"),
        ("Tonu", "I thought my academic life was completely over! But a wise senior professor smiled, picked up my cards, and whispered: 'Rest your palms flat on the podium, take one deep breath, and remember that everyone here wants you to succeed.'"),
        ("Solu", "What an incredible gift of empathy!"),
        ("Tonu", "And I have one of my own! On my very first dinner date with a girl I liked in university, I wanted to look cool and sophisticated like James Bond!"),
        ("Solu", "So I wore a stiff leather jacket that squeaked every time I moved! When I tried to pull out her chair with a debonair flourish, my elbow caught the edge of the table and sent an entire vase of red roses crashing into the restaurant floor!"),
        ("Tonu", "Haha! James Bond destroyed the floral centerpiece!"),
        ("Solu", "Water and rose petals went everywhere! But she burst out laughing, and seeing her laugh made me laugh at myself. That clumsy accident broke the tension and turned into a wonderful four-hour conversation!"),

        # SECTION 12: THE POWER OF DELIBERATE PAUSING & VOCAL GRAVITAS
        ("Tonu", "Let's also talk about the rhythm of speech in first impressions: The Power of the Deliberate Pause!"),
        ("Solu", "When people are nervous during an introduction or interview, their words rush out at two hundred miles an hour like a runaway freight train!"),
        ("Tonu", "They fear that if there is one second of silence, the interviewer will think they are slow or stupid!"),
        ("Solu", "In reality, the greatest communicators in history do the exact opposite! When asked a difficult question, they pause for two full seconds, look thoughtful, take a calm breath, and then answer with measured authority."),
        ("Tonu", "A deliberate pause conveys supreme confidence. It signals that you are comfortable with silence, that you think deeply before you speak, and that your words carry weight."),

        # SECTION 13: RECOVERING FROM AN AWKWARD FIRST IMPRESSION
        ("Tonu", "What happens if you have a terrible day, spill coffee on your shirt, trip on the rug, or say something clumsy during a first impression? Can a bad first impression ever be salvaged, Solu?"),
        ("Solu", "Yes! Absolutely! And the secret is not trying to pretend it didn't happen, or getting defensive and flustered!"),
        ("Tonu", "The secret is Self-Deprecating Humor and complete psychological ownership!"),
        ("Solu", "If you trip or make an awkward blunder, smile warmly, laugh at yourself, and say: 'Well, that was certainly a dramatic entrance! Let's pretend I walked in with total grace and start over!'"),
        ("Tonu", "Psychologists call this the 'Pratfall Effect'! When someone who is competent makes a clumsy mistake and laughs at themselves with genuine humility, people actually find them MORE likable and approachable!"),
        ("Solu", "It proves that you are authentic, comfortable in your own skin, and have zero fragile ego."),

        # SECTION 8: VOCABULARY & IDIOM SPOTLIGHT (6 KEY IDIOMS)
        ("Tonu", "Now, let's step into our signature segment: Key Everyday English Vocabulary and Idioms! Today, we have selected six colorful, essential expressions about first impressions, charisma, and interpersonal dynamics."),
        ("Solu", "Let's master them together! Tonu, what is our very first expression for today?"),
        ("Tonu", "Our first expression is 'put one's best foot forward'. To 'put your best foot forward' means to show your most impressive qualities, behavior, and appearance, especially when trying to make a positive first impression."),
        ("Solu", "Let's listen to a natural conversational example: 'I made sure to arrive early, dress professionally, and put my best foot forward during the final panel interview.'"),
        ("Tonu", "That is an essential interview phrase! What is our second expression, Solu?"),
        ("Solu", "Our second expression is 'break the mold'. When someone or something 'breaks the mold', it means they are unique, unconventional, and refreshingly different from everyone else in their category."),
        ("Tonu", "Here is an everyday example: 'Her innovative, interactive presentation style completely broke the mold and captivated the entire corporate audience.'"),
        ("Solu", "Inspiring! Tonu, introduce our third expression."),
        ("Tonu", "Our third expression is 'win someone over'. To 'win someone over' means to successfully persuade someone to like you, trust you, or agree with your point of view after initial hesitation."),
        ("Solu", "Let's hear an example: 'The skeptical client was hesitant at first, but Daniel's warm empathy and thorough preparation quickly won them over.'"),
        ("Tonu", "Charm and preparation working together! What is our fourth expression, Solu?"),
        ("Solu", "Our fourth expression describes undeniable social magnetism: 'light up the room'. When someone 'lights up the room', it means their joyful energy, charismatic smile, and warmth instantly make everyone feel happier and more comfortable."),
        ("Tonu", "For example: 'Whenever Sophia enters a gathering, her infectious laughter and genuine kindness truly light up the room.'"),
        ("Solu", "What a wonderful compliment to give someone! Tonu, take us to our fifth expression."),
        ("Tonu", "Our fifth expression is 'rub someone the wrong way'. To 'rub someone the wrong way' means to unintentionally annoy, irritate, or make someone feel uncomfortable through your demeanor, tone, or attitude."),
        ("Solu", "Here is how you can use it: 'His sarcastic remarks and crossed arms during the team meeting rubbed several colleagues the wrong way.'"),
        ("Tonu", "A great cautionary phrase! And what is our sixth and final expression for today, Solu?"),
        ("Solu", "Our sixth expression is 'break the ice'. To 'break the ice' means to say or do something warm, witty, or friendly that dispels awkward tension and gets a conversation flowing comfortably among strangers."),
        ("Tonu", "Let's hear an example: 'At the start of the international dinner, the host broke the ice by asking everyone to share a funny travel mishap.'"),

        # SECTION 9: INTERACTIVE SPEAKING PRACTICE
        ("Solu", "Now, it is time for our Interactive Speaking Challenge! This is your turn to speak English out loud along with us. Stand tall, roll your shoulders back, breathe deeply, and speak each sentence with warmth, rhythm, and confidence!"),
        ("Tonu", "Sentence number one: 'Putting your best foot forward begins with open body language and an authentic smile.' Your turn!"),
        ("Solu", "Say it out loud with clear pronunciation: 'Putting your best foot forward begins with open body language and an authentic smile.'"),
        ("Tonu", "Great cadence! Sentence number two: 'Her genuine curiosity and active listening quickly won the client over.' Your turn!"),
        ("Solu", "Repeat with steady confidence: 'Her genuine curiosity and active listening quickly won the client over.'"),
        ("Tonu", "Wonderful! Sentence number three: 'Making warm eye contact and remembering names makes people feel deeply valued.' Your turn!"),
        ("Solu", "Speak it clearly: 'Making warm eye contact and remembering names makes people feel deeply valued.'"),
        ("Tonu", "Sentence number four: 'Charisma is not about showing off, but making others feel fascinating and appreciated.' Your turn!"),
        ("Solu", "Let's say sentence number four together: 'Charisma is not about showing off, but making others feel fascinating and appreciated.'"),
        ("Tonu", "Outstanding work! Your spoken English is sounding more authoritative, charismatic, and natural with every single lesson."),

        # SECTION 10: REFLECTION & FAREWELL
        ("Solu", "And now, it is time for today's Weekly Reflection Question! We want you to practice writing in English down in the comment section below."),
        ("Tonu", "Here is today's question: 'Think about a person you met who made an unforgettable, positive first impression on you. What specific body language, vocal tone, or words did they use that made you feel so comfortable?'"),
        ("Solu", "Share your story and observations in English in the comments below! Tonu and I read and reply to your reflections every day."),
        ("Tonu", "Remember, true charisma is an internal state of generosity. When you enter a room focusing on how you can make others feel safe, seen, and appreciated, you will never have to worry about first impressions again."),
        ("Solu", "Keep practicing your spoken English with courage, joy, and consistency. Take wonderful care of yourself, and stand tall!"),
        ("Tonu", "Until next time, goodbye from Tonu!"),
        ("Solu", "And goodbye from Solu!"),
        ("Both", "Happy learning, shine your light, and goodbye!")
    ]
    return turns

if __name__ == "__main__":
    t = build_ep31()
    gen_common.verify_and_save(31, "scripts/daily_speak_ep31_full.txt",
                              "The Psychology of First Impressions & Body Language Secrets",
                              "Daily Speak English | English Listening & Speaking Practice",
                              t)
