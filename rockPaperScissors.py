import random



playAgain = 'yes'
while playAgain == 'yes':
    computerScore = 0
    yourScore = 0
    while computerScore < 3 and yourScore < 3:
        options = ["rock", "paper", "scissors"]
        player1 = random.choice(options)
        player2 = input("rock(R),paper(P) or scissors(S):")
        if player2 == "R" or player2 == "r":
            player2 = "rock"
        elif player2 == "P" or player2== "p":
             player2 = "paper"
        elif player2 == "S"or player2 == "s":
            player2 = "scissors"
        if player1 == player2:
            print("Computer chose:" + player1 + "\nIt's a tie")
        elif player1 == 'rock' and player2 == "paper":
            yourScore += 1
            print("Computer chose:" + player1 + "\nPaper wins. You Win\nYour Score: " + str(yourScore) + "\nComputer's Score: " +str(computerScore))

        elif player1 == 'paper' and player2 == "rock":
            computerScore += 1
            print("Computer chose:" +player1+"\nPaper wins. Computer Wins\nYour Score: "+str(yourScore)+"\nComputer's Score: "+str(computerScore))


        elif player1 == 'rock' and player2 == "scissors":
            computerScore += 1
            print("Computer chose:" +player1+"\nRock wins. Computer Wins\nYour Score: "+str(yourScore)+"\nComputer's Score: "+str(computerScore))


        elif player1 == 'scissors' and player2 == "rock":
            yourScore += 1
            print("Computer chose:" +player1+"\nRocks wins. You Win\nYour Score: "+str(yourScore)+"\nComputer's Score: "+str(computerScore))


        elif player1 == 'paper' and player2 == "scissors":
            yourScore += 1
            print("Computer chose:" +player1+"\nScissors wins. You Win\nYour Score: "+str(yourScore)+"\nComputer's Score: "+str(computerScore))

        elif player1 == 'scissors' and player2 == "paper":
            computerScore += 1
            print("Computer chose:" +player1+"\nScissors wins. Computer Wins\nYour Score: "+str(yourScore)+"\nComputer's Score: "+str(computerScore))
        else:
            print("You chose an invalid option. Try Again:")

    if computerScore >= 3:
        print("The Computer Wins the Game!!")
    else:
        print("Hurray!! You are smarter than a computer")
    playAgain = input("Do want to play again?: ")
    if playAgain == 'no':
        print ("Thanks for playing")