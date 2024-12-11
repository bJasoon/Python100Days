from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

is_race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

def initialize_turtle():
    initial_y = 150
    for color in colors:
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(color)
        new_turtle.penup()
        new_turtle.setpos(-230,initial_y)
        initial_y -= 50
        turtles.append(new_turtle)

initialize_turtle()
if user_bet:
    is_race_on = True

while is_race_on:

    for current_turtle in turtles:
        if current_turtle.xcor() > 230:
            is_race_on = False
            if current_turtle.pencolor() == user_bet:
                print(f"You won! The {current_turtle.pencolor()} turtle is the winner!")
            else:
                print(f"You lost! The {current_turtle.pencolor()} turtle is the winner!")

        current_turtle.forward(random.randint(0,10))

screen.exitonclick()