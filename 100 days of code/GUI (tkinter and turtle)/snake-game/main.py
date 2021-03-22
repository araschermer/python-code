from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game!")
screen.tracer(0)
snake = Snake()
food = Food()
screen.listen()
scoreboard = Scoreboard()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_on = True
while game_on:
    screen.update()
    time.sleep(.1)
    snake.move_snake()
    # detect collision with food:
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.increase_size()
    # detect collision with wall:
    if snake.head.xcor() > 280 or -280 > snake.head.xcor() or -280 > snake.head.ycor() or snake.head.ycor() > 280:
        # game_on = False
        # scoreboard.game_over()
        scoreboard.reset_scoreboard()
        snake.reset_snake()
    # detect collision with body: GAME OVER
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 7:
            # game_on = False
            # scoreboard.game_over()
            scoreboard.reset_scoreboard()
            snake.reset_snake()

screen.exitonclick()
