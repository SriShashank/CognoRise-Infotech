import random 
while True:
    options = ["rock", "paper", "scissors"]
    user_choice = input("Choose rock, paper, or scissors: ")
    computer_choice = random.choice(options)

    print("Your choice: ", user_choice)

    print("Computer choice: ", computer_choice)

    if user_choice == computer_choice:

        print("It's a Tie")

    elif user_choice == "rock" and computer_choice == "scissors":

        print("You win")

    elif user_choice == "paper" and computer_choice == "rock":

        print("You win!")

    elif user_choice == "scissors" and computer_choice == "paper":

        print("You win!")

    else:

        print("Computer wins!")

    repeat = input("\nPlay again? (yes/no): ")
    if repeat.lower() != "yes":
        print("Thanks for playing!")
        break
