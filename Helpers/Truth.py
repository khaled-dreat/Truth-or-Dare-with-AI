import random

def Truth():
    print("Player chose Truth")
    print("A Random Truth Questions will be Given")

    Question = {1: "What is your favorite Color ?",
                2: "What do you do in your free time ?",
                3: "How many times you eat a day ?",
                4: "When was the last time you lied?",
                5: "What's your biggest fear?",
                6: "What's the worst thing you've ever done?",
                7: "Do you have a hidden talent?",
                8: "Who was your first celebrity crush?",
                9: "hat's the most drunk you've ever been?",
                10: "Have you ever cheated in an exam?",
                11: "What's the worst thing you've ever said to anyone?",
                12: "What's your worst habit?",
                13: "What's the biggest mistake you've ever made?",
                14: "What's the strangest dream you've had?",
                15: "What's the biggest misconception about you?",
                16: "What's the most trouble you've been in?",
                17: "What's the biggest misconception about you?",
                18: "What's your biggest regret?",
                19: "What's the strangest dream you've had?",
                20: "What is your favorite Color",
                21: "What is your favorite Color",
                22: "What is your favorite Color",
                23: "What is your favorite Color",
                24: "What is your favorite Color",
                25: "What is your favorite Color",
                26: "What is your favorite Color",
                27: "What is your favorite Color",
                28: "What is your favorite Color",
                29: "What is your favorite Color",
                30: "What is your favorite Color"}

    Randomize = random.choice(list(Question))

    return(Question[Randomize])



