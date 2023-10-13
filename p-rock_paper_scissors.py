# Rock Paper Scissors Lizard Spock

import random

# Main menu
print("===================")
print("Rock Paper Scissors")
print("===================")
print("1) ✊")
print("2) ✋")
print("3) ✌️")
print("4) 🦎")
print("5) 🖖")

player = int(input("Pick a number: "))
computer = random.randint(1, 5)

# Player choice
if player == 1:
    print("Player: ✊")
elif player == 2:
    print("Player: ✋")
elif player == 3:
    print("Player: ✌️")
elif player == 4:
    print("Player: 🦎")
elif player == 5:
    print("Player: 🖖")
else:
    print("Incorrect option ❌")

# Computer choice
if computer == 1:
    print("Computer: ✊")
elif computer == 2:
    print("Computer: ✋")
elif computer == 3:
    print("Computer: ✌️️")
elif computer == 4:
    print("Computer: 🦎")
else:
    print("Computer: 🖖")

# player choice = computer choice it's a tie
if player == computer:
    print("It's a tie!")
# All computer won
elif (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1) or (
        player == 1 and computer == 5) or (player == 2 and computer == 4) or (player == 3 and computer == 5) or (
        player == 4 and computer == 1) or (player == 4 and computer == 3) or (player == 5 and computer == 4) or (
        player == 5 and computer == 2):
    print("The computer won!")
# All player won
elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2) or (
        player == 1 and computer == 4) or (player == 2 and computer == 5) or (player == 3 and computer == 4) or (
        player == 4 and computer == 5) or (player == 4 and computer == 2) or (player == 5 and computer == 3) or (
        player == 5 and computer == 1):
    print("The player won!")
else:
    print("Error")

