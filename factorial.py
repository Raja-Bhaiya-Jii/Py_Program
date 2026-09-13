"""Program 7: Factorial Calculator
Computes factorial using both recursion and iteration."""
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def main():
    n = int(input("Enter a number: "))
    print(f"Recursive: {factorial_recursive(n)}")
    print(f"Iterative: {factorial_iterative(n)}")

if __name__ == "__main__":
    main()
