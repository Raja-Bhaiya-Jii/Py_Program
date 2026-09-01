"""
Prime Number Checker
====================
Checks whether a number is prime and lists primes up to a limit.

Author: Om Singh Rajput
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes_up_to(limit):
    return [n for n in range(2, limit + 1) if is_prime(n)]

def main():
    try:
        n = int(input("Enter a number to check: "))
    except ValueError:
        print("Invalid number.")
        return
    if is_prime(n):
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")

    limit = int(input("List primes up to: "))
    print(primes_up_to(limit))

if __name__ == "__main__":
    main()