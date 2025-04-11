from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("dark turquoise")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.x_range = random.randint(-280, 280)
        self.y_range = random.randint(-250, 280)
        self.goto(self.x_range, self.y_range)