from turtle import Turtle

class Score(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.score=0
        self.z=0
        self.print_score(x,y,self.z)
    def print_score(self,x,y,z):
        self.goto(x,y)
        self.clear()
        if z != 0:
            self.score += 1
        self.write(self.score, align="center", font=("Futura", 40, "normal"))
