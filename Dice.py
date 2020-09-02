'''Generate a random number
print it
ask the user if the want to roll again'''
import random
def dice():
    diceNumber = random.randint(1,6)
    print(diceNumber)

try:
    answer =input("Do you want roll a die?\n")
    while answer == "yes":
      if answer == "yes":
        dice()
        answer = input("Do you want roll a die?\n")

    print("Thanks for using,")


except:
    print("Invalid")