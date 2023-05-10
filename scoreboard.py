from turtle import Turtle, Screen

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.player_1_score = 0
        self.player_2_score = 0
        self.hideturtle()
        self.color("white")
        self.write_score()

    def write_score(self):
        self.goto(-100,180)
        self.write(self.player_2_score, align = "center", font= ("arial", 30, "normal"))
        self.goto(100, 180)
        self.write(self.player_1_score, align = "center", font= ("arial", 30, "normal"))


    def player_1_point(self):
        self.player_1_score += 1
        self.clear()
        self.write_score()

    def player_2_point(self):
        self.player_2_score += 1
        self.clear()
        self.write_score()

    def end_game(self, winner):
        self.goto(0,0)
        self.write(f"{winner} wins!", align="center", font=("arial", 60, "normal"))