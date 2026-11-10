with open("scripts/generate_episodes_07_08.py", "r") as f:
    code = f.read()

# Additions to EP07
target_07 = '    ("Solu", "When you approach your career with curiosity, adaptability, and emotional intelligence, you will thrive wherever you go."),'
add_07 = '''    ("Tonu", "Let's also discuss writing the perfect post-interview thank-you email, because so many job candidates neglect this critical step!"),
    ("Solu", "Sending a thoughtful thank-you email within twenty-four hours after your interview can be the deciding factor between two equally qualified candidates!"),
    ("Tonu", "What should that email say, Solu?"),
    ("Solu", "Keep it concise and personalized! Thank the interviewer for their time, reiterate your enthusiasm for the role, and reference a specific interesting topic you discussed during the interview."),
    ("Tonu", "For example: 'Dear Sarah, thank you so much for taking the time to speak with me today about the Senior Marketing Manager position. I especially enjoyed our discussion about your upcoming international expansion into European markets. Our conversation confirmed my strong enthusiasm for joining your team!'"),
    ("Solu", "That shows that you were truly engaged, not just copying and pasting a generic internet template."),
    ("Tonu", "And how should professionals prepare when they want to ask for a well-deserved promotion or raise?"),
    ("Solu", "Start keeping an 'Accomplishments Tracker' or brag sheet six months in advance! Document every project you completed, metrics you improved, positive feedback from clients, and extra responsibilities you assumed."),
    ("Tonu", "When you have concrete documentation of your measurable impact, asking for a raise is based on proven value rather than emotional feelings."),
    ("Solu", "And how do you gracefully exit a conversation at a crowded networking mixer without being awkward?"),
    ("Tonu", "You say: 'It was fantastic learning about your new product launch, Mark! I don't want to monopolize all your time this evening, but here is my business card, and I would love to connect with you on LinkedIn tomorrow!'"),
    ("Solu", "Polite, graceful, and leaves a memorable professional impression."),
    ("Solu", "When you approach your career with curiosity, adaptability, and emotional intelligence, you will thrive wherever you go."),'''

code = code.replace(target_07, add_07)

# Additions to EP08
target_08 = '    ("Solu", "Knowing these real-world conversation templates gives you the confidence to handle any everyday life situation abroad with complete poise."),'
add_08 = '''    ("Solu", "Knowing these real-world conversation templates gives you the confidence to handle any everyday life situation abroad with complete poise."),
    ("Tonu", "Let's also talk about taking public transportation and asking for directions on the street!"),
    ("Solu", "Oh, definitely! Imagine you are on a busy subway platform. How do you confirm you are on the right train?"),
    ("Tonu", "You turn to a fellow commuter and ask politely: 'Excuse me, does this train go all the way to Central Station, or do I need to transfer at 14th Street?'"),
    ("Solu", "And the commuter says, 'This is an express train; it goes directly to Central Station without any transfers!'"),
    ("Tonu", "And you say, 'Awesome, thank you so much for your help!'"),
    ("Solu", "And what if you are looking for a seat on a crowded bus?"),
    ("Tonu", "You point to the empty seat and say with a polite smile, 'Pardon me, is this seat taken?'"),
    ("Solu", "And they say, 'No, go ahead and sit down!' Simple courtesy makes daily public life so pleasant."),
    ("Tonu", "Now let's talk about neighborhood life and chatting with your neighbors. Having a warm relationship with the people living next door makes a house feel like a home."),
    ("Solu", "Yes! When a new neighbor moves in, you can bring over a small plate of homemade cookies and say: 'Hi there! I live in apartment 4B right next door. Just wanted to welcome you to the building! If you ever need to borrow a tool or have questions about trash pickup days, feel free to knock on my door.'"),
    ("Tonu", "That immediately breaks the ice and creates a safe, welcoming community atmosphere."),
    ("Solu", "And what about weekend domestic routines? Like Saturday morning cleaning and laundry?"),
    ("Tonu", "There is deep mental satisfaction in putting clean sheets on your bed, dusting the shelves, and organizing your living space."),
    ("Solu", "An organized, tidy environment directly creates an organized, calm mind!"),'''

code = code.replace(target_08, add_08)

with open("scripts/generate_episodes_07_08.py", "w") as f:
    f.write(code)

