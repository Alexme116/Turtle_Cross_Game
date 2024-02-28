from turtle import Turtle

class TurtleP(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(0, -280)
        self.left(90)

    def move_up(self):
        self.forward(20)
    
    def move_down(self):
        if self.ycor() > -280:
            self.backward(20)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 20, "normal"))