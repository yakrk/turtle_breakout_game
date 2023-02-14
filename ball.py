from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 1
        self.y_move = 1
        self.move_speed = 1
        self.speed(self.move_speed)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        
    def direction(self):
        if self.x_move > 0:
            is_moving_right = True
        else:
            is_moving_right = False
        return is_moving_right
