from turtle import Turtle

FONT = ("Courier", 20, "normal")
ALIGNMENT="left"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-250, 250)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def level_up(self):
        self.level += 1
        self.update_scoreboard()
        # self.write(f"GOOD JOB!", align="center", font=FONT)

    def game_over(self):
        self.goto(-80, 0)
        self.write(f"GAME OVER!", align=ALIGNMENT, font=FONT)
