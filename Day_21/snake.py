from turtle import Turtle
INITIAL_X = 0
MOVE_DISTANCE = 20
SEGMENT_GAP = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]
        
        
    def create_snake(self):
        initial_x = INITIAL_X
        for _ in range(0,3):
            snake_body = Turtle(shape="square")
            snake_body.color("white")
            snake_body.penup()
            snake_body.setpos(initial_x,0)
            initial_x -= SEGMENT_GAP
            self.segment.append(snake_body)

    def grow_snake(self, end):
        tail = Turtle(shape="square")
        tail.color("white")
        tail.penup()
        tail.setpos(end.position())
        self.segment.append(tail)

    def move(self):
        for segment_num in range(len(self.segment) - 1, 0, -1):
            self.segment[segment_num].setpos(self.segment[segment_num - 1].xcor(), self.segment[segment_num - 1].ycor())

        self.head.forward(MOVE_DISTANCE)
        
    def up(self):
        if self.head.heading() != UP and self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP and self.head.heading() != DOWN:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != LEFT and self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        

    def right(self):
        if self.head.heading() != LEFT and self.head.heading() != RIGHT:
            self.head.setheading(RIGHT)