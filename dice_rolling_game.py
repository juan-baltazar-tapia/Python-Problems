# PROBLEM
# Ask user - roll dice (y/n)
# if its not y or n, print Invalid Choice in console
# if yes -> roll dice
# if no, end program
import random

MESSAGE = 'Roll the dice? (y/n): '

while True:
    #print(MESSAGE)
    input1 = input(MESSAGE)
    input1 = input1.lower()

    if (input1 != 'y') and (input1 != 'n'):
        print('Invalid Choice!')
    elif input1 == 'y':
        int1 = str(random.randint(1,6))
        int2 = str(random.randint(1,6))
        print('(' + int1 + ', ' + int2 + ')')
    elif input1 == 'n':
        print('Thanks for playing!')
        break
    
    
   