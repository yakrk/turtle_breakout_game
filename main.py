# import Turtle
from turtle import Screen, Turtle
from ball import Ball
from paddle import Paddle
from brick import Bricks
from score import Score

# show screen 
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout Game")
screen.tracer(0)

# define class
paddle = Paddle((0, -250))
ball = Ball()
score = Score()

#define bars
start_x_position = -380
start_y_position = 100
bricks = []
for j in range(4):
    y_position = j*30 + start_y_position
    for i in range(12):
        x_position = i * 70 + start_x_position
        bricks.append(Bricks((x_position, y_position)))

# define initial variables
screen.listen()
screen.onkeypress(paddle.go_left, "Left")
screen.onkeypress(paddle.go_right, "Right")


# set ball action
game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    
    #ball movement against walls
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()
        
    if ball.ycor() > 280: 
        ball.bounce_y()
        
    if ball.ycor() < -290:
        game_is_on = False
        score.game_over()
        
    #ball movement against paddle
    if ball.distance(paddle) < 30:
        ball.bounce_y()

    #ball movement against brick
    for brick in bricks:
        if ball.distance(brick) < 30:
            ball.bounce_y()
            brick.disappear()
            score.add_score()
            

screen.exitonclick()