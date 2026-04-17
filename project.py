import random
import string


def generate_password(length):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    all_chars = letters + digits + symbols
    password = ""

    for i in range(length):
        password += random.choice(all_chars)

    return password


while True:
    print("\n--- Password Generator ---")
    print("1. Generate Password")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        length = int(input("Enter password length: "))
        password = generate_password(length)
        print("Generated Password:", password)

    elif choice == "2":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")