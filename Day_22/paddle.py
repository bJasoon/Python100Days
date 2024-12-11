from turtle import Turtle

PADDLE_SHAPE = "square"
PADDLE_COLOR = "white"
PADDLE_WIDTH = 5
PADDLE_LENGTH = 1
PADDLE_SPEED = 30
UP = 90
DOWN = 270

class Paddle(Turtle):
    def __init__(self, player_x_pos):
        super().__init__()
        self.shape(PADDLE_SHAPE)
        self.color(PADDLE_COLOR)
        #self.setheading(UP)
        self.penup()
        self.setposition(x=player_x_pos,y=0)
        self.turtlesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_LENGTH)

    def move_up(self):
        if self.ycor() >= 240:
            return
        else:
            self.setposition(x=self.xcor(),y=(self.ycor() + PADDLE_SPEED))

    def move_down(self):
        if self.ycor() <= -240:
            return
        else:
            self.setposition(x=self.xcor(),y=(self.ycor() - PADDLE_SPEED))


        

    
