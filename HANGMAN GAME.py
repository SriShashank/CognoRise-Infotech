import random

word_list = ["sri", "shashank", "abhi", "ramsai", "vaj", "balagopal", "ganesh", "dhanush"]

def select_random_word():
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def hangman_display(incorrect_guesses):

    stages = [
        """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     / \\
            -
        """,
        """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     / 
            -
        """,
        """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |      
            -
        """,
        """
            --------
            |      |
            |      O
            |     \\|
            |      |
            |     
            -
        """,
        """
            --------
            |      |
            |      O
            |      |
            |      |
            |     
            -
        """,
        """
            --------
            |      |
            |      O
            |    
            |      
            |     
            -
        """,
        """
            --------
            |      |
            |      
            |    
            |      
            |     
            -
        """
    ]
    return stages[incorrect_guesses]

def main():
    print("Welcome to Hangman!")
    while True:
        word = select_random_word()
        guessed_letters = []
        incorrect_guesses = 0

        print("\nNew game started!")
        while True:
            print(hangman_display(incorrect_guesses))
            print("Word:", display_word(word, guessed_letters))

            guess = input("Guess a letter: ").lower()
            if guess in guessed_letters:
                print("You already guessed that letter!")
                continue

            guessed_letters.append(guess)

            if guess not in word:
                incorrect_guesses += 1
                print("Incorrect guess!")
                if incorrect_guesses == len(hangman_display(0).strip().split("\n")) - 1:
                    print("You lost! The word was:", word)
                    break
            else:
                print("Correct guess!")

            if all(letter in guessed_letters for letter in word):
                print("Congratulations! You won!")
                break

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thank you for playing Hangman!")
            break

if __name__ == "__main__":
    main()
