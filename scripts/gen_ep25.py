#!/usr/bin/env python3
import gen_common

def build_ep25():
    turns = [
        # SECTION 1: WARM WELCOME & HOOK
        ("Tonu", "Hey hey, lovely listeners! Welcome back to Daily Speak English, your favorite place to improve your English listening and speaking skills. I'm Tonu!"),
        ("Solu", "And I'm Solu! We are so glad you are joining us today for another deeply meaningful, eye-opening, and practical English conversation."),
        ("Tonu", "Solu, have you ever noticed that two people can graduate with the exact same university degree, earn the exact same salary, yet twenty years later, one person is deeply in debt and constantly stressed, while the other is financially free, peaceful, and thriving?"),
        ("Solu", "Yes! It is one of the most common puzzles in the modern world. People assume that financial success depends on mastering complex mathematics, studying advanced economic charts, or picking winning stocks on Wall Street!"),
        ("Tonu", "But in reality, personal finance is not a hard science like physics or engineering; it is a soft skill! Doing well with money has a little to do with how smart you are, and a LOT to do with how you behave!"),
        ("Solu", "That is the profound central insight of Morgan Housel's bestselling masterpiece, 'The Psychology of Money'! And that brings us right to today's topic: The Psychology of Money, Overcoming Greed and Fear, and Redefining True Wealth."),
        ("Tonu", "Money is a subject that triggers intense human emotions: anxiety, pride, envy, security, excitement, and fear. Almost every family on Earth has whispered about money behind closed doors."),
        ("Solu", "And yet, in school and university, we are taught trigonometry, cell biology, and ancient history, but almost nobody ever teaches us how to manage our emotional relationship with our own paycheck!"),
        ("Tonu", "Which is why so many brilliant doctors, engineers, and lawyers find themselves living paycheck to paycheck despite huge earnings! Technical intelligence without financial emotional intelligence is a recipe for stress."),
        ("Solu", "Today, we want to help you master the psychological mindset behind wealth, break free from the stressful traps of consumerism, and master essential everyday English expressions to talk about money with maturity and confidence."),

        # SECTION 2: WEALTH VERSUS RICHES: WHAT YOU DON'T SEE
        ("Tonu", "Let's begin with the crucial distinction that Morgan Housel draws between being 'Rich' versus being 'Wealthy'! Solu, what is the difference between rich and wealthy?"),
        ("Solu", "This distinction completely blew my mind when I first read it! 'Rich' is your current income and what you display visibly to the outside world. Rich is the shiny luxury sports car, the giant diamond watch, the designer handbag, and the expensive restaurant photos on Instagram."),
        ("Tonu", "In other words, being rich is about outward appearance and spending money! If someone drives a two hundred thousand dollar sports car, the only factual piece of data you know about their finances is that they have two hundred thousand dollars LESS than they had before they bought the car, or they have a massive monthly loan payment!"),
        ("Solu", "Exactly! Whereas 'Wealth' is the exact opposite: Wealth is what you DON'T see! Wealth is the unspent cash in your savings account, the untouched stock portfolio, the emergency fund, and the unpurchased luxury items."),
        ("Tonu", "Wealth is financial options that haven't been cashed in yet. Wealth is the quiet freedom to sleep soundly at night without worrying about how you will pay next month's mortgage if you lose your job."),
        ("Solu", "Housel writes: 'Spending money to show people how much money you have is the fastest way to have less money!'"),
        ("Tonu", "What a powerful, razor-sharp quote! So many people go into crushing debt pretending to be rich, trying to impress strangers on the street who don't even care about them!"),
        ("Solu", "When you see someone driving a Ferrari, you rarely think: 'Wow, the person driving that car is so cool.' Instead, you imagine YOURSELF sitting in that car and thinking how cool you would look! Nobody is thinking about the driver!"),

        # SECTION 3: LIFESTYLE CREEP & THE MOVING GOALPOST
        ("Tonu", "Now let's examine another psychological trap that catches millions of hardworking people: 'Lifestyle Creep' or lifestyle inflation!"),
        ("Solu", "Lifestyle Creep happens when your expenses automatically rise to match every single increase in your income. When you were a university student, you survived happily on fifty dollars a week, eating simple noodles and walking everywhere."),
        ("Tonu", "Then you get your first job earning thirty thousand a year, and you think: 'If only I could earn fifty thousand, all my financial stress would vanish forever!'"),
        ("Solu", "Five years later, you earn fifty thousand, but you move into a pricier apartment, buy a newer car, and eat at fancier restaurants—and you are just as stressed and broke as you were before!"),
        ("Tonu", "And then you earn one hundred thousand, and the cycle repeats! The financial goalpost keeps moving further and further down the field!"),
        ("Solu", "Psychologists call this the 'Hedonic Treadmill'. You run faster and faster, buy more and more expensive things, but your internal happiness level returns to the exact same baseline after a few weeks."),
        ("Tonu", "The only way to step off the Hedonic Treadmill is to deliberately decouple your spending from your ego! When your salary increases, increase your savings rate first before you upgrade your lifestyle."),

        # SECTION 4: THE CONCEPT OF 'ENOUGH' & CONTROLLING GREED
        ("Solu", "Let's talk about the hardest financial skill in the world: getting the goalpost to stop moving. In other words, knowing the meaning of 'Enough'!"),
        ("Tonu", "Knowing when you have enough is the ultimate protection against ruin. There is a heartbreaking story Morgan Housel tells in his book about two men: Rajat Gupta and Bernie Madoff."),
        ("Solu", "Tell our listeners about Rajat Gupta, Tonu. It is such a cautionary tale of greed."),
        ("Tonu", "Rajat Gupta was an orphan in India who rose through sheer brilliance to become the CEO of McKinsey, one of the most prestigious consulting firms on Earth! He retired with a personal fortune of over one hundred million dollars!"),
        ("Solu", "One hundred million dollars! That is enough money for ten generations of a family to live in luxury."),
        ("Tonu", "Yet, when Gupta sat on corporate boards alongside billionaires who had ten times more money than him, he felt insecure! He wanted to be a billionaire too. So he engaged in illegal insider trading, got caught by the FBI, and went to federal prison, destroying his reputation and life!"),
        ("Solu", "He risked what he had and desperately needed—his freedom, dignity, and reputation—for what he didn't need and didn't even care about: an extra digit in his bank balance!"),
        ("Tonu", "There is no reason to risk what is important to you for what is not important to you. If your sense of self-worth depends on having more than your neighbor, you will never be wealthy, no matter how many millions you possess."),

        # SECTION 5: THE TRUE DIVIDEND OF MONEY: FREEDOM OVER TIME
        ("Solu", "So if true wealth is not about flashy sports cars or billionaire status symbols, what IS the highest dividend that money pays, Tonu?"),
        ("Tonu", "The highest dividend that money pays is the ability to control your own time!"),
        ("Solu", "The ability to wake up every single morning and say: 'I can do whatever I want today with whom I want, for as long as I want.'"),
        ("Tonu", "Decades of happiness research confirm that having a feeling of autonomy—feeling in control of your daily calendar—is a far more reliable predictor of life satisfaction than how much money you earn or the square footage of your home!"),
        ("Solu", "When you have saved several years of living expenses, you have what investors call 'Walk-Away Money' or freedom money."),
        ("Tonu", "Walk-Away Money changes your entire life posture! If your boss treats you disrespectfully, you can walk away. If you get sick, you can take six months off to heal without worrying about paying rent. If a fascinating startup opportunity arises, you can take a lower salary to pursue your passion."),
        ("Solu", "Money used to buy things produces temporary dopamine, but money used to buy freedom produces permanent peace of mind."),

        # SECTION 6: SAVING FOR AN UNPREDICTABLE RAINY DAY
        ("Tonu", "Now, let's talk about saving money. Many financial advisors tell people: 'You must save money for a specific goal—like buying a house, saving for a wedding, or purchasing a car.'"),
        ("Solu", "And Morgan Housel completely challenges that conventional advice! He says: 'You should save money just to save money! You do not need a specific reason to save!'"),
        ("Tonu", "Why is saving without a specific goal so brilliant, Solu?"),
        ("Solu", "Because life is inherently unpredictable! The future is guaranteed to throw curveballs at you that you could never anticipate on a spreadsheet: a sudden global pandemic, an unexpected medical emergency, a roof that collapses in a storm, or a sudden layoff!"),
        ("Tonu", "When you save money just to save money, you are purchasing financial shock absorbers. You are buying a cushion against the random surprises of life."),
        ("Solu", "And it gives you the flexibility to seize unexpected positive opportunities! If a once-in-a-lifetime business opportunity presents itself during a market crash, people with cash savings can invest when everyone else is panicking."),

        # SECTION 7: COMPOUND INTEREST & PATIENCE
        ("Tonu", "We cannot talk about wealth without mentioning the eighth wonder of the world: Compound Interest!"),
        ("Solu", "Warren Buffett, the most celebrated investor in history, has a net worth exceeding one hundred billion dollars. But here is the secret that most people overlook: over ninety-nine percent of Warren Buffett's wealth was accumulated AFTER his fiftieth birthday!"),
        ("Tonu", "Ninety-nine percent! His secret was not just picking brilliant companies; his secret was TIME! He started investing when he was just ten years old and kept his money compounding quietly for over eighty years!"),
        ("Solu", "Most people want to get rich quick. They chase volatile cryptocurrency schemes, lottery tickets, and day-trading fads because they lack patience."),
        ("Tonu", "Compounding works like planting an oak tree. For the first five years, you barely see a tiny green sprout. But twenty years later, you have a massive, indestructible tree providing shade for your entire home."),
        ("Solu", "Patience and emotional discipline beat raw financial intelligence every single day."),

        # SECTION 8: CHILDHOOD MONEY SCRIPTS & EMOTIONAL BLUEPRINTS
        ("Solu", "Tonu, have you ever thought about where our emotional beliefs about money actually come from?"),
        ("Tonu", "Financial psychologists have found that most adults are subconsciously acting out 'Money Scripts' that were formed before they were even ten years old!"),
        ("Solu", "Explain what a Money Script is, Tonu. That is so insightful!"),
        ("Tonu", "If you grew up in a household where your parents were constantly shouting and crying over unpaid heating bills, your brain subconsciously associates money with panic, fear, and scarcity!"),
        ("Solu", "And as an adult, that person might hoard every single penny out of terrifying anxiety, unable to enjoy a simple dinner at a cafe even when they have millions in the bank!"),
        ("Tonu", "Or, on the other extreme, someone who grew up in scarcity might become a compulsive spender: the moment money enters their bank account, they feel an urgent impulse to spend it immediately before it disappears!"),
        ("Solu", "Examining your childhood money scripts allows you to replace subconscious fear and shame with healthy, intentional financial habits."),

        # SECTION 9: TAILS YOU WIN: THE POWER OF THE PARETO PRINCIPLE
        ("Tonu", "Another brilliant concept Morgan Housel explains is what he calls 'Tails, You Win'!"),
        ("Solu", "What does 'Tails, You Win' mean in simple English, Tonu?"),
        ("Tonu", "It means that in business, investing, and life, a tiny fraction of events—the extreme 'tail events'—account for almost all the major positive results!"),
        ("Solu", "Think about a massive company like Amazon or Apple! Amazon has launched dozens of failed products and experiments over twenty-five years that lost millions of dollars."),
        ("Tonu", "Yes! Does anyone remember the Amazon Fire Phone? It was a colossal, embarrassing failure!"),
        ("Solu", "Yet, one single tail event—Amazon Web Services, their cloud computing division—succeeded so astronomically that it made all the other dozens of failures completely irrelevant!"),
        ("Tonu", "And the same applies to your personal career! You can go on fifty job interviews that end in rejection, but you only need ONE brilliant job offer to change the trajectory of your entire life!"),
        ("Solu", "You don't need to be right all the time; you just need to survive your mistakes and stay in the game long enough for your tail events to compound!"),

        # SECTION 10: EXPERIENCES VS MATERIAL GOODS & GENEROSITY
        ("Tonu", "Now let's examine how we actually spend money to maximize human happiness: Buying Material Possessions versus Buying Experiences!"),
        ("Solu", "Psychological research from Cornell University shows that buying a brand-new material object—like a new television, a designer jacket, or a new sofa—provides a quick burst of excitement that rapidly fades away within a couple of weeks!"),
        ("Tonu", "Why does that happen, Solu?"),
        ("Solu", "Because the physical object just sits there in your living room. Your brain gets used to it, and it becomes the new invisible background normal."),
        ("Tonu", "Whereas shared experiences—like taking a train trip through the mountains with your best friend, attending a live music festival, or learning to cook Italian pasta in Florence—actually GROW more valuable in your memory over time!"),
        ("Solu", "Years later, you and your friend will laugh and reminisce about that trip over dinner with deep warmth! Experiences become an inseparable part of your personal identity and storytelling."),
        ("Tonu", "A new luxury sports jacket will eventually wear out, tear, or go out of fashion, but the memory of seeing the northern lights in Norway with your loved ones stays with you until your final breath."),
        ("Solu", "That is an investment that pays compound dividends in pure joy across your entire lifetime."),
        ("Tonu", "And finally, generosity! Studies show that using a portion of your money to help someone in need, buy a thoughtful meal for a friend, or support a local animal shelter activates the brain's pleasure centers far more intensely than spending that same money on yourself."),

        # SECTION 11: THE SEDUCTION OF PESSIMISM VS REALISTIC OPTIMISM
        ("Solu", "Now let's talk about the news headlines: The Seduction of Pessimism! Why do doom-and-gloom financial predictions always sound so much smarter than optimism?"),
        ("Tonu", "Morgan Housel points out that pessimism sounds like someone trying to help you and warn you of danger, while optimism sounds like a naive sales pitch!"),
        ("Solu", "If someone stands up and shouts: 'The stock market is going to crash next week and the global economy is heading for disaster!', everyone listens with wide eyes and terror!"),
        ("Tonu", "Yet, if someone calmly says: 'Over the next thirty years, human beings will solve medical problems, invent cleaner energy, increase productivity, and grow wealth,' people shrug and think: 'Oh, you are just an unrealistic dreamer!'"),
        ("Solu", "And yet, throughout all of modern history, it is the patient optimists who have created businesses, invested steadily, and built lasting generational wealth!"),
        ("Tonu", "Realistic optimism doesn't mean believing that bad things will never happen. It means knowing that problems and market crashes are temporary setbacks on an upward, compounding human journey."),

        # SECTION 12: ROOM FOR ERROR & THE MARGIN OF SAFETY
        ("Solu", "And that brings us to the final golden rule: Always give yourself a massive 'Margin of Safety'!"),
        ("Tonu", "What is a margin of safety, Solu?"),
        ("Solu", "A margin of safety means designing your financial plan so that you don't need the world to be perfect for you to survive and succeed!"),
        ("Tonu", "If your budget only works if you never get sick, your car never breaks down, and your investments always return ten percent every single year, your plan is built on glass!"),
        ("Solu", "Leave plenty of breathing room. Prepare for the reality that the future will surprise you. A healthy margin of safety lets you sleep peacefully at night no matter what storm is brewing outside."),

        # SECTION 13: VOCABULARY & IDIOM SPOTLIGHT (6 KEY IDIOMS)
        ("Tonu", "Now, let's step into our signature segment: Key Everyday English Vocabulary and Idioms! Today, we have selected six colorful, essential expressions related to money, saving, and financial psychology."),
        ("Solu", "Let's master them together! Tonu, what is our very first financial expression for today?"),
        ("Tonu", "Our first expression is 'nest egg'. A 'nest egg' is a substantial sum of money that someone has saved, invested, or put aside over many years for the future or for retirement."),
        ("Solu", "Let's listen to a natural conversational example: 'By saving twenty percent of her paycheck each month, Clara built a comfortable nest egg that allowed her to retire at age fifty-five.'"),
        ("Tonu", "That is an inspiring example. What is our second expression, Solu?"),
        ("Solu", "Our second expression is 'tighten one's belt'. To 'tighten your belt' means to reduce your spending, cut down on unnecessary expenses, and live more frugally, especially during tough financial times."),
        ("Tonu", "Here is how you can use it in conversation: 'After my company announced budget cuts, we decided to tighten our belts by canceling unused subscriptions and cooking all our meals at home.'"),
        ("Solu", "Very practical! Tonu, what is our third expression?"),
        ("Tonu", "Our third expression is 'live beyond one's means'. To 'live beyond your means' means to spend more money than you earn, relying on credit cards, loans, and debt to fund a luxurious lifestyle."),
        ("Solu", "For example: 'He was earning a decent salary, but by leasing luxury sports cars and buying designer suits, he was constantly living beyond his means and sinking deeper into debt.'"),
        ("Tonu", "A very common cautionary tale! What is our fourth expression, Solu?"),
        ("Solu", "Our fourth expression is 'make ends meet'. To 'make ends meet' means to earn just enough money to pay for basic necessities like rent, food, and utilities, with nothing left over."),
        ("Tonu", "Let's hear an example: 'When I was starting my small graphic design business, I had to work night shifts as a barista just to make ends meet.'"),
        ("Solu", "So relatable for many entrepreneurs. Tonu, introduce our fifth expression."),
        ("Tonu", "Our fifth expression is 'rainy day fund'. A 'rainy day fund' is an emergency savings account reserved specifically for unexpected financial crises, medical bills, or urgent household repairs."),
        ("Solu", "Here is a great sentence: 'Having three months of living expenses tucked away in a rainy day fund gave him total peace of mind when his car broke down.'"),
        ("Tonu", "And what is our sixth and final expression for today, Solu?"),
        ("Solu", "Our sixth expression is 'foot the bill'. To 'foot the bill' means to pay for the full cost of something, especially for an expensive dinner, event, or repair."),
        ("Tonu", "For example: 'My generous grandfather insisted on footing the bill for our entire family reunion dinner last weekend.'"),

        # SECTION 9: INTERACTIVE SPEAKING PRACTICE
        ("Solu", "Now, it is time for our Interactive Speaking Challenge! This is your turn to speak English out loud with us. Stand tall, relax your jaw, and repeat each sentence with natural emotion and steady rhythm!"),
        ("Tonu", "Sentence number one: 'True wealth is not about what you spend, but the freedom and peace of mind you build.' Your turn!"),
        ("Solu", "Say it out loud with warmth and clarity: 'True wealth is not about what you spend, but the freedom and peace of mind you build.'"),
        ("Tonu", "Great cadence! Sentence number two: 'Having a solid rainy day fund protects you from life's unexpected emergencies.' Your turn!"),
        ("Solu", "Repeat with steady confidence: 'Having a solid rainy day fund protects you from life's unexpected emergencies.'"),
        ("Tonu", "Wonderful! Sentence number three: 'It is so easy to fall into the trap of living beyond your means to impress strangers.' Your turn!"),
        ("Solu", "Speak it clearly: 'It is so easy to fall into the trap of living beyond your means to impress strangers.'"),
        ("Tonu", "Sentence number four: 'Controlling your own daily time is the highest dividend that money can ever pay.' Your turn!"),
        ("Solu", "Let's say sentence number four together: 'Controlling your own daily time is the highest dividend that money can ever pay.'"),
        ("Tonu", "Outstanding work! Your pronunciation and spoken confidence are shining brighter with every lesson."),

        # SECTION 10: REFLECTION & FAREWELL
        ("Solu", "And now, it is time for today's Weekly Reflection Question! We want you to practice writing in English down in the comment section below."),
        ("Tonu", "Here is today's question: 'If money were not a limiting factor in your life right now, how would you spend an average Tuesday? What does true financial freedom mean to you personally?'"),
        ("Solu", "Would you spend your days painting, traveling with loved ones, writing books, gardening, or volunteering for a cause you believe in? Let us know your dream day in the comments!"),
        ("Tonu", "Solu and I read through every single comment, and we love replying to your thoughts and cheering you on."),
        ("Solu", "Remember, wealth is built one wise decision at a time, just like English fluency is built one sentence at a time."),
        ("Tonu", "Celebrate your daily progress, be kind to yourself, and take wonderful care of your wellbeing."),
        ("Solu", "Until next time, goodbye from Solu!"),
        ("Tonu", "And goodbye from Tonu!"),
        ("Both", "Happy learning, live wisely, and goodbye!")
    ]
    return turns

if __name__ == "__main__":
    t = build_ep25()
    gen_common.verify_and_save(25, "scripts/daily_speak_ep25_full.txt",
                              "The Psychology of Money: Greed, Fear & True Wealth",
                              "Daily Speak English | English Listening & Speaking Practice",
                              t)
