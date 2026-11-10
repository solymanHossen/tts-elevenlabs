with open("scripts/generate_episodes_11_12_13.py", "r") as f:
    code = f.read()

ep11_add = '''    ("Solu", "Let's also talk about the fundamental difference between cooking and baking!"),
    ("Tonu", "Oh, that is such a classic culinary truth: Cooking is an art, but baking is a precise science!"),
    ("Solu", "Exactly! When you are cooking a soup, pasta sauce, or stir-fry, you can taste as you go, add an extra pinch of chili flakes, toss in some extra garlic, and improvise!"),
    ("Tonu", "While in baking, if you alter the baking powder by half a teaspoon or the oven temperature by twenty degrees, your cake won't rise, or your bread turns into a heavy brick!"),
    ("Solu", "Precision and chemistry rule the bakery! And what are some essential cooking techniques every beginner should master?"),
    ("Tonu", "Let's break down basic culinary verbs: Sautéing means cooking food quickly in a small amount of hot oil or butter over medium-high heat while stirring."),
    ("Solu", "Simmering means cooking liquid gently just below the boiling point, where tiny bubbles rise slowly to the surface!"),
    ("Tonu", "While boiling means vigorous, large bubbles rolling rapidly at one hundred degrees Celsius!"),
    ("Solu", "And braising means searing meat or vegetables at high heat to develop flavor, and then cooking it slowly in a covered pot with broth for hours until it is meltingly tender."),
    ("Tonu", "And roasting means cooking uncovered in the dry heat of an oven, caramelizing the natural sugars in root vegetables like carrots and potatoes!"),
    ("Solu", "Now let's explore global tea and coffee rituals across cultures. Beverage culture is fascinating!"),
    ("Tonu", "In the United Kingdom, afternoon tea with warm scones, clotted cream, strawberry jam, and Earl Grey tea is an elegant social tradition."),
    ("Solu", "In Japan, the Chanoyu tea ceremony is a sacred, meditative practice of mindfulness, harmony, and respect."),
    ("Tonu", "In Turkey, Turkish coffee is brewed in a special copper pot called a cezve, served unfiltered and thick with rich foam, often enjoyed alongside Turkish delight sweets!"),
    ("Solu", "And in Ethiopia, the birthplace of coffee, the coffee ceremony is an elaborate multi-hour hospitality ritual where green beans are roasted over hot coals right in front of the guests!"),
    ("Tonu", "Now, let's talk about fermented foods and gut health, which has become a huge health topic lately."),
    ("Solu", "Yes! Scientists call our gut the 'second brain' because over ninety percent of our body's serotonin is produced in the gut!"),
    ("Tonu", "Eating fermented foods rich in live probiotics—like authentic sourdough bread, kimchi, sauerkraut, kefir, and plain yogurt—nourishes our microbiome, boosts immunity, and improves mental well-being!"),
    ("Solu", "And what about dining etiquette in formal restaurants?"),
    ("Tonu", "The golden rule of table silverware: work your way from the outside in! The outermost fork and spoon are for the first salad or appetizer, and the innermost utensils are for the main entree."),
    ("Solu", "And place your cloth napkin on your lap as soon as you sit down! If you need to excuse yourself from the table temporarily, place the napkin loosely on your chair, not crumpled on the table."),
    ("Tonu", "These small manners make you feel completely at ease in any formal banquet or business dinner."),'''

target_11 = '    ("Solu", "Such great culinary wisdom! Now let\'s explore our special English vocabulary section! Let\'s examine seven colorful everyday idioms and expressions that are inspired by food and cooking."),'
code = code.replace(target_11, ep11_add + "\n" + target_11)

