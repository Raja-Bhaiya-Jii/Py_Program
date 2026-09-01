"""
Word Counter
============
Counts words, lines, and characters in a text.

Author: Om Singh Rajput
"""

def count_stats(text):
    words = text.split()
    lines = text.splitlines()
    chars = len(text)
    return len(words), len(lines), chars

def main():
    print("Enter your text (press Enter twice to finish):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    text = "\n".join(lines)
    words, line_count, chars = count_stats(text)
    print(f"Words: {words}")
    print(f"Lines: {line_count}")
    print(f"Characters: {chars}")

if __name__ == "__main__":
    main()