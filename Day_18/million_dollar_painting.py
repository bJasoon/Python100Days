#import colorgram
from random import choice
from turtle import Turtle, Screen

# colors_extracted = colorgram.extract('Day 18\\image.jpg', 20)
# color_set = []

# for color in colors_extracted:
#     color_set.append((color.rgb.r,color.rgb.g,color.rgb.b))

# print(color_set)

color_set = [(209, 165, 124), (140, 49, 106), (164, 169, 38), (244, 80, 56), (228, 115, 163), (3, 143, 56), (241, 65, 140), (1, 143, 184), (162, 55, 51), (50, 203, 226), (254, 230, 0), (20, 166, 126), (244, 223, 49), (171, 186, 177), (27, 197, 220), (232, 165, 190)]

# You can manipulate the values here to change the painting
canvas_size = 500 # This code assumes that the canvas is perfectly square
gap_dots = 50 # This variable determines the paces between dots / It is better to set this to something that is divisible by the canvas_size
dot_size = 20 # This variable determines the dot size

def initialize_turtle():
    painting.up()
    painting.hideturtle()
    painting.speed("fastest")
    canvas.colormode(255)

def paint_hirst():
    '''This function runs a 2 for loops that go paints a dot through the x-axis for the inner loop and iterates upward to the
    y-axis in the outer loop. It utilizes non hard-coded values for the x and y position that is calculated by dividing the canvas_size
    into half and makes that number negative to indicate the left side of the canvas an positive for the right side.'''

    for y_pos in range(-abs(int(canvas_size/2)), (int(canvas_size/2)), gap_dots): #gap_dots is the iterator of the for loop 
        painting.sety(y_pos)                                                      #and serves as the y or x position of the turtle

        for x_pos in range(-abs(int(canvas_size/2)), (int(canvas_size/2)), gap_dots):
            painting.setx(x_pos)
            painting.down()
            painting.dot(dot_size, choice(color_set))
            painting.up()
            

        painting.setx(-abs(int(canvas_size/2)))

painting = Turtle()
canvas = Screen()

initialize_turtle()
paint_hirst()

# First implementation, simple but with hard coded values
# for _ in range(10):
#     for _ in range(10):
#         painting.color(random.choice(color_set))
#         painting.down()
#         painting.dot(20)

#         painting.up()
#         painting.setx(painting.xcor() + 50)
    
#     painting.sety(painting.ycor() + 50)
#     painting.setx(-250)
    

canvas.exitonclick()