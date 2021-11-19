#
# 
# 

import turtle
import time
import random

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

# Snake Food
food = turtle.Turtle()
food.speed(0) # This is the animation speed
food.shape("circle") # This is where you select a shape for the snake head
food.color("red")
food.penup()
food.goto(0,100) # Starting position

segments = []

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
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

    # Check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the segments
        segments.clear()


    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    
    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)


    move()

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments
            segments.clear()


    time.sleep(delay)

wn.mainloop()
