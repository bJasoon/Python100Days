from turtle import Turtle, Screen

tom = Turtle()
screen = Screen()
tom.speed("fastest")

def draw_forward():
    tom.forward(10)

def draw_backwards():
    tom.backward(10)

def turn_left():
    tom.left(10)

def turn_right():
    tom.right(10)

def clear_drawing():
    tom.penup()
    tom.home()
    tom.pendown()
    tom.clear()
    

screen.listen()
screen.onkey(key="w", fun=draw_forward)
screen.onkey(key="s", fun=draw_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_drawing)

screen.exitonclick()