#!/usr/bin/env python3
import gen_common

def build_ep27():
    turns = [
        # SECTION 1: WARM WELCOME & HOOK
        ("Tonu", "Hey hey, lovely listeners! Welcome back to Daily Speak English, your favorite place to improve your English listening and speaking skills. I'm Tonu!"),
        ("Solu", "And I'm Solu! We are so delighted to welcome you back for another warm, creative, and inspiring English practice conversation."),
        ("Tonu", "Solu, look at my fingertips right now! What do you notice?"),
        ("Solu", "Let me see... Tonu, are those streaks of dried blue and green paint on your knuckles?"),
        ("Tonu", "Yes! Blue and green acrylic paint! I spent all of yesterday afternoon painting a wooden bookshelf in my living room, and I had clay dust all over my apron!"),
        ("Solu", "That is such a glorious sight! There is something deeply grounding about having real, physical materials on your hands."),
        ("Tonu", "It truly is. And that brings us directly to today's soul-nourishing topic: The Joy of Hobbies, Crafts, and Making Things with Your Own Two Hands!"),
        ("Solu", "Think about the modern workday for a moment: most people spend eight to ten hours tapping on glass smartphones, clicking plastic computer mice, and typing on keyboards."),
        ("Tonu", "Everything we produce in the digital knowledge economy is invisible! Lines of code, email threads, spreadsheet cells, slide presentations—at the end of the day, you close your laptop screen and there is nothing physical you can hold, smell, or touch."),
        ("Solu", "And that creates a deep, subconscious hunger in the human spirit. Human beings evolved over hundreds of thousands of years using their hands to weave baskets, shape clay pots, carve wood, bake bread, and cultivate soil."),
        ("Tonu", "When we reconnect with hands-on crafts—whether it is pottery, knitting, gardening, woodworking, or painting—something magical happens to our mental health."),
        ("Solu", "Today, we want to celebrate the revival of hands-on creativity, rescue hobbies from the toxic pressure of hustle culture, and teach you rich, colorful everyday English vocabulary to talk about arts, crafts, and creativity with effortless fluency!"),
        ("Tonu", "Because taking time to create with your hands is one of the kindest gifts you can give to your tired mind after a busy week of mental work."),
        ("Solu", "It restores your spirit, grounds your attention, and brings back the simple pleasure of human play."),

        # SECTION 2: THE TRAP OF MONETIZING EVERY HOBBY (HUSTLE CULTURE)
        ("Tonu", "Let's begin by tackling a massive modern plague: The toxic pressure to monetize every single hobby!"),
        ("Solu", "Oh, this makes my blood boil, Tonu! Have you noticed that whenever someone starts baking lovely sourdough bread or knitting colorful scarves, the very first question people ask is: 'Are you going to open an Etsy shop? Can you sell these online?'"),
        ("Tonu", "Yes! Or: 'You should turn this into a side hustle! You could start an Instagram page and sell your pottery for fifty dollars a cup!'"),
        ("Solu", "Why does every human activity have to be converted into capitalistic profit? Hustle culture has convinced people that doing something purely for fun, play, or relaxation is a waste of productive time!"),
        ("Tonu", "And the tragic irony is: the moment you turn your beloved, peaceful weekend hobby into a commercial business, you ruin the very peace it gave you!"),
        ("Solu", "Suddenly, you have client deadlines, shipping delays, packaging expenses, customer complaints, and profit margins! Your joyful creative refuge becomes another stressful second job!"),
        ("Tonu", "We need to reclaim the sacred right to have hobbies that produce ZERO money! You are allowed to paint water-color landscapes that never leave your living room!"),
        ("Solu", "You are allowed to play the acoustic guitar even if you only know four chords and will never perform on a concert stage!"),
        ("Tonu", "And best of all: You are allowed to be completely MEDIOCRE at your hobby! The goal of a craft is not perfection or commercial validation; the goal is the joy of the process itself!"),
        ("Solu", "Children understand this intuitively! When a five-year-old child takes a box of colorful crayons and draws a purple flying dog on paper, they don't stop and wonder: 'Is this drawing good enough to sell in an art gallery?'"),
        ("Tonu", "Haha! Never! They giggle with total delight, proud of their imaginative creation!"),
        ("Solu", "Somewhere along the way to adulthood, we developed this neurotic fear of looking foolish or unpolished, and it paralyzed our creative instincts."),
        ("Tonu", "Reconnecting with a hands-on hobby is how we invite that joyful, fearless inner child back into our daily lives!"),

        # SECTION 3: MIHALY CSIKSZENTMIHALYI & THE FLOW STATE
        ("Solu", "Now let's explore the neuroscience behind crafts: The concept of 'Flow' discovered by psychologist Mihaly Csikszentmihalyi!"),
        ("Tonu", "Flow is that magical psychological state where you become so utterly absorbed in an activity that time seems to dissolve completely!"),
        ("Solu", "Have you ever sat down to knit a sweater, carve a piece of cedar wood, or arrange flowers in a vase, and suddenly you look at the clock and realize that four hours have passed in what felt like twenty minutes?"),
        ("Tonu", "That is the Flow state! In Flow, the prefrontal cortex—the part of the brain that houses your inner critic, your worries about tomorrow's bills, and your past regrets—temporarily quiets down!"),
        ("Solu", "Psychologists call this 'transient hypofrontality'. The chatter of self-doubt vanishes, and your entire consciousness merges seamlessly with the needle, the clay, or the paintbrush."),
        ("Tonu", "It is an active form of meditation. Many people struggle to sit on a cushion with their eyes closed for thirty minutes because their mind races with anxious thoughts."),
        ("Solu", "But give that same person a spinning pottery wheel, a ball of soft yarn, or a batch of sourdough dough to knead, and their nervous system settles into serene tranquility naturally."),

        # SECTION 4: THE TACTILE SENSE & DIGITAL DETOX
        ("Tonu", "Let's talk about the incredible sensory richness of physical crafts! What are some of your favorite hands-on hobbies, Solu?"),
        ("Solu", "I have fallen deeply in love with traditional bread baking! Mixing flour, spring water, salt, and living wild yeast with my bare hands; kneading the dough until it feels smooth and elastic like a baby's cheek; letting it ferment overnight; and baking it in a scorching Dutch oven until the crust crackles and sings!"),
        ("Tonu", "Oh Solu, that sounds like pure poetry! The aroma of freshly baked sourdough filling the entire house is one of the greatest pleasures known to humankind!"),
        ("Solu", "And what about you, Tonu? What crafts light up your heart?"),
        ("Tonu", "I love pottery and ceramics! Sitting at a potter's wheel, feeling the cool, wet, silky earth spinning between your palms, and centering the clay requires your full, undivided physical presence."),
        ("Solu", "If your mind wanders to your email inbox for even five seconds, the clay wobbles off-center and collapses!"),
        ("Tonu", "Exactly! The material demands your honesty and presence. It teaches you patience, humility, and tactile sensitivity."),
        ("Solu", "And what about gardening? Putting seeds into dark compost, watering them faithfully, and watching tiny green sprouts push up through the soil toward the sunlight."),
        ("Tonu", "Gardening reconnects you with the slow, ancient rhythms of the natural seasons. In a digital world where everything happens in milliseconds, a tomato plant takes ninety days to bear fruit, reminding us that the most beautiful things in life cannot be rushed."),
        ("Solu", "And what about learning to play an acoustic musical instrument, like the guitar, piano, or violin?"),
        ("Tonu", "Oh, playing an instrument is such an exquisite tactile craft! When you press your fingertips onto nickel guitar strings or wooden piano keys, you are not pressing a digital button that triggers an electronic sound sample!"),
        ("Solu", "You are physically causing a steel string to vibrate across a hollow wooden soundbox! When you strum an acoustic guitar, you can feel the sound vibrations resonating against your very chest and ribs."),
        ("Tonu", "It creates a physical intimacy with sound that streaming music on Spotify through plastic earbuds can never replicate."),
        ("Solu", "And your fingers develop calluses! Those calluses are the honorable badges of dedication and practice."),

        # SECTION 5: WABI-SABI & THE BEAUTY OF IMPERFECTION
        ("Solu", "Now let's explore a timeless Japanese aesthetic philosophy that every craftsperson cherishes: 'Wabi-Sabi' and 'Kintsugi'!"),
        ("Tonu", "What is Wabi-Sabi, Solu? It is such a poetic world concept!"),
        ("Solu", "Wabi-Sabi is the Japanese art of finding beauty in imperfection, impermanence, and simplicity!"),
        ("Tonu", "When a machine in a mega-factory stamps out one million plastic bowls, every single bowl is mathematically identical, sterile, and cold."),
        ("Solu", "But when a human potter throws a ceramic bowl on a wheel, there are subtle fingerprints left in the glaze, a gentle asymmetry in the rim, and unique variations in the kiln firing!"),
        ("Tonu", "Those imperfections are not mistakes; they are the soul of the maker! They prove that a living human being poured their care and heartbeat into that object."),
        ("Solu", "And look at 'Kintsugi'—the Japanese practice of repairing broken pottery with golden lacquer!"),
        ("Tonu", "Instead of throwing a cracked ceramic cup into the trash or trying to hide the crack with invisible glue, Kintsugi highlights the repair with pure gold!"),
        ("Solu", "It celebrates the object's history and fractures as a badge of honor, making the repaired bowl far more beautiful and valuable than it was when brand new."),
        ("Tonu", "What a magnificent metaphor for human life! Our scars, struggles, and imperfections are where our unique character and resilience shine brightest."),

        # SECTION 6: THE MAKER MINDSET: REPAIRING VS CONSUMING
        ("Solu", "Let's also talk about how crafts transform our relationship with consumer culture. What is the 'Maker Mindset', Tonu?"),
        ("Tonu", "In our throwaway society, when a toaster stops working or a jacket loses a button, people's default reaction is to throw it into a landfill and order a replacement on Amazon with one click!"),
        ("Solu", "We have become passive, helpless consumers who don't know how any of the objects in our daily lives actually work!"),
        ("Tonu", "The Maker Mindset changes that completely! When you learn basic woodworking, sewing, or bicycle repair, you realize: 'I can fix this! I can mend this torn seam with colorful thread; I can sand down this scratched tabletop and give it new life!'"),
        ("Solu", "It gives you an immense feeling of self-efficacy and independence. You stop being a passive spectator and become an active creator."),
        ("Tonu", "And making handmade gifts for friends and family! Giving someone a hand-knitted woolen scarf, a jar of homemade blackberry jam, or a hand-carved wooden pen communicates love in a way that buying a generic gift card never could."),

        # SECTION 7: ANALOG RENAISSANCE: 35MM FILM & VINYL RECORDS
        ("Solu", "Have you noticed the incredible revival of analog technologies among young people? Film cameras and vinyl records are booming!"),
        ("Tonu", "Yes! It is what cultural commentators call the 'Analog Renaissance'! With smartphones, you can take five thousand digital photos in an afternoon without thinking, and they just sit forgotten in the cloud."),
        ("Solu", "Whereas on a 35mm film camera, you only have twenty-four or thirty-six exposures on the entire roll! Each frame costs real money to develop."),
        ("Tonu", "So you slow down. You check the golden hour lighting, you frame the composition carefully, you hold your breath, and you click the mechanical shutter with deep reverence."),
        ("Solu", "And then you wait a week for the photo lab to develop the negatives! That delayed anticipation makes the physical printed photographs infinitely more precious."),
        ("Tonu", "And vinyl records! Taking the heavy black disc out of its cardboard sleeve, gently setting the needle into the groove, and listening to an entire album from track one to track ten without skipping or shuffling."),
        ("Solu", "It restores the album as a cohesive work of art, rather than disposable sonic wallpaper."),

        # SECTION 8: COOKING AS EVERYDAY CRAFT & SENSORY FEAST
        ("Solu", "Let's also celebrate the most universal, accessible craft of all: Cooking!"),
        ("Tonu", "Cooking is pure chemistry, art, and love combined! Slicing crisp onions, hearing garlic sizzle in extra virgin olive oil, kneading fresh pasta dough with eggs and semolina flour!"),
        ("Solu", "When you cook from scratch, you feed not only your physical body, but your soul and your family."),
        ("Tonu", "It engages all five senses simultaneously: the sound of a simmering soup, the aroma of toasted rosemary, the colors of vibrant peppers, the texture of sourdough crust, and the explosion of flavor on your tongue."),

        # SECTION 9: REPAIR CAFES & COMMUNITY MAKERSPACES
        ("Solu", "What about community gathering around crafts? Have you heard of 'Repair Cafes', Tonu?"),
        ("Tonu", "Oh, Repair Cafes are such an inspiring grassroots movement! On Saturday mornings in community centers and church halls across Europe and the Americas, skilled volunteer retirees and neighbors bring their toolboxes!"),
        ("Solu", "People bring their broken radios, cracked vintage lamps, jammed sewing machines, and wobbly wooden chairs!"),
        ("Tonu", "And instead of throwing them away, the volunteers teach you how to repair them side-by-side while sharing tea and coffee! It fights landfill waste, bridges generational divides, and rebuilds neighborhood solidarity."),

        # SECTION 10: CRAFTING FOR TRAUMA RECOVERY & MENTAL HEALTH
        ("Solu", "There is also compelling clinical research on the neurological healing power of crafts like knitting, embroidery, and woodcarving."),
        ("Tonu", "Psychiatrists have noted that the repetitive, rhythmic bilateral hand movements of knitting stimulate both brain hemispheres in a way that mimics EMDR therapy!"),
        ("Solu", "It helps the brain soothe anxiety, process grief, and calm post-traumatic stress. When soldiers and veterans engage in woodworking or ceramics, their nervous systems find profound relief."),

        # SECTION 11: UPCYCLING, SASHIKO & THRIFT RESTORATION
        ("Tonu", "Another exciting modern craft trend is 'Upcycling' and visible mending!"),
        ("Solu", "Tell our listeners about visible mending, Tonu!"),
        ("Tonu", "In Japan, there is a traditional embroidery technique called 'Sashiko'. Instead of trying to invisibly hide a tear in your favorite denim jacket or wool sweater, you use bright contrasting thread to stitch beautiful geometric patterns right over the patch!"),
        ("Solu", "It turns a tear into a piece of wearable art! And what about furniture flipping? Going to a local thrift shop, buying a scratched wooden nightstand for fifteen dollars, sanding it down, and painting it a rich forest green with vintage brass handles."),
        ("Tonu", "You take something discarded and unloved, and through your own physical effort and creativity, you turn it into a statement piece that will last for another thirty years."),

        # SECTION 12: CALLIGRAPHY, FOUNTAIN PENS & CREATIVE JOURNALING
        ("Solu", "Let's also mention the tactile bliss of Calligraphy, fountain pens, and handwritten journaling!"),
        ("Tonu", "Oh, the feeling of a heavy fountain pen nib gliding across thick, creamy cotton paper with rich sepia ink!"),
        ("Solu", "When you write by hand, brain imaging studies show that multiple sensory and motor regions synchronize. You retain ideas better, process emotions more deeply, and write with more thoughtful care than when rapidly clacking on a plastic keyboard."),
        ("Tonu", "Keeping a visual diary or bullet journal with small sketches, pressed wildflowers, and handwritten reflections is a priceless treasure you will cherish decades from now."),

        # SECTION 13: HOW TO START A CRAFT ON A BUDGET
        ("Solu", "How can someone listening right now start a hands-on hobby if they don't have a lot of money or a giant garage workshop?"),
        ("Tonu", "Start small with accessible, low-cost crafts! You don't need a five-thousand-dollar woodworking lathe to be creative."),
        ("Solu", "Pick up a simple sketchpad and two graphite pencils for five dollars! Or buy a skein of yarn and a pair of wooden knitting needles."),
        ("Tonu", "Or try origami—the Japanese art of paper folding! All you need is square sheets of colored paper and curiosity."),
        ("Solu", "Schedule a two-hour 'Screen-Free Craft Date' with yourself every Sunday afternoon. Put your phone in another room, brew a pot of herbal tea, put on acoustic instrumental music, and let your hands play!"),

        # SECTION 8: VOCABULARY & IDIOM SPOTLIGHT (6 KEY IDIOMS)
        ("Tonu", "Now, let's step into our signature segment: Key Everyday English Vocabulary and Idioms! Today, we have selected six colorful, essential expressions inspired by crafts, creativity, and hands-on making."),
        ("Solu", "Let's explore them together! Tonu, what is our very first craft expression for today?"),
        ("Tonu", "Our first expression is 'hands-on experience'. 'Hands-on experience' is knowledge, skill, or wisdom gained through direct practical doing and physical participation, rather than just reading theory in textbooks."),
        ("Solu", "Let's listen to a natural example sentence: 'She had read dozens of books about gardening, but getting hands-on experience in her grandmother's vegetable patch taught her how plants really grow.'"),
        ("Tonu", "That captures it perfectly. What is our second expression, Solu?"),
        ("Solu", "Our second expression is 'start from scratch'. To 'start from scratch' means to begin a project completely from the very beginning, using only raw basic materials without any pre-made components or shortcuts."),
        ("Tonu", "Here is an everyday example: 'Instead of using boxed cake mix, David baked the entire chocolate birthday cake starting from scratch with fresh butter, eggs, and cocoa.'"),
        ("Solu", "Delicious! Tonu, introduce our third expression."),
        ("Tonu", "Our third expression is 'a labour of love'. A 'labour of love' is a difficult, time-consuming piece of work or creative project undertaken purely out of passion, devotion, and personal pleasure, rather than for monetary profit."),
        ("Solu", "Let's hear an example: 'Restoring that vintage 1968 wooden sailboat took grandfather five years of weekend work, but it was an absolute labour of love.'"),
        ("Tonu", "What a lovely sentiment. What is our fourth expression, Solu?"),
        ("Solu", "Our fourth expression describes supreme creative focus: 'in the zone'. When someone is 'in the zone', it means they are in a state of peak concentration, effortless absorption, and peak creative performance."),
        ("Tonu", "For example: 'Once Clara sat down at the piano with her sketchbook, she was completely in the zone and composed three new melodies before sunset.'"),
        ("Solu", "Inspiring! Tonu, take us to our fifth expression."),
        ("Tonu", "Our fifth expression is 'rough around the edges'. When an object, project, or person is 'rough around the edges', it means it has authentic charm and solid quality, but lacks polished refinement or smooth perfection."),
        ("Solu", "Here is how you can use it: 'My first handmade ceramic coffee mug was a little rough around the edges and slightly lopsided, but it is still my favorite cup to drink from every morning.'"),
        ("Tonu", "And what is our sixth and final expression for today, Solu?"),
        ("Solu", "Our sixth expression is 'leave one's mark'. To 'leave your mark' means to create something memorable, lasting, and meaningful that has a positive, enduring impact on others or the world."),
        ("Tonu", "Let's hear an example: 'Through his hand-built wooden furniture and community workshops, the master carpenter truly left his mark on our entire town.'"),

        # SECTION 9: INTERACTIVE SPEAKING PRACTICE
        ("Solu", "Now, it is time for our Interactive Speaking Challenge! This is your opportunity to speak English out loud with us. Stand tall, relax your shoulders, and repeat each phrase with natural rhythm and expressive warmth!"),
        ("Tonu", "Sentence number one: 'Making things with my own hands gives me a deep sense of peace and accomplishment.' Your turn!"),
        ("Solu", "Say it out loud with clear pronunciation: 'Making things with my own hands gives me a deep sense of peace and accomplishment.'"),
        ("Tonu", "Great cadence! Sentence number two: 'Restoring that antique wooden table was an absolute labour of love.' Your turn!"),
        ("Solu", "Repeat with steady confidence: 'Restoring that antique wooden table was an absolute labour of love.'"),
        ("Tonu", "Wonderful! Sentence number three: 'Whenever I work on my pottery, I enter the zone and lose track of time.' Your turn!"),
        ("Solu", "Speak it clearly: 'Whenever I work on my pottery, I enter the zone and lose track of time.'"),
        ("Tonu", "Sentence number four: 'It is so freeing to pursue a creative hobby purely for the joy of making, without worrying about profit.' Your turn!"),
        ("Solu", "Let's say sentence number four together: 'It is so freeing to pursue a creative hobby purely for the joy of making, without worrying about profit.'"),
        ("Tonu", "Outstanding work! Your spoken English is sounding more expressive, fluent, and confident every single day."),

        # SECTION 10: REFLECTION & FAREWELL
        ("Solu", "And now, it is time for today's Weekly Reflection Question! We want you to practice writing in English down in the comment section below."),
        ("Tonu", "Here is today's question: 'What is your favorite hands-on hobby, craft, or creative activity? What physical thing do you love creating, fixing, or tending to with your hands, and how does it make you feel?'"),
        ("Solu", "Do you love cooking, knitting, sketching, gardening, carpentry, or playing an instrument? Tell us all about your creative outlet in English in the comments!"),
        ("Tonu", "Solu and I read every single comment, and reading about your passions brings so much joy to our community."),
        ("Solu", "Remember that creativity is your birthright. You don't need anyone's permission to make things, play, and express your soul."),
        ("Tonu", "Keep practicing your English every single day with curiosity and joy. Take wonderful care of yourself, and have a beautiful, creative day!"),
        ("Solu", "Until next time, goodbye from Solu!"),
        ("Tonu", "And goodbye from Tonu!"),
        ("Both", "Happy learning, keep creating, and goodbye!")
    ]
    return turns

if __name__ == "__main__":
    t = build_ep27()
    gen_common.verify_and_save(27, "scripts/daily_speak_ep27_full.txt",
                              "Hobbies, Crafts & The Joy of Making Things",
                              "Daily Speak English | English Listening & Speaking Practice",
                              t)
