'''Project 6-5: Tic Tac Toe 
Create a two-player Tic Tac Toe game. 
Console 
Welcome to Tic Tac Toe 
+---+---+---+ 
|   |   |   | 
+---+---+---+ 
|   |   |   | 
+---+---+---+ 
|   |   |   | 
+---+---+---+ 
X's turn 
Pick a row (1, 2, 3): 1
Pick a column (1, 2, 3): 1
+---+---+---+ 
| X |   |   | 
+---+---+---+ 
|   |   |   | 
+---+---+---+ 
|   |   |   | 
+---+---+---+ 
O's turn 
Pick a row (1, 2, 3): 1
Pick a column (1, 2, 3): 2
... 
... 
X's turn 
Pick a row (1, 2, 3): 3
Pick a column (1, 2, 3): 3
+---+---+---+ 
| X | O | O | 
+---+---+---+ 
|   | X |   | 
+---+---+---+ 
|   |   | X | 
+---+---+---+ 
X wins! 
Game over! 
Specifications 
 Use a list of lists to store the Tic Tac Toe grid. 
 If the user picks an invalid row or column or a cell that’s already taken, display an 
error message. 
 If there is a winner, the game should display an appropriate message and end. 
Otherwise, it should continue until the grid is full and end in a tie.
'''


def welcome():
    print("TIC TAC TOE!!!")

def theBoard():
    board = ["   1   2   3   \n +---+---+---+ \n |   |   |   | \n"]




def main():
    welcome()


if __name__ == "__main__":
    main()