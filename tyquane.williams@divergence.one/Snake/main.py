#
# 
# 

import turtle
import time

delay = 0.1

# Screen Setup
wn = turtle.Screen()
wn.title("Snake") # This is where you change the Title 
wn.bgcolor("green") # This is where you set the background color
wn.setup(width=600, height=600) # This is where you set up the game dimensions
wn.tracer(0) # Turns off the screen updates

# Snake Head
head = turtle.Turtle()
head.speed(0) # This is the animation speed
head.shape("square") # This is where you select a shape for the snake head
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop" # This is where you can decide the direction the snake will go


# Functions
def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_left():
    head.direction = "left"

def go_right():
    head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard Bindings
wn.listen()
wn.onkeypress(go_up, "w") # The Snake will go up when you press w on the keyboard
wn.onkeypress(go_down, "s") # The Snake will go down when you press s on the keyboard
wn.onkeypress(go_left, "a") # The Snake will go left when you press a on the keyboard
wn.onkeypress(go_right, "d") # The Snake will go right when you press d on the keyboard

# Main Game Loop
while True:
    wn.update()

    move()

    time.sleep(delay)

wn.mainloop()
