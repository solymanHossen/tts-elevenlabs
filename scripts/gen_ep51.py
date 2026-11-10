#!/usr/bin/env python3
"""
Daily Speak English - Episode 51
Title: Overcoming Perfectionism: The 80% Rule & Good Enough
Requirements:
- Starts with Tonu: "Hey hey, lovely listeners!..."
- Words >= 3,550 (strict duration >= 25.5 - 28.0 mins)
- High-level engaging, natural conversational English
"""

import gen_common

def build_ep51():
    turns = [
        # SECTION 1: MAGNETIC OPENING
        ("Tonu", "Hey hey, lovely listeners! Welcome back to Daily Speak English, your favorite place to become fluent, confident, and unstoppable in English! I'm Tonu!"),
        ("Solu", "And I'm Solu! Welcome back, everyone! Today, we are taking an axe to a gilded, beautiful cage that traps the most talented, conscientious, and ambitious minds on Earth: 'Perfectionism', the paralyzing terror of making mistakes, and the liberating psychology of the '80% Good Enough Rule'!"),
        ("Tonu", "Solu, think about how perfectionism disguises itself! In job interviews, when someone asks: 'What is your greatest weakness?', people proudly smile and say: 'Oh, I'm just such a perfectionist! I care too much! I have impossibly high standards!'"),
        ("Solu", "Yes! People wear perfectionism like a badge of moral nobility! They think perfectionism means excellence, high craftsmanship, and stellar ambition!"),
        ("Tonu", "But modern psychology has proven that perfectionism is NOT the pursuit of excellence at all! Perfectionism is the ultimate manifestation of FEAR!"),
        ("Solu", "It is the fear of being judged, the fear of being criticized, the fear of looking awkward, and the terror of not being worthy!"),
        ("Tonu", "And what is the real-world result of perfectionism? Paralysis! You never publish your book because chapter three isn't perfect; you never launch your business because the website isn't perfect; and you never speak English in public because your grammar isn't one hundred percent flawless!"),
        ("Solu", "Today, we are going to explore Dr. Brené Brown's research on shame, analyze Anne Lamott's liberating concept of the 'Ugly First Draft', discover the Silicon Valley philosophy that 'Done is better than perfect', share Japanese Wabi-Sabi aesthetics, and master fluent English expressions!"),
        ("Tonu", "As author Elizabeth Gilbert wrote: 'Perfectionism is just fear in really good shoes and a mink coat!' Today, we are taking off those uncomfortable shoes and choosing freedom!"),

        # SECTION 2: BRENÉ BROWN: PERFECTIONISM VS HEALTHY STRIVING
        ("Solu", "Let's begin by examining the groundbreaking sociological research of Dr. Brené Brown at the University of Houston!"),
        ("Tonu", "Dr. Brown spent two decades studying vulnerability, shame, and empathy. What is the fundamental difference she discovered between 'Healthy Striving' and 'Perfectionism', Solu?"),
        ("Solu", "Healthy striving is internally focused! It asks: 'How can I grow? How can I master my craft? What can I learn from this mistake?'"),
        ("Tonu", "Perfectionism, on the other hand, is completely EXTERNALLY focused! It asks: 'What will they think of me? How do I look? How can I protect myself from criticism, blame, and ridicule?'"),
        ("Solu", "Perfectionism is a twenty-ton shield that we haul around, believing that if we look perfect, speak perfect, dress perfect, and perform perfect, we can avoid the pain of shame and judgment!"),
        ("Tonu", "And the tragic irony is that that heavy shield prevents us from ever being truly seen, truly authentic, or truly connected with other human beings!"),
        ("Solu", "Healthy striving embraces the messy, imperfect process of growth; perfectionism demands the flawless final product before you even begin."),

        # SECTION 3: THE 80% RULE & THE LAW OF DIMINISHING RETURNS
        ("Tonu", "Let's explore a practical mathematical and psychological principle: 'The 80% Rule' and the Law of Diminishing Returns!"),
        ("Solu", "In economics and engineering, it is universally recognized that achieving the first eighty percent of a project's quality requires twenty percent of the effort and time!"),
        ("Tonu", "That first eighty percent delivers almost ALL the functional value, clarity, and usefulness of the product!"),
        ("Solu", "Now, what does the perfectionist do? The perfectionist spends eighty percent MORE time, sleepless nights, and agony trying to polish that tiny, invisible last twenty percent!"),
        ("Tonu", "They rewrite an email twenty-five times to change three adjectives! They adjust the color shade of a slide background by two percent! They re-record a podcast thirty times because of one breath sound!"),
        ("Solu", "And does the client or audience notice that last two percent? NEVER!"),
        ("Tonu", "All that extra agony produces zero tangible value, while stealing eighty percent of your life, energy, and sanity!"),
        ("Solu", "Adopt the 80% Rule! When a project reaches eighty or eighty-five percent excellence, SHIP IT! Release it into the world, gather real feedback, and move on to your next creation!"),

        # SECTION 4: ANNE LAMOTT: PERMISSION TO MAKE 'SHITTY FIRST DRAFTS'
        ("Solu", "Let's explore one of the most famous pieces of creative advice in literary history: bestselling author Anne Lamott's book 'Bird by Bird'!"),
        ("Tonu", "Lamott dedicated an entire famous chapter to what she called 'Shitty First Drafts'!"),
        ("Solu", "Why is the concept of an ugly first draft so revolutionary for perfectionists, Tonu?"),
        ("Tonu", "Because perfectionists stare at a blank white computer screen, waiting for Pulitzer Prize-winning prose to flow effortlessly from their fingers on the very first try!"),
        ("Solu", "And when their first sentence looks clumsy, they hit the backspace key, delete it, freeze, and say: 'I have no talent! I am a failure!'"),
        ("Tonu", "Anne Lamott explains that almost all great writers—even the literary giants—sit down and write awful, clumsy, embarrassing, incoherent first drafts!"),
        ("Solu", "The first draft is simply you shoveling sand into the sandbox so that you have something to build sandcastles with later!"),
        ("Tonu", "You cannot edit a blank page! You cannot improve something that doesn't exist!"),
        ("Solu", "Give yourself radical permission to write badly, to speak clumsily, and to paint messily on your first try! Excellence is not born in the first draft; excellence is sculpted through patient revision."),

        # SECTION 5: WABI-SABI & KINTSUGI: THE BEAUTY OF THE BROKEN
        ("Tonu", "Let's travel to Japan to study two ancient aesthetic philosophies that completely dismantle perfectionism: 'Wabi-Sabi' and 'Kintsugi'!"),
        ("Solu", "What is Wabi-Sabi, Solu?"),
        ("Solu", "Wabi-Sabi is the traditional Japanese worldview centered on the acceptance of transience and imperfection!"),
        ("Tonu", "In Western design, beauty is often defined as symmetrical, flawless, polished, and eternal: like a sterile marble statue or a scratch-free chrome kitchen."),
        ("Solu", "In Wabi-Sabi, true beauty is found in things that are imperfect, impermanent, and incomplete!"),
        ("Tonu", "A rustic ceramic bowl with an asymmetrical curve, a wooden table weathered by decades of rain, moss growing over an old stone lantern!"),
        ("Solu", "And look at 'Kintsugi'—the ancient Japanese art of repairing broken pottery!"),
        ("Tonu", "When a cherished porcelain bowl falls and shatters on the floor, Westerners throw it in the trash!"),
        ("Solu", "A Japanese Kintsugi master gathers the shattered shards and repairs them using natural lacquer dusted with pure gold, silver, or platinum powder!"),
        ("Tonu", "The golden seams do not hide the cracks; the gold proudly illuminates the fractures! The repaired bowl is considered far more valuable and beautiful than it was before it broke, because its scars tell the sacred story of its resilience!"),
        ("Solu", "Your flaws, your mistakes, your scars, and your awkward moments are your golden Kintsugi seams. Never hide your humanity."),

        # SECTION 6: 'DONE IS BETTER THAN PERFECT': THE SILICON VALLEY CREED
        ("Solu", "Let's look at the philosophy that built the modern digital economy: the Silicon Valley mantra painted in giant red letters across tech headquarters: 'Done is Better Than Perfect'!"),
        ("Tonu", "Why did tech visionaries like Sheryl Sandberg and Reid Hoffman champion this motto?"),
        ("Solu", "LinkedIn founder Reid Hoffman famously said: 'If you are not embarrassed by the first version of your product, you have launched too late!'"),
        ("Tonu", "Think about the very first version of Facebook, Google, or Amazon in the 1990s!"),
        ("Solu", "They looked hideous! They were basic, clunky, text-heavy websites with low-resolution graphics!"),
        ("Tonu", "If Jeff Bezos or Mark Zuckerberg had waited until their software was 'flawless' and 'perfect' before launching, they would still be tweaking code in their dorm rooms, and other entrepreneurs would have conquered the market!"),
        ("Solu", "They launched an imperfect, functional Minimum Viable Product, collected real customer feedback, and improved it iteratively ten thousand times!"),
        ("Tonu", "Action beats contemplation! A completed imperfect project running in the real world is infinitely more powerful than a flawless masterpiece that exists only in your imagination."),

        # SECTION 7: DONALD WINNICOTT & 'THE GOOD ENOUGH PARENT'
        ("Solu", "Let's look at a profound developmental psychology concept from British pediatrician and psychoanalyst Donald Winnicott: 'The Good Enough Mother'!"),
        ("Tonu", "Winnicott studied thousands of mothers and infants, and made a discovery that stunned the psychiatric world: trying to be a 'perfect parent' is actively HARMFUL to a child's psychological development!"),
        ("Solu", "Why would a perfect parent harm a child, Tonu?"),
        ("Tonu", "If a parent anticipates every single need before the baby even cries, if they never let the child experience frustration, disappointment, or minor delays, the child never learns emotional self-soothing or resilience!"),
        ("Solu", "The child grows up fragile, assuming the entire universe must instantly cater to their demands!"),
        ("Tonu", "A 'Good Enough Parent' is loving, attuned, and reliable, but allows natural, minor failures and delays!"),
        ("Solu", "Those small, safe imperfections teach the child: 'I can survive frustration. The world is imperfect, and I am resilient enough to handle it!'"),
        ("Tonu", "You don't need to be a perfect parent, a perfect partner, or a perfect employee! You just need to be a 'Good Enough' human being who shows up with love, consistency, and presence."),

        # SECTION 8: OVERCOMING PERFECTIONISM IN SPOKEN ENGLISH
        ("Solu", "Now, let's address the number one roadblock that silences millions of English language learners: Accent and Grammar Perfectionism!"),
        ("Tonu", "How many times have you wanted to speak in an English meeting, join an international conversation, or answer a question, but your internal critic shouted: 'Stop! You don't know if that verb is in past perfect tense! What if your accent sounds strange? What if you use the wrong preposition? Sit down and keep quiet!'"),
        ("Solu", "That perfectionist voice is the enemy of your dreams! Let's establish this fundamental truth: THE GOAL OF LANGUAGE IS COMMUNICATION, NOT PERFECTION!"),
        ("Tonu", "If you walk into a bakery in New York, London, or Sydney and say: 'Please, one croissant, hot coffee,' did you communicate?"),
        ("Solu", "Yes! One hundred percent! The barista understood you, smiled, and handed you a warm croissant and coffee! Mission accomplished!"),
        ("Tonu", "Native speakers make grammar mistakes every single day! They use incorrect tenses, repeat words, and stumble over sentences."),
        ("Solu", "Nobody is grading you with a red pen in real life! The only bad English is the English that stays trapped inside your mouth because you were afraid of looking imperfect!"),
        ("Tonu", "Speak with joy, speak with your accent, make twenty mistakes a day, and celebrate every single word!"),

        # SECTION 9: REFRAMING MISTAKES AS SCIENTIFIC DATA
        ("Solu", "Let's borrow the mindset of Thomas Edison and the scientific laboratory: reframing failures as data!"),
        ("Tonu", "When Thomas Edison was inventing the incandescent electric light bulb, he tested over nine thousand different filaments that all failed!"),
        ("Solu", "A journalist asked him: 'Mr. Edison, how does it feel to have failed nine thousand times?'"),
        ("Tonu", "Edison smiled and replied: 'I have not failed nine thousand times. I have successfully discovered nine thousand ways that will not work!'"),
        ("Solu", "A perfectionist views a mistake as a shameful character defect: 'I failed, therefore I AM a failure!'"),
        ("Tonu", "A scientist views a mistake as valuable experimental data: 'Aha! That sentence structure didn't work. Fascinating! Let me adjust the variable and try again!'"),
        ("Solu", "When you treat your life as a laboratory rather than a courtroom, self-judgment dissolves into curious exploration."),

        # SECTION 10: EMBRACING YOUR 'WARTS AND ALL' HUMANITY
        ("Tonu", "Let's reflect on the immortal words of Oliver Cromwell to the portrait painter Samuel Cooper in the seventeenth century."),
        ("Solu", "Cooper wanted to paint Cromwell with smooth, idealized skin, hiding his facial scars and wrinkles."),
        ("Tonu", "Cromwell sternly commanded him: 'Paint me as I am: warts and all!'"),
        ("Solu", "People don't fall in love with perfect mannequins! We connect with living human beings with all their quirks, scars, eccentricities, and vulnerabilities!"),
        ("Tonu", "When you have the courage to show up 'warts and all', people breathe a sigh of relief in your presence! You give them permission to be human too."),

        # SECTION 11: THE FAMOUS POTTERY EXPERIMENT: QUANTITY CRUSHES QUALITY
        ("Solu", "Let's examine one of the most astonishing experiments on creative mastery in history: the famous pottery experiment from the book 'Art & Fear' by David Bayles and Ted Orland!"),
        ("Tonu", "A ceramics teacher divided his university pottery class into two distinct groups on the first day of the semester!"),
        ("Solu", "Group A was told: 'Your entire grade will be based purely on QUANTITY! On the final day of class, we will bring a bathroom scale. If you produce fifty pounds of clay pots, you get an A! If you produce forty pounds, you get a B!'"),
        ("Tonu", "Group B was told: 'Your entire grade will be based purely on QUALITY! You only need to produce ONE single pot, but that single pot must be an absolute masterpiece of perfection to earn an A!'"),
        ("Solu", "Now, listeners, what do you think happened at the end of the semester? Which group produced the most beautiful, exquisite, high-quality ceramic pots?"),
        ("Tonu", "Group A! The quantity group!"),
        ("Solu", "Why did the quantity group produce significantly higher quality art than the perfectionist group?"),
        ("Tonu", "Because the quantity group rolled up their sleeves and threw hundreds of pounds of clay onto the potter's wheel every single day! They made thousands of mistakes, broke hundreds of handles, saw glazes crack, learned from their errors in real time, and their technical skills skyrocketed!"),
        ("Solu", "Meanwhile, the 'perfection' group sat around for three months reading books, theorizing about grand aesthetics, paralyzed by fear! And on the final day, they brought in mediocre, clumsy pots because they had zero real-world clay experience!"),
        ("Tonu", "Quantity leads to quality! To become a master in English speaking, you must throw lots of clay on the wheel! Speak lots of sentences, make lots of clumsy mistakes, and your fluency will naturally blossom!"),

        # SECTION 12: ADAPTIVE VS MALADAPTIVE PERFECTIONISM
        ("Solu", "Let's explore an important clinical distinction in psychology: 'Adaptive Perfectionism' versus 'Maladaptive Perfectionism'!"),
        ("Tonu", "What is an Adaptive Perfectionist, Solu?"),
        ("Solu", "An adaptive perfectionist sets high standards, takes pride in their craft, and works diligently. BUT when they make a mistake, their self-esteem remains completely intact! They say: 'That didn't work. Let me learn and fix it!'"),
        ("Tonu", "They enjoy the journey and feel proud of their progress!"),
        ("Solu", "Now, what is a Maladaptive Perfectionist?"),
        ("Tonu", "A maladaptive perfectionist fuses their self-worth directly with their performance! If they get ninety-five percent on an exam instead of one hundred percent, they plunge into self-loathing, depression, and despair!"),
        ("Solu", "They feel like an utter failure because they cannot tolerate the natural existence of human flaws!"),
        ("Tonu", "Shift from maladaptive rigidity to adaptive flexibility! Strive with joy, celebrate your eighty percent victories, and detach your fundamental human worth from your daily productivity score!"),

        # SECTION 13: THE PRATFALL EFFECT: WHY FLAWS MAKE YOU LOVED
        ("Solu", "Let's explore a brilliant social psychology discovery by Dr. Elliot Aronson at Harvard University: 'The Pratfall Effect'!"),
        ("Tonu", "Dr. Aronson tested how people perceived candidates answering difficult trivia questions."),
        ("Solu", "A highly competent candidate answered ninety-two percent of questions correctly with polished brilliance."),
        ("Tonu", "In one condition, at the end of the interview, the brilliant candidate accidentally knocked over a cup of coffee, spilling it all over their shirt and clumsily saying: 'Oh dear, I spilled coffee all over myself!'"),
        ("Solu", "How did the audience rate the candidate who spilled coffee compared to when they didn't spill coffee, Tonu?"),
        ("Tonu", "Their likability and attractiveness skyrocketed! They were rated significantly MORE likable, warm, and approachable!"),
        ("Solu", "Why? Because human beings feel intimidated, distant, and uncomfortable around someone who seems cold, robotic, and flawless!"),
        ("Tonu", "The minor blunder—the pratfall—humanized them! It signaled: 'I am brilliant, but I am also an ordinary, lovable, clumsy human being just like you!'"),
        ("Solu", "When you make a minor mistake speaking English, don't panic! That tiny blunder makes you charming, relatable, and approachable!"),
        ("Tonu", "Nobody connects with cold perfection; people connect with the warmth of shared imperfection and vulnerability."),
        ("Solu", "When you laugh off your own blunders with ease, you make everyone around you feel safe to speak without fear."),

        # SECTION 14: LIVE ROLEPLAY: SUBMITTING A HIGH-QUALITY PROJECT AT 85%
        ("Solu", "Now let's demonstrate a realistic real-world roleplay! Imagine you are working on a company presentation or report, and your perfectionist colleague wants to delay the deadline by a week to endlessly tweak the design."),
        ("Tonu", "Most people get dragged into the perfectionist trap and work late all weekend!"),
        ("Solu", "Let's demonstrate how someone who understands the 80% Rule leads the project across the finish line! Tonu, play the perfectionist colleague."),
        ("Tonu", "Solu, wait! We can't send this market proposal to the executive team today! Slide twelve looks slightly off-center, and I want to re-interview five more clients to add more quotes! Let's ask for an extension!"),
        ("Solu", "Here is how you lead with wisdom: 'Tonu, I love how deeply you care about our work! Looking at our deck right now, our core strategic insights, market data, and budget projections are exceptionally strong and clear. We have delivered eighty-five percent of top-tier value. Delaying the deadline risks losing our client's momentum, whereas shipping it today allows leadership to give us real-time feedback. Let's make that minor alignment fix on slide twelve in ten minutes, celebrate our hard work, and hit send together!'"),
        ("Tonu", "Look at how magnificent that leadership was! You validated their care, anchored the project in functional value, highlighted the risk of delay, and drove the team to completion!"),
        ("Solu", "That is how champions deliver real results in the real world."),

        # SECTION 12: VOCABULARY & IDIOM SPOTLIGHT (6 KEY IDIOMS)
        ("Tonu", "Now, let's step into our signature segment: Key Everyday English Idioms and Phrases! Today, we have selected six colorful, essential expressions about perfection, mistakes, and realism!"),
        ("Solu", "Let's master them together! Tonu, what is our very first idiom for today?"),
        ("Tonu", "Our first expression is the modern productivity motto: 'done is better than perfect'. 'Done is better than perfect' means that completing a task, even with minor flaws, is far more valuable and useful than striving endlessly for unattainable perfection."),
        ("Solu", "Let's listen to a natural conversational example: 'Instead of obsessing over every single sentence for another month, she submitted her master's thesis, knowing that done is better than perfect.'"),
        ("Tonu", "Ship it with pride! What is our second expression, Solu?"),
        ("Solu", "Our second expression describes hidden brilliance: 'a diamond in the rough'. A 'diamond in the rough' is someone or something that has exceptional potential, talent, or beauty, but lacks superficial polish, refinement, or perfect appearance."),
        ("Tonu", "Here is how you can use it: 'His spoken English had some grammar mistakes, but his creative storytelling made him an absolute diamond in the rough.'"),
        ("Solu", "Polish comes with time! Tonu, introduce our third idiom."),
        ("Tonu", "Our third expression describes total authenticity: 'warts and all'. To accept or describe someone 'warts and all' means to accept them completely, including all their flaws, shortcomings, and imperfections."),
        ("Solu", "Let's hear an example: 'True friends are those rare souls who see you as you truly are, and love you warts and all.'"),
        ("Tonu", "Unconditional love embraces warts and all! What is our fourth expression, Solu?"),
        ("Solu", "Our fourth expression describes petty over-analysis: 'split hairs'. To 'split hairs' means to argue or obsess over tiny, insignificant differences or details that don't really matter."),
        ("Tonu", "For example: 'We have agreed on the main contract terms; let's not split hairs over minor wording and finalize the agreement.'"),
        ("Solu", "Don't split hairs when the big picture is clear! Tonu, take us to our fifth idiom."),
        ("Tonu", "Our fifth expression describes doing shoddy work: 'cut corners'. To 'cut corners' means to do something in the easiest, cheapest, or fastest way possible, often sacrificing quality, safety, or ethics."),
        ("Solu", "Notice that being good enough is NOT cutting corners! Here is an example: 'The construction company cut corners on concrete reinforcement, leading to severe structural cracks.'"),
        ("Tonu", "Deliver excellence without cutting corners, but without perfectionist paralysis! And what is our sixth expression, Solu?"),
        ("Solu", "Our sixth expression describes thoroughness: 'leave no stone unturned'. To 'leave no stone unturned' means to do everything possible and search thoroughly in order to achieve a goal or find a solution."),
        ("Tonu", "Let's hear an example: 'The detectives left no stone unturned in their investigation to uncover the missing evidence.'"),

        # SECTION 16: INTERACTIVE SPEAKING PRACTICE
        ("Solu", "Now, it is time for our Interactive Speaking Challenge! This is your turn to speak English out loud along with us. Open your chest, pronounce each syllable with warmth, freedom, and courage, and repeat each sentence with steady cadence!"),
        ("Tonu", "Sentence number one: 'Done is better than perfect; I give myself permission to learn, grow, and ship.' Your turn!"),
        ("Solu", "Speak it out loud with clear cadence: 'Done is better than perfect; I give myself permission to learn, grow, and ship.'"),
        ("Tonu", "Beautiful rhythm! Sentence number two: 'My accent and mistakes are proof of my courage to speak and connect.' Your turn!"),
        ("Solu", "Repeat with steady conviction: 'My accent and mistakes are proof of my courage to speak and connect.'"),
        ("Tonu", "Wonderful! Sentence number three: 'True excellence is a joyful journey of progress, not a rigid demand for perfection.' Your turn!"),
        ("Solu", "Say it clearly: 'True excellence is a joyful journey of progress, not a rigid demand for perfection.'"),
        ("Tonu", "Sentence number four: 'When I embrace my humanity, warts and all, my authentic brilliance shines.' Your turn!"),
        ("Solu", "Let's say sentence number four together: 'When I embrace my humanity, warts and all, my authentic brilliance shines.'"),
        ("Tonu", "Outstanding work! Notice how liberating, energetic, and natural your spoken English sounds when you speak without fear!"),
        ("Solu", "Every sentence you speak out loud dissolves the paralyzing illusion of perfectionism and anchors confident fluency into your voice."),

        # SECTION 17: REFLECTION & FAREWELL
        ("Solu", "And now, it is time for today's Weekly Reflection Question! We want you to practice writing in English down in the comment section below."),
        ("Tonu", "Here is today's question: 'What is a project, conversation, or creative idea that you have been postponing because of perfectionism? How will you apply the 80% Rule this week to take imperfect action and finish it?'"),
        ("Solu", "Writing your thoughts in English breaks the spell of perfectionism and connects you with thousands of fellow learners worldwide. Share your story in the comments below!"),
        ("Tonu", "Solu and I read through every single comment, and we are right there in the comments celebrating your bravery!"),
        ("Solu", "When you let go of perfection, you open the floodgates of creativity, joy, and meaningful progress in every dimension of your life."),
        ("Tonu", "The world doesn't need your perfection; the world needs your authentic voice and your loving presence."),
        ("Solu", "Give yourself the grace to be a work in progress, celebrating every small step of growth along the way."),
        ("Tonu", "Stand tall in your uniqueness, let your light shine without apology, and know that you are already more than enough."),
        ("Solu", "Remember: perfection is a mirage that keeps you thirsty. Excellence is an oasis that nourishes your soul. Choose excellence, embrace your humanity, and let your voice be heard."),
        ("Tonu", "Speak boldly, ship your gifts, and keep practicing your English with radiant joy every single day!"),
        ("Solu", "Until next time, goodbye from Solu!"),
        ("Tonu", "And goodbye from Tonu!"),
        ("Both", "Happy learning, done is better than perfect, and goodbye!")
    ]
    return turns

if __name__ == "__main__":
    t = build_ep51()
    gen_common.verify_and_save(51, "scripts/daily_speak_ep51_full.txt",
                              "Overcoming Perfectionism: The 80% Rule & Good Enough",
                              "Daily Speak English | English Listening & Speaking Practice",
                              t)
