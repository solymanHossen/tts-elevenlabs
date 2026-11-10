with open("scripts/generate_episodes_11_12_13.py", "r") as f:
    code = f.read()

ep11_add4 = '''    ("Tonu", "Let's also talk about the art of seasoning and balancing the five basic tastes!"),
    ("Solu", "Oh, the five basic tastes: Sweet, Sour, Salty, Bitter, and Umami!"),
    ("Tonu", "Great chefs know that when a dish tastes flat or boring, adding more salt is rarely the answer."),
    ("Solu", "Usually, it is missing acidity! A squeeze of fresh lemon juice, a splash of rice vinegar, or a dash of balsamic vinegar brightens the entire profile of a dish instantly."),
    ("Tonu", "And umami—the savory, deep flavor found in parmesan cheese rinds, soy sauce, sun-dried tomatoes, and roasted mushrooms—gives food that irresistible craveable depth."),
    ("Solu", "And what about seasonal cooking? Why is eating seasonal food so much better?"),
    ("Tonu", "Strawberries picked in the height of sunny June taste like pure nectar, while strawberries shipped across three continents in December taste like watery cardboard!"),
    ("Solu", "Eating seasonally supports local farms, costs less money, and connects our biological bodies with the rhythm of the seasons."),
    ("Tonu", "And what a joy it is to look forward to seasonal treats—crisp apples and pumpkin soups in autumn, hearty stews in winter, fresh asparagus and peas in spring!"),
    ("Solu", "Food gives our calendar year its rhythm and flavor."),'''

target_11 = '    ("Solu", "That is the wonderful diversity of human palates; there is room at the culinary table for everyone!"),'
code = code.replace(target_11, target_11 + "\n" + ep11_add4)

ep13_add4 = '''    ("Tonu", "Let's also discuss the myth of multitasking! Many people proudly write 'Excellent Multitasker' on their resume!"),
    ("Solu", "Neuroscience has conclusively proven that human brains physically cannot focus on two complex cognitive tasks at the same time!"),
    ("Tonu", "What people call multitasking is actually 'context switching'—rapidly shifting your attention back and forth between two tasks!"),
    ("Solu", "And every single time you switch between typing an email and answering a phone call, your brain pays a heavy 'switching cost' in lost time, increased errors, and mental fatigue!"),
    ("Tonu", "Single-tasking—doing one single thing at a time with your full undivided presence—is the true mark of mastery!"),
    ("Solu", "And what about the power of creating an 'Anti-Distraction Environment'?"),
    ("Tonu", "Willpower is like a muscle that gets tired. If your smartphone is sitting directly on your desk face up, your brain has to constantly exert willpower to ignore it!"),
    ("Solu", "Put physical distance between you and your distractions! Keep your phone charging in another room when doing deep work."),
    ("Tonu", "Use website blockers to temporarily disable news and social media sites during your work blocks."),
    ("Solu", "Make the right actions easy and the distracting actions difficult!"),
    ("Tonu", "And have you heard of the 'Five-Minute Rule' for starting difficult tasks?"),
    ("Solu", "Tell yourself: 'I will just work on this report for five minutes. If I still hate it after five minutes, I have permission to stop.'"),
    ("Tonu", "And eighty percent of the time, once you overcome that initial hurdle of starting, you keep going naturally!"),'''

target_13 = '    ("Tonu", "That vocal declaration creates an airtight psychological barrier between your professional responsibilities and your personal evening peace."),'
code = code.replace(target_13, target_13 + "\n" + ep13_add4)

with open("scripts/generate_episodes_11_12_13.py", "w") as f:
    f.write(code)

