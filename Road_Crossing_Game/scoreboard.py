FONT = ("Courier", 24, "normal")
from turtle import Turtle
ALIGNMENT="center"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.time=0.1
        self.penup()
        self.hideturtle()
        self.score = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 260)
        self.write(f"Level : {self.score}", align="center", font=FONT)
        

    def point(self):
        self.score += 1
        self.time*=0.5
        self.update_scoreboard()
    def game_over(self):
        self.goto(150, 260)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)