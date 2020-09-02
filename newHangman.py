# create a while loop that keeps going until the word is guessed
import random
from word import words

playAgain = "yes"
while playAgain == "yes":
    lives = 6
    secretWord = random.choice(words)
    wordElementList = set(secretWord)
    wordElementList1 = list(secretWord)
    # print(wordElementList)
    # print(secretWord)
    usedLetter = set()

    while len(wordElementList) > 0 and lives > 0:
        print("You have "+str(lives)+" lives left.\nYou have already used these letters: "," ".join(usedLetter))
        displayWords =list()
        for i in wordElementList1:
            if i in usedLetter:
                displayWords.append(i)
            else:
                displayWords.append("_")
    #if letter is in usedletter and in wordElementList1 print letter, else print "_"
        print("Word Progress: ","".join(displayWords))
        userGuess = input("Input your guess:").lower()
        if userGuess in usedLetter:
            print("You've already used this letter.")
        else:
            if userGuess in wordElementList:
                wordElementList.remove(userGuess)
                usedLetter.add(userGuess)
            elif userGuess not in wordElementList and lives > 1:
                print("Try Again")
                lives -= 1
                usedLetter.add(userGuess)
            else:
                lives -= 1
                usedLetter.add(userGuess)

    if lives == 0:
        print("You lose. The word was "+secretWord)
    else:

        print("You guessed the word "+secretWord)

    playAgain = input("\nDo want to play again?")
    if playAgain == "no":
        print("Thanks for playing. See you next time!")

