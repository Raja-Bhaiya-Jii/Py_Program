"""
Palindrome Checker
==================
Checks whether a given string is a palindrome.

Author: Om Singh Rajput
"""

def is_palindrome(text):
    cleaned = "".join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]

def main():
    text = input("Enter a word or phrase: ")
    if is_palindrome(text):
        print(f"'{text}' is a palindrome!")
    else:
        print(f"'{text}' is not a palindrome.")

if __name__ == "__main__":
    main()