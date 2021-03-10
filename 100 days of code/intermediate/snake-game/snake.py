from turtle import Turtle

SIZE = 1
MOVE_DISTANCE = 10
STARTING_POSITION = 0
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def move_snake(self):
        for segment_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_number - 1].xcor()
            new_y = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def create_snake(self):
        for _ in range(3):
            self.increase_size()
            self.segments[0].color("orange")

    def increase_size(self):
        x = STARTING_POSITION
        segment = Turtle(shape = "square")
        segment.shapesize(SIZE)
        segment.color("white")
        segment.penup()
        segment.goto(x, 0)
        x -= 20
        self.segments.append(segment)
