"""Program 3: Even or Odd Checker
Checks if a number is even or odd."""
def is_even(n):
    return n % 2 == 0

def main():
    n = int(input("Enter a number: "))
    if is_even(n):
        print(f"{n} is even")
    else:
        print(f"{n} is odd")

if __name__ == "__main__":
    main()
