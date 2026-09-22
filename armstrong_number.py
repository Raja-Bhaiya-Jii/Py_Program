"""Program 17: Armstrong Number Checker
Checks if a number is an Armstrong number."""

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n

def main():
    n = int(input("Enter a number: "))
    if is_armstrong(n):
        print(f"{n} is an Armstrong number")
    else:
        print(f"{n} is not an Armstrong number")

if __name__ == "__main__":
    main()
