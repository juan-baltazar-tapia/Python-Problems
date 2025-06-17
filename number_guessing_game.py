# Make a number guessing game.
# From 1 to 100
# if number is above target, Too high!
# if number is below target, Too low!
# if number is guessed correctly, 
# Congratutlations! You guessed the number. 
# if not a valid number, Please enter a valid number

#pick a random number 1-100
# get user input, while user_input != random_number
#.   loop too high or too low

import random

random_number = random.randint(1,100)
while True:
    user_input = input('Guess the number between 1 and 100: ')
    if user_input.isdigit() and int(user_input) > 0 and int(user_input) < 101:
        user_input = int(user_input)
        if user_input > random_number:
            print('Too high!')
        elif user_input < random_number:
            print('Too low!')
        else:
            print('Congratutlations! You guessed the number')
            break
    else:
        print('Enter a valid number')