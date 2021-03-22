from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.title("PONG")
screen.setup(width = 800, height = 600)
screen.listen()

left_paddle = Paddle("left")
right_paddle = Paddle("right")
left_paddle.paddle_listen(screen)
right_paddle.paddle_listen(screen)
ball = Ball()
scoreboard = Scoreboard()
game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # detect collision with the paddle
    if left_paddle.distance(ball) < 50 and ball.xcor() > -320 or right_paddle.distance(ball) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    # detect when paddle misses:
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.point_l()

    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.point_r()

screen.exitonclick()
