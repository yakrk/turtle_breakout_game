from turtle import Turtle


class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.shapesize(stretch_wid=0.5, stretch_len=3, outline=5)
        self.penup()
        self.goto(position)
        
    def go_left(self):
        new_x = self.xcor() - 30
        self.goto(new_x, self.ycor())
        
    def go_right(self):
        new_x = self.xcor() + 30
        self.goto(new_x, self.ycor())