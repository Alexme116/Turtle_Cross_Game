from turtle import Turtle
from random import choice

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(choice(colors))
        self.goto(300, choice(range(-250, 250, 40)))
    
    def move(self):
        self.backward(10)