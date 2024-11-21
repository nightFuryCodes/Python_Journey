
from turtle import Screen, Turtle
from paddles import Paddles
from ball import Ball
import time
from scoreboard import Score
screen = Screen()

screen.bgcolor("black")
screen.setup(800, 600)
screen.title("pong")
screen.tracer(0)

l_paddle = Paddles((-380, 0))
r_paddle = Paddles((370, 0))

l_score = Score((-200, 240))
r_score = Score((200, 240))



ball = Ball()
screen.listen()

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.05)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 350:
        ball.bounce_x()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -350  :
        ball.bounce_x()

    if ball.xcor() > 380 :
        ball.reset_position()
        l_score.increase()

    if ball.xcor() < -380:
        r_score.increase()
        ball.reset_position()


screen.exitonclick()
