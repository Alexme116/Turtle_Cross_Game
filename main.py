from turtle import Screen
from turtleP import TurtleP
from cars import Car
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
cars = []

# Game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car = Car()
    cars.append(car)
    carscopy = cars.copy()
    for car in carscopy:
        car.move()
        if car.xcor() < -200:
            cars.remove(car)


screen.exitonclick()