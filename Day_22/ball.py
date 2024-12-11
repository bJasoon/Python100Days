from turtle import Turtle
import random

BALL_SHAPE = "circle"
BALL_COLOR = "white"
INITIAL_BALL_SPEED = 15
BALL_SPEED_FACTOR = 0.30

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(BALL_SHAPE)
        self.color(BALL_COLOR)
        self.ball_speed = INITIAL_BALL_SPEED
        self.penup()
        self.home()
        self.setheading(random.randint(-60,60))
        #self.setheading(300)   

    def move(self):
        self.forward(self.ball_speed)

    def bounce_down(self):
        if self.heading() in range(90,270):
            self.setheading(random.randint(200,260))
        else:
            self.setheading(random.randint(290, 340))

    def bounce_up(self):
        if self.heading() in range(90,270):
            self.setheading(random.randint(110, 160))
        else:
            self.setheading(random.randint(20, 60))
            pass

    def bounce_paddle(self,ball_x_cor):
        if ball_x_cor > 0:
            self.setheading(random.randint(120,240))
        else:
            self.setheading(random.randint(-60,60))
        self.ball_speed += (INITIAL_BALL_SPEED*BALL_SPEED_FACTOR)

    def reset(self, ball_x_cor):
        self.home()
        self.ball_speed = INITIAL_BALL_SPEED
        if ball_x_cor >= 400:
            self.setheading(random.randint(120,240))
        elif ball_x_cor <= -400:
            self.setheading(random.randint(-60,60))


