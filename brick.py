from turtle import Turtle

class Bricks(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=3, outline=5)
        self.penup()
        self.goto(position)
        
    def disappear(self):
        self.goto(50000,50000)
        