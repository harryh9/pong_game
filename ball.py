from turtle import Turtle
import random

HEADING = [0,90,180,270]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.penup()
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.shape("circle")
        self.speed("normal")
        #self.first_heading = random.randint(0,3)
        #self.setheading(HEADING[self.first_heading])
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def reset_ball(self):
        self.goto(0,0)


    def hit(self):
        self.x_move *= -1

