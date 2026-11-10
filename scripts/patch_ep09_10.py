with open("scripts/generate_episodes_09_10.py", "r") as f:
    code = f.read()

# Additions to EP09
target_09 = '    ("Solu", "Now, let\'s dive into our special English vocabulary section! Let\'s explore seven powerful everyday idioms and expressions related to dreams, ambition, and personal development."),'
add_09 = '''    ("Tonu", "Let's also talk about the incredible power of having an Accountability Partner!"),
    ("Solu", "Oh, an accountability partner! The American Society of Training and Development found that having a specific accountability appointment with a partner increases your chances of achieving a goal to ninety-five percent!"),
    ("Tonu", "Ninety-five percent! That is astonishing. When you only keep a goal inside your own head, it is so easy to negotiate with yourself and quit on a cold morning."),
    ("Solu", "Right! 'Oh, I am too tired today, I will start next Monday.' But when you know your accountability partner is waiting for your check-in text at eight in the morning, you get out of bed!"),
    ("Tonu", "And how should people handle critics, skeptics, and naysayers who mock their dreams?"),
    ("Solu", "Remember Theodore Roosevelt's famous speech, 'The Man in the Arena'! The credit belongs to the person who is actually in the arena, whose face is marred by dust and sweat, who strives valiantly."),
    ("Tonu", "Not to the critic sitting comfortably in the cheap seats pointing out where the doer stumbled!"),
    ("Solu", "People who criticize your big dreams are almost always people who gave up on their own dreams. Never take advice about swimming from someone who never got into the water!"),
    ("Tonu", "And let's touch upon the 'Upper Limit Problem' described by author Gay Hendricks."),
    ("Solu", "The Upper Limit Problem! That is such a psychological eye-opener. Why do people self-sabotage when things start going really well in their life?"),
    ("Tonu", "Because each of us has an internal thermostat for how much happiness, love, and success we believe we deserve!"),
    ("Solu", "So when life gets better than our old thermostat setting, our subconscious gets anxious and triggers an argument, gets sick, or makes a careless mistake to bring us back down to familiar comfort!"),
    ("Tonu", "Recognizing that self-sabotage allows you to consciously expand your capacity for joy, abundance, and success."),
    ("Solu", "Now, let's dive into our special English vocabulary section! Let's explore seven powerful everyday idioms and expressions related to dreams, ambition, and personal development."),'''

code = code.replace(target_09, add_09)

# Additions to EP10
target_10 = '    ("Solu", "Now, let\'s explore our special English vocabulary section! Let\'s examine seven essential, cutting-edge expressions and idioms related to technology, innovation, and modern life."),'
add_10 = '''    ("Tonu", "Let's also dive into the critical topic of digital privacy, cyber hygiene, and protecting yourself online!"),
    ("Solu", "Oh, digital security is paramount today! Every website we visit, every app we install, and every search query we type leaves a digital footprint."),
    ("Tonu", "Data broker companies build massive psychological profiles of our spending habits, political views, and daily routines to target us with manipulative ads!"),
    ("Solu", "So what are three essential digital hygiene rules everyone should follow today, Tonu?"),
    ("Tonu", "Rule number one: use a dedicated password manager and create complex, unique passwords for every account. Never use the same password across multiple websites!"),
    ("Solu", "Rule number two: enable Two-Factor Authentication, or 2FA, on every email, banking, and social media account. An authenticator app adds an ironclad layer of defense!"),
    ("Tonu", "And rule number three: be extremely cautious with public Wi-Fi networks in cafes and airports! Use a virtual private network, or VPN, to encrypt your data."),
    ("Solu", "Now let's talk about deepfakes, voice cloning, and media literacy in the age of generative video!"),
    ("Tonu", "Yes! We have reached a point where AI can generate photorealistic videos of world leaders saying things they never said, or clone a family member's voice to attempt financial phone scams!"),
    ("Solu", "The old saying was 'Seeing is believing.' In the AI era, seeing is no longer proof!"),
    ("Tonu", "How can people cultivate critical media literacy?"),
    ("Solu", "Always verify shocking news before sharing it! Check reliable, verified journalistic outlets, use reverse image search, and look for primary sources. If an emotional video seems designed to make you instantly enraged, pause and investigate!"),
    ("Tonu", "And what about the fascinating intersection between AI and human creativity? Can artificial intelligence create real art and music?"),
    ("Solu", "AI can certainly compose a catchy melody or generate a stunning painting by recognizing mathematical patterns in millions of previous human works."),
    ("Tonu", "But what gives art its profound soul is the human experience behind it! The artist's mortal struggles, their broken hearts, their personal grief, and their triumphs."),
    ("Solu", "A computer has never experienced heartbreak, has never watched a parent grow old, and has never looked at a newborn baby with tears of joy."),
    ("Tonu", "AI is a magnificent creative co-pilot—a digital paintbrush—but the true soul and creative intent will always remain uniquely human!"),
    ("Solu", "And let's look at the future of education and global work. Virtual reality, real-time speech translation, and remote collaboration are turning our planet into a global village."),
    ("Tonu", "A young student in Bangladesh, Brazil, or Kenya can now collaborate on a robotics project with engineers in Tokyo and London in real time!"),
    ("Solu", "Geographic location is no longer your destiny. If you have an internet connection, curiosity, and English communication skills, the entire world is your playground."),
    ("Tonu", "Now, let's explore our special English vocabulary section! Let's examine seven essential, cutting-edge expressions and idioms related to technology, innovation, and modern life."),'''

code = code.replace(target_10, add_10)

with open("scripts/generate_episodes_09_10.py", "w") as f:
    f.write(code)

