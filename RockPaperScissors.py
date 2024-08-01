import random

def rockPaperScissors(user_input, computer_input):
    if  ((user_input == "rock") & (computer_input == "rock")):
        print("The computer threw rock. Rock and rock ends in a draw.")
    elif((user_input == "scissors") & (computer_input == "scissors")):
        print("The computer threw scissors. Scissors and scissors ends in a draw.")
    elif((user_input == "paper") & (computer_input == "paper")):
        print("The computer threw paper. Paper and paper ends in a draw.")

    elif((user_input == "rock") & (computer_input == "scissors")):
        print("The computer threw scissors. Rock beats scissors, you win!")
    elif((user_input == "paper") & (computer_input == "rock")):
        print("The computer threw rock. Paper beats rock, you win!")
    elif((user_input == "scissors") & (computer_input == "paper")):
        print("The computer threw paper. Scissors beats paper, you win!")

    elif((user_input == "rock") & (computer_input == "paper")):
        print("The computer threw paper. Paper beats rock, computer wins!")
    elif((user_input == "paper") & (computer_input == "scissors")):
        print("The computer threw scissors. Scissors beats paper, computer win!")
    elif((user_input == "scissors") & (computer_input == "rock")):
        print("The computer threw rock. Rock beats paper, computer wins!")

rock = "rock"
paper = "paper"
scissors = "scissors"

list = (rock, paper, scissors)
computer = random.choice(list)

response = input("Do you want to play rockPaperScissors? 'Y' for yes, any other key for no: ").upper()
while response == "Y":
    user = input("Rock. Paper. Scissors. Shoot!: ").lower()
    computer = random.choice(list)
    rockPaperScissors(user,computer)
    response = input("Do you want to play again? 'Y' for yes, any other key for no: ").upper()