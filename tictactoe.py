from random import randint
board = []

for x in range(3):
    board.append(["-"] * 3)

def print_board(board):
    for row in board:
        print(" ".join(row))

def spot_free(row, column):
    for i in range(3):
        if i == row:
            relevantRow = board[i]
            if not relevantRow[column] == "-":
                return False
            else:
                return True

def you_win():
    print("Congratulations, you won!")

def computer_win():
    print("Looks like I win this round.")
                    
def game_over(board):
    row1 = board[0]
    row2 = board[1]
    row3 = board[2]
    for i in range(3):
    #testing for a vertical line
        if row1[i] == row2[i] and row2[i] == row3[i]:
            if row1[i] == "X":
                you_win()
                return True
            elif row1[i] == "O":
                computer_win()
                return True
            else:
                return False
    #testing for a diagonal line
        elif (row1[0] == row2[1] and row2[1] == row3[2]) or \
            (row1[2] == row2[1] and row2[1] == row3[0]):
            if row2[1] == "X":
                you_win()
                return True
            if row2[1] == "O":
                computer_win()
                return True
            else:
                return False
     #testing for a horizontal line
        elif board[i] == ["X", "X", "X"]:
            you_win()
            return True
        elif board[i] == ["O", "O", "O"]:
            computer_win()
            return True
        else:
            return False

print("Are you ready to play TicTacToe? Today, you'll be playing against the computer: me! \
Choose a row and a column for your first move.")
print_board(board)
turn = 0
while game_over(board) == False and turn < 5:
    #Player's turn
    row = int(input("Row: ")) - 1
    column = int(input("Column: ")) - 1
    if row > 2 or column > 2 or row < 0 or column < 0:
        print("Sorry, but that's not in the table! Try again next turn.")
    else:
        if spot_free(row, column) == True:
            selectedRow = board[row]
            selectedRow[column] = "X"
            print("The board now looks like this:")
            print_board(board)
        else:
            print("That spot has already been filled! Try again next turn.")
    turn = turn + 1
    #Computer's turn
    print("Here's my move:")
    cRow = randint(0,2)
    cColumn = randint(0,2)
    while spot_free(cRow, cColumn) == False:
        cRow = randint(0,2)
        cColumn = randint(0,2)
    if spot_free(cRow, cColumn) == True:
        selectedRow = board[cRow]
        selectedRow[cColumn] = "O"
        print_board(board)   
print("Good game.")
            