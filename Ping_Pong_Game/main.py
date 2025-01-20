import time
import turtle
from Paddle_file import Paddle
from ball import Ball
import score_board
screen=turtle.Screen()
screen.setup(800,600)
screen.title("PING-PONG 🏓")
screen.bgcolor("black")
screen.tracer(0)

paddle=Paddle(350)
puddle=Paddle(-360)
gol=Ball()
r_score=score_board.Score(150,240)
l_score=score_board.Score(-150,240)

screen.listen()
screen.onkey(key="Up",fun=paddle.up)
screen.onkey(key="Down",fun=paddle.down)
screen.onkey(key="w",fun=puddle.up)
screen.onkey(key="s",fun=puddle.down)
dotted=turtle.Turtle()
def dotted_line():
    dotted.penup()
    dotted.pencolor("white")
    dotted.goto(0,300)
    dotted.setheading(270)
    for i in range(0,61):
        if i%2==0:
            dotted.pendown()
            dotted.fd(10)
        else:
            dotted.penup()
            dotted.fd(10)


Game_on=True
while Game_on:
    dotted_line()
    time.sleep(gol.fast)
    screen.update()
    gol.move()

    if gol.ycor()>=287 or gol.ycor()<=-280:
        gol.bouncey()
    if gol.distance(puddle) <50 and gol.xcor()<-340:
        gol.bouncexy()
    if gol.distance(paddle) <50 and gol.xcor()>332:
        gol.bouncexy()
    if gol.xcor() > 405:
        gol.reset_po()
        l_score.print_score(-150, 240, 1)
    if gol.xcor()<-405 :
        gol.reset_po()
        r_score.print_score(150, 240,1)

screen.exitonclick()