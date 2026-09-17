"""Program 12: Largest of Three Numbers
Finds the largest among three numbers."""
def largest(a, b, c):
    return max(a, b, c)

def main():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    c = float(input("Enter third number: "))
    print(f"Largest: {largest(a, b, c)}")

if __name__ == "__main__":
    main()