ep12_add = '''    ("Solu", "Let's also talk about the fascinating health benefits of thermal stress: Cold exposure and Heat therapy!"),
    ("Tonu", "Oh, saunas and ice baths! They have exploded in popularity among athletes, biohackers, and health enthusiasts worldwide."),
    ("Solu", "What does scientific research say about regular sauna use, Tonu?"),
    ("Tonu", "Long-term Finnish studies following thousands of participants found that using a traditional sauna four to seven times a week reduces the risk of cardiovascular mortality by fifty percent!"),
    ("Solu", "Fifty percent! That is comparable to the most powerful cardiac medications in the world. When you sit in a sauna, your heart rate increases to exercise levels, your blood vessels dilate, and your body produces heat shock proteins that repair damaged cellular structures."),
    ("Tonu", "And what about cold showers or ice baths?"),
    ("Solu", "Immersing yourself in cold water for just two to three minutes triggers an immediate, sustained two-hundred-and-fifty percent increase in baseline dopamine!"),
    ("Tonu", "Dopamine is our neurotransmitter for focus, motivation, and drive. Plus, cold exposure activates brown adipose tissue, which burns calories to produce internal heat!"),
    ("Solu", "Now let's talk about the concept of 'Movement Snacks' throughout the workday!"),
    ("Tonu", "Movement snacks! I love that name! What is a movement snack, Solu?"),
    ("Solu", "Sitting continuously in a desk chair for eight hours is biologically unnatural. A movement snack means taking a two-minute break every hour to do ten squats, five push-ups against your desk, or stretching your hip flexors!"),
    ("Tonu", "Just two minutes of movement resets your blood circulation, clears brain fog, and prevents postural fatigue."),
    ("Solu", "And what about Zone Two cardiovascular training? Many longevity physicians, like Dr. Peter Attia, consider Zone Two cardio the single best predictor of lifespan."),
    ("Tonu", "What exactly is Zone Two cardio, Solu?"),
    ("Solu", "Zone Two is low-intensity, steady-state cardio where you can maintain a conversation without gasping for breath, but you couldn't easily sing a song!"),
    ("Tonu", "Like brisk walking uphill, easy cycling, or gentle rowing. Training in Zone Two trains your mitochondria to burn fat efficiently and clears cellular lactate."),
    ("Solu", "And what about the crucial role of hydration and electrolytes? Many people drink water all day but still feel tired and suffer from headaches!"),
    ("Tonu", "Because drinking gallons of plain distilled water can actually flush essential electrolytes out of your system! We need a balance of sodium, potassium, and magnesium to conduct electrical nerve impulses in our brain and heart."),
    ("Solu", "Adding a tiny pinch of natural mineral sea salt and fresh lemon to your morning water makes a noticeable difference in energy levels."),'''

target_12 = '    ("Tonu", "Now, let\'s explore our special English vocabulary section! Let\'s examine seven very common everyday English expressions and idioms related to health, fitness, and vitality."),'
code = code.replace(target_12, ep12_add + "\n" + target_12)

ep13_add = '''    ("Solu", "Let's also dive into the transformative power of Time Blocking and Calendar Audits!"),
    ("Tonu", "Oh, time blocking is an absolute superpower for anyone trying to manage a busy life! How does time blocking differ from a standard to-do list?"),
    ("Solu", "A to-do list is simply an unorganized wish list of tasks with no relationship to the hours available in the day. You look at twenty tasks and feel overwhelmed!"),
    ("Tonu", "While time blocking treats your calendar as physical real estate! You assign specific, dedicated blocks of time for your top priorities."),
    ("Solu", "For example: Monday morning from nine to eleven is a dedicated block for English study and writing. No meetings, no phone calls, no email!"),
    ("Tonu", "When a task has a scheduled appointment on your calendar, you protect it and it actually gets done."),
    ("Solu", "And what about the Pareto Principle, the famous eighty-twenty rule?"),
    ("Tonu", "Italian economist Vilfredo Pareto discovered that eighty percent of outcomes come from just twenty percent of inputs!"),
    ("Solu", "In business, eighty percent of revenue comes from twenty percent of clients. In language learning, eighty percent of everyday conversation uses just twenty percent of vocabulary!"),
    ("Tonu", "Identify your high-impact twenty percent and pour your best energy into it, rather than getting bogged down in low-value busywork."),
    ("Solu", "And what about batch processing emails and messages?"),
    ("Tonu", "Constantly leaving your email inbox open and replying to notifications all day causes severe cognitive fragmentation!"),
    ("Solu", "Instead, batch your communications! Check and process emails only twice a day—say, at eleven in the morning and four in the afternoon."),
    ("Tonu", "During the rest of the day, close your email client completely and focus on deep, meaningful work."),
    ("Solu", "And have you heard of the weekly review practice from David Allen's Getting Things Done?"),
    ("Tonu", "The GTD Weekly Review! Spending just thirty minutes every Sunday evening reviewing the past week's accomplishments, decluttering your inbox, and mapping out the top three goals for the week ahead."),
    ("Solu", "When Monday morning arrives, you hit the ground running with absolute clarity, rather than scrambling around trying to figure out what to do!"),'''

target_13 = '    ("Tonu", "Now, let\'s explore our special English vocabulary section! Let\'s examine seven high-impact idioms and expressions related to time, productivity, and getting things done."),'
code = code.replace(target_13, ep13_add + "\n" + target_13)

with open("scripts/generate_episodes_11_12_13.py", "w") as f:
    f.write(code)

