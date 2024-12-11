#Rock beats Scissors
#Paper beats Rock
#Scissors beats Paper

import random

# ASSCII Art
#Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
win = "You win!"
lose = "You lose!"
draw = "Draw!"

RPS_Art = [rock,paper,scissors]
computer_choice = random.randint(0,2)

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors\n"))

print(f"\nYou Chose:\n{RPS_Art[player_choice]}")

print("Computer chose:")
print(RPS_Art[computer_choice])

if player_choice == 2:
    if computer_choice == 0:
        player_choice = -1
elif computer_choice == 2:
    if player_choice == 0:
        computer_choice = -1


if player_choice == computer_choice:
    print(draw)
elif player_choice < computer_choice:
    print(lose)
else:
    print(win)





