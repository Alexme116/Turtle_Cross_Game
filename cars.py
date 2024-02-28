from turtle import Turtle
from random import choice

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

class Car:
    def __init__(self):
        self.all_cars = []
    
    def create_car(self):
        chance = choice(range(6))
        if chance != 1:
            return
        car = Turtle("square")
        car.shapesize(1, 2)
        car.penup()
        car.color(choice(colors))
        car.goto(300, choice(range(-250, 250, 40)))
        self.all_cars.append(car)

    def move(self, speed):
        speed += 4
        for car in self.all_cars:
            car.backward(speed)
            if car.xcor() < -320:
                self.all_cars.remove(car)
                car.hideturtle()
