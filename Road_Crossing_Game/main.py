import time
import random
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
draw=turtle.Turtle()
draw.hideturtle()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
draw.penup()
draw.pencolor("red")
draw.goto(-300,250)
draw.pendown()
draw.setheading(0)
draw.fd(600)
tom=Player()
score=Scoreboard()

car=CarManager()

screen.listen()
screen.onkey(tom.go_up, "Up")
screen.onkey(tom.go_down, "Down")
game_is_on = True
while game_is_on:
    time.sleep(score.time)
    screen.update()
    car.create_car()
    car.move()
    
    if tom.ycor() > 250:
        tom.reset_postion()
        score.point()
    for i in car.all_cars:
        if i.distance(tom) < 20:
            game_is_on = False
            score.game_over()
screen.exitonclick()