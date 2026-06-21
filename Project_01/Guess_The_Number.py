# "My Version" (Without Watching tutorial)

import random

seleted_number = random.randint(1, 1000)


def guess_number(guessed_number):

    if guessed_number > seleted_number:
        guessed_number = int(input("TRY GUESSING SMALLER NUMBER: "))
        guess_number(guessed_number)
        

    elif guessed_number < seleted_number:
        guessed_number = int(input("TRY GUESSING LARGER NUMBER: "))
        guess_number(guessed_number)
    
    else:
        return print("HURRAH, YOU GUESSED IT RIGHT IN")
        
num = int(input("GUESS THE NUMBER: "))
guess_number(num)