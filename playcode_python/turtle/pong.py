# Simple Pong Game
# By @thekilian - 5/2/19

import turtle

wn = turtle.Screen()
wn.title("Pong by @thekilian")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) # speed for the animation
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # default is 20 x 20
paddle_a.penup() # so it doesn't draw a line
paddle_a.goto(-350, 0) # initial position

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) # speed for the animation
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) # default is 20 x 20
paddle_b.penup() # so it doesn't draw a line
paddle_b.goto(350, 0) # initial position

# Ball
ball = turtle.Turtle()
ball.speed(0) # speed for the animation
ball.shape("square")
ball.color("white")
ball.penup() # so it doesn't draw a line
ball.goto(0, 0) # initial position

# Functions
def paddle_a_up():
    y = paddle_a.ycor() # ycor is from the turtle module. This line gets the ycoordinate
    y += 20 # add 20px to the ycor
    paddle_a.sety(y) # set the y of the paddle to the new ycoordinate

# Keyboard binding
wn.listen() # listen for keyboard input
wn.onkeypress(paddle_a_up, "w") # when w is pressed, call the paddle_a_up function

# https://www.youtube.com/watch?v=C6jJg9Zan7w&t=10s
# CONTINUE FROM 13:20

# Main game loop
while True:
    wn.update()
