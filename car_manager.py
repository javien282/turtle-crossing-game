from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            rand_y = random.randint(-250, 250)
            new_car.goto(300, rand_y)
            self.cars.append(new_car)

    def move_forward(self):
        for new_car in self.cars:
            new_car.forward(STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        speed = STARTING_MOVE_DISTANCE
        speed_increase = speed + MOVE_INCREMENT
        for new_car in self.cars:
            new_car.forward(speed_increase)




