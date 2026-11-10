with open("scripts/generate_episodes_07_08.py", "r") as f:
    code = f.read()

# Additions to EP07
target_07 = '    ("Tonu", "And when receiving feedback, resist the urge to get defensive! Take a breath, listen actively, and say: \'Thank you for that feedback. How do you suggest I improve this section for next time?\'"),'
add_07 = '''    ("Tonu", "And when receiving feedback, resist the urge to get defensive! Take a breath, listen actively, and say: 'Thank you for that feedback. How do you suggest I improve this section for next time?'"),
    ("Solu", "And how should professionals disagree with a colleague's proposal during a high-stakes meeting without creating hostility?"),
    ("Tonu", "Use collaborative phrasing! Never say 'That will never work' or 'That is a terrible plan.'"),
    ("Solu", "Instead, say: 'I understand the objective behind this proposal, but I have a few concerns regarding the timeline and budget. What if we piloted a smaller trial version first to test user response before committing the entire annual budget?'"),
    ("Tonu", "That invites problem-solving instead of defensive argumentation! It shows that you are focused on protecting the company's resources."),
    ("Solu", "And what about leaving a company? Resigning gracefully is an art form!"),
    ("Tonu", "Never burn your bridges! The professional world is surprisingly small, and former colleagues or bosses often become future clients, references, or business partners."),
    ("Solu", "Give proper standard notice, offer to train your replacement, document your active workflows, and express gratitude for the opportunities you were given."),'''

code = code.replace(target_07, add_07)

# Additions to EP08
target_08 = '    ("Solu", "An organized, tidy environment directly creates an organized, calm mind!"),'
add_08 = '''    ("Solu", "An organized, tidy environment directly creates an organized, calm mind!"),
    ("Tonu", "Now let's talk about gym and workout etiquette for our listeners who exercise!"),
    ("Solu", "Oh, fitness conversation! Imagine you want to use a piece of gym equipment that someone is resting near. What do you ask?"),
    ("Tonu", "You walk over and say politely: 'Excuse me, are you using this machine, or can I jump in between your sets?'"),
    ("Solu", "And if they are almost finished, they might say, 'I just have one final set left, and then it is all yours!'"),
    ("Tonu", "And you say, 'Take your time, no rush at all!' And always remember gym rule number one: wipe down the bench with disinfectant spray after you finish your workout, and put the dumbbells back on the rack!"),
    ("Solu", "Re-racking your weights is universal gym courtesy!"),
    ("Tonu", "And what about weekend farmers markets? I love visiting local farmers markets on Sunday mornings!"),
    ("Solu", "The sights and smells are wonderful! You chat with local farmers and say: 'Good morning! Are these heirloom tomatoes locally grown? How much are they per pound?'"),
    ("Tonu", "And the farmer says, 'Yes, they were harvested yesterday morning from our family farm. They are three dollars a pound.'"),
    ("Solu", "And you say, 'I will take two pounds, please, and a loaf of that freshly baked sourdough bread!'"),
    ("Tonu", "Supporting local farmers and enjoying fresh, seasonal food adds such rich color and nourishment to our weekly routine."),
    ("Solu", "And finally, let's talk about the transition ritual from workday to evening relaxation."),
    ("Tonu", "Yes! When you arrive home or close your laptop after work, physically change out of your work clothes into comfortable loungewear, wash your face with cool water, and take three deep breaths to signal to your mind that the workday is officially over."),
    ("Solu", "That psychological boundary lets you be truly present with your loved ones for dinner."),'''

code = code.replace(target_08, add_08)

with open("scripts/generate_episodes_07_08.py", "w") as f:
    f.write(code)

