import random as r
import string as s

def generate_password(len_pass):
    # Define characters for different complexity levels
    lowercase = s.ascii_lowercase
    uppercase = s.ascii_uppercase
    digits = s.digits
    special = s.punctuation

    # Combine all characters
    all_chars = lowercase + uppercase + digits + special

    # Generate password using random.choice
    password = ''.join(r.choice(all_chars) for _ in range(len_pass))
    return password

def main():
    try:
        # Prompt user for password length
        len_pass = int(input("Enter the desired length of the password: "))

        # Generate and display password
        password = generate_password(len_pass)
        print("Generated Password:", password)

    except ValueError:
        print("Invalid input. Please enter a valid integer for password length.")

if __name__ == "__main__":
    main()
