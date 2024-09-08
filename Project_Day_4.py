#ROKC, PAPER, SCISSORS GAME
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
Choice = [rock, paper, scissors]
import random as rd
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

print("Choice of user")
print(Choice[user_choice])

computer_choice = rd.randint(0,2)
print("Choice of computer")
print(Choice[computer_choice])

if user_choice == computer_choice:
    print("Draw")
elif(user_choice == 0):
    if(computer_choice == 1):
        print("Computer won")
    else:
        print("You won")

elif(user_choice == 1):
    if(computer_choice == 2):
        print("Computer won")
    else:
        print("You won")

elif(user_choice == 2):
    if(computer_choice == 0):
        print("Computer won")
    else:
        print("You won")

else:
    print("Invalid choice!! You lose!!")