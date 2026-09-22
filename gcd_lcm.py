"""Program 18: GCD and LCM Calculator
Computes the greatest common divisor and least common multiple."""

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b) if a and b else 0

def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(f"GCD: {gcd(a, b)}")
    print(f"LCM: {lcm(a, b)}")

if __name__ == "__main__":
    main()
