from turtle import Turtle, Screen

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PyPong")
screen.tracer(0)

paddle = Turtle(shape="square")
paddle.penup()
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.goto(350, 0)

screen.listen()


def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


screen.onkey(go_up, "Up")
screen.onkeypress(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkeypress(go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()



screen.exitonclick()
