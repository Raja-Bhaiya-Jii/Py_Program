"""Program 9: Count Vowels
Counts the number of vowels in a string."""
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in s if ch in vowels)

def main():
    s = input("Enter a string: ")
    print(f"Number of vowels: {count_vowels(s)}")

if __name__ == "__main__":
    main()
