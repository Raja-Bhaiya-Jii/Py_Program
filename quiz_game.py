"""
Day 14: Quiz Game
A simple multiple-choice quiz game with scoring.
"""

import json

QUESTIONS = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "New Delhi", "Kolkata", "Chennai"],
        "answer": 1,
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Venus", "Jupiter", "Mars", "Saturn"],
        "answer": 2,
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"],
        "answer": 1,
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["African Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
        "answer": 1,
    },
    {
        "question": "In which year did India gain independence?",
        "options": ["1945", "1946", "1947", "1948"],
        "answer": 2,
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["Go", "Gd", "Au", "Ag"],
        "answer": 2,
    },
    {
        "question": "Which is the longest river in the world?",
        "options": ["Amazon", "Nile", "Ganga", "Yangtze"],
        "answer": 1,
    },
    {
        "question": "How many continents are there on Earth?",
        "options": ["5", "6", "7", "8"],
        "answer": 2,
    },
]


def run_quiz():
    print("=" * 50)
    print("          WELCOME TO THE QUIZ GAME!")
    print("=" * 50)
    print(f"You will answer {len(QUESTIONS)} questions.\n")

    score = 0

    for i, q in enumerate(QUESTIONS, start=1):
        print(f"Q{i}: {q['question']}")
        for idx, opt in enumerate(q["options"]):
            print(f"  {idx + 1}. {opt}")

        while True:
            try:
                choice = int(input("\nYour answer (1-4): "))
                if 1 <= choice <= len(q["options"]):
                    break
                print(f"Please enter a number between 1 and {len(q['options'])}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        if choice - 1 == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            correct = q["options"][q["answer"]]
            print(f"❌ Wrong! The correct answer is: {correct}\n")

    print("=" * 50)
    print(f"  QUIZ OVER! You scored {score}/{len(QUESTIONS)}")
    percentage = (score / len(QUESTIONS)) * 100
    if percentage == 100:
        print("  🏆 Perfect score! You're a genius!")
    elif percentage >= 75:
        print("  🌟 Great job!")
    elif percentage >= 50:
        print("  👍 Good effort! Keep learning.")
    else:
        print("  📚 Keep practicing, you'll get there!")
    print("=" * 50)


if __name__ == "__main__":
    run_quiz()
