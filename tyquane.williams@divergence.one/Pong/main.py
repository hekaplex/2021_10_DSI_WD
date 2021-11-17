#
#
#

import turtle # This is a bulit in module called Turtle. (This is not Pygame!)

wn = turtle.Screen() # This is how you create the screen
wn.title("Pong") # This is where you can change the title
wn.bgcolor("black") # This is where you made the background black
wn.setup(width=800, height=600) # This is where you set the dimensions of the game window
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) # This is how control the speed of the paddle
paddle_a.shape("square") # This is where you decided the shape of the paddle
paddle_a.color("white") # This is where you decide the color of the paddle 
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # This is where you decide the shape of the paddle
paddle_a.penup()
paddle_a.goto(-350, 0) # This is where you decide the placement of the paddle

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) # This is how control the speed of the paddle
paddle_b.shape("square") # This is where you decided the shape of the paddle
paddle_b.color("white") # This is where you decide the color of the paddle
paddle_b.shapesize(stretch_wid=5, stretch_len=1) # This is where you decide the shape of the paddle
paddle_b.penup()
paddle_b.goto(350, 0) # This is where you decide the placement of the paddle

# Ball
ball = turtle.Turtle()
ball.speed(0) # This is how control the speed of the ball
ball.shape("square") # This is where you decided the shape of the ball
ball.color("white") # This is where you decide the color of the ball
ball.penup()
ball.goto(0, 0) # This is where you decide the placement of the paddle

# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

# Keyboard Input
wn.listen()
wn.onkeypress(paddle_a_up, "w")


# Main Game Loop
while True:
    wn.update()
