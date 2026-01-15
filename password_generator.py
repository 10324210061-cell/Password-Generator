import secrets
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4.")
        return None

    # Character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Make sure password has all types of characters
    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]

    # Combine all characters
    all_chars = lowercase + uppercase + digits + symbols

    # Fill remaining length
    for _ in range(length - 4):
        password.append(secrets.choice(all_chars))

    # Shuffle for randomness
    secrets.SystemRandom().shuffle(password)

    # Convert list to string
    return "".join(password)


# Main program
try:
    length = int(input("Enter the length of the password: "))
    result = generate_password(length)

    if result:
        print("Generated Strong Password:", result)
except ValueError:
    print("Please enter a valid number.")
