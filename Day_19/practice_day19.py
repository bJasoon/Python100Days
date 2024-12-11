#Event listeners
from turtle import Turtle, Screen

tom = Turtle()
screen = Screen()

def move_forwards():
    tom.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forwards)




screen.exitonclick()