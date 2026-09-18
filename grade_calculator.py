"""Program 13: Grade Calculator
Assigns a letter grade based on a score."""
def get_grade(score):
    if score >= 90: return "A"
    if score >= 80: return "B"
    if score >= 70: return "C"
    if score >= 60: return "D"
    return "F"

def main():
    score = float(input("Enter score (0-100): "))
    print(f"Grade: {get_grade(score)}")

if __name__ == "__main__":
    main()
