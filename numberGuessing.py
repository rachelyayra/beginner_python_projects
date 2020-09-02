import random

guessNumber = str(random.randint(0,100)) # Generates random numbers in a given range
score = 3 # suser's score
scoreLimit = 0 # limit where game is ended
try:
    if int(guessNumber) <= 10:
        inputNumber = input("Guess the Secret Number for a prize:\nHint:\nSecret Number is less than or equal to 10:\n") # starting prompt
    else:
        inputNumber = input("Guess the Secret Number for a prize:\nHint:\nSecret Number is more than 10:\n")
    while inputNumber != guessNumber and score > scoreLimit: # if the number inputted is not the same as the secret number and the scorelimit is not passed,
        score -= 1 # subtract 1
        hint = int(inputNumber) - int(guessNumber)
        if hint < 0:
            inputNumber = input("Try Again:\nHint\nSecret Number is " + str(abs(hint)) + " more than your guess\n")# give hint
        else:
            inputNumber = input("Try Again:\nHint\nSecret Number is " + str(abs(hint)) + " less than your guess\n")
# if the while condition is not satisfied, meaning answer is correct or the score limit is exceeded. to diffentiate, use an is if statement
    if inputNumber == guessNumber:
        print("You Win, You score is\t" + str(score))
    else:print("You scored " + str(score) + ", you Lose")

except:
    print("Invalid")