# extract color from image
import colorgram
from colorgram.colorgram import Rgb

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
from random import choice
import turtle as turtle_module

color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
              (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102)]
turtle_module.colormode(255)
pen = turtle_module.Turtle()
pen.penup()
pen.setheading(225)
pen.forward(250)
pen.setheading(0)


def draw_dots(dots_per_line):
    for _ in range(dots_per_line):
        # pen.pendown()
        pen.dot(20, choice(color_list))
        pen.penup()
        pen.forward(50)


def draw_n_dots(dots_per_line, number_of_lines):
    pen.speed("fastest")
    pen.hideturtle()
    for _ in range(1, number_of_lines + 1):
        draw_dots(dots_per_line)
        pen.setheading(90)
        pen.forward(50)
        pen.setheading(180)
        pen.forward(500)
        pen.setheading(0)


draw_n_dots(dots_per_line = 10, number_of_lines =10)

screen = turtle_module.Screen()
screen.exitonclick()
