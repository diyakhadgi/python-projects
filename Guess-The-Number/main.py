#for computer to generate random number

import random

def guess(x):
    # generates random number
    random_number = random.randint(1, x) 
    guess = 0
    while guess != random_number:
        guess = int(input(f"guess a number between 1 and {x}: "))
        if guess < random_number:
            print("sorry, guess again. Too low")
        elif guess > random_number:
            print("sorry, guess again. Too high")
        else:
            print("You won.")
guess(10)

