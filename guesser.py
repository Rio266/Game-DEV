import random

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100...")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Number is too low")
            elif guess > secret_number:
                print("Number is too high")
            else:
                print(f"Correct! You got it in {attempts} attempts!")
                break

        except ValueError:
            print("Please enter a valid number.")

    print("Game over")

game()