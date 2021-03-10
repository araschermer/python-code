from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier-Bold", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.goto(-100, 200)
        self.write(f" {self.l_score}", align = ALIGNMENT, font = FONT)
        self.goto(100, 200)
        self.write(f" {self.r_score}", align = ALIGNMENT, font = FONT)

    def point_l(self):
        self.l_score += 1
        self.clear()
        self.update_score()

    def point_r(self):
        self.r_score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align = ALIGNMENT, font = FONT)
