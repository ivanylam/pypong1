from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PyPong")
screen.tracer(0)

r_paddle = Paddle((-350, 0))
l_paddle = Paddle((350, 0))
ball = Ball()
screen.listen()

screen.onkey(l_paddle.go_up(), "Up")
screen.onkeypress(l_paddle.go_up, "Up")
screen.onkey(l_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_down, "Down")

screen.onkey(r_paddle.go_up(), "w")
screen.onkeypress(r_paddle.go_up, "w")
screen.onkey(r_paddle.go_down, "s")
screen.onkeypress(r_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #detect wall bounce
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()


screen.exitonclick()
