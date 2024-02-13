import random 

def get_user_choice():
    """
    Prompt the user for their choice of rock, paper, or scissors.
    """
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def determine_winner(user_choice, computer_choice):
    """
    Determine the winner based on the user's choice and the computer's choice.
    """
    if user_choice == computer_choice:
        return "It's a Tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    """
    Main function to run the game.
    """
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        options = ["rock", "paper", "scissors"]
        
        # Get user's choice
        user_choice = get_user_choice()
        
        # Generate computer's choice
        computer_choice = random.choice(options)
        
        print("Your choice:", user_choice)
        print("Computer choice:", computer_choice)

        # Determine the winner
        result = determine_winner(user_choice, computer_choice)
        print(result)

        # Ask if the user wants to play again
        repeat = input("\nPlay again? (yes/no): ")
        if repeat.lower() != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
