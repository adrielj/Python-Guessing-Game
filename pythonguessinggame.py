
import random
theComputerNumber = random.randint(1, 1000000)
print (theComputerNumber)

numberOfGuesses = 0
lowGuessRange = 1
highGuessRange = 1000000
gameOver = False

while not gameOver:
    print ("Enter your guess between" ,lowGuessRange, "to" ,highGuessRange)
    playerGuess = int (input ("Enter your guess: "))
    if (playerGuess < lowGuessRange or playerGuess > highGuessRange):
        print ("Your guess is out of range! Try again.")
        continue
    if playerGuess > theComputerNumber:
        highGuessRange = playerGuess
        numberOfGuesses = numberOfGuesses + 1
        if numberOfGuesses is 20:
            print ("Sorry! You have run out of guesses.")
            gameOver = True
        else:
            print ("The number is lower. You have guessed " ,numberOfGuesses, " times.")
            continue
    if playerGuess < theComputerNumber:
        lowGuessRange = playerGuess
        numberOfGuesses = numberOfGuesses + 1
        if numberOfGuesses is 20:
            print ("Sorry! You have run out of guesses.")
            gameOver = True
        else:
            print("The number is higher.You have guessed" ,numberOfGuesses, "times" )
            continue
    if playerGuess == theComputerNumber:
        print ("Congratulations! That's correct!")
        gameOver = True



        
    
