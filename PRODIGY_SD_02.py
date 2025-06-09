import random

def main():
    print("Number Guessing Game")
    print("I have picked a number between 1 and 100. Try to guess it!")

    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it right.")
                print(f"It took you {attempts} attempts to guess the number.")
                break
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
