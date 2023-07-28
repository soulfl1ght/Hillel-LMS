import random

def rannum():
    randnum = random.randint(1, 10)

    while True:
        guess = int(input("Try to guess a number in a range from 1 to 10: "))

        if guess == randnum:
            print("Congratulations! You`ve guessed the number!.")
            break
        else:
            print("Oops! Mistake!")

rannum()
