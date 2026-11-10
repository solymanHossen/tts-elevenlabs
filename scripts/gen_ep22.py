#!/usr/bin/env python3
import gen_common

def build_ep22():
    turns = [
        # SECTION 1: WARM WELCOME & HOOK
        ("Tonu", "Hey hey, lovely listeners! Welcome back to Daily Speak English, your favorite place to improve your English listening and speaking skills. I'm Tonu!"),
        ("Solu", "And I'm Solu! We are thrilled to welcome you back for another heartfelt, practical, and engaging episode."),
        ("Tonu", "Today, we are tackling a topic that touches the hearts, minds, and anxieties of almost everyone across the globe: Navigating Modern Dating, Building Meaningful Relationships, and Finding True Love!"),
        ("Solu", "Oh boy, modern dating! If you ask ten people today how they feel about modern dating, at least eight of them will let out a deep, exhausted sigh!"),
        ("Tonu", "It is so true, Solu! Between smartphone dating apps, algorithmic matchmaking, endless swiping, and modern communication dilemmas, finding genuine romantic companionship has never felt more complicated."),
        ("Solu", "Yet, at our human core, our desire to be seen, to be cherished, and to share life with a partner has remained identical for thousands of years."),
        ("Tonu", "So today, we want to look at the psychology of dating, unpack the traps of modern dating culture, explore the green flags of healthy love, and teach you fantastic everyday English vocabulary to talk about romance and relationships."),
        ("Solu", "Whether you are single and searching, happily married, or just curious about human psychology, today's conversation will give you valuable insights and natural English fluency."),

        # SECTION 2: DATING APPS VS MEETING ORGANICALLY
        ("Tonu", "Let's start right at the epicenter of modern romance: Dating Apps versus Meeting Organically in the real world."),
        ("Solu", "A few decades ago, people met their partners through mutual friends, university classes, neighborhood gatherings, or shared hobbies. Today, over fifty percent of couples meet through a digital screen!"),
        ("Tonu", "On one hand, dating apps offer incredible reach. You can meet wonderful people outside your immediate social circle or profession that you would never otherwise bump into on the street."),
        ("Solu", "That is true. But on the other hand, dating apps have introduced a psychological phenomenon known as the 'Paradox of Choice'!"),
        ("Tonu", "The Paradox of Choice! That was popularized by psychologist Barry Schwartz. When human beings are presented with hundreds of options, we actually become less satisfied and more indecisive!"),
        ("Solu", "Exactly! When you swipe through endless profiles, your brain mistakenly believes that a 'flawless, perfect person' is waiting just one swipe away. So people treat human beings like catalog items."),
        ("Tonu", "And it leads to what psychologists call 'dating app fatigue' or burnout. You exchange superficial text messages with dozens of strangers, asking the exact same questions: 'Where do you work? What are your hobbies? What are you doing this weekend?'"),
        ("Solu", "And after a few weeks of repetitive digital small talk, you feel emotionally drained before you have even met for a single cup of coffee!"),
        ("Tonu", "Which is why so many people are returning to what we call 'organic dating'—meeting people through run clubs, cooking classes, volunteering projects, and book groups!"),
        ("Solu", "When you meet someone while engaging in an activity you genuinely love, you already have built-in common ground. You see how they treat people, how they laugh, and their natural body language before any romantic pressure is applied."),

        # SECTION 3: THE FIRST DATE & BEYOND INTERROGATION
        ("Tonu", "Now let's imagine you do secure a first date! You are meeting someone at a cozy cafe on a Saturday afternoon. Solu, what is the biggest mistake people make on first dates?"),
        ("Solu", "Without a doubt, turning the date into a stressful job interview!"),
        ("Tonu", "Haha! That is so painfully awkward! 'So, where do you see yourself in five years? What are your greatest strengths and weaknesses? Why did you leave your previous relationship?'"),
        ("Solu", "Exactly! People become so focused on evaluating the other person or trying to perform like an impressive candidate that they forget to just connect like two playful human beings."),
        ("Tonu", "A first date shouldn't be an interrogation; it should be an exploration. The best conversationalists are not the ones who talk about their achievements, but the ones who make the other person feel genuinely fascinating!"),
        ("Solu", "There is a classic rule: 'Be interested rather than interesting.' Ask open-ended questions that tap into emotions and passions, rather than sterile facts."),
        ("Tonu", "Instead of asking 'What is your job title?', ask 'What project or hobby are you working on right now that really excites your curiosity?'"),
        ("Solu", "Notice how that second question immediately invites the person to smile, light up, and tell an emotional story!"),
        ("Tonu", "And listen actively! Don't just wait for your turn to speak. React with warmth, nod, and ask follow-up questions."),

        # SECTION 4: GHOSTING & EMOTIONAL MATURITY
        ("Solu", "Now, we have to address one of the most painful modern phenomena: 'Ghosting'. Tonu, how would you define ghosting for our listeners?"),
        ("Tonu", "Ghosting is when someone you have been dating, texting, or communicating with suddenly cuts off all contact without any explanation, warning, or goodbye. They simply vanish into thin air like a ghost!"),
        ("Solu", "Ghosting has become so rampant because digital screens create emotional distance. It is much easier to simply ignore someone's message or block their number than to have an uncomfortable, two-minute honest conversation."),
        ("Tonu", "But ghosting is an indicator of emotional immaturity and conflict avoidance. When someone ghosts, they leave the other person with painful ambiguity and self-doubt. The victim wonders: 'Did I say something wrong? Was I not attractive enough? Did something happen to them?'"),
        ("Solu", "If you go on a date with someone and realize there is no romantic spark, what is the mature, respectful way to handle it?"),
        ("Tonu", "Send a kind, clear, and graceful message! You can simply say: 'Thank you so much for meeting me yesterday; I had a lovely time talking with you. However, I didn't feel a romantic connection, but I genuinely wish you the very best!'"),
        ("Solu", "That takes thirty seconds to type, preserves the other person's dignity, and demonstrates emotional maturity and respect."),
        ("Tonu", "And if someone ever ghosts you, remember: their disappearance is a reflection of their lack of communication skills, not your worth as a human being."),

        # SECTION 5: RED FLAGS VS GREEN FLAGS
        ("Solu", "Now let's talk about evaluating compatibility: Red Flags versus Green Flags! Everyone on social media talks about red flags, but what are some crucial warning signs early in dating?"),
        ("Tonu", "A major red flag is how they treat service staff—the waiter, the barista, or the taxi driver! If someone is charming and sweet to you, but rude, impatient, or condescending to a server, pay very close attention!"),
        ("Solu", "Yes! That shows you how they will treat you once the initial honeymoon phase wears off and they become comfortable."),
        ("Tonu", "Another red flag is someone who badmouths every single one of their former partners, claiming that every ex was 'crazy' or toxic. If everyone in their past was terrible, they are probably the common denominator who lacks accountability!"),
        ("Solu", "And what about green flags, Tonu? What are the positive signs that indicate someone could be a wonderful, healthy long-term partner?"),
        ("Tonu", "A huge green flag is emotional regulation and calmness during misunderstandings. When something goes wrong—for example, the restaurant loses your reservation or traffic is terrible—do they stay patient, or do they fly into a rage?"),
        ("Solu", "Another wonderful green flag is consistency. Their words match their actions. If they say they will call you at eight, they call you at eight. You don't have to spend your energy playing guessing games."),
        ("Tonu", "And a massive green flag is celebrating your successes! A great partner does not feel threatened or jealous when you achieve a promotion, learn a new skill, or shine. They are your loudest cheerleader!"),

        # SECTION 6: ATTACHMENT STYLES & COMMUNICATING NEEDS
        ("Solu", "Let's touch briefly on psychology. Many psychologists and therapists today talk about 'Attachment Theory'. What are the core attachment styles, Tonu?"),
        ("Tonu", "Psychologists usually identify three primary adult attachment styles: Secure, Anxious, and Avoidant."),
        ("Solu", "Someone with a 'Secure' attachment feels comfortable with intimacy, expresses their emotions openly, and doesn't panic when their partner needs personal space."),
        ("Tonu", "Someone with an 'Anxious' attachment often worries about whether their partner truly loves them. They crave frequent reassurance and may feel intense anxiety if a text message isn't answered immediately."),
        ("Solu", "And someone with an 'Avoidant' attachment tends to pull away, withdraw, or become distant whenever emotional closeness feels overwhelming or suffocating."),
        ("Tonu", "Understanding your own attachment style—and your partner's style—can save you from endless unnecessary arguments!"),
        ("Solu", "It helps you realize: 'They aren't withdrawing because they hate me; they are overwhelmed and need a moment to breathe.' Or: 'They are asking for reassurance because they feel insecure, not because they want to control me.'"),
        ("Tonu", "Clear, compassionate communication bridges the gap between different emotional styles."),

        # SECTION 7: MAINTAINING INDIVIDUALITY IN LOVE
        ("Solu", "Tonu, what happens when people become so absorbed in a new romance that they completely lose their own identity?"),
        ("Tonu", "Oh, that is what relationship experts call 'enmeshment' or losing yourself. They abandon their own hobbies, stop seeing their old friends, and adopt their partner's entire personality!"),
        ("Solu", "And ironically, that often destroys the very attraction that brought them together in the first place! You fell in love with a distinct, passionate individual who had their own life, dreams, and quirks."),
        ("Tonu", "Exactly! A healthy relationship is not two half-people merging into one blob. It is two complete, whole individuals standing side-by-side, holding hands while looking in the same direction."),
        ("Solu", "You need togetherness, but you also need autonomy. You need your own friendships, your own creative outlets, and your own quiet moments alone."),
        ("Tonu", "Distance and independence create the space for longing, appreciation, and fresh conversation when you reunite at the end of the day."),

        # SECTION 8: THE FIVE LOVE LANGUAGES
        ("Solu", "Let's explore another transformative framework that has saved thousands of marriages: Dr. Gary Chapman's 'The Five Love Languages'!"),
        ("Tonu", "Oh, the Five Love Languages is such a brilliant concept, Solu! Chapman noticed that people naturally express love in the way they wish to receive it, but their partner might speak a completely different love language!"),
        ("Solu", "Let's break down the five languages for our listeners. What is the first one, Tonu?"),
        ("Tonu", "The first is 'Words of Affirmation'. People with this love language thrive on verbal compliments, heartfelt letters, encouraging words, and hearing 'I appreciate you' or 'I am so proud of you.'"),
        ("Solu", "The second is 'Quality Time'. For these people, nothing says love more than full, undivided attention—no smartphone scrolling, no television in the background, just deep eye contact and shared presence."),
        ("Tonu", "The third is 'Receiving Gifts'. And this is not about materialism or monetary expense! It is about thoughtfulness—bringing someone their favorite pastry, a unique seashell you found on a walk, or a book you knew they would cherish."),
        ("Solu", "The fourth is 'Acts of Service'. Actions speak louder than words! Fixing a broken cabinet, making them coffee on a rainy morning, or doing the grocery shopping when they are swamped with work."),
        ("Tonu", "And the fifth is 'Physical Touch'—holding hands while walking, warm hugs after a stressful day, sitting close on the sofa, and physical affection."),
        ("Solu", "Imagine a husband whose primary language is Acts of Service: he spends his whole Saturday cleaning the car and fixing the roof, thinking he is being the most loving partner in the world!"),
        ("Tonu", "While his wife's primary language is Quality Time: she feels neglected and unloved because he didn't sit down and talk with her for thirty minutes! Understanding each other's language prevents so many heartbreaking misunderstandings."),

        # SECTION 9: CONFLICT RESOLUTION & GOTTMAN'S FOUR HORSEMEN
        ("Solu", "Now, let's talk about the reality of disagreements. Every couple, no matter how deeply in love they are, will inevitably experience conflict."),
        ("Tonu", "Conflict is not a sign of failure; it is an inevitable part of blending two separate lives together! The critical factor is not WHETHER you fight, but HOW you fight."),
        ("Solu", "Dr. John Gottman, who studied thousands of couples over four decades, identified what he calls 'The Four Horsemen'—the four toxic communication behaviors that predict relationship collapse."),
        ("Tonu", "What are those four behaviors, Solu?"),
        ("Solu", "The first is 'Criticism'—attacking your partner's core character rather than addressing a specific behavior. For example, instead of saying 'You forgot to take out the trash,' saying 'You are so lazy and irresponsible!'"),
        ("Tonu", "The second is 'Contempt'—mocking, eye-rolling, sneering, and making sarcastic, insulting remarks. Gottman found that contempt is the number one predictor of divorce!"),
        ("Solu", "The third is 'Defensiveness'—refusing to take any responsibility for your mistakes and immediately turning around to blame your partner."),
        ("Tonu", "And the fourth is 'Stonewalling'—completely shutting down, walking out of the room, giving the silent treatment, and refusing to communicate at all."),
        ("Solu", "The antidote to those toxic habits is simple: complain about the specific situation without blaming character, express appreciation daily, take responsibility for your 2% of the issue, and take a 20-minute calming break if your heart rate spikes above 100 beats per minute!"),

        # SECTION 10: LONG DISTANCE RELATIONSHIPS & BUILDING TRUST
        ("Tonu", "Solu, what about Long Distance Relationships? In our globalized world, so many couples have to navigate living in different cities or even different continents!"),
        ("Solu", "Long-distance relationships require immense trust, creative communication, and radical intentionality! When you can't rely on physical presence, your emotional connection must be rock-solid."),
        ("Tonu", "A great strategy for long-distance couples is scheduling 'virtual dates'—cooking the exact same pasta recipe at the same time over video call, or pressing 'play' on the same movie together."),
        ("Solu", "And having a clear 'end date'—knowing when the distance will eventually close—gives both partners a tangible beacon of hope to hold onto during lonely evenings."),

        # SECTION 11: INTERCULTURAL RELATIONSHIPS & DATING IN ENGLISH
        ("Tonu", "And speaking of our global listeners, what about Intercultural Romance—dating someone from a different country or cultural background?"),
        ("Solu", "Intercultural relationships are such a breathtaking journey of mutual discovery! You get introduced to new cuisines, family traditions, music, and perspectives on the world."),
        ("Tonu", "But it also requires an extra dose of patience and curiosity. Different cultures have very different communication styles—some cultures are very direct and speak their minds immediately, while other cultures value indirect politeness and preserving harmony."),
        ("Solu", "And if English is your shared language or one partner's second language, humor and sarcasm can sometimes get lost in translation!"),
        ("Tonu", "Yes! That is why having a playful attitude—laughing together at linguistic blunders rather than feeling offended—is the secret sauce of intercultural love."),

        # SECTION 12: HEALING A BROKEN HEART & SELF-COMPASSION
        ("Solu", "Before we move to our vocabulary, Tonu, let's address someone listening right now whose heart is aching from a recent breakup."),
        ("Tonu", "Heartbreak is one of the most intense forms of psychological pain a human can endure. Brain scans show that the agony of romantic rejection activates the exact same neural pathways as severe physical pain."),
        ("Solu", "If you are going through a breakup right now, give yourself permission to grieve. It is okay to cry, to feel sad, and to mourn the future you had envisioned."),
        ("Tonu", "Don't rush to numb the pain with unhealthy rebounds or social media stalking. Implement what therapists call the 'No Contact Rule' to give your emotional circuits time to reset and heal."),
        ("Solu", "Pour that love back into yourself: reconnect with forgotten hobbies, spend time in nature, exercise, read inspiring books, and lean on trusted friends."),
        ("Tonu", "Remember: a relationship ending does not mean you failed; it simply means that chapter is complete, and the next beautiful chapter of your life is waiting to be written."),

        # SECTION 13: VOCABULARY & IDIOM SPOTLIGHT (6 KEY IDIOMS)
        ("Tonu", "Now, it is time for our signature segment: Key Everyday English Vocabulary and Idioms! Today, we have selected six widely used romantic idioms and relationship expressions."),
        ("Solu", "Let's explore them together! Tonu, what is our very first relationship expression?"),
        ("Tonu", "Our first expression is 'hit it off'. To 'hit it off' means to immediately like someone and get along exceptionally well from the very moment you first meet them."),
        ("Solu", "Let's hear a realistic conversational example: 'I was nervous before meeting Sarah at the cafe, but we hit it off immediately and ended up talking for three straight hours!'"),
        ("Tonu", "That is a great example. What is our second expression, Solu?"),
        ("Solu", "Our second expression is 'tie the knot'. To 'tie the knot' is a classic, affectionate idiom that means to get married."),
        ("Tonu", "Here is how you can use it: 'After dating through four years of medical school, Mark and Elena finally decided to tie the knot in a small garden wedding last summer.'"),
        ("Solu", "Wonderful! Tonu, what is our third expression?"),
        ("Tonu", "Our third expression is 'head over heels'. When someone is 'head over heels' in love, it means they are deeply, intensely, and completely infatuated or in love with someone."),
        ("Solu", "For example: 'Ever since James met Priya at the conference, he has been head over heels in love; he cannot stop smiling whenever her name comes up!'"),
        ("Tonu", "So sweet! What is our fourth expression, Solu?"),
        ("Solu", "Our fourth expression describes trouble in paradise: 'on the rocks'. When a relationship, marriage, or partnership is 'on the rocks', it means it is experiencing severe difficulties, instability, or is in danger of breaking apart."),
        ("Tonu", "Let's listen to an example: 'Their marriage was on the rocks for nearly a year due to constant work stress, but working with a couples counselor helped them rebuild their trust.'"),
        ("Solu", "Important and realistic. Tonu, introduce our fifth expression."),
        ("Tonu", "Our fifth expression is 'lead someone on'. To 'lead someone on' means to encourage someone to believe you have romantic feelings for them or want a serious relationship with them, when in reality you have no true intention of committing."),
        ("Solu", "Here is a cautionary example: 'If you only view him as a casual friend, don't keep flirting with him and accepting expensive gifts; it isn't fair to lead him on.'"),
        ("Tonu", "And what is our sixth and final expression for today, Solu?"),
        ("Solu", "Our sixth expression is 'see eye to eye'. To 'see eye to eye' with someone means to completely agree with them, share the same viewpoint, or be in full alignment on important matters."),
        ("Tonu", "Let's hear an example: 'While they have very different personalities, they see eye to eye when it comes to financial planning and how they want to raise their future children.'"),

        # SECTION 9: INTERACTIVE SPEAKING PRACTICE
        ("Solu", "Now, it is time for our Interactive Speaking Challenge! Get ready to exercise your English speaking muscles. Stand tall, relax your shoulders, and repeat each phrase out loud with us with natural emotion!"),
        ("Tonu", "Sentence number one: 'We hit it off from the very first conversation and discovered we shared a passion for travel.' Your turn!"),
        ("Solu", "Say it out loud with warmth and clarity: 'We hit it off from the very first conversation and discovered we shared a passion for travel.'"),
        ("Tonu", "Fantastic job! Sentence number two: 'Open and honest communication is the foundation of any healthy long-term relationship.' Your turn!"),
        ("Solu", "Repeat it with steady confidence: 'Open and honest communication is the foundation of any healthy long-term relationship.'"),
        ("Tonu", "Excellent flow! Sentence number three: 'They don't always agree on small matters, but they see eye to eye on their core values.' Your turn!"),
        ("Solu", "Speak it clearly: 'They don't always agree on small matters, but they see eye to eye on their core values.'"),
        ("Tonu", "Sentence number four: 'It is so important to maintain your own passions and friendships even when you are head over heels in love.' Your turn!"),
        ("Solu", "Let's repeat that final sentence together: 'It is so important to maintain your own passions and friendships even when you are head over heels in love.'"),
        ("Tonu", "Brilliant work! You should be very proud of your effort today."),

        # SECTION 10: REFLECTION & FAREWELL
        ("Solu", "And now, here is today's Weekly Reflection Question! We want you to practice writing in English in the comments below."),
        ("Tonu", "Here is the question: 'What is the number one 'green flag' or positive quality that you appreciate most in a romantic partner or lifelong friend? And why is it so important to you?'"),
        ("Solu", "Is it kindness, honesty, a great sense of humor, patience, or intellectual curiosity? Let us know your thoughts in full English sentences down in the comments!"),
        ("Tonu", "We cherish every single message you write, and reading your insights brings so much warmth to our hearts."),
        ("Solu", "Remember that true love begins with loving and respecting yourself. When you know your own worth, you attract people who honor and appreciate you for who you are."),
        ("Tonu", "Keep practicing your English every single day, keep your heart open, and take wonderful care of yourself."),
        ("Solu", "Until next time, goodbye from Solu!"),
        ("Tonu", "And goodbye from Tonu!"),
        ("Both", "Happy learning, keep loving, and see you next time!")
    ]
    return turns

if __name__ == "__main__":
    t = build_ep22()
    gen_common.verify_and_save(22, "scripts/daily_speak_ep22_full.txt",
                              "Navigating Modern Dating & Finding True Love",
                              "Daily Speak English | English Listening & Speaking Practice",
                              t)
