import random
number = random.randint(1, 10)
guesses = 5
while guesses > 0:
    num = int(input("What's a number from 1 to 10-"))
    if num > number:
        print("Lower!")
        guesses = guesses - 1
    elif num < number:
        print("Higher!")
        guesses = guesses - 1
    elif num == number:
        print("Correct!")
        guesses = 0


