"""Program 10: Sum of Digits
Calculates the sum of digits of a number."""
def sum_of_digits(n):
    return sum(int(d) for d in str(abs(n)))

def main():
    n = int(input("Enter a number: "))
    print(f"Sum of digits: {sum_of_digits(n)}")

if __name__ == "__main__":
    main()
