from random import choice, randint
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 5
SHAPE = "square"


class CarManager:
    def __init__(self):
        self.crossing_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def move(self):
        for car in self.crossing_cars:
            car.backward(self.car_speed-randint(1, 5))

    def create_car(self):
        random_chances = randint(0, 9)
        if random_chances % 3 == 0:
            new_car = Turtle()
            new_car.shape(SHAPE)
            new_car.penup()
            new_car.color(choice(COLORS))
            new_car.shapesize(stretch_wid = 1, stretch_len = 2)
            y = randint(-250, 250)
            new_car.goto(300, y)
            self.crossing_cars.append(new_car)
        return self.crossing_cars

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT
