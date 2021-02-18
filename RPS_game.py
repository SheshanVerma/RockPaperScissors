# Rock Paper scissor Gme

from random import randint

# Moves a player can perform

moves = ["rock", "paper", "scissor"]

# While loop for the run under till stop

while True:
    computer = moves[randint(0, 2)]
    player = input("Please Choose Rock , Paper or Scissors or would you like to end the game?").lower()
    if player == "e" or player == "E":
        print("The Game is Ended!..")
        break
    elif player == computer:
        print("Tie, Computer Choose the Same ")
    elif player == "rock":
        if computer == "paper":
            print("You Lose ! ", computer, "beats", player)
        else:
            print("You Win !", player, "beats", computer)
    elif player == "paper":
        if computer == "scissor":
            print("You Lose ! ", computer, "beats", player)
        else:
            print("You Win !", player, "beats", computer)
    elif player == "scissor":
        if computer == "paper":
            print("You Lose ! ", computer, "beats", player)
        else:
            print("You Win !", player, "beats", computer)
    else:
        print("Please Check your Spelling !...")
