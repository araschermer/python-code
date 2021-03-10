import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0) # for a smoother visualization of the movements on the  screen
player = Player()
screen.listen()
screen.onkeypress(player.up, "Up")
game_is_on = True
car_manager = CarManager()
scoreboard = Scoreboard()

while game_is_on:
    time.sleep(.1)
    screen.update()
    scoreboard.update_scoreboard()
    car_manager.create_car()
    car_manager.move()
    # detect collision with cars
    for car in car_manager.crossing_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
    # if turtle crossed finish line, level up
    if player.crossed():
        player.go_to_start()
        scoreboard.update_scoreboard()
        scoreboard.level_up()
        car_manager.speed_up()
screen.exitonclick()