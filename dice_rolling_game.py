# Abu Kamal
# following with Mosh
# below are the instruction to make prog

import random

# Loop
while True:
    choice = input("Please roll the dice? (y/n): ").lower()
    # Ask: roll the dice
    if choice == "y":
        # if user enters y
        num1 = random.randint(1, 6)
        num2 = random.randint(1, 6)
        # Generate two random number
        print(f'({num1}, {num2})')
        # print them
    elif choice == n:
        # if user enter n
        print('Thnaks for playing!')
        # print Thank you
        break
        # Terminate
    else:
        print('Invalid choice')
        # Else
        # print invalid choice
