from turtle import Turtle, Screen
import turtle as t

# generate a random hero name
# import heroes
# print(heroes.gen())

from random import choice, randint

#
pen = Turtle()
pen.shape("turtle")
pen.color("red")
sides = 10
angle = 360 / sides
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]


# draw shapes, triangle , square , pentagon, ..
def draw_shape(sides):
    angle = 360 / sides
    for _ in range(sides):
        pen.forward(100)
        pen.right(angle)


for _ in range(3, 11):
    pen.color(choice(colours))
    draw_shape(_)

# turtle Random walk
direction = [0, 90, 180, 270]
t.colormode(255)


def random_color():
    """generate random colour"""
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_colour = (r, g, b)
    return random_colour


def random_walk():
    for _ in range(50):
        pen.speed("fastest")
        pen.color(random_color())
        pen.forward(randint(5, 50))
        pen.setheading(choice(direction))
        pen.pensize(randint(2, 10))


random_walk()


# make_spirograph
def make_spirograph(shifting_degrees):
    pen.pensize(1)
    pen.speed("fastest")
    for _ in range(int(360 / shifting_degrees)):
        pen.circle(100)
        pen.color(random_color())
        heading = pen.heading()
        pen.setheading(heading + 5)


make_spirograph(shifting_degrees = 5)

screen = Screen()
screen.exitonclick()
