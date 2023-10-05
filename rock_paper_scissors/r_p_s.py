import random
from sys import exit


def determine_winner():
    options =  ["rock","paper","scissors"]
    user_wins = 0
    computer_wins = 0
    while True:
        user_pick = input("Choose: Rock, Paper or Scissors? \n").lower()
        random_number = random.randint(0,2)
        # rock = 0, paper = 1, scissors = 2
        computer_pick = options[random_number]
        print(f"Computer picked {computer_pick}")
        if user_pick == "q":
            break
        elif user_pick == computer_pick:
            print("Draw!")
            continue
        elif user_pick == "rock" and computer_pick == "scissors":
            print("You won!")
            user_wins += 1
            continue
        elif user_pick == "paper" and computer_pick == "rock":
            print("You won!")
            user_wins += 1
            continue
        elif user_pick == "scissors" and computer_pick == "paper":
            print("You won!")
            user_wins += 1
            continue
        else:
            print("You lost!")
            computer_wins += 1
            continue
       
    print(f"Scoreboard:\nUser: {user_wins}\nComputer: {computer_wins}")
   

    

def playGame():
    print("test")
    decision = input("Do you want to play the game?\nType: Y or N\n")
    if decision == "y":
        determine_winner()
    elif decision == "n":
        print("See you later!")
        exit()
    else:
        print("Try again")


    
      

playGame()


