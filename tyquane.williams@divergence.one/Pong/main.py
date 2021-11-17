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
ball.dx = 0.2 # This is where the ball movement is set (ball moves 0.2 pixels over)
ball.dy = -0.2 # This is where the ball movement is set (ball moves 0.2 pixels over)

# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20 # This where you set the upward movement distance for paddleA
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20 # This where you set the downward movement distance for paddleA
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20 # This where you set the upward movement distance for paddleB
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20 # This where you set the downward movement distance for paddleB
    paddle_b.sety(y)

# Keyboard Input
wn.listen()
wn.onkeypress(paddle_a_up, "w") # This is where you set the button for moving paddleA upwards
wn.onkeypress(paddle_a_down, "s") # This is where you set the button for moving paddleA downwards
wn.onkeypress(paddle_b_up, "Up") # This is where you set the button for moving paddleB upwards
wn.onkeypress(paddle_b_down, "Down")  # This is where you set the button for moving paddleB downwards

# Main Game Loop
while True:
    wn.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Boundaries
    if ball.ycor() > 290: # This is the upper boarder for the ball to bounce off from (Top)
        ball.sety(290) # This tells the ball not to go any further than the 290 coordinate
        ball.dy *= -1 # This tells the ball to head downwards by -1 once is reaches the 290 coordinate

    if ball.ycor() < -290: # This is the lower boarder for the ball to bounce off from (Bottom)
        ball.sety(-290) # This tells the ball not to go any further than the -290 coordinate
        ball.dy *= -1 # This tells the ball to head upwards by -1 once is reaches the -290 coordinate

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

