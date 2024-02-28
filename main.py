from turtle import Screen
from player import TurtleP
from cars import Car
from level import Level
import time

# Screen configuration
screen = Screen()
screen.title("Turtle Cross Game")
screen.setup(width=600, height=600)
screen.tracer(0)

# Turtle configuration
turtle = TurtleP()
screen.listen()
screen.onkey(turtle.move_up, "Up")
screen.onkey(turtle.move_down, "Down")

# Car generation
cars = Car()

# Level generation
level = Level()

# Game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move(level.level)

    for car in cars.all_cars:
        if car.distance(turtle) < 20:
            turtle.game_over()
            game_is_on = False

    if turtle.ycor() > 280:
        turtle.goto(0, -280)
        level.level_up()

# Screen exit
screen.exitonclick()