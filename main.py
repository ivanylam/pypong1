from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PyPong")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
screen.listen()
scoreboard = Scoreboard()

screen.onkey(r_paddle.go_up(), "Up")
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkeypress(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up(), "w")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect wall bounce
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    #detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 325 or ball.distance(l_paddle) < 50 and ball.xcor() < -325:
        ball.bounce_x()

    #when right paddle misses
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_point()

    # when left paddle misses
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
