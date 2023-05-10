from turtle import Turtle


class Bat(Turtle):
    def __init__(self,position):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.shape("square")
        self.shapesize(stretch_wid=0.5,stretch_len=4)
        self.color("white")
        self.goto(position)

    def up(self):
        if self.ycor() < 190:
            new_y_cor = self.ycor() + 20
            self.goto(self.xcor(), new_y_cor)

    def down(self):
        if self.ycor() > -190:
            new_y_cor = self.ycor() - 20
            self.goto(self.xcor(), new_y_cor)
