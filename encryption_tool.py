# Day 16: Caesar Cipher Encryption Tool
# A simple command-line tool to encrypt and decrypt messages using the Caesar cipher

def encrypt(text, shift):
    """Encrypt text using Caesar cipher with the given shift value."""
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26
            result += chr(shifted + base)
        else:
            result += char
    return result


def decrypt(text, shift):
    """Decrypt text that was encrypted with the given shift value."""
    return encrypt(text, -shift)


def brute_force(text):
    """Try all 26 possible shifts to crack an encrypted message."""
    print("\n--- Brute Force Decryption ---")
    for shift in range(1, 26):
        print(f"  Shift {shift:2d}: {decrypt(text, shift)}")


def main():
    print("=" * 50)
    print("    CAESAR CIPHER ENCRYPTION TOOL")
    print("=" * 50)

    while True:
        print("\nOptions:")
        print("  1. Encrypt a message")
        print("  2. Decrypt a message")
        print("  3. Brute-force decrypt (try all shifts)")
        print("  4. Exit")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == '1':
            message = input("Enter the message to encrypt: ")
            try:
                shift = int(input("Enter the shift value (1-25): "))
                if not 1 <= shift <= 25:
                    print("Shift must be between 1 and 25.")
                    continue
            except ValueError:
                print("Invalid shift value. Please enter a number.")
                continue
            encrypted = encrypt(message, shift)
            print(f"\n  Encrypted message: {encrypted}")

        elif choice == '2':
            message = input("Enter the message to decrypt: ")
            try:
                shift = int(input("Enter the shift value used for encryption: "))
            except ValueError:
                print("Invalid shift value. Please enter a number.")
                continue
            decrypted = decrypt(message, shift)
            print(f"\n  Decrypted message: {decrypted}")

        elif choice == '3':
            message = input("Enter the encrypted message: ")
            brute_force(message)

        elif choice == '4':
            print("\nGoodbye!")
            break

        else:
            print("Invalid choice. Please select 1-4.")


if __name__ == "__main__":
    main()