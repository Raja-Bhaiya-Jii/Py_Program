"""
Rock Paper Scissors
===================
Play rock-paper-scissors against the computer.

Author: Om Singh Rajput
"""

import random

CHOICES = ["rock", "paper", "scissors"]

def determine_winner(player, computer):
    if player == computer:
        return "Tie"
    wins = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    if wins[player] == computer:
        return "You win!"
    return "Computer wins!"

def main():
    print("=== Rock Paper Scissors ===")
    while True:
        player = input("Enter rock/paper/scissors (or 'quit'): ").lower()
        if player == "quit":
            print("Thanks for playing!")
            break
        if player not in CHOICES:
            print("Invalid choice.")
            continue
        computer = random.choice(CHOICES)
        print(f"Computer chose: {computer}")
        print(determine_winner(player, computer))

if __name__ == "__main__":
    main()