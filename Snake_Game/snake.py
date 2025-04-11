

import turtle
class Snake:
    def __init__(self):
        self.snake_body = []
        self.Forward = 20
        self.Position = [(0, 0), (-20, 0), (-40, 0)]
        self.new_x =0
        self.new_y =0
        self.counti()
    def counti(self):
        self.position = self.Position
        for i in self.position:
          self.add_snake(i)
        self.head = self.snake_body[0]
    def add_snake(self,i):
        self.a = turtle.Turtle("square")
        self.a.color("white")
        self.a.penup()
        self.a.goto(i)
        self.snake_body.append(self.a)
    def extend(self):
        self.add_snake(self.snake_body[-1].position())
    def move(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            self.new_x = self.snake_body[seg_num - 1].xcor()
            self.new_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(self.new_x, self.new_y)
        self.head.fd(self.Forward)
    def up(self):
        if self.head.heading()==270:
            pass
        else:
            self.head.setheading(90)

    def down(self):
        if self.head.heading()==90:
            pass
        else:
            self.head.setheading(270)
    def right(self):
        if self.head.heading()==180:
            pass
        else:
            self.head.setheading(0)
    def left(self):
        if self.head.heading()==0:
            pass
        else:
            self.head.setheading(180)
    def reset_snake(self):
        for j in self.snake_body:
            j.goto(2000,2000)
        self.snake_body.clear()
        self.counti()
