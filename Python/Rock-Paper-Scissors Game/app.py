import random

def play_game(user_choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print(">> You win!")
    else:
        print(">> Computer wins!")

def main():
    print("Welcome to Rock-Paper-Scissors Game!")
    print("Enter 'rock', 'paper', or 'scissors'. Enter 'exit' to quit.")

    while True:
        user_choice = input("\nEnter your choice: ").lower()

        if user_choice in ['rock', 'paper', 'scissors']:
            play_game(user_choice)
        elif user_choice == 'exit':
            print("Exiting game...")
            break
        else:
            print("Invalid choice. Please enter 'rock', 'paper', 'scissors', or 'exit'.")

if __name__ == "__main__":
    main()
