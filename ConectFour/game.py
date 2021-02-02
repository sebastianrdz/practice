import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7
def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0

def get_next_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flipud(board))

def winning_move(board, piece):
    # Check horizontal location fpr win
    for c in range (COLUMN_COUNT):
        curr = 0
        for r in range(ROW_COUNT):
            if board[c][r] == piece:
                curr += 1
            else:
                curr = 0
            if curr == 4:
                return True
    return False

board = create_board()
game_over = False
turn = 0

print_board(board)
while not game_over:
    # Ask player one imput
    if turn == 0:
        col = input("Player 1, Make your selection (0-6):")
        if is_valid_location(board,col):
            row = get_next_row(board,col)
            drop_piece(board, row, col, 1)

            if winning_move(board, 1):
                print("Congratulations player 1, you won!!!")
                game_over == True

    # Ask playeer two imput
    else:
        col = input("Player 2, Make your selection (0-6):")
        if is_valid_location(board,col):
            row = get_next_row(board,col)
            drop_piece(board, row, col, 2)

            if winning_move(board, 2):
                print("Congratulations player 2, you won!!!")
                game_over == True
    print_board(board)
    turn += 1
    turn = turn % 2



