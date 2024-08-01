import random
import string


def generate_password(length, include_uppercase, include_lowercase, include_digits, include_special):
    if not any([include_uppercase, include_lowercase, include_digits, include_special]):
        print("Error: At least one character type must be selected.")
        return None

    character_pool = ''
    if include_uppercase:
        character_pool += string.ascii_uppercase
    if include_lowercase:
        character_pool += string.ascii_lowercase
    if include_digits:
        character_pool += string.digits
    if include_special:
        character_pool += string.punctuation

    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password


def main():
    try:
        length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return

    include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
    include_lowercase = input("Include lowercase letters? (yes/no): ").strip().lower() == 'yes'
    include_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
    include_special = input("Include special characters? (yes/no): ").strip().lower() == 'yes'

    password = generate_password(length, include_uppercase, include_lowercase, include_digits, include_special)

    if password:
        print(f"Generated password: {password}")


if __name__ == "__main__":
    main()
