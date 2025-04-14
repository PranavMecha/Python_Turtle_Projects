import turtle
import pandas

screen = turtle.Screen()
screen.title("Pune Taluka Guessing Game")
image = "Pune-District.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("/Users/notpranavramane/Work/100_Days_Python/Day_25_MapGame/Map_Project/talukas.csv")
all_states = data.taluka.to_list()
guessed_states = []

while len(guessed_states) < 14:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/13 Talukas Correct",
                                    prompt="What's another taluka's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("talukas.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.taluka == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
