# number guessing game that asks user for a number between 1 and 100

import random
# variable for correct guess
answer = random.randint(1, 100)
# variable for user guess
userGuess = int(input("Guess a number between 1 and 100: "))
# variable for number of guess left
numGuesses = 10

# incorrect conditions
while(userGuess != answer and numGuesses > 0):
    if(userGuess > answer):
        print("Too high!")
    elif(userGuess < answer):
        print("Too low!")
    numGuesses -= 1
    userGuess = int(input("Guess a number between 1 and 100: "))

# win/lose statements
if(userGuess == answer):
    print("You win! You had " + str(numGuesses) + " guesses remaining.")
else:
    print("You lose!")
