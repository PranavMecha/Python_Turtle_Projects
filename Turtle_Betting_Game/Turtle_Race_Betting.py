import turtle
import random

race=False

screen=turtle.Screen()
screen.setup(width=500,height=500)
user_bet=screen.textinput(title="Make Your Bet",prompt="Which color turtle will win the race ?")
colour=["red","orange","green","dark turquoise","blue","purple"]

racer=[]

j=-150
for i in range(0,6):
    a = turtle.Turtle("turtle")
    a.color(colour[i])
    a.penup()
    a.goto(-230,j)
    j=j+50
    racer.append(a)
if user_bet:
    race=True
while race:

    for a_candi in racer:
        if a_candi.xcor()>230:
            if a_candi.pencolor()==user_bet:
                print(f"Congrats Your {a_candi.pencolor()} turtle won the race ")

                race=False
                break
            else:
                print(f"Oops!! {a_candi.pencolor()} turtle won the race.")
                race = False
                break
        distance = random.randint(0, 10)
        a_candi.fd(distance)

screen.exitonclick()