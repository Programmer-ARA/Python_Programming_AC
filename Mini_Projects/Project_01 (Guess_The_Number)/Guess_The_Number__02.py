# With Tutorial

import random

target = random.randint(1, 100)

Attempt = 0

while True:
    userChoice = input("GUESS THE NUMBER or QUIT(Q): ")
    if(userChoice == "Q"):
        break

    userChoice = int(userChoice)
    Attempt += 1
    
    if userChoice == target:
        print("HURRAH, YOU GUESSED IT RIGHT, in", Attempt, "Attempt")
        break

    elif userChoice > target:
        print("TRY GUESSING SMALL NUMBER")

    else:
        print("TRY GUESSING BIG NUMBER")
    

print("----- GAME ENDED -----")