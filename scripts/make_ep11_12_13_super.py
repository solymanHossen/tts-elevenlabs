with open("scripts/generate_episodes_11_12_13.py", "r") as f:
    code = f.read()

ep11_extra2 = '''    ("Solu", "Now, let's celebrate street food culture around the world!"),
    ("Tonu", "Oh, street food! Some of the most mouthwatering, authentic dishes on Earth are served from tiny street carts and night markets, not Michelin-starred restaurants!"),
    ("Solu", "Think about Bangkok's bustling night markets with steaming bowls of Pad Thai, sizzling mango sticky rice, and spicy coconut soups!"),
    ("Tonu", "Or Mexico City street stalls with fresh corn tortillas, slow-roasted al pastor pork with pineapple, and spicy salsa verde!"),
    ("Solu", "Or Istanbul's Bosphorus waterfront with toasted sesame simit bread and freshly grilled fish sandwiches!"),
    ("Tonu", "Street food is the beating culinary heart of any city. It is affordable, democratic, and brings together people from all walks of life."),
    ("Solu", "And what about the fascinating history of herbs and spices? Spices literally shaped the map of modern human civilization!"),
    ("Tonu", "Yes! For centuries, merchant ships sailed across treacherous oceans on the historic Silk Road and Spice Route in search of black pepper, cinnamon, cardamom, cloves, and nutmeg."),
    ("Solu", "Spices were once as precious as gold, used not only for seasoning but for preserving meats and medicinal healing."),
    ("Tonu", "And today, we can open our kitchen pantry and have access to all the spices of the world for just a few dollars! We live in a culinary golden age."),
    ("Solu", "And what about the deep emotional link between food and nostalgia?"),
    ("Tonu", "Psychologists call it the 'Proustian memory effect'! Because our olfactory sense of smell is wired directly to the amygdala and hippocampus in our brain, the aroma of a dish your grandmother cooked forty years ago can transport you instantly back to childhood!"),
    ("Solu", "Food is memory. When we cook ancestral recipes, we keep the spirit and love of our ancestors alive."),
    ("Tonu", "And what are your top tips for hosting an unforgettable dinner party with friends?"),
    ("Solu", "First: choose dishes you can prepare in advance, like a slow-cooked stew or a chilled pasta salad! If the host is trapped behind the stove all night sweating, nobody can relax."),
    ("Tonu", "Second: create a cozy, welcoming atmosphere with warm lighting, candles, and a gentle background music playlist."),
    ("Solu", "And third: focus on laughter and deep conversation rather than trying to impress anyone with perfection! Hospitality is about making guests feel loved, not intimidated."),'''

target_11 = '    ("Solu", "Now listeners, it is time for our favorite interactive segment: The Speaking Practice Challenge!"),'
code = code.replace(target_11, ep11_extra2 + "\n" + target_11)

ep12_extra2 = '''    ("Solu", "Let's also talk about the vital difference between nasal breathing and mouth breathing!"),
    ("Tonu", "Oh, this is such a transformative health insight from James Nestor's bestselling book Breath!"),
    ("Solu", "Many people have developed the unconscious habit of breathing through their mouth, especially when sleeping or stressed."),
    ("Tonu", "And mouth breathing causes shallow breathing, snoring, sleep apnea, poor oxygen delivery to tissues, and dental problems!"),
    ("Solu", "While our nose is a sophisticated air filtration, humidification, and temperature-regulating organ!"),
    ("Tonu", "When we inhale through our nose, our nasal passages produce nitric oxide, a molecule that dilates blood vessels, increases oxygen absorption in our lungs by twenty percent, and kills airborne microbes!"),
    ("Solu", "And have you heard of the 'Physiological Sigh' discovered by neuroscientists?"),
    ("Tonu", "The physiological sigh! Two quick inhales through the nose, followed by a long, slow, extended exhale through the mouth!"),
    ("Solu", "Let's do that once together! Inhale deeply, top it off with another quick sniff, and slowly exhale all the air out..."),
    ("Tonu", "Ah! Doing just two or three physiological sighs immediately collapses alveolar air sacs in your lungs, slows your heart rate, and switches off acute stress in under ten seconds!"),
    ("Solu", "And what about functional mobility and the famous sit-to-stand test for longevity?"),
    ("Tonu", "European physicians developed the sitting-rising test: can you sit down cross-legged on the floor and stand back up without using your hands, knees, or arms for support?"),
    ("Solu", "Studies showed that people who can rise from the floor with minimal support have significantly lower all-cause mortality as they age!"),
    ("Tonu", "It measures core strength, hip flexibility, and neurological balance—the very attributes that keep you independent and vibrant throughout life."),
    ("Solu", "And let's touch upon the biological miracle of Autophagy through intermittent fasting."),
    ("Tonu", "Autophagy translates from Greek as 'self-eating'! When your body is in a fasted state for fourteen to sixteen hours, your cells begin sweeping away senescent, damaged cellular debris and recycling proteins."),
    ("Solu", "It is like having an internal sanitation crew cleaning your cellular engine!"),'''

target_12 = '    ("Solu", "Now listeners, it is time for our favorite interactive segment: The Speaking Practice Challenge!"),'
code = code.replace(target_12, ep12_extra2 + "\n" + target_12)

ep13_extra2 = '''    ("Solu", "Now let's explore David Allen's famous 'Two-Minute Rule' from Getting Things Done!"),
    ("Tonu", "The Two-Minute Rule is so wonderfully practical! If an incoming task or email will take less than two minutes to complete, do it immediately!"),
    ("Solu", "Don't write it on a to-do list, don't file it, don't postpone it! Just take ninety seconds and knock it out."),
    ("Tonu", "Because the mental energy required to remember, track, and review an unfinished two-minute task is ten times greater than the effort to simply get it done!"),
    ("Solu", "And what about Energy Management versus Time Management? Many productivity experts argue that managing your energy is far more important than managing your time!"),
    ("Tonu", "You can have eight open hours on your calendar, but if your physical energy is completely drained, you will accomplish nothing of value!"),
    ("Solu", "Understand your biological chronotype: Are you an early morning lark whose analytical brain peaks at eight in the morning, or a night owl who thrives in the evening?"),
    ("Tonu", "Schedule your most demanding, creative deep work during your peak biological energy window, and save mindless administrative chores for your low-energy slumps!"),
    ("Solu", "And have you heard of Mihaly Csikszentmihalyi's concept of 'Flow State'—the state of optimal human performance?"),
    ("Tonu", "Flow state! Being completely immersed, focused, and absorbed in an activity where time seems to stand still and self-doubt vanishes!"),
    ("Solu", "What triggers a flow state, Tonu?"),
    ("Tonu", "Clear goals, immediate feedback, and a challenge that slightly exceeds your current skill level by about four percent!"),
    ("Solu", "If the task is too easy, you feel bored; if it is too difficult, you feel anxious. But when it stretches your ability just enough, you enter the flow zone!"),
    ("Tonu", "And finally, cultivate digital minimalism! Keep a clean computer desktop, close unused browser tabs, and create a distraction-free physical workspace."),
    ("Solu", "A calm, clutter-free desk invites a calm, focused mind."),'''

target_13 = '    ("Tonu", "Now listeners, it is time for our favorite interactive segment: The Speaking Practice Challenge!"),'
code = code.replace(target_13, ep13_extra2 + "\n" + target_13)

with open("scripts/generate_episodes_11_12_13.py", "w") as f:
    f.write(code)

