"""
File Operations
===============
Demonstrates reading, writing, and appending to files.

Author: Om Singh Rajput
"""

def write_file(filename, content):
    with open(filename, "w") as f:
        f.write(content)
    print(f"Written to {filename}")

def read_file(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: {filename} not found"

def append_file(filename, content):
    with open(filename, "a") as f:
        f.write(content)
    print(f"Appended to {filename}")

def main():
    filename = "sample.txt"
    write_file(filename, "Hello, World!\n")
    append_file(filename, "This is an appended line.\n")
    print("File contents:\n" + read_file(filename))

if __name__ == "__main__":
    main()