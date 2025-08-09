import random
cnPrompts = ['mountain', 'river', 'ocean', 'bridge',
             'factory', 'city', 'glass', 'pen', 'schoolbus',
             'train', 'island', 'hotel', 'pancake', 'underwear',
             'wine', 'basin', 'seat', 'head', 'badge', 'basketball',
             'football', 'soccer', 'foot', 'goat', 'conditioner',
             'soda', 'beetle', 'bean', 'cracker', 'snapchat', 'highlighter', 'trampoline', 'fortune cookie',
             'opera', 'arts and crafts', 'exercise', 'math', 'blizzards', 'extra credit', 'zebra', 'meme', 'ultimate frisbee', 'printer ink',
             'iPad', 'silly putty', 'keychain', 'frozen yogurt', 'paper clip', 'lifesaver', 'hand sanitizer',
             'true leadership', 'corporate','post office', 'telescope', 'umbrella', 'cactus', 'violin', 'lighthouse',
             'skateboard', 'teapot', 'microscope', "hammock", 'toaster', 'chandelier', 'snowglobe', 'pinwheel', 'typewriter', 'pinwheel',
             "rubik's cube", 'lava lamp', 'tambourine', 'chessboard', 'xylophone', 'boomerang', 'abacus', 'origami', 'ukulele',
             'windmill', 'ferris wheel', 'kaleidoscope', 'sundial', 'hammock', 'toaster', 'skateboard', 'lighthouse', ' backpack',
             'canoe', 'easel', 'globe', 'harmonica', 'ice cream cone', 'jigsaw puzzle', 'kite', 'easel', 'mug', 'nail polish', 'octopus', 'piano'
             'globe', 'canoe', 'yoyo', 'whistle', 'telescope', 'quilt', 'ladder', 'sculpture',]
anPrompts = ["anxiety", "fear", "anger", "beauty", "charity",
                 "beliefs", "confusion", "chaos", "despair", "comfort",
                 "communication", "democracy", "interest", "knowledge",
                 "sacrifice", "opportunity", "loyalty", "wisdom",
                 "trust", "sorrow", "pessimism", "generosity", "grief",
                 "overwork", "stress", "satisfaction", "pleasure",
                 "luxury", "freedom", "bravery", "brilliance",
                 "behavior", "brutality", 'nostalgia', 'zeal', 'empathy',
                 'awe', 'ambiguity', 'transcendence', 'quiescence', 'melancholy',
                 'ebullience', 'elation', 'equanimity', 'reverence', 'apathy',
                 'euphoria', 'courage', 'integrity', 'harmony', 'faith', 'justice',
             'patience', 'humility', 'creativity', 'inspiration', 'solitude', 'hope', 'compassion',
             'vulnerability', 'ambition', 'curiosity', 'resilience', 'clarity', 'sentiment', 'tranquility',
             'unity', 'gratitude', 'intuition', 'commitment', 'reflection', 'serenity', 'authenticity', 'tenacity', 'eagerness', 'anxiety',
             'passion', 'deliberation', 'whimsy', 'fortitude', 'liberation', 'satisfaction', 'deception', 'enlightenment',
             'simplicity', 'frustration', 'indifference', 'composure', 'enthusiasm', 'contentment', 'isolation', 'motivation',
             'dread', 'bliss', 'intensity', 'disillusionment', 'collaboration', 'authenticity', 'intimacy', 'vulnerability', 'clarity', 'tenacity',
             'enigma', 'desperation', 'elation', 'innovation']
fpPrompts = ['Harry Styles', "Cristiano Ronaldo", "Lionel Messi",
                 "David Beckham", "Neymar Jr.", "Kylian Mbappe",
                 'Patrick Mahomes', "Tom Brady", 'Selena Gomez',
                 "Dwayne Johnson (the rock)", 'Kim Kardashian',
                 'Ariana Grande', 'Beyonce', 'Jennifer Lopez',
                 'Taylor Swift', 'Virat Kohli', 'Katy Perry',
                 'Miley Cyrus', 'Steve Jobs', 'Nelson Mandela',
                 "Albert Einstein", 'Maya Angelou',
                 'Martin Luther King Jr.', 'Malala Yousafzai',
                 'Stephen Hawking', "Barack Obama", 'Greta Thunberg',
                 'Malcolm X', "Abraham Lincoln", "Helen Keller",
                 "Franklin D. Roosevelt", "Rosa Parks",
                 "Elon Musk", "Oprah Winfrey", "J.K. Rowling",
                 "Socrates", "Lady Gaga", "Michael Jordan",
                 "Serena Williams", "Muhammad Ali", "Kamala Harris",
                 'Donald Trump', "Brene Brown", "Leonardo di Caprio", "Emma Watson",
             "Bill Gates", "Ellen deGeneres", "Bob Marley", "Michelle Obama", "Freddie Mercury",
             "Jane Goodall", "Winston Churchill", "Frida Kahlo", "Pablo Picasso", "Galileo Galilei", "Stephen King",
             "Mark Zuckerberg", "Kobe Bryant", "Adele", "Harrison Ford", "Billie Eilish", "Nelson Mandela",
             "Charles Darwin", "Anne Frank", "Marie Curie", "Henry Ford", "Catherine the Great", "Jimi Hendrix", "Keanu Reeves",
             "Hedy Lamarr", "Kendrick Lamar", "Gordon Ramsay"]
