def guessingGame():

    import random

    num = random.randint(1,9)
    guess = 0
    count = 0

    while guess != num and guess != "exit":
        guess = input("Guess")
