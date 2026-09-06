"""
Day 15: Password Generator
A command-line password generator that creates strong, random passwords
with customizable length and character set options.
"""

import random
import string
import argparse


def generate_password(length=12, use_upper=True, use_lower=True,
                      use_digits=True, use_symbols=True,
                      exclude_ambiguous=False):
    """Generate a random password with the specified options.

    Args:
        length: Password length (minimum 4).
        use_upper: Include uppercase letters (A-Z).
        use_lower: Include lowercase letters (a-z).
        use_digits: Include digits (0-9).
        use_symbols: Include special characters (!@#$%^&*...).
        exclude_ambiguous: Exclude ambiguous characters like l, 1, O, 0, I.

    Returns:
        A randomly generated password string.
    """
    if length < 4:
        raise ValueError("Password length must be at least 4.")

    ambiguous = set("l1O0I`'\"|")

    pools = []
    required = []

    if use_lower:
        pool = string.ascii_lowercase
        if exclude_ambiguous:
            pool = "".join(c for c in pool if c not in ambiguous)
        pools.append(pool)
        required.append(random.choice(pool))

    if use_upper:
        pool = string.ascii_uppercase
        if exclude_ambiguous:
            pool = "".join(c for c in pool if c not in ambiguous)
        pools.append(pool)
        required.append(random.choice(pool))

    if use_digits:
        pool = string.digits
        if exclude_ambiguous:
            pool = "".join(c for c in pool if c not in ambiguous)
        pools.append(pool)
        required.append(random.choice(pool))

    if use_symbols:
        pool = "!@#$%^&*()-_=+[]{};:,.<>?/~"
        pools.append(pool)
        required.append(random.choice(pool))

    if not pools:
        raise ValueError("At least one character set must be selected.")

    all_chars = "".join(pools)
    remaining = length - len(required)
    password_chars = required + [random.choice(all_chars) for _ in range(remaining)]
    random.shuffle(password_chars)
    return "".join(password_chars)


def password_strength(password):
    """Estimate password strength on a scale of 1-5."""
    score = 0
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in "!@#$%^&*()-_=+[]{};:,.<>?/~" for c in password):
        score += 1
    labels = ["Very Weak", "Weak", "Fair", "Good", "Strong", "Very Strong"]
    return labels[min(score, 5)]


def main():
    parser = argparse.ArgumentParser(description="Generate a strong random password.")
    parser.add_argument("-l", "--length", type=int, default=12, help="Password length (default: 12)")
    parser.add_argument("--no-upper", action="store_true", help="Exclude uppercase letters")
    parser.add_argument("--no-lower", action="store_true", help="Exclude lowercase letters")
    parser.add_argument("--no-digits", action="store_true", help="Exclude digits")
    parser.add_argument("--no-symbols", action="store_true", help="Exclude special characters")
    parser.add_argument("--exclude-ambiguous", action="store_true", help="Exclude ambiguous chars (l, 1, O, 0, I)")
    parser.add_argument("-n", "--count", type=int, default=1, help="Number of passwords to generate")
    args = parser.parse_args()

    for i in range(args.count):
        pwd = generate_password(
            length=args.length,
            use_upper=not args.no_upper,
            use_lower=not args.no_lower,
            use_digits=not args.no_digits,
            use_symbols=not args.no_symbols,
            exclude_ambiguous=args.exclude_ambiguous,
        )
        strength = password_strength(pwd)
        print(f"Password {i + 1}: {pwd}  (Strength: {strength})")


if __name__ == "__main__":
    main()