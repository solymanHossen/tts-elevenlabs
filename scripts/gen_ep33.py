#!/usr/bin/env python3
"""
Generator for Daily Speak English - Episode 33 (26+ Minutes Each)
=================================================================
Mindful Eating, Gut Health & Food Psychology
Target: >= 3,550 words, >= 140 turns (guarantees 26 to 28 minutes at 0.90x speed).
"""

import gen_common

def build_ep33():
    turns = [
        # SECTION 1: WARM MAGNETIC HOOK
        ("Tonu", "Hey hey, lovely listeners! Welcome back to Daily Speak English, your favorite place to become fluent, confident, and unstoppable in English! I'm Tonu!"),
        ("Solu", "And I'm Solu! We are so thrilled to welcome you back for another vibrant, deeply nourishing, and fascinating English conversation."),
        ("Tonu", "Solu, let me ask you an honest, revealing question: When you ate lunch today, what were your eyes looking at? Were you looking at the colors and textures of your meal, or were you staring at a smartphone screen, scrolling through social media videos?"),
        ("Solu", "Oh Tonu, you caught me completely red-handed! I was eating a bowl of chicken noodles with my left hand while rapidly swiping through news headlines on my phone with my right hand!"),
        ("Tonu", "And did you actually taste the food? Did you smell the ginger, notice the crisp vegetables, or chew slowly?"),
        ("Solu", "To be completely honest, after three minutes, the bowl was empty, and I barely remembered swallowing it! It was pure mindless consumption!"),
        ("Tonu", "And that brings us directly into today's vital, life-changing topic: Mindful Eating, Gut Health, and The Fascinating Psychology of Our Relationship with Food!"),
        ("Solu", "In our frantic, modern society, food has become just another chore to rush through. People eat while driving cars, while answering work emails, and while binge-watching television dramas."),
        ("Tonu", "Yet, food is not just fuel; food is biology, chemistry, emotion, memory, culture, and medicine for your soul!"),
        ("Solu", "How you eat is just as important as what you eat. Two people can eat the exact same salad, but if one person eats while screaming at an email, their body produces stomach acid and stress hormones that impair digestion!"),
        ("Tonu", "While the person who eats that salad in calm gratitude absorbs every single mineral, vitamin, and antioxidant."),
        ("Solu", "Today, we are going to explore the cutting-edge neuroscience of the Gut-Brain Axis, unpack the difference between physical hunger and emotional eating, discover the ancient Japanese longevity secret of 'Hara Hachi Bu', and teach you fantastic everyday English vocabulary to talk about food, health, and wellbeing with effortless fluency!"),

        # SECTION 2: THE GUT-BRAIN AXIS & THE SECOND BRAIN
        ("Tonu", "Let's begin with a mind-blowing medical revolution that has transformed biology over the past decade: The 'Gut-Brain Axis' and your Microbiome!"),
        ("Solu", "Did you know that neuroscientists now officially call your digestive system your 'Second Brain'?"),
        ("Tonu", "Tell our listeners about that, Solu! How can our stomach be a brain?"),
        ("Solu", "Your gut contains over five hundred million neurons—more nerve cells than your entire spinal cord! And it communicates directly with your brain via the massive 'Vagus Nerve'."),
        ("Tonu", "Have you ever had a 'gut feeling' about someone or felt 'butterflies in your stomach' when you were nervous before a big speech?"),
        ("Solu", "Yes! Those aren't just poetic metaphors! That is your enteric nervous system physically reacting and sending instant neural signals to your brain!"),
        ("Tonu", "Your gut is literally a feeling organ that senses danger, intuition, and emotion long before your conscious mind puts it into words."),
        ("Solu", "And here is the most astonishing scientific fact: Over ninety percent of the human body's SEROTONIN—the master neurotransmitter responsible for happiness, calm, and emotional stability—is produced inside your gut by your microbiome!"),
        ("Solu", "Ninety percent! Let that sink in for a moment! If your diet is packed with ultra-processed junk food, artificial sweeteners, deep-fried trans fats, and excess sugar, you kill off your beneficial gut bacteria!"),
        ("Tonu", "And when your gut microbiome becomes inflamed and imbalanced, your serotonin production collapses! You feel sudden anxiety, inexplicable sadness, brain fog, and chronic fatigue."),
        ("Solu", "Many people visit doctors asking for mood medications when what they truly need is a diet of fiber-rich leafy greens, fermented yogurt, colorful berries, and wholesome lentils!"),
        ("Tonu", "What you feed your stomach directly determines how your brain feels, thinks, and handles stress."),

        # SECTION 3: EMOTIONAL EATING VERSUS PHYSICAL HUNGER
        ("Solu", "Now, let's explore the psychological trap that catches millions of people every evening: Emotional Eating!"),
        ("Tonu", "What is the difference between true Physical Hunger and Emotional Hunger, Tonu?"),
        ("Tonu", "Physical hunger develops slowly and gradually! It gives you gentle signals: your stomach rumbles, and you would be delighted to eat a simple apple or a plate of vegetables."),
        ("Solu", "Whereas Emotional Hunger strikes like a sudden thunderbolt! It demands immediate gratification!"),
        ("Tonu", "And emotional hunger craves very specific, hyper-palatable foods: 'I don't want an apple; I need a box of chocolate donuts, a tub of ice cream, or greasy potato chips right this second!'"),
        ("Solu", "And why does our brain crave sugar and fat when we are stressed, bored, or lonely?"),
        ("Tonu", "Because refined sugar and fat trigger an instant, massive release of dopamine and endorphins in the brain's reward centers! It acts as a temporary chemical painkiller!"),
        ("Solu", "If you had an exhausting argument with your manager at work, your subconscious brain seeks a dopamine bandage. So you eat half a pizza on the sofa, not because your stomach needs calories, but because your heart needs comfort!"),
        ("Tonu", "And the tragic aftermath of emotional eating is always guilt, shame, and bloating. The problem that caused your stress is still there, but now you feel worse about yourself."),
        ("Solu", "The next time you find yourself standing in front of the open refrigerator door at 10 PM, PAUSE! Take three deep breaths, put your hand on your heart, and ask yourself gently: 'Am I truly hungry, or am I tired, lonely, stressed, or bored?'"),
        ("Tonu", "If you are lonely, food cannot hug you; call a friend! If you are tired, food cannot sleep for you; go to bed! If you are stressed, food cannot solve your deadlines; take a warm bath or a walk in nature!"),

        # SECTION 4: THE 20-MINUTE SATIETY LAG & SPEED EATING
        ("Solu", "Let's talk about the biology of speed: Why eating too quickly causes overeating and weight gain!"),
        ("Tonu", "When food enters your stomach and small intestine, your digestive cells release chemical hormones—like Leptin and Cholecystokinin—that travel through your bloodstream to tell your brain's hypothalamus: 'Stop eating! The tank is full!'"),
        ("Solu", "And how long does it take for those satiety hormones to reach the brain, Tonu?"),
        ("Tonu", "It takes about TWENTY MINUTES! There is a twenty-minute biological delay!"),
        ("Solu", "So if you inhale your entire double cheeseburger and large fries in five minutes flat, your brain still thinks you are completely starving!"),
        ("Tonu", "So you order dessert, eat a slice of chocolate cake, and ten minutes later, when the hormonal signals finally arrive, you feel painfully stuffed, bloated, and miserable!"),
        ("Solu", "Whereas, if you simply slow down, chew your food thoroughly, and take twenty-five minutes to finish your meal, your brain receives the fullness signals while you are only halfway through the plate! You naturally stop eating without feeling deprived."),

        # SECTION 5: OKINAWAN WISDOM: HARA HACHI BU
        ("Solu", "Now let's travel across the Pacific Ocean to the Japanese island of Okinawa—one of the world's celebrated 'Blue Zones' where people regularly live healthy, vibrant lives past the age of one hundred!"),
        ("Tonu", "Okinawa! What is the sacred ancient eating ritual that Okinawans repeat before every meal, Solu?"),
        ("Solu", "Before taking their first bite of food, Okinawan elders recite the Confucian phrase: 'Hara Hachi Bu'!"),
        ("Tonu", "What does 'Hara Hachi Bu' mean in English?"),
        ("Solu", "It translates to: 'Eat until your stomach is eighty percent full!'"),
        ("Tonu", "Eighty percent! In Western consumer culture, people eat until they are one hundred and twenty percent full—until their belt hurts and they have to lie down on the couch!"),
        ("Solu", "When you stop eating at eighty percent capacity, you leave twenty percent of breathing space for your digestive fire! You finish your meal feeling light, energized, alert, and ready to walk or work, rather than slipping into a sluggish food coma!"),
        ("Tonu", "It prevents metabolic overload, reduces oxidative cellular stress, and is one of the primary medical reasons why Okinawans have the lowest rates of heart disease, stroke, and cancer in the entire developed world."),

        # SECTION 6: THE FRENCH PARADOX & THE PLEASURE OF DINING
        ("Tonu", "Now let's examine another culinary mystery that fascinated epidemiologists for decades: 'The French Paradox'!"),
        ("Solu", "What is the French Paradox, Tonu?"),
        ("Tonu", "French people eat rich, creamy cheeses, full-fat butter, croissants, dark chocolate, and duck fat, yet they have significantly lower rates of obesity and cardiovascular disease than Americans or Britons who eat low-fat diet foods!"),
        ("Solu", "Why is that, Tonu? How do the French stay so healthy while enjoying decadent foods?"),
        ("Tonu", "Because the French culture approaches eating as a sacred social ritual and an art form, rather than a hurried chore!"),
        ("Solu", "In France, people rarely eat alone in front of a television. They gather around a dressed table with friends and family. A typical Sunday lunch can last two or three hours!"),
        ("Tonu", "They eat tiny, exquisitely crafted portions of high-quality ingredients, savoring every delicate nuance of flavor. They talk, laugh, debate, and drink water between small bites."),
        ("Solu", "When eating is accompanied by joy, laughter, and relaxation, your body remains in the parasympathetic nervous system—the 'Rest and Digest' state!"),
        ("Tonu", "Your digestive enzymes flow freely, your blood sugar stabilizes, and your body metabolizes nutrients efficiently. Pleasure and presence are true digestive superfoods."),

        # SECTION 7: THE INDUSTRIAL BLISS POINT & FOOD ENGINEERING
        ("Solu", "Now let's expose the sinister side of modern supermarkets: Michael Moss's bestselling investigation, 'Salt Sugar Fat: How the Food Giants Hooked Us'."),
        ("Tonu", "What did investigative journalist Michael Moss reveal about processed food, Solu?"),
        ("Solu", "He revealed that giant food corporations employ teams of neuroscientists, chemists, and sensory engineers whose sole job is to engineer what they call the 'Bliss Point' in ultra-processed snacks!"),
        ("Tonu", "The Bliss Point! What is the Bliss Point?"),
        ("Solu", "The Bliss Point is the precise mathematical combination of salt, refined sugar, and hydrogenated fat that triggers the maximum possible dopamine explosion in your brain, while purposely avoiding triggering satiety signals!"),
        ("Tonu", "So that famous potato chip slogan: 'Bet you can't eat just one'—that was not a joke; it was a biological design specification!"),
        ("Solu", "Exactly! Potato chips and sugary cereals are literally engineered to melt in your mouth quickly so your brain doesn't register that you are chewing dense calories!"),
        ("Tonu", "They trick your evolutionary biology. When you realize that processed foods are manufactured to be biologically addictive, you stop beating yourself up for lacking willpower and start avoiding those toxic aisles completely!"),
        ("Solu", "And here is a radical truth: Mindful eating does NOT mean you can never enjoy a decadent dessert or a slice of artisan pizza again!"),
        ("Tonu", "In fact, mindful eating makes treats ten times more pleasurable!"),
        ("Solu", "When people eat a pastry with guilt, they swallow it rapidly while feeling ashamed, barely tasting the butter and chocolate!"),
        ("Tonu", "Whereas, if you choose to indulge mindfully, you sit down, put it on a beautiful ceramic plate, eat a single exquisite bite, let it melt across your palate, and experience pure bliss!"),
        ("Solu", "You satisfy your soul's desire with three mindful bites, rather than eating an entire box in unconscious shame."),

        # SECTION 8: INTERMITTENT FASTING & AUTOPHAGY
        ("Solu", "Let's also talk about the restorative power of giving your digestive tract a break: Intermittent Fasting and Autophagy!"),
        ("Tonu", "In our culture of 24/7 snacking, people eat from 7 AM until midnight! Your poor digestive organs never get a single hour of rest!"),
        ("Solu", "In 2016, Japanese scientist Yoshinori Ohsumi won the Nobel Prize in Medicine for discovering the cellular mechanism of 'Autophagy'."),
        ("Tonu", "Autophagy translates from Greek as 'self-eating'. When you fast for twelve to sixteen hours overnight, your body runs out of incoming glucose and shifts into deep cellular recycling mode!"),
        ("Solu", "Your cells seek out damaged proteins, mutated components, and intracellular bacteria, and break them down into fresh building blocks!"),
        ("Tonu", "It cleans out cellular debris, lowers inflammation, sharpens mental clarity, and gives your hardworking gut lining time to repair and rebuild itself."),

        # SECTION 9: COOKING AT HOME AS REVOLUTIONARY MEDICINE
        ("Solu", "Tonu, what is the single most powerful habit someone can build to transform their health and finances simultaneously?"),
        ("Tonu", "Cooking your own meals at home with raw, whole ingredients!"),
        ("Solu", "Restaurant chefs and takeout kitchens are not cooking for your longevity; they are cooking for flavor and reviews! So they dump cups of hidden butter, refined seed oils, and high-fructose syrup into restaurant dishes."),
        ("Tonu", "When you cook at home, you have complete control over what enters your temple. You choose cold-pressed olive oil, fresh sea salt, and crisp organic vegetables."),
        ("Solu", "And cooking is an act of love! When you cook for your children or your partner, you infuse that meal with your care, patience, and warmth."),

        # SECTION 10: HYDRATION & THE THIRST TRAP
        ("Tonu", "And before we talk about practical drills, Solu, let's mention the simplest health hack of all: Hydration!"),
        ("Solu", "Did you know that the brain's hypothalamus regulates both hunger and thirst using identical neurochemical pathways?"),
        ("Tonu", "Which means when your body is mildly dehydrated, your brain often misinterprets that signal as a sudden food craving!"),
        ("Solu", "You think you need a bag of cookies or a sandwich, but your body is simply begging for clean water!"),
        ("Tonu", "Drink a large glass of warm water, wait ten minutes, and eighty percent of the time, that artificial craving vanishes completely."),

        # SECTION 11: THE RAINBOW DIET & THE 30-PLANT RULE
        ("Solu", "Now let's talk about the biological secret discovered by the world's largest microbiome study: The '30-Plant Rule'!"),
        ("Tonu", "What is the 30-Plant Rule, Solu? It sounds like a lot of vegetables!"),
        ("Solu", "Researchers at the American Gut Project analyzed stool samples from thousands of people across the globe to see what diet produced the healthiest, most resilient gut bacteria."),
        ("Tonu", "And what was the number one dietary factor?"),
        ("Solu", "It wasn't being strictly vegan, paleo, or keto! The single most reliable predictor of a thriving microbiome was eating THIRTY different species of plants each week!"),
        ("Tonu", "Thirty different plants! How can an ordinary busy person hit thirty different plants without going crazy at the supermarket?"),
        ("Solu", "It is much easier than it sounds! 'Plants' include not just vegetables, but seeds, nuts, whole grains, herbs, and spices!"),
        ("Tonu", "Aha! So if you sprinkle chia seeds, pumpkin seeds, and walnuts on your morning oatmeal, you just consumed four different plant species in one single breakfast bowl!"),
        ("Solu", "And cooking with turmeric, black pepper, rosemary, garlic, and fresh basil adds five more plants! Each different colored plant provides unique polyphenol antioxidants that feed different families of beneficial gut bacteria."),

        # SECTION 12: GRANDMA'S KITCHEN & SENSORY SCENT MEMORIES
        ("Tonu", "Solu, have you ever caught a sudden whiff of cinnamon, roasted garlic, or warm sourdough bread, and felt like you were instantly transported through time?"),
        ("Solu", "Yes! That is what neuroscientists call 'Proustian Memory'—named after French author Marcel Proust!"),
        ("Tonu", "Your olfactory bulb—the scent processor in your brain—has a direct, super-fast highway to your amygdala and hippocampus, where emotional memories are stored!"),
        ("Solu", "So the aroma of your grandmother's chicken stew or cardamom tea doesn't just remind you of food; it floods your entire nervous system with the emotional safety, love, and protection of your childhood."),
        ("Tonu", "Food is living ancestral heritage. When we cook traditional family recipes, we preserve the stories and love of generations past."),

        # SECTION 13: COFFEE, MATCHA & THE 90-MINUTE ADENOSINE RULE
        ("Solu", "Let's also talk about our favorite daily ritual: Coffee and Tea!"),
        ("Tonu", "Neurobiologist Dr. Andrew Huberman popularized a brilliant rule about coffee timing: 'The 90-Minute Rule'!"),
        ("Solu", "What happens when you drink a double espresso ten seconds after opening your eyes in bed, Tonu?"),
        ("Tonu", "When you wake up, your brain still has leftover 'Adenosine'—the sleepiness chemical! If you drink caffeine immediately, caffeine blocks the adenosine receptors, but does NOT clear them away!"),
        ("Solu", "And then at 2 PM in the afternoon, when the caffeine wears off, that giant backlog of adenosine binds to your receptors all at once, and you suffer a massive afternoon energy crash!"),
        ("Tonu", "Wait sixty to ninety minutes after waking before your first cup of coffee or matcha tea! Let your body's natural morning cortisol clear the adenosine naturally, and your caffeine will give you sustained, crash-free energy all day long!"),

        # SECTION 14: PRACTICAL MINDFUL EATING DRILLS
        ("Solu", "How can someone listening right now practice Mindful Eating at their very next meal today?"),
        ("Tonu", "Let's share four simple, transformative mindful eating rules!"),
        ("Solu", "Rule number one: The Screen-Free Table! Banish all smartphones, tablets, laptops, and televisions from your dining table! Create a sacred boundary where food and human conversation are the only stars."),
        ("Tonu", "Rule number two: Engage Your Senses First! Before you take your first bite, pause for ten seconds. Look at the vibrant colors of your food. Inhale the aroma deeply into your nostrils. Appreciate the sunlight and the labor of the farmers and cooks who brought that meal to your plate."),
        ("Solu", "Rule number three: The Fork-Down Technique! Put your fork, spoon, or chopsticks down on the table between every single bite! Don't load up the next bite while you are still chewing the current one."),
        ("Tonu", "Rule number four: Chew Twenty Times! Chew each mouthful slowly until it is almost liquid before swallowing. It pre-digests your food with saliva enzymes, eases the burden on your stomach, and allows you to experience the full symphony of flavors!"),
        ("Solu", "Eating mindfully three times a day becomes an effortless, built-in meditation practice that grounds your awareness without needing a silent yoga retreat."),
        ("Tonu", "Your dining table becomes your daily temple of presence, gratitude, and physical rejuvenation."),

        # SECTION 8: VOCABULARY & IDIOM SPOTLIGHT (6 KEY IDIOMS)
        ("Tonu", "Now, let's step into our signature segment: Key Everyday English Vocabulary and Idioms! Today, we have selected six colorful, essential expressions inspired by food, eating, and cooking."),
        ("Solu", "Let's master them together! Tonu, what is our very first culinary expression for today?"),
        ("Tonu", "Our first expression is 'bite off more than one can chew'. To 'bite off more than you can chew' means to take on a project, commitment, or responsibility that is far too big, difficult, or overwhelming for you to manage."),
        ("Solu", "Let's listen to a natural conversational example: 'Taking on three freelance client projects while studying for his master's degree was biting off more than he could chew.'"),
        ("Tonu", "A very common cautionary phrase! What is our second expression, Solu?"),
        ("Solu", "Our second expression is 'food for thought'. 'Food for thought' refers to an interesting idea, fact, or perspective that gives you serious reasons to reflect and think deeply."),
        ("Tonu", "Here is an everyday example: 'The professor's lecture on the gut microbiome gave all the medical students immense food for thought.'"),
        ("Solu", "Brilliant! Tonu, introduce our third expression."),
        ("Tonu", "Our third expression is 'take something with a pinch of salt'. To 'take something with a pinch of salt' means to view a claim, story, or piece of advice with healthy skepticism, realizing it may be exaggerated or not completely accurate."),
        ("Solu", "Let's hear an example: 'The sensational diet book promised you would lose ten kilograms in five days, but I took their promises with a heavy pinch of salt.'"),
        ("Tonu", "Very smart! What is our fourth expression, Solu?"),
        ("Solu", "Our fourth expression describes accidentally revealing secrets: 'spill the beans'. To 'spill the beans' means to prematurely or unintentionally disclose confidential information or a surprise."),
        ("Tonu", "For example: 'We were planning a surprise birthday dinner for Maya, but her little brother accidentally spilled the beans two days early!'"),
        ("Solu", "Classic blunder! Tonu, take us to our fifth expression."),
        ("Tonu", "Our fifth expression is 'have bigger fish to fry'. To 'have bigger fish to fry' means to have more important, pressing, or urgent matters to attend to, rather than wasting time on minor trifles."),
        ("Solu", "Here is how you can use it: 'I am not going to argue about who forgot to buy the paper napkins; we have far bigger fish to fry before the conference begins.'"),
        ("Tonu", "And what is our sixth and final expression for today, Solu?"),
        ("Solu", "Our sixth expression describes bitter jealousy: 'sour grapes'. 'Sour grapes' refers to an attitude where someone pretends to despise or criticize something they secretly desire, simply because they were unable to get it."),
        ("Tonu", "Let's hear an example: 'He claimed he never really wanted the promotion anyway because managerial work is boring, but everyone knew it was just sour grapes.'"),

        # SECTION 9: INTERACTIVE SPEAKING PRACTICE
        ("Solu", "Now, it is time for our Interactive Speaking Challenge! This is your turn to speak English out loud along with us. Open your vocal cords, breathe from your belly, and repeat each phrase with natural rhythm and steady confidence!"),
        ("Tonu", "Sentence number one: 'Slowing down to savor every bite transforms food from a chore into a healing ritual.' Your turn!"),
        ("Solu", "Say it out loud with clear pronunciation: 'Slowing down to savor every bite transforms food from a chore into a healing ritual.'"),
        ("Tonu", "Great cadence! Sentence number two: 'Be careful not to bite off more than you can chew when taking on new responsibilities.' Your turn!"),
        ("Solu", "Repeat with steady confidence: 'Be careful not to bite off more than you can chew when taking on new responsibilities.'"),
        ("Tonu", "Wonderful! Sentence number three: 'Practicing the Japanese principle of Hara Hachi Bu keeps your body light and energized.' Your turn!"),
        ("Solu", "Speak it clearly: 'Practicing the Japanese principle of Hara Hachi Bu keeps your body light and energized.'"),
        ("Tonu", "Sentence number four: 'True nourishment begins when you listen to your body rather than emotional cravings.' Your turn!"),
        ("Solu", "Let's say sentence number four together: 'True nourishment begins when you listen to your body rather than emotional cravings.'"),
        ("Tonu", "Outstanding work! Your spoken English is sounding more expressive, fluent, and confident every single day."),

        # SECTION 10: REFLECTION & FAREWELL
        ("Solu", "And now, it is time for today's Weekly Reflection Question! We want you to practice writing in English down in the comment section below."),
        ("Tonu", "Here is today's question: 'What is your current relationship with food? Do you usually eat rushed in front of a screen, or do you take time to savor your meals with loved ones? And what is one mindful eating habit you will try this week?'"),
        ("Solu", "Will you put your phone away during dinner, chew each bite twenty times, or practice stopping at eighty percent full? Share your commitment in the comments below!"),
        ("Tonu", "Solu and I read through every single comment, and we love replying to your personal stories and celebrating your English growth."),
        ("Solu", "Remember that your body is the only home you will live in for your entire life. Treat it with reverence, nourish it with whole foods, and feed your mind with inspiring ideas."),
        ("Tonu", "Keep practicing your English every single day with curiosity and joy. Take wonderful care of yourself, and have a delicious, peaceful day!"),
        ("Solu", "Until next time, goodbye from Solu!"),
        ("Tonu", "And goodbye from Tonu!"),
        ("Both", "Happy learning, eat mindfully, and goodbye!")
    ]
    return turns

if __name__ == "__main__":
    t = build_ep33()
    gen_common.verify_and_save(33, "scripts/daily_speak_ep33_full.txt",
                              "Mindful Eating, Gut Health & Food Psychology",
                              "Daily Speak English | English Listening & Speaking Practice",
                              t)
