from turtle import Turtle
import turtle

screen = turtle.Screen()

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.fast=0.05
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 7
        self.y_move = 7

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bouncey(self):
        self.y_move *= -1

    def bouncexy(self):
        self.x_move *= -1
        self.fast *= 0.5

    def reset_po(self):
        self.fast=0.05
        self.goto(0, 0)
        self.bouncexy()


