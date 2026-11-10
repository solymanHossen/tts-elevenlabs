with open("scripts/generate_episodes_07_08.py", "r") as f:
    code = f.read()

# Additions to EP07
target_07 = '    ("Tonu", "Now, let\'s dive into our special English vocabulary section! Let\'s explore seven high-impact workplace idioms and business expressions that native speakers use every day."),'
add_07 = '''    ("Solu", "Let's also talk about the classic interview trap question: 'What is your greatest weakness?'"),
    ("Tonu", "Oh, that dreaded question! Many people answer with fake weaknesses like 'I work too hard' or 'I am too much of a perfectionist.'"),
    ("Solu", "Hiring managers can see through those cliché answers in two seconds! What is the authentic way to answer that question, Tonu?"),
    ("Tonu", "Choose a genuine area of improvement that isn't fatal to the core job role, and immediately explain the proactive steps you are taking to overcome it!"),
    ("Solu", "Give us an example!"),
    ("Tonu", "For example: 'In the past, I found it challenging to delegate tasks because I wanted to ensure everything was done my way. However, I recently took a leadership workshop and implemented clear milestone check-ins with my team. As a result, I now delegate effectively and empower my colleagues to take ownership.'"),
    ("Solu", "That shows high self-awareness and active commitment to personal growth!"),
    ("Tonu", "And what should candidates do at the end of the interview when the hiring manager asks: 'Do you have any questions for us?'"),
    ("Solu", "Never say 'No, I think you covered everything!' Saying you have no questions makes you seem disinterested or unprepared."),
    ("Tonu", "Always come with three thoughtful questions! For example: 'What does success look like in this role over the first ninety days?'"),
    ("Solu", "Or: 'What is the biggest challenge currently facing the team, and how can the person in this role help solve it?'"),
    ("Tonu", "And my personal favorite: 'What do you personally enjoy most about working at this company?'"),
    ("Solu", "Those questions demonstrate strategic thinking and make the conversation a two-way dialogue."),
    ("Tonu", "Now let's touch upon the art of the thirty-second elevator pitch! When you are at a networking conference or industry event, how do you introduce yourself?"),
    ("Solu", "A great elevator pitch has three parts: Who you help, the problem you solve, and the unique value you create!"),
    ("Tonu", "For example: 'I help tech startups streamline their customer onboarding process so they can reduce churn and boost user retention by thirty percent.'"),
    ("Solu", "Short, impactful, and memorable! It sparks curiosity and invites the other person to ask follow-up questions."),
    ("Tonu", "And let's talk about remote work communication etiquette on platforms like Slack and Microsoft Teams."),
    ("Solu", "Yes! Remote work relies heavily on asynchronous text. Always provide complete context in your message rather than just sending 'Hi' and waiting five minutes for the other person to reply!"),
    ("Tonu", "Send the complete question, relevant links, and what deadline you are working against in one clear message. It respects everyone's focus and time!"),
    ("Solu", "And in video meetings, mute your microphone when not speaking, maintain eye contact with the camera, and summarize agreed next steps before wrapping up."),
    ("Tonu", "Now, let's dive into our special English vocabulary section! Let's explore seven high-impact workplace idioms and business expressions that native speakers use every day."),'''

code = code.replace(target_07, add_07)

# Additions to EP08
target_08 = '    ("Tonu", "Now, let\'s explore our special English vocabulary section! Let\'s examine seven very common everyday English expressions and idioms about daily life and routines."),'
add_08 = '''    ("Solu", "Let's also walk our listeners through ordering at a coffee shop, because ordering coffee in English has its own unique terminology!"),
    ("Tonu", "Oh, definitely! When you walk into a specialty cafe, the barista asks, 'Hi there! What can I get started for you today?'"),
    ("Solu", "And you can specify the size, milk preference, sweetness, and temperature! For example: 'Could I please get a medium iced oat milk latte with just one pump of vanilla syrup?'"),
    ("Tonu", "And then the barista asks, 'Is that for here or to go?'"),
    ("Solu", "And you reply, 'To go, please!' Then they say, 'That'll be four dollars and fifty cents. Tap your card right on the terminal when you are ready.'"),
    ("Tonu", "And you tap your card and say, 'Thank you so much!' It is that simple, smooth, and natural."),
    ("Solu", "Now let's roleplay mailing a package at the post office! What happens when you step up to the postal counter?"),
    ("Tonu", "You place your parcel on the counter and say, 'Good afternoon! I would like to send this package to Canada, please.'"),
    ("Solu", "And the postal worker asks, 'Would you prefer standard ground delivery or express shipping with tracking?'"),
    ("Tonu", "And you say, 'How many business days does express shipping take?'"),
    ("Solu", "And the worker says, 'Express shipping takes two to three business days and includes full tracking and signature on delivery.'"),
    ("Tonu", "And you say, 'Perfect, let's go with express shipping, please!' Then you fill out the quick customs declaration form, pay the postage, and take your tracking receipt."),
    ("Solu", "And what about calling to schedule a doctor or dentist appointment?"),
    ("Tonu", "You call the clinic reception and say, 'Hello! I would like to schedule a routine dental checkup and teeth cleaning, please. Do you have any openings later this week?'"),
    ("Solu", "And the receptionist says, 'Let me check the schedule... We have an opening this Thursday at ten in the morning or Friday at two in the afternoon. Which works better for you?'"),
    ("Tonu", "And you say, 'Thursday morning at ten works perfectly for me. Thank you!'"),
    ("Solu", "Knowing these real-world conversation templates gives you the confidence to handle any everyday life situation abroad with complete poise."),
    ("Tonu", "And let's talk about the beauty of evening hobbies! After working or studying all day, doing an offline hobby like tending to house plants, sketching, or listening to records helps your mind decompress."),
    ("Solu", "It creates a sanctuary of peace in your daily life."),
    ("Tonu", "Now, let's explore our special English vocabulary section! Let's examine seven very common everyday English expressions and idioms about daily life and routines."),'''

code = code.replace(target_08, add_08)

with open("scripts/generate_episodes_07_08.py", "w") as f:
    f.write(code)

