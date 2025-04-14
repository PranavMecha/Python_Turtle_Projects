import turtle
import pandas
screen=turtle.Screen()
tom=turtle.Turtle()
tom.penup()
screen.bgpic("Pune-district.gif")
screen.title("Taluka Guessing Game")
data=pandas.read_csv("talukas.csv")
taluka=data.taluka
taluka_list=taluka.to_list()

def game():
    total = 0
    guess=""
    while total<13:
        guess=screen.textinput(f"Total Guessed : {total}/13","Enter your Guess :")
        if guess in taluka_list:
            row=data[data.taluka==guess]
            x=int(row.x)
            y=int(row.y)
            tom.goto(x,y)
            tom.pendown()
            tom.write(arg=guess,align='left', font=('Arial', 18, 'normal'))
            tom.penup()
            taluka_list.remove(guess)
            total+=1
        if guess=="Exit":
            screen.bye()
    while True:
        guess = screen.textinput("Congrats! You guessed all talukas 😁", "Type 'Exit' to close the game.")
        if guess == "Exit":
            screen.bye()
            break


game()




