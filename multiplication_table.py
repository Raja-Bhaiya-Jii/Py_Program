"""Program 11: Multiplication Table
Generates a multiplication table for a given number."""
def multiplication_table(n, upto=10):
    for i in range(1, upto + 1):
        print(f"{n} x {i} = {n * i}")

def main():
    n = int(input("Enter a number: "))
    multiplication_table(n)

if __name__ == "__main__":
    main()
