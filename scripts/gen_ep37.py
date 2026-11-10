#!/usr/bin/env python3
"""
Daily Speak English - Episode 37
Title: Overcoming Imposter Syndrome & Unlocking Quiet Confidence
Requirements:
- Starts with Tonu: "Hey hey, lovely listeners!..."
- Words >= 3,550 (strict duration >= 25.5 - 28.0 mins)
- High-level engaging, natural conversational English
"""

import gen_common

def build_ep37():
    turns = [
        # SECTION 1: MAGNETIC OPENING
        ("Tonu", "Hey hey, lovely listeners! Welcome back to Daily Speak English, your favorite place to become fluent, confident, and unstoppable in English! I'm Tonu!"),
        ("Solu", "And I'm Solu! Welcome back, everyone! Today, we are taking on a psychological phantom that haunts almost every ambitious, intelligent, and conscientious human being on Earth: 'Imposter Syndrome' and the secret journey to unlocking genuine, quiet confidence!"),
        ("Tonu", "Solu, have you ever walked into an important meeting, stepped onto a stage, or joined an international conference, and suddenly this terrifying little voice inside your skull whispers: 'What are you doing here? You don't belong in this room! Everyone here is smarter, more qualified, and more articulate than you! Any minute now, they are going to realize you are an absolute fraud!'"),
        ("Solu", "Oh, absolutely! That icy chill of panic is so familiar to millions of people! You look around the room, everyone seems so poised, polished, and confident, and you feel like an actor wearing an oversized suit waiting for someone to tap you on the shoulder and expose you!"),
        ("Tonu", "And here is the astonishing paradox: research shows that the people who suffer most severely from Imposter Syndrome are not underachievers or phonies; they are high-achieving, deeply dedicated, capable professionals, artists, and students!"),
        ("Solu", "Today, we are going to expose the psychological roots of Imposter Syndrome, analyze the five distinct imposter archetypes, share concrete cognitive tools to dissolve self-doubt, and practice advanced conversational English that will make your voice ring with authority!"),

        # SECTION 2: THE SCIENTIFIC ORIGIN: CLANCE & IMES (1978)
        ("Tonu", "Let's travel back to 1978 to discover where this concept originated! Two clinical psychologists, Dr. Pauline Clance and Dr. Suzanne Imes, conducted a study with over one hundred and fifty high-achieving women."),
        ("Solu", "These were women with doctorates, prestigious university faculty positions, and top corporate titles. Despite their objective, verifiable accolades, what did Dr. Clance and Dr. Imes discover?"),
        ("Tonu", "Almost all of them were secretly convinced that their success was an accident! They believed their high grades were a grading error, their promotions were due to luck or charisma, and that they had somehow fooled the admissions committee!"),
        ("Solu", "They originally labeled this 'The Imposter Phenomenon'! And subsequent research across four decades revealed that it affects men and women equally, across every single profession—surgeons, software engineers, authors, and world leaders!"),
        ("Tonu", "In fact, legendary author Maya Angelou, who wrote eleven bestselling books, won numerous Pulitzers, and was nominated for the National Book Award, once confessed: 'I have written eleven books, but each time I think, 'Uh-oh, they’re going to find out now. I’ve run a game on everybody, and they’re going to find me out!''"),
        ("Solu", "Think about that! Maya Angelou, one of the greatest literary giants of the twentieth century, felt like a fraud! And Tom Hanks, two-time Academy Award winner, said in an interview: 'No matter what we've done, there comes a point where you think: How did I get here? When are they going to discover that I am in fact a fraud and take it all away?'"),
        ("Tonu", "If Maya Angelou and Tom Hanks feel like imposters, then whenever you feel self-doubt speaking English or presenting your ideas, you are in extraordinary company!"),

        # SECTION 3: THE DUNNING-KRUGER EFFECT VS IMPOSTER SYNDROME
        ("Solu", "Now, let's look at the fascinating neurological contrast between Imposter Syndrome and what psychologists call 'The Dunning-Kruger Effect'!"),
        ("Tonu", "The Dunning-Kruger Effect, discovered by David Dunning and Justin Kruger at Cornell University, shows that individuals with very low competence in a subject suffer from illusory superiority! They think they are absolute geniuses!"),
        ("Solu", "Because they know so little about a topic, they are completely blind to how vast and complex the field actually is! So they walk into a room with total, unearned arrogance!"),
        ("Tonu", "Meanwhile, competent, highly skilled individuals know how vast the subject is! They understand the nuances, the complexities, and how much they have yet to master."),
        ("Solu", "And because they see the summit of the mountain so clearly, they underestimate their own immense skill, falsely assuming that if something is easy or obvious to them, it must be easy and obvious to everyone else!"),
        ("Tonu", "So if you are doubting your abilities, that self-doubt is actually proof of your intelligence! True fools never doubt themselves; only the wise question their competence!"),

        # SECTION 4: THE FIVE IMPOSTER ARCHETYPES (DR. VALERIE YOUNG)
        ("Solu", "Dr. Valerie Young, one of the world's foremost experts on imposter syndrome, identified five distinct archetypes or sub-types. Let's see which archetype resonates most with our listeners!"),
        ("Tonu", "Archetype number one is 'The Perfectionist'!"),
        ("Solu", "The Perfectionist sets impossibly high standards for themselves. If they achieve ninety-nine percent on an exam or deliver a project that is ninety-eight percent flawless, they fixate on the tiny two percent flaw and feel like an absolute failure!"),
        ("Tonu", "For the perfectionist, anything less than perfection equals defeat. Archetype number two is 'The Natural Genius'!"),
        ("Solu", "The Natural Genius judges their competence based on speed and ease! If they don't understand a complex English grammar rule or master a new coding framework on the very first try, their internal alarm rings: 'I must be stupid! If I was truly smart, this would be effortless!'"),
        ("Tonu", "They confuse the natural struggle of learning with personal inadequacy! Archetype number three is 'The Soloist'!"),
        ("Solu", "The Soloist believes that to be genuinely competent, they must accomplish everything entirely alone! If they have to ask for assistance, mentorship, or clarification, they feel weak and ashamed, believing it invalidates their success!"),
        ("Tonu", "Archetype number four is 'The Expert'!"),
        ("Solu", "The Expert believes they cannot apply for a job, raise their hand in a meeting, or publish their opinion until they know every single piece of information, have ten certifications, and memorize the entire encyclopedia! They constantly feel unqualified!"),
        ("Tonu", "And Archetype number five is 'The Superhuman'!"),
        ("Solu", "The Superhuman feels they must excel effortlessly in every single dimension of life simultaneously: they must be the top employee, the perfect parent, the marathon runner, the gourmet chef, and the immaculate host! If they drop even one plate, they feel like an imposter!"),
        ("Tonu", "Listeners, which of these five sounds like your internal critic? Identifying your pattern is the first step toward neutralizing its power!"),

        # SECTION 5: PLURALISTIC IGNORANCE & THE OUTSIDE VS INSIDE BIAS
        ("Solu", "Let's explore a powerful sociological phenomenon called 'Pluralistic Ignorance'!"),
        ("Tonu", "Pluralistic ignorance is a psychological situation where every individual in a group secretly doubts themselves or disagrees, but falsely assumes that everyone else agrees or feels totally confident because no one speaks up!"),
        ("Solu", "Think about an English classroom or a corporate boardroom! The speaker presents a complicated strategy. You look around the table: everyone is nodding, taking notes, looking composed."),
        ("Tonu", "You think: 'Oh my goodness, everyone understands this except me! I better nod along and keep my mouth shut!'"),
        ("Solu", "What you cannot see is that eighty percent of the people in that room are having the exact same internal panic attack!"),
        ("Tonu", "We compare our internal chaos, self-doubt, and vulnerabilities to other people's curated, external public faces! You are comparing your unedited behind-the-scenes blooper reel to someone else's polished highlight movie!"),
        ("Solu", "The moment someone has the courage to raise their hand and say: 'Excuse me, could you clarify that last point? I want to make sure I understand,' a visible wave of relief washes across the entire room!"),

        # SECTION 6: ATTRIBUTION BIAS & LUCK VS SKILL
        ("Tonu", "Now let's examine 'Attribution Bias'—how we assign credit for success and failure."),
        ("Solu", "People with imposter syndrome have a broken internal credit system! When they succeed, they attribute it to external factors: 'Oh, I just got lucky,' 'The test was unusually easy,' 'They were desperate and had no one else to hire.'"),
        ("Tonu", "But when they make a tiny mistake or experience a setback, they immediately attribute it to internal personal flaws: 'See? I knew I was incompetent! I knew I didn't have what it takes!'"),
        ("Solu", "Meanwhile, truly arrogant people do the exact reverse: when they succeed, they take all the personal credit, and when they fail, they blame the weather, the government, or their coworkers!"),
        ("Tonu", "To heal imposter syndrome, you must learn to balance your attribution! When you succeed, acknowledge the hundreds of hours of solitary practice, the discipline, the focus, and the skills you invested! You didn't just get lucky; you positioned yourself to catch that opportunity!"),

        # SECTION 7: THE EVIDENCE PORTFOLIO & BRAG SHEET
        ("Solu", "Let's provide our listeners with a tangible, practical exercise to combat imposter feelings: 'The Evidence Portfolio' or 'The Brag Sheet'!"),
        ("Tonu", "Our brains suffer from what psychologists call 'Negativity Bias'. We remember one critical email for six months, but we forget ten compliments within thirty seconds!"),
        ("Solu", "To counter this, create a digital folder on your phone or desktop, or buy a dedicated notebook, titled 'The Evidence Portfolio'!"),
        ("Tonu", "Every time a client sends an appreciative email, every time a manager praises your initiative, every time you solve a difficult technical problem, take a screenshot or write it down!"),
        ("Solu", "Save your university degrees, positive performance reviews, kind text messages from colleagues, and moments of personal resilience!"),
        ("Tonu", "When imposter syndrome attacks you before an interview or presentation, open your Evidence Portfolio and read through the facts!"),
        ("Solu", "Feelings are not facts! Your anxiety might tell you that you are incapable, but the hard, documented evidence in front of your eyes proves that you have succeeded repeatedly across many years!"),

        # SECTION 8: SHIFTING FROM PERFORMANCE TO SERVICE
        ("Tonu", "Here is one of the most profound psychological shifts to cure social anxiety and imposter syndrome: shift your mindset from 'Performance' to 'Contribution and Service'!"),
        ("Solu", "Explain that profound distinction, Tonu. How does shifting to service liberate us?"),
        ("Tonu", "When you are trapped in a 'Performance Mindset', your attention is entirely focused on yourself: 'How do I sound? Do they think I have an accent? Am I making grammar mistakes? Do they think I look awkward?'"),
        ("Solu", "That self-obsession generates intense anxiety! You are judging yourself like an Olympic athlete waiting for scores!"),
        ("Tonu", "Now, switch to a 'Service Mindset'! Ask: 'How can I help the people in this room? What value or clarity can I offer? How can my ideas solve their problems or uplift their spirits?'"),
        ("Solu", "The moment your focus shifts from protecting your own ego to serving the audience, your fear evaporates! You are no longer defending an identity; you are offering a gift!"),
        ("Tonu", "Whether you are speaking English, delivering a presentation, or meeting a new client, focus entirely on them! Your quiet confidence will shine naturally."),

        # SECTION 9: REFRAMING THE INNER CRITIC: FROM ENEMY TO PROTECTOR
        ("Solu", "Let's also look at that harsh inner critic inside our head! Why does our brain generate that critical voice in the first place?"),
        ("Tonu", "Your inner critic is not your enemy; your inner critic is an overprotective, anxious security guard!"),
        ("Solu", "From an evolutionary perspective, our ancestral brains wanted us to stay safe within the tribe. If you stood out, took a big risk, or spoke up, you risked social rejection and exile from the tribe, which meant literal physical death!"),
        ("Tonu", "So your inner critic shouts: 'Don't speak up! Don't volunteer for that leadership role! Stay small, stay invisible, and nobody can hurt you!'"),
        ("Solu", "When that voice whispers 'You are not ready,' don't fight it with anger. Smile and say: 'Thank you for trying to keep me safe, but I am an adult now, I am prepared, and I can handle the discomfort of growing.'"),
        ("Tonu", "Acknowledge the fear, thank your brain for its vigilance, and step onto the stage anyway!"),

        # SECTION 10: EMBRACING 'LEARNER STATUS' & PERMISSION TO BE A BEGINNER
        ("Solu", "Let's specifically speak to our English language learners who feel like imposters when speaking to native or fluent speakers!"),
        ("Tonu", "Many learners say: 'Solu, I feel so embarrassed because my English vocabulary is limited, and I can't express my true intellectual depth like I do in my native language!'"),
        ("Solu", "Remember this golden rule: Speaking a second language with an accent and grammatical mistakes is not a sign of low intelligence; it is a badge of immense courage!"),
        ("Tonu", "It means your brain is operating in two completely different linguistic systems! A person who speaks broken English is someone who knows another language entirely!"),
        ("Solu", "Adopt what Carol Dweck calls a 'Growth Mindset' and proudly claim 'Learner Status'!"),
        ("Tonu", "If you don't know a word, don't pretend or shrink in shame! Say with a bright smile: 'How do you express that concept in English?' People love helping someone who is genuinely curious and confident in their learning journey!"),

        # SECTION 11: THE LINKEDIN ILLUSION & COMPARISON CULTURE
        ("Solu", "Now let's address the toxic fuel that feeds modern imposter syndrome twenty-four hours a day: social media and professional networking platforms like LinkedIn!"),
        ("Tonu", "You open your feed during breakfast, and within thirty seconds you see: 'Thrilled to announce I was selected for Forbes 30 Under 30!', 'Humbled to have closed our ten-million-dollar funding round!', 'So proud to start my new role as Vice President!'"),
        ("Solu", "You haven't even finished your morning coffee, and suddenly you feel like the biggest underachiever in human history!"),
        ("Tonu", "Remember that professional platforms are curated public relations broadcasts! Nobody posts about the forty-seven job rejection emails they received, the panic attacks in the office restroom, or the contracts they lost!"),
        ("Solu", "When you consume other people's curated triumphs, your brain calculates an artificial baseline of reality that doesn't exist anywhere in the real world!"),
        ("Tonu", "Unfollow accounts that trigger feelings of worthlessness, take digital sabbaticals, and measure your progress solely against who you were yesterday, not against someone else's highlight reel!"),

        # SECTION 12: ABRAHAM MASLOW & THE JONAH COMPLEX
        ("Solu", "Let's also explore a paradoxical psychological phenomenon discovered by renowned psychologist Abraham Maslow: 'The Jonah Complex'!"),
        ("Tonu", "What is the Jonah Complex, Solu? Most people have heard of the fear of failure, but what did Maslow discover?"),
        ("Solu", "Maslow discovered that many human beings suffer not from the fear of failure, but from 'The Fear of Greatness'—the fear of their own highest possibilities!"),
        ("Tonu", "Why would anyone be afraid of their own greatness, talent, or success?"),
        ("Solu", "Because genuine success brings immense responsibility, higher expectations, and visibility! If you step into your full brilliance, people will expect you to deliver at a world-class level consistently!"),
        ("Tonu", "And it might also create distance or envy among old friends and relatives who prefer you to stay small and average!"),
        ("Solu", "So people subconsciously sabotage their promotions, shrink in meetings, and claim they are imposters just to retreat back into the comfortable safety of mediocrity!"),
        ("Tonu", "Do not run away from your destiny like the biblical prophet Jonah! Embrace the discomfort of visibility, expand your capacity, and let your brilliance serve humanity!"),

        # SECTION 13: THE PERSONAL BOARD OF DIRECTORS
        ("Solu", "Here is another actionable strategy: assemble what executive coaches call 'A Personal Board of Directors'!"),
        ("Tonu", "What is a personal board of directors, Solu?"),
        ("Solu", "In business, a company has a board of trustees who provide objective guidance and reality checks. In your personal life, choose three to five trusted mentors, colleagues, or wise friends who know your true character and skills!"),
        ("Tonu", "These should be individuals who will celebrate your genuine victories without jealousy, but will also give you honest, grounded, constructive feedback when you need to improve!"),
        ("Solu", "When imposter syndrome whispers that you are worthless, schedule a twenty-minute call with a member of your personal board of directors and say: 'I'm experiencing severe self-doubt about this new project. Can you give me an objective assessment of where I stand?'"),
        ("Tonu", "Their grounded, external reality check will immediately cut through your emotional distortions and restore your perspective!"),
        ("Solu", "Having even one truth-teller in your corner can keep your feet on solid ground when emotional self-doubt tries to pull you into a dark spiral."),
        ("Tonu", "Surround yourself with people who see your potential before you can see it yourself, and let their belief support you until your own takes root."),

        # SECTION 14: LIVE ROLEPLAY: ANSWERING AN INTERVIEW QUESTION WITH QUIET CONFIDENCE
        ("Solu", "Now let's demonstrate a realistic real-world roleplay! Imagine you are in a job interview in English, and the interviewer asks about a skill or software tool that you have only moderate experience with."),
        ("Tonu", "An imposter either panics and lies: 'Yes, I am a world-class master at that!' or they disqualify themselves: 'Oh, I'm really bad at that, I probably can't do this job.'"),
        ("Solu", "Let's demonstrate how someone with authentic, quiet confidence answers! Tonu, ask me the question."),
        ("Tonu", "Solu, our engineering team uses Advanced Cloud Architecture, but looking at your resume, you haven't worked with this specific enterprise platform before. Can you handle this role?"),
        ("Solu", "Here is the grounded, confident response: 'You are completely right, Tonu. While I haven't worked with that specific enterprise platform yet, my core foundation in distributed systems and cloud protocols is exceptionally strong. In my previous role, I mastered two completely new database systems within three weeks and deployed them to production without downtime. I love diving into new technical ecosystems, and I am confident I will be fully up to speed with your architecture within my first month.'"),
        ("Tonu", "Look at the power of that answer! You didn't lie, you didn't apologize, and you didn't cower! You acknowledged reality, pointed to your proven track record of rapid learning, and projected calm, steady capability!"),
        ("Solu", "Employers hire problem-solvers who can learn, not walking encyclopedias."),

        # SECTION 12: VOCABULARY & IDIOM SPOTLIGHT (6 KEY IDIOMS)
        ("Tonu", "Now, let's step into our signature vocabulary segment: Key Everyday English Idioms and Phrases! Today, we have selected six colorful, essential expressions about confidence, courage, and self-belief!"),
        ("Solu", "Let's master them together! Tonu, what is our very first idiom for today?"),
        ("Tonu", "Our first expression is the famous saying: 'fake it till you make it'. To 'fake it till you make it' means to act with confidence, professionalism, or optimism even when you feel insecure, until genuine confidence and competence develop naturally."),
        ("Solu", "Let's listen to a natural conversational example: 'When Sophia was promoted to department director, she felt terrified, but she faked it till she made it, and within six months she was leading with genuine poise.'"),
        ("Tonu", "Action precedes feeling! What is our second expression, Solu?"),
        ("Solu", "Our second expression describes feelings of being overwhelmed: 'out of one's depth'. To be 'out of your depth' means to be in a situation that is beyond your current knowledge, experience, or ability to manage."),
        ("Tonu", "Here is how you can use it: 'During the high-level financial merger discussions, the junior analyst felt completely out of his depth.'"),
        ("Solu", "Recognizing when you are out of your depth is how you ask the right questions! Tonu, introduce our third expression."),
        ("Tonu", "Our third expression is essential for mental health: 'give oneself credit'. To 'give yourself credit' means to acknowledge, appreciate, and celebrate your own achievements, hard work, and progress."),
        ("Solu", "Let's hear an example: 'You survived a grueling year of study and passed your IELTS exam; you really need to give yourself more credit!'"),
        ("Tonu", "Stop minimizing your victories! What is our fourth expression, Solu?"),
        ("Solu", "Our fourth expression is about compassion: 'cut someone some slack'. To 'cut someone some slack' means to be gentle, forgiving, and less critical or demanding toward someone, especially when they are under stress."),
        ("Tonu", "And cut YOURSELF some slack! For example: 'You are learning a new language while working full-time; cut yourself some slack if you make a few grammar mistakes!'"),
        ("Solu", "Be kind to yourself! Tonu, take us to our fifth idiom."),
        ("Tonu", "Our fifth expression describes heroic courage: 'rise to the occasion'. To 'rise to the occasion' means to perform exceptionally well and succeed in dealing with a difficult challenge or unexpected crisis."),
        ("Solu", "Here is an inspiring example: 'When our keynote speaker fell ill thirty minutes before the international conference, Daniel rose to the occasion and delivered a magnificent speech.'"),
        ("Tonu", "And what is our sixth and final expression for today, Solu?"),
        ("Solu", "Our sixth expression is 'own one's success'. To 'own your success' means to fully accept, embrace, and take proud responsibility for your accomplishments without deflecting praise or chalking it up to mere luck."),
        ("Tonu", "Let's hear an example: 'Instead of saying it was just pure luck, Elena stood tall and truly owned her success after winning the national design award.'"),

        # SECTION 13: INTERACTIVE SPEAKING PRACTICE
        ("Solu", "Now, it is time for our Interactive Speaking Challenge! This is your turn to speak English out loud along with us. Lift your chin, pull your shoulders back, breathe deeply from your diaphragm, and repeat each sentence with authority and clear cadence!"),
        ("Tonu", "Sentence number one: 'I belong in every room I enter, and my voice and perspective have genuine value.' Your turn!"),
        ("Solu", "Speak it out loud with clear conviction: 'I belong in every room I enter, and my voice and perspective have genuine value.'"),
        ("Tonu", "Outstanding presence! Sentence number two: 'Instead of downplaying my hard work, I am learning to give myself credit and own my success.' Your turn!"),
        ("Solu", "Repeat with steady confidence: 'Instead of downplaying my hard work, I am learning to give myself credit and own my success.'"),
        ("Tonu", "Wonderful! Sentence number three: 'Making mistakes while speaking English is not failure; it is the natural evidence of learning and courage.' Your turn!"),
        ("Solu", "Say it clearly: 'Making mistakes while speaking English is not failure; it is the natural evidence of learning and courage.'"),
        ("Tonu", "Sentence number four: 'When challenging situations arise, I have the grit, talent, and resilience to rise to the occasion.' Your turn!"),
        ("Solu", "Let's say sentence number four together: 'When challenging situations arise, I have the grit, talent, and resilience to rise to the occasion.'"),
        ("Tonu", "Brilliant work! Feel how strong, resonant, and natural your spoken English sounds when you speak with genuine conviction!"),

        # SECTION 14: REFLECTION & FAREWELL
        ("Solu", "And now, it is time for today's Weekly Reflection Question! We want you to practice writing in English down in the comment section below."),
        ("Tonu", "Here is today's question: 'Have you ever experienced Imposter Syndrome in your career, studies, or English learning journey? What is one accomplishment in your life that you need to stop attributing to luck and start giving yourself real credit for?'"),
        ("Solu", "Writing your personal victory down in English breaks the spell of self-doubt and anchors your confidence. Share your story in the comments below!"),
        ("Tonu", "Solu and I read through every single comment, and we will be right there in the comment section celebrating your milestones with you!"),
        ("Solu", "Remember that you don't need to know everything to be worthy, capable, and respected."),
        ("Tonu", "Walk tall, believe in your power, and keep speaking English with bold enthusiasm every single day!"),
        ("Solu", "Until next time, goodbye from Solu!"),
        ("Tonu", "And goodbye from Tonu!"),
        ("Both", "Happy learning, own your brilliance, and goodbye!")
    ]
    return turns

if __name__ == "__main__":
    t = build_ep37()
    gen_common.verify_and_save(37, "scripts/daily_speak_ep37_full.txt",
                              "Overcoming Imposter Syndrome & Unlocking Quiet Confidence",
                              "Daily Speak English | English Listening & Speaking Practice",
                              t)
