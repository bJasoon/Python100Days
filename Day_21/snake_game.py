from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard, Coordinates
import time

WALL_COLLISION_FACTOR = 15
SNAKE_COLLISION_FACTOR = 10
SCREEN_TIME_REFRESH = 0.1

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

game_on = True
snake = Snake()
food = Food()
score = Scoreboard()
pos = Coordinates()
screen.listen()

screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

while game_on:
    screen.update()
    pos.clear()

    time.sleep(SCREEN_TIME_REFRESH)
    snake.move()

    if snake.head.distance(food) < WALL_COLLISION_FACTOR:
        food.change_loc()
        score.add_score()
        snake.grow_snake(snake.segment[-1])

    pos.display_pos(snakeHead=snake.head)
    
    # if snake.head.position() > (300,) or snake.head.position() < (-300,):
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 290 or snake.head.ycor() < -280:
    #if snake.head.xcor() not in range(-300,300) or snake.head.ycor() not in range(-300,300):
        game_on = False
        score.game_over()

    # for segment_check in snake.segment:
    #     if segment_check == snake.head:
    #         pass 
    #     elif snake.head.distance(segment_check) < SNAKE_COLLISION_FACTOR:
    #         game_on = False
    #         score.game_over()

    for segment_check in snake.segment[1:]:
        if snake.head.distance(segment_check) < SNAKE_COLLISION_FACTOR:
            game_on = False
            score.game_over()

screen.exitonclick()
