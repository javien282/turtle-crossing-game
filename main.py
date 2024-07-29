import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_forward, key="Up")
screen.onkey(player.move_backward, key="Down")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_forward()

    # Detect player crossing finish line
    if player.ycor() > 280:
        scoreboard.add_point()
        car.increase_speed()
        player.reset_position()

    # Detect player distance from cars
    for cars in car.cars:
        if cars.distance(player) < 25:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()