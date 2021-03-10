from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE = 280
MOVEMENT_DIRECTION = 90


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(MOVEMENT_DIRECTION)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def crossed(self):
        if self.ycor() > FINISH_LINE:
            return True
        else:
            return False

    def go_to_start(self):
        self.goto(STARTING_POSITION)
