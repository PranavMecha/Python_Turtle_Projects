
from turtle import Turtle

t = open("score.txt", mode="r")
a=t.read()
t.close()
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.i=0
        self.j=0
        self.penup()
        self.high_score = int(a)
        self.hideturtle()
        self.goto(-300,350)
        self.increment(self.j)
    def reset_score(self):

        if self.i>self.high_score:
            self.high_score=self.i
        j=0
        self.increment(j)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over", align="center", font=("Arial", 50, "normal"))

    def increment(self,j):
        self.clear()
        self.goto(-300, 350)
        if j!=0:
            self.i+=1
        else:
            self.i=0
        self.write(f"Score : {self.i}",align="center",font=("Arial",35,"normal"))
        self.goto(200, 350)
        self.write(f"High_Score : {self.high_score}", align="center", font=("Arial", 35, "normal"))



