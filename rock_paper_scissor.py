# Abu Kamal
# Game of childhood
""" 
Ask the user to make a choice
if choice is not valid
print an error
#Let the computer to make achoice
print choice
determine the winner
Ask the user if they want to continue
if not Terminate
refractoring to function

"""

import random

ROCK = "r"
SCISSORS = "s"
PAPER = "p"
emojis = {ROCK: '🪨', PAPER: '🗞️', SCISSORS: '✂️'}
choices = tuple(emojis.keys())


def get_user_choice():
    while True:
        user_choice = input('Rock, paper, or scissor? (r/p/s): ').lower()
        if user_choice in choices:
            return user_choice
        else:
            print('Invalid choice!')


def display_choices(user_choice, computer_choice):
    print(f'you chose {emojis[user_choice]}')
    print(f'computer chose {emojis[computer_choice]}')


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print('Ties')
    elif (
        (user_choice == ROCK and computer_choice == SCISSORS) or
        (user_choice == SCISSORS and computer_choice == PAPER) or
            (user_choice == PAPER and computer_choice == ROCK)):
        print('You win')
    else:
        print('You lose')


def play_game():
    while True:
        user_choice = get_user_choice()

        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)
        determine_winner(user_choice, computer_choice)

        should_continue = input('Continue? (y/n): ').lower()
        if should_continue == 'n':
            break


play_game()
