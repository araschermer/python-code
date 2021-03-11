from turtle import Turtle
from pathlib2 import Path

ALIGNMENT = 'center'
FONT = ("Courier-Bold", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highest_score = 0
        if Path('highest_score.txt').is_file():
            with open("highest_score.txt", "r") as file:
                self.highest_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}, Highest Score: {self.highest_score}", align = ALIGNMENT, font = FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align = ALIGNMENT, font = FONT)

    def reset_scoreboard(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            self.save_highest_score()
        self.score = 0
        self.update_score()

    def save_highest_score(self):
        with open("highest_score.txt", "w") as file:
            file.write(str(self.highest_score))
