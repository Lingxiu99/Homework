import random

def guessing_game():
    number_to_guess = random.randint(1, 20)
    attempts = 0
    max_attempts = 3

    print("Welcome to the Guessing Game!")
    print("You have to guess a number between 1 and 20.")
    print("You have", max_attempts, "attempts.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        
        attempts += 1

        if guess == number_to_guess:
            print("Congratulations! You guessed the correct number in", attempts, "attempts.")
            return
        elif guess < number_to_guess:
            print("Try again! Your guess is too low.")
        else:
            print("Try again! Your guess is too high.")

    print("Sorry, you have used all your attempts. The correct number was", number_to_guess)

guessing_game()

