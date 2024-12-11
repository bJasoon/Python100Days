import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

FINISH_LINE_Y = 280

car_fleet = []

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
score = Scoreboard()
cars = CarManager()

screen.onkey(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move()

    if player.ycor() >= FINISH_LINE_Y:
        player.reset()
        score.add_level()
        cars.level_up()

    for car_check in cars.car_fleet:
        if player.distance(car_check) < 25 and (player.ycor() <= (car_check.ycor()) + 15):
            game_is_on = False
            score.game_over()
    

screen.exitonclick()    
