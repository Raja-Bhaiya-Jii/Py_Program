"""
Number Guessing Game
====================
The computer picks a random number and the player tries to guess it.

Author: Om Singh Rajput
"""

import random

def main():
    secret = random.randint(1, 100)
    attempts = 0
    print("Guess a number between 1 and 100!")

    while True:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Enter a valid number.")
            continue

        attempts += 1
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break

if __name__ == "__main__":
    main()