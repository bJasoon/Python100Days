from turtle import Turtle
import random
FOOD_SHAPE = "circle"
FOOD_COLOR = "blue"
FOOD_DIAMETER = 0.5

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.color(FOOD_COLOR)
        self.shape(FOOD_SHAPE)
        self.penup()
        self.shapesize(stretch_len=FOOD_DIAMETER,stretch_wid=FOOD_DIAMETER)
        self.speed("fastest")
        self.change_loc()

    def change_loc(self):
        self.goto(x=random.randint(-280,280),y=random.randint(-280,280))

