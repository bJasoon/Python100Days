# from turtle import Turtle, Screen

# # Object construction from class Turtle
# timmy = Turtle()

# print(timmy)
# timmy.shape("turtle")
# timmy.color("cyan")
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)

# my_screen.exitonclick()


#=========================================================

from prettytable import PrettyTable

POKEMON_NAME = ["Pikachu", "Squirtle", "Charmander"]
POKEMON_TYPE = ["Electric", "Water", "Fire"]

table = PrettyTable()
table.add_column("Pokemon Name ",POKEMON_NAME)
table.add_column("Type", POKEMON_TYPE)
table.align = "l"

print(table)