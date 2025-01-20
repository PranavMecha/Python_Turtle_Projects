from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,x):
        self.y_new=0
        self.x_=x
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(self.x_, self.y_new)

    def up(self):

        if self.y_new==240:
            pass
        else:
            self.y_new+=20
        self.goto(self.x_,self.y_new)

    def down(self):

        if self.y_new == -240:
            pass
        else:
            self.y_new -= 20
        self.goto(self.x_, self.y_new)



