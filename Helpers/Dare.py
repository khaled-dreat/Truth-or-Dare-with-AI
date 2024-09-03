import random

def Dare():
    print("Player chose Dare")
    print("A Random Dare will be Given")

    Question = {1: "Show the most embarrassing photo on your phone",
                2: "Show the last five people you texted and what the messages said",
                3: "Let the rest of the group DM someone from your Instagram account",
                4: "Eat a raw piece of garlic",
                5: "Do 100 squats",
                6: "Keep three ice cubes in your mouth until they melt ",
                7: "Say something dirty to the person on your left",
                8: "Give a foot massage to the person on your right",
                9: "Put 10 different available liquids into a cup and drink it ",
                10: "Yell out the first word that comes to your mind",
                11: "Eat a spoonful of mustard",
                12: "Keep your eyes closed until it's your go again",
                13: "Empty out your wallet/purse and show everyone what's inside",
                14: "Pretend to be the person to your right for 10 minutes",
                15: "Try and make the group laugh as quickly as possible",
                16: "Tell everyone an embarrassing story about yourself",
                17: "Try to lick your elbow",
                18: "Tell the saddest story you know",
                19: "Howl like a wolf for two minutes",
                20: "Dance without music for two minutes",
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



