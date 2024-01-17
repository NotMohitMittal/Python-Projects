import random 
import sys
import cowsay
from pyfiglet import figlet_format

def selected_number ():
    return random.randrange(1, 101)

the_number = selected_number()
# print(the_number)

def distance(number):
    if the_number < number :
        cowsay.tux("Too High, Try again.")
    elif the_number > number:
        cowsay.cow("Too Low, Try again.")
         

# The UI for the User

game = figlet_format("Number Guessing Game")
print(game)

count = 0
while True:
    user_input = int(input("\nGuess A Number Betweeen 1 - 100:  "))
    distance(user_input)
    count += 1
    
    if user_input == the_number:
        sys.exit(f"Congratulations! You have completed the game is {count} attempts.")
        
    else: 
        another_input = int(input("\nGuess A Number Between 1 - 100:  "))
        distance(another_input)
        count += 1
        if another_input == the_number:
            sys.exit(f"Congratulations! You have completed the game is {count} attempts.")
