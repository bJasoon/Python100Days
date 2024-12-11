from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

CAR_SHAPE = "square"
STARTING_NUM_CARS = 30
NUM_CARS_INCREMENT = 5

class CarManager():
    def __init__(self):
        self.car_speed = STARTING_MOVE_DISTANCE
        self.car_fleet = []
        self.amount_cars = STARTING_NUM_CARS

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1 and len(self.car_fleet) <= self.amount_cars:
            car = Turtle()
            car.shape(CAR_SHAPE)
            car.penup()
            car.turtlesize(stretch_len=2)
            car.setheading(180)
            car.setposition(310, random.randint(-250, 250))
            car.color(random.choice(COLORS))

            self.car_fleet.append(car)
        
    def move(self):
        for car in self.car_fleet:
            if car.xcor() <= -310:
                car.setposition(310, random.randint(-250, 250))
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
        self.amount_cars += NUM_CARS_INCREMENT
    