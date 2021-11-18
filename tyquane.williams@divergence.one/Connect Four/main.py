import numpy as np # This is a module for Python. (This is not Pygame!)

def create_board(): # This is where you are defining the variable
    board = np.zeros((6,7)) # This is where you decide how many rows and colums are displayed (up/down, right/left)
    return board # This is where your returning the function

board = create_board()
game_over = False
turn = 0

while not game_over:
    # Ask for Player 1 Input
    if turn == 0:
        selection = int(input("Player 1 Make Your Selection (0-6):"))

        print(selection)
        print(type(selection))
    
    # Ask for Player 2 Input
