import random
import string

def generate_password(length=12):
    if length < 6:
        raise ValueError("Password length should be at least 6 characters.")

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits)
    ]

    all_chars = lowercase + uppercase + digits
    password += random.choices(all_chars, k=length - len(password))

    random.shuffle(password)

    return ''.join(password)

print("Generated Password:", generate_password(12))
