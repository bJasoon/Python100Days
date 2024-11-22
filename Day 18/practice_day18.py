from turtle import Turtle, Screen
from random import randint, choice


timmy_the_turtle = Turtle()
screen = Screen()
screen.colormode(255)
timmy_the_turtle.shape("turtle")
#timmy_the_turtle.width(15)

# for i in range(10):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.up()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.down()

# color = [randint(0,255),randint(0,255),randint(0,255)]
# timmy_the_turtle.color(color)
# timmy_the_turtle.forward(200)

#====================================
#Draw different shapes challenge

# for sides in range(3,11):
#     timmy_the_turtle.color(randint(0, 255),randint(0, 255),randint(0, 255))
#     # timmy_the_turtle.forward(50)
#     # print(i)
#     current_shape_angle = 360/sides

#     for _ in range(0, sides):
#         timmy_the_turtle.right(current_shape_angle)
#         timmy_the_turtle.forward(100)

#====================================
#Draw a random walk
# timmy_the_turtle.width(10)
# timmy_the_turtle.speed("fastest")

# This is my implementation
# def movement(move):
#     match move:
#         case "south":
#             timmy_the_turtle.right(180)
#         case "east":
#             timmy_the_turtle.right(90)
#         case "west":
#             timmy_the_turtle.left(90)

#     timmy_the_turtle.forward(35)

# while True:
#     timmy_the_turtle.color(randint(0, 255),randint(0, 255),randint(0, 255))
#     movement(choice(["south","east","west"]))

#Suggested implementation
# for _ in range(200):
#     timmy_the_turtle.color(randint(0, 255),randint(0, 255),randint(0, 255))
#     timmy_the_turtle.forward(35)
#     timmy_the_turtle.setheading(choice([0,90,180,270]))

#====================================
#Draw a spirograph
timmy_the_turtle.speed("fastest")

#My implementation
# This is probably bad since values are hard coded
# for angle in range(0, 361, 5):
#     timmy_the_turtle.color(randint(0, 255),randint(0, 255),randint(0, 255))
#     timmy_the_turtle.setheading(angle)
#     timmy_the_turtle.circle(100)

# Suggested implementation
# def draw_spirograph(size_gap, radius):
#     for _ in range(int(360/size_gap)):
#         timmy_the_turtle.color(randint(0, 255),randint(0, 255),randint(0, 255))
#         timmy_the_turtle.setheading(timmy_the_turtle.heading() + size_gap)
#         timmy_the_turtle.circle(radius)

# draw_spirograph(25,180)
# draw_spirograph(5,100)
# draw_spirograph(1,50)

#====================================

screen.exitonclick()

#====================================
# import turtle as t
# tim = t.Turtle()