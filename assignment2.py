import random

# Function to display a welcome message
def welcome():
    print("===================================")
    print("===================================")
    print("Welcome to the Number Guessing Game!")
    print("===================================")
    print("===================================")
    print("I have picked a random number between 1 and 100.")
    print("Can you guess what it is? Let's find out! \n")

# Function to play the guessing game
def play_game():
    number = random.randint(1, 100)  # Random number between 1 and 100
    attempts = 0  # Count number of attempts

    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))  # Get user's guess
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.\n")
            elif guess < number:
                print("Too low! Try again.\n")
            elif guess > number:
                print("Too high! Try again.\n")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts! \n")
                break
        except ValueError:
            print("Invalid input! Please enter a number.\n")

# Main function
def main():
    welcome()
    while True:
        play_game()
        again = input("Do you want to play again? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thanks for playing! Goodbye! 👋\n")
            break

# Run the program
if __name__ == "__main__":
    main()
