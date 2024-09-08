# TREASURE HUNT GAME
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

def game():
    print("Welcome to Treasure Island. Your mission is to find the treasure.")
    print("Currently you are on a pathway that is getting split into two parts.")
    print("Where do you wanna go? Type 'LEFT' for going left or 'RIGHT' for going right...")

    direction = input().upper()

    if direction == 'LEFT':
        print("Now you've arrived at a lake and you are able to locate the treasure Island at the centre of the lake...")
        print("You've two choices: Wait for boat or swim across the lake...")
        print("Type 'SWIM' to swim across or 'WAIT' to wait for the boat...")

        option = input().upper()

        if option == 'WAIT':
            print("You crossed the lake n reached the Treasure Island. You came across the treasure house with three doors")
            print("Choose one of the three doors i.e 'RED', 'YELLOW' and 'BLUE'...")

            door = input().upper()

            if door == 'YELLOW':
                print("You have found the treasure... Congratulations... YOU WON...(T_T)")
            elif door == 'BLUE':
                print("You have been eaten by a PYTHON... GAME OVER...(T_T)")
            else:
                print("You have been burnt in a FIRE... GAME OVER...(T_T)")
        else:
            print("You tried to swim but got eaten by a CROCY... GAME OVER...(T_T)")
    else:
        print("You fell down a WATERFALL... GAME OVER...(T_T)")

game()