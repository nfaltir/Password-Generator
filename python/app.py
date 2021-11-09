import random
print("\n=====================PASSWORD GENERATOR=====================\n")
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_-=+`~[{]}\\|:;,./?"
password_length = int(input("Enter password length (Enter 0 to quit): "))
while password_length != 0:
    password_count = int(input("How many new passwords you want to generate: "))
    for x in range (0, password_count):
        password = ""
        for x in range(0, password_length):
            password_character = random.choice(characters)
            password = password + password_character
        print(f"\nNew Password: {password}\n")
    password_length = int(input("Enter password length (Enter 0 to quit): "))



