# Project 3: Random Password Generator
# Created By: Nandani Patidar

import random
import string

print("===== Random Password Generator =====")

keyword = input("Enter a keyword: ")
birthdate = input("Enter your birth date (DDMMYYYY): ")

length = int(input("Enter password length (8-20): "))

if length < 8 or length > 20:
    print("Error: Password length must be between 8 and 20 characters.")
else:
    special_chars = "!@#$%^&*"

    # Create a base password using keyword and birth year
    password = keyword[:3] + birthdate[-4:]

    # Add random characters until the required length is reached
    while len(password) < length:
        password += random.choice(
            string.ascii_letters +
            string.digits +
            special_chars
        )

    # Shuffle the password for better security
    password_list = list(password)
    random.shuffle(password_list)

    final_password = "".join(password_list)

    print("\n===== Password Generated Successfully =====")
    print("strong Password :", final_password)
    print("Length   :", len(final_password))