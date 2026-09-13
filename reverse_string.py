"""Program 8: Reverse a String
Reverses a string using slicing and a manual loop."""
def reverse_slice(s):
    return s[::-1]

def reverse_manual(s):
    rev = ""
    for ch in s:
        rev = ch + rev
    return rev

def main():
    s = input("Enter a string: ")
    print(f"Slicing: {reverse_slice(s)}")
    print(f"Manual:  {reverse_manual(s)}")

if __name__ == "__main__":
    main()
