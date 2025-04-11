import time
import turtle
import snake
from Food import Food
from score import ScoreBoard
screen=turtle.Screen()
screen.setup(800,800)
box=turtle.Turtle()
screen.bgcolor("black")
screen.title("The Snake Game 🐍")

screen.tracer(0)

box.penup()
box.goto(300,300)
box.pendown()
box.pencolor("red")
box.pensize(10)
for i in range(0,4):
    box.rt(90)
    box.fd(600)
box.hideturtle()
viper=snake.Snake()
food=Food()
result=ScoreBoard()

screen.listen()
screen.onkey(key="Up",fun=viper.up)
screen.onkey(key="Down",fun=viper.down)
screen.onkey(key="Right",fun=viper.right)
screen.onkey(key="Left",fun=viper.left)

Game_on=True
while Game_on:
    screen.update()
    time.sleep(0.1)
    viper.move()

    if viper.head.distance(food)<20:
        food.refresh()
        result.increment(1)
        viper.extend()
    if viper.head.xcor()>290 or viper.head.xcor()<-290 or viper.head.ycor()>290 or viper.head.ycor()<-290:
        result.reset_score()
        x=open("score.txt",mode="w")
        x.write(str(result.high_score))
        x.close()
        viper.reset_snake()

    for segments in viper.snake_body[1:]:
            if viper.head.distance(segments)<10:
                result.reset_score()
                viper.reset_snake()

screen.exitonclick()
