# import turtle
# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("green")
# timmy.right(90)
# for i in range(0, 20):
#     timmy.forward(i) #these forward(), Screen(), exitonclick() are methods for our module.
# my_screen = Screen()
#
# print(my_screen.canvheight) #this canvaheight is an attribute
# my_screen.exitonclick()
# for steps in range(0, 100, 6):
#     for c in ('blue', 'red', 'green'):
#         timmy.color(c)
#         timmy.forward(steps)
#         timmy.right(30)
# turtle.mainloop()
# turtle.screen.title('Object-oriented turtle demo')
# turtle.screen.bgcolor("orange")

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon", ['Pikachu', 'squirtle', 'charmander'])
table.add_column("Type", ['Electric', 'Water', 'Fire'])
table.add_row(['Bulbasaur', 'Grass'])
table.add_rows([['Haunter', 'Ghost'], ['Kadabra', 'Psychic'], ['Laprus', 'Ice']])e


table.align = "l"

print(table)