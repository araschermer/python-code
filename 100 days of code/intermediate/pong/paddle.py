from turtle import Turtle

UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.create_paddle(position)

    def up(self):
        # self.setheading(UP)
        ycor = self.ycor() + 20
        self.goto(self.xcor(), ycor)

    def down(self):
        # self.setheading(DOWN)
        ycor = self.ycor() - 20
        self.goto(self.xcor(), ycor)

    def create_paddle(self, position):
        self.shape("square")
        self.shapesize(stretch_wid = 5, stretch_len = 1)
        self.color("white")
        self.penup()
        if self.position == "left":
            self.goto(-350, 0)
        elif self.position == "right":
            self.goto(350, 0)
        else:
            self.goto(position)

    def paddle_listen(self, screen):
        if self.position == "right":
            screen.onkey(self.up, "Up")
            screen.onkey(self.down, "Down")
        else:
            screen.onkey(self.up, "w")
            screen.onkey(self.down, "s")
