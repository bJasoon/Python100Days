from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

game_on = True
snake = Snake()
screen.listen()

screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
        
        
screen.exitonclick()