cePrompts = ["The US Congress", 'Cybersecurity', "Apple", "Peace in the Middle East", "The Presidential Election", "Ukraine", "Private Space Travel",
                 "CIA", "The Stock Market", "Tech Regulations", "Social Media's Influence", "COP28 Climate Summit", "Earthquake in Turkey", "Presidential Election", ]
qPrompts = ['Maya Angelou: “You will face many defeats in life, but never let yourself be defeated."','Nelson Mandela: “It always seems impossible until it’s done.”',
            'Albert Einstein: “Imagination is more important than knowledge.”', 'Martin Luther King Jr.: “The time is always right to do what is right.”',
            'Socrates: “The unexamined life is not worth living.”', 'Winston Churchill: “Success is not final, failure is not fatal: It is the courage to continue that counts.”',
            'Steve Jobs: “Your time is limited, don’t waste it living someone else’s life.”', 'Mahatma Gandhi: “Be the change that you wish to see in the world.”',
            'Brene Brown: “Vulnerability is the birthplace of innovation, creativity, and change.”','Ruth Bader Ginsburg: “Real change, enduring change, happens one step at a time.”',
            'Eleanor Roosevelt: “You gain strength, courage, and confidence by every experience in which you really stop to look fear in the face.”',
            'Malala Yousafzai: “I raise up my voice—not so that I can shout, but so that those without a voice can be heard.”',
            'Confucius: “Real knowledge is to know the extent of one’s ignorance.',
            'Isaac Asimov: “The saddest aspect of life right now is that science gathers knowledge faster than society gathers wisdom.”', 'Anonymous: “Knowledge speaks, but wisdom listens.”',
            'Anonymous: “Courage is not the absence of fear, but the triumph over it.”','Anonymous: “The future belongs to those who believe in the beauty of their dreams.”',
            'Anonymous: “The only limit to our realization of tomorrow will be our doubts of today.”', '“There’s no one I’d rather be than me.” Wreck-It Ralph',
            'Peter Pan:“All it takes is faith and trust.”','Snow White: “You’re never too old to be young.”','Albus Dumbledore: "It takes a great deal of bravery to stand up to our enemies, but just as much to stand up to our friends."',
            'Albus Dumbledore: It matters not what someone is born, but what they grow to be.', 'Albus Dumbledore: The truth. It is a beautiful and terrible thing, and should therefore be treated with great caution.',
            'Arnold Palmer: "Always make a total effort, even when the odds are against you."', 'Wayne Gretzky: "You miss 100% of the shots you don’t take."'
            'Lord of the Rings: "There’s some good in this world, Mr. Frodo, and it’s worth fighting for!"', 'Master Oogway: "Yesterday is a history, tomorrow is a mystery, but today is a gift. That is why it is called the “present!”"',
            'Yoda: "Do, or do not. There is no “try.”"', 'Dead Poets Society, Professor Keating: "Seize the day… make your lives extraordinary."', 'Albert Einstein: “Creativity is intelligence having fun.”',
            'Albert Einstein: “At least once a day, allow yourself the freedom to think and dream for yourself.”', 'Albert Einstein: “The more I learn, the more I realize how much I don’t know.”',
            'Albert Einstein: “Life is like riding a bicycle. To keep your balance, you must keep moving.”', 'Albert Einstein: “Genius is 1% talent and 99% percent hard work.”',
            'Albert Einstein: “If you can’t explain it to a six year old, you don’t understand it yourself.”', 'Mike Ditka: "You’re never a loser until you quit trying."',
            'Lou Brock: "Show me a guy who’s afraid to look bad, and I’ll show you a guy you can beat every time"', 'J.K. Rowling: "If you don’t like to read, you haven’t found the right book."',
            'Shrek: "After awhile, you learn to ignore the names people call you and just trust who you are."', 'Winnie the Pooh: “You are braver than you believe, stronger than you seem, and smarter than you think.”',
            'Pinnochio: “The most fantastic, magical things can happen, and it all starts with a wish.”', 'Mary Poppins: “Open different doors, you may find a you there that you never knew was yours. Anything can happen.”',
            'Peter Pan: “All it takes is faith and trust.”', 'Chris Gardner, The Pursuit of Happyness: "Don’t ever let somebody tell you, you can’t do something, not even me… If you want something, go get it. Period."',
            'The Emperor in Mulan: "The flower that blooms in adversity is the most rare and beautiful of all"', 'Albert Einstein: “What is right is not always popular and what is popular is not always right.”',
            ]
   
def promptSelection(prompt_list):
    x, y, z = random.sample(prompt_list, 3)
    print(x)
    print(y)
    print(z)


def promptCN():
    promptSelection(cnPrompts)

def promptAN():
    promptSelection(anPrompts)

def promptFP():
    promptSelection(fpPrompts)

def promptCE():
    promptSelection(cePrompts)

def promptQ():
    promptSelection(qPrompts)

def promptAll():
    combinedList = cnPrompts + anPrompts + fpPrompts + cePrompts + qPrompts
    promptSelection(combinedList)

prompt_functions = {
    "AN": promptAN,
    "CN": promptCN,
    "FP": promptFP,
    "Q": promptQ,
    "CE": promptCE,
    "random": promptAll
   
}
   


promptInput = input("Which type of prompt? Type AN for abstract noun, CN for common noun, FP for famous people, Q for quotes,CE for current events or random for some random ones: ")

if promptInput in prompt_functions:
    prompt_functions[promptInput]()
else:
    print("Invalid input. Please enter AN, CN, Q, CE or FP.")
