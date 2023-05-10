from turtle import Turtle, Screen
from bats import Bat
from ball import Ball
from scoreboard import Scoreboard
import time

# set up screen
screen = Screen()
screen.screensize(canvwidth=600,canvheight=400)
screen.bgcolor("black")
screen.setworldcoordinates(-300,-200,300,200)
screen.title("Pong")
screen.tracer(0)

# Create game objects
ball = Ball()
scoreboard = Scoreboard()
bat_1 = Bat((280,0))
bat_2 = Bat((-280,0))

#assign controls to players
screen.listen()
screen.onkeypress(bat_1.up, "Up")
screen.onkeypress(bat_1.down, "Down")
screen.onkeypress(bat_2.up, "w")
screen.onkeypress(bat_2.down, "s")

# Gameplay within a while loop to a maximum score of 10
while True:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() >= 190 or ball.ycor() <= -190:
        ball.bounce()

    if ball.xcor() >= 280 or ball.xcor() <= -280:
        if ball.distance(bat_1) < 40 or ball.distance(bat_2) < 40:
            ball.hit()
        elif ball.xcor() >= 280:
            scoreboard.player_1_point()
            ball.reset_ball()
        elif ball.xcor() <= -280:
            scoreboard.player_2_point()
            ball.reset_ball()

    if scoreboard.player_1_score == 10:
        scoreboard.end_game("Player 1")
        break
    elif scoreboard.player_2_score == 10:
        scoreboard.end_game("Player 2")
        break

screen.exitonclick()