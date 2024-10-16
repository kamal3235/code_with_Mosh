# Abu Kamal
# Code for number guessing game
# Following Mosh tutarial


# Generate a random number
import random

number_to_guess = random.randint(1, 100)
# Loop
while True:
    try:
        guess = int(input("Guess the number between 1 and 100: "))
        if guess < number_to_guess:
            print("Too low")
        # if number < guess
        # print too low
        elif guess > number_to_guess:
            print("Too high")
        # if number > guess
        # print too high
        else:
            print("Congratualation! You guessed the number.")
            break
        # Else
        # print well done
        # Ask the user to make a guess
    except ValueError:
        print("Please enter a valid number")
# if not valid number
# print an error
