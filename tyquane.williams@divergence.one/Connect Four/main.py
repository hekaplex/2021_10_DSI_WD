import numpy as np # This is a module for Python. (This is not Pygame!)

def create_board(): # This is where you are defining the variable
    board = np.zeros((6,7)) # This is where you decide how many rows and colums are displayed (up/down, right/left)
    return board # This is where your returning the function

board = create_board()
print(board) # This is how you are having the image shown
