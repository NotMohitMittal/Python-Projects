import pyfiglet
import cowsay
import random
from sys 

project = pyfiglet.figlet_format("HangMan")
print(project)

print("You have been kidnapped by some bad people. Play this game on behalf of the given instructions to save your life otherwise you will get hanged.\n")
print("You have 6 chances in total to guess the word given below, ues them wisely or get 'Hanged'.")

# requirements
emptyString = ""
words = ["captive", "something", "hostage", "person", "overweight", "keyboard"]


selectedWord = random.choice(words)
# print(selectedWord)
hangMan = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''',
r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========= ''']

# while True:
for j in range(len(selectedWord)):
    newString = emptyString + "_"
    emptyString = newString # empty string is the container holding the blank string "_____"
print(f"Your word is {emptyString}")

count = 0
sucess = 0
totalLives = 6
listImage = 0
print(hangMan[count])
while count < 6:
    userChoice = input("Guess the word or the letters:  ")
    
    if userChoice in selectedWord:
        index = selectedWord.find(userChoice)
        modifying = emptyString[:index] + userChoice + emptyString[index+len(userChoice):]
        emptyString = modifying
        sucess += 1
        print("That's a correct answer.")
        print(emptyString)

        if emptyString == selectedWord:
            cowsay.milk(f"You have saved your life in {sucess} attempts.")
            sys.exit("Good Bye")
    else:
        count += 1
        print(hangMan[count])
        totalLives -= 1
        print(f"\n\n You have {totalLives} chances left.")
        if totalLives == 0:
            cowsay.dragon(f"Now, You are Dead.")
            sys.exit("No one can save you in our World.\n\n")
