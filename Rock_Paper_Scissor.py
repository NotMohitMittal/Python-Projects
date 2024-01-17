# This code has lots of bugs needed to be fixed the input in the second time isn't getting evalutated properly


import random
import cowsay
import pyfiglet

game = pyfiglet.figlet_format("Rock, Paper and Scissor")
print(game)


computer = random.choice(["rock", "paper", "scissor"])

player = input("Rock(R), Paper(P) or Scissor(S):  ").lower().strip()

player_options = ["rock", "paper" , "scissor", "r", "p", "s", "Cheat"]

for i in player_options:
    if player in player_options:
       continue
    else:
        print("Seems like you have selected the wrong opetion, Please choose a correct one...  ") 
        player_another = input("Rock(R), Paper(P) or Scissor(S):  ").lower().strip()
        if player_another in player_options:
            continue 
        



print("Select one of the Following Options:-  ")

print(f"You choose {player}")
print(f"The computer choose {computer}")

if player == "rock" and computer == "paper":
    cowsay.cow("You Loose")
elif player == "paper" and computer == "scissor":
    cowsay.cow("You Loose.")
elif player == "scissor" and computer == "rock":
    cowsay.cow("You Losse")
elif computer == player:
    cowsay.cow("This is a Tie")
else:
    cowsay.cow("You Won!!")




