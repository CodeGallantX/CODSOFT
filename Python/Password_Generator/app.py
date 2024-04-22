# This is my Password Generator project for CODSOFT Internship programme

import random
import string


def gen_pswd(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("Gorilla Guard here, let's generate passwords!!")
    while True:
        user_input = input("\nEnter desired length of your password, Enter 'Q' to exit: ")
        if user_input.lower() == 'q':
            print("Exiting application....")
            break
        try:
            length = int(user_input)
            if length <= 0:
                print("Invalid input. Length must be a positive integer.")
            else:
                password = gen_pswd(length)
                print("Generated Password: ", password)
        except ValueError:
            print("Invalid input. Please enter a valid positive integer for the length.")
            continue


if __name__ == "__main__":
    main()
