"""Program 19: Star Pyramid Pattern
Prints a pyramid of stars of height n."""

def pyramid(n):
    for i in range(1, n + 1):
         spaces = " " * (n - i)
         stars = "*" * (2 * i - 1)
         print(spaces + stars)

def main():
    n = int(input("Enter pyramid height: "))
    pyramid(n)

if __name__ == "__main__":
    main()
