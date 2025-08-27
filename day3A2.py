
'''
Create a pixel art character using the code below.

Things to think about:
Use of global variables
Use of color
Use of functions
Use of parameters
Use of arguments
Use of lists
Use of for loops

'''
PIXEL_SIZE = 20

PIXEL_ART_ARRAY = [
    #0-7
    ["white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "aquamarine", "aquamarine", "darkcyan", "aquamarine", "aquamarine", "aquamarine", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "aquamarine", "aquamarine", "white", "white", "white", "white", "white", "white"], #
    ["white", "white", "white", "white", "white", "white","white", "white", "white", "aquamarine", "aquamarine", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "aquamarine", "darkcyan", "darkcyan", "black", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "black", "white", "white", "white", "white"], #
    ["aquamarine", "aquamarine", "aquamarine", "aquamarine", "aquamarine", "white", "white", "white", "aquamarine", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "aquamarine", "darkcyan", "darkcyan", "darkcyan", "black", "darkcyan", "darkcyan", "aquamarine", "aquamarine", "aquamarine", "black", "black", "black", "white", "white", "white", "white", "white"], #
    ["black", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "aquamarine", "aquamarine", "aquamarine", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "aquamarine", "darkcyan", "darkcyan", "tan", "darkcyan", "darkcyan", "black", "aquamarine", "aquamarine", "aquamarine", "black", "white", "white", "white", "white", "white", "white", "white", "white"], #
    ["black", "tan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "aquamarine", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "aquamarine", "darkcyan", "tan", "tan", "tan", "darkcyan", "black", "aquamarine", "aquamarine", "black", "white", "white", "white", "white", "white", "white", "white", "white", "white"], #
    ["black", "tan", "tan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "aquamarine", "aquamarine", "aquamarine", "aquamarine", "aquamarine", "tan", "tan", "darkcyan", "darkcyan", "black", "black", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white"], #
    ["black", "tan", "tan", "tan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "aquamarine", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "aquamarine", "tan", "darkcyan", "darkcyan", "black", "darkcyan", "aquamarine", "aquamarine", "aquamarine", "white", "white", "white", "white", "white", "white", "white", "white", "white"], #
    ["black", "tan", "aquamarine", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "aquamarine", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "aquamarine", "aquamarine", "white", "white", "white", "white", "white", "white", "white"],
    #8-15
    ["white", "white", "black", "black", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "aquamarine", "aquamarine", "aquamarine", "aquamarine", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "black", "white", "white","white","white"],
    ["white", "white","white", "black", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "black", "white", "white", "white", "teal", "aquamarine", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "aquamarine", "aquamarine", "aquamarine", "aquamarine", "black", "white", "white", "white"],
    ["white", "white", "aquamarine", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "black", "aquamarine", "white", "green", "white", "white", "teal", "aquamarine", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "aquamarine","aquamarine","aquamarine","aquamarine","aquamarine","aquamarine","aquamarine", "black", "white", "white"],
    ["white", "white", "aquamarine", "darkcyan", "aquamarine", "aquamarine", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "black", "white", "white", "green", "black", "white", "white", "aquamarine", "darkcyan", "darkcyan", "darkcyan", "aquamarine","aquamarine", "black", "black", "black", "black", "black", "black", "black", "white", "white"],
    ["white", "white", "aquamarine", "darkcyan", "aquamarine", "teal", "aquamarine", "darkcyan", "darkcyan", "black", "aquamarine", "white", "white", "green", "black", "white", "white", "aquamarine", "darkcyan", "darkcyan", "aquamarine", "black", "black", "black", "white", "white", "white", "white", "white", "white", "white", "white", "white"],
    ["white", "white", "white", "black", "black", "teal", "teal", "black", "darkcyan", "black", "white", "white", "white", "white", "black", "white", "coral", "aquamarine", "aquamarine", "darkcyan", "darkcyan", "darkcyan", "aquamarine", "black", "black", "white", "aquamarine", "aquamarine", "white", "white", "white", "white", "white"],
    ["white", "white", "white", "white", "black", "white", "aquamarine", "black", "black", "black", "white", "white", "white", "white", "white", "coral", "tan", "tan", "tan", "black", "darkcyan", "darkcyan", "darkcyan", "aquamarine", "aquamarine", "black", "white", "white", "aquamarine", "white", "white", "white", "white"],
    ["white", "white", "white", "white", "black", "white", "aquamarine", "aquamarine", "black", "white", "white", "white", "white", "white", "coral", "tan", "tan", "tan", "tan", "black", "aquamarine", "aquamarine", "aquamarine", "aquamarine", "black", "white", "white", "white", "teal", "teal", "teal", "teal", "white", "white"],
    #16-23 red swapped to tan
    ["white", "white", "white", "white", "white", "black", "black", "black", "orange", "orange", "orange", "orange", "orange", "tan", "tan", "orange", "orange", "tan", "tan", "black", "aquamarine", "black", "black", "black", "khaki", "khaki", "aquamarine", "aquamarine", "khaki", "khaki", "khaki", "aquamarine"], #
    ["white", "white", "white", "white", "white", "black", "black", "black", "black", "tan", "tan", "tan", "tan", "tan", "tan", "tan", "tan", "coral", "black", "aquamarine", "black", "khaki", "khaki", "khaki", "khaki", "teal", "teal", "khaki", "khaki", "khaki", "khaki", "aquamarine"], #
    ["white", "white", "white", "white", "white", "white", "white", "white", "tan", "tan", "tan", "tan", "tan", "tan", "tan", "coral", "black", "black", "aquamarine", "aquamarine", "black", "teal", "teal", "teal", "teal", "teal", "teal", "teal", "teal", "aquamarine", "aquamarine", "white"], #
    ["white", "white", "white", "white", "maroon", "maroon", "maroon", "maroon", "white", "white", "tan", "tan", "tan", "black", "black", "black", "coral", "aquamarine", "aquamarine", "aquamarine", "aquamarine", "black", "black", "black", "teal", "teal", "gray", "gray", "teal", "teal", "teal", "aquamarine"], #
    ["white", "white", "white", "aquamarine", "teal", "khaki", "khaki", "firebrick", "maroon", "maroon", "white", "white", "white", "tan", "coral", "coral", "coral", "coral", "aquamarine", "aquamarine", "aquamarine", "aquamarine", "black", "black", "teal", "teal", "teal", "teal", "gray", "gray", "teal", "teal", "aquamarine"], #
    ["white", "white", "white", "aquamarine", "aquamarine", "aquamarine", "aquamarine", "khaki", "firebrick", "firebrick", "maroon", "white", "white", "tan", "tan", "coral", "coral", "coral", "aquamarine", "aquamarine", "black", "aquamarine", "aquamarine", "black", "teal", "teal", "teal", "gray", "black", "black", "black", "white"], #
    ["white", "white", "white", "aquamarine", "gray", "gray", "gray", "aquamarine", "khaki", "teal", "teal", "maroon", "white", "tan", "orange", "tan", "tan", "coral", "aquamarine", "aquamarine", "black", "black", "black", "black", "black", "black", "black", "black", "white", "white", "white", "white"], #
    ["white", "white", "white", "aquamarine", "gray", "gray", "gray", "gray", "aquamarine", "khaki", "teal", "teal", "maroon", "white", "black", "tan", "tan", "tan", "aquamarine", "darkcyan", "darkcyan", "black", "black", "khaki", "khaki", "aquamarine", "firebrick", "maroon", "white", "white", "white", "white"], #
        #23-31
    ["white", "white", "aqua", "gray", "gray", "gray", "aqua", "gray", "aqua", "white", "gray", "red", "maroon", "black", "black", "coral", "tan", "black", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "aqua", "white", "white", "aqua", "red", "maroon", "white", "white", "white"], #
    ["white", "white", "white", "black", "gray", "aqua", "gray", "gray", "aqua", "white", "red", "red", "maroon", "aqua", "aqua", "black", "black", "black", "black", "darkcyan", "darkcyan", "aqua", "aqua", "white", "teal", "aqua", "white", "maroon", "white", "white", "white"], #
    ["white", "white", "white", "black", "aqua", "gray", "gray", "aqua", "aqua", "aqua", "gray", "red", "red", "black", "aqua", "black", "white", "white", "white", "black", "black", "black", "black", "teal", "teal", "aqua", "white", "white", "maroon", "white", "white"], #
    ["white", "white", "white", "white", "black", "gray", "aqua", "aqua", "aqua", "aqua", "teal", "red", "red", "black", "black", "white", "white", "white", "white", "white", "white", "white", "black", "black", "aqua", "white", "white", "white", "maroon", "white", "white"], #
    ["white", "white", "white", "white", "white", "black", "aqua", "aqua", "aqua", "aqua", "teal", "red", "red", "black", "white", "white", "white", "white", "white", "white", "darkcyan", "white", "black", "white", "white", "red", "red", "maroon", "white", "white"], #
    ["white", "white", "white", "white", "white", "white", "black", "aqua", "aqua", "aqua", "teal", "red", "black", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "black", "red", "red", "red", "maroon", "white", "white"], #
]
import turtle
from turtle import *
from random import randint

pen = turtle.Turtle()

pen.pensize(0)
pen.speed(0)

screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.setup(width=640, height=640)

side_length = PIXEL_SIZE

def draw_pixel(x,y,color):
    pen.penup()

    pen.goto(x,y)

    pen.pendown()

    pen.fillcolor(color)
    pen.begin_fill()

    for _ in range(4):
        pen.forward(side_length)
        pen.right(90)             

    pen.end_fill()

for y in range(0, 31):
    for x in range(32):
        draw_pixel(-320+PIXEL_SIZE*x,320+PIXEL_SIZE*y*-1, PIXEL_ART_ARRAY[y][x])
        print("y: ", y, "x:", x)

turtle.done()      


# drawing a grid
for y in range(3):
    for x in range(3):
        print(f"y: {y}, x: {x}")