from turtle import Turtle

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-260, 260)
        self.write(f"Level: {self.level}", align="left", font=("Arial", 20, "normal"))

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=("Arial", 20, "normal"))