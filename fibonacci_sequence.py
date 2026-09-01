"""
Fibonacci Sequence Generator
============================
Generates the Fibonacci sequence up to n terms.

Author: Om Singh Rajput
"""

def fibonacci(n):
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

def main():
    try:
        n = int(input("How many Fibonacci terms? "))
    except ValueError:
        print("Invalid number.")
        return
    if n <= 0:
        print("Enter a positive integer.")
        return
    print(fibonacci(n))

if __name__ == "__main__":
    main()