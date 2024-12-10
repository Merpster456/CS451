import random
from mine_probability import *
import time

def create_board(rows, cols, num_mines, move1=(0, 0)):
    # Initialize board with 0s
    board = [[0 for _ in range(cols)] for _ in range(rows)]

    # Randomly place mines (-1 represents a mine)
    mines_placed = 0
    while mines_placed < num_mines:
        r = random.randint(0, rows - 1)
        c = random.randint(0, cols - 1)
        if (r, c) == move1 or board[r][c] == -1:
            continue
        board[r][c] = -1
        mines_placed += 1
        # Update neighboring cells' counts
        for i in range(max(0, r - 1), min(rows, r + 2)):
            for j in range(max(0, c - 1), min(cols, c + 2)):
                if board[i][j] != -1:
                    board[i][j] += 1
    return board

def print_board(board, revealed):
    # Function to print the current state of the game board
    for i, row in enumerate(board):
        row_display = []
        for j, cell in enumerate(row):
            if revealed[i][j]:
                row_display.append(str(cell) if cell != -1 else "M")
            else:
                row_display.append("#")
        print(" ".join(row_display))
    print()

def get_current_board(board, revealed):
    # Function to get the current state of the game board
    current_board = []
    for i, row in enumerate(board):
        row_display = []
        for j, cell in enumerate(row):
            if revealed[i][j]:
                row_display.append(str(cell) if cell != -1 else "M")
            else:
                row_display.append("#")
        current_board.append(row_display)
    return current_board

def reveal_cell(board, revealed, row, col):
    # Reveal the selected cell and, if it's empty (0), reveal adjacent cells recursively
    if revealed[row][col]:
        return
    revealed[row][col] = True
    if board[row][col] == 0:
        # Reveal all neighboring cells if it's a zero
        for i in range(max(0, row - 1), min(len(board), row + 2)):
            for j in range(max(0, col - 1), min(len(board[0]), col + 2)):
                if not revealed[i][j]:
                    reveal_cell(board, revealed, i, j)

def play_minesweeper(rows, cols, num_mines, move1):
    # Create the board and reveal the first move
    board = create_board(rows, cols, num_mines, move1)
    revealed = [[False for _ in range(cols)] for _ in range(rows)]
    
    # Reveal the first move
    reveal_cell(board, revealed, move1[0], move1[1])

    while True:
        print_board(board, revealed)
        # Check if player has won (all non-mine cells revealed)
        if all(revealed[i][j] or board[i][j] == -1 for i in range(rows) for j in range(cols)):
            print("Congratulations! You've won!")
            break

        # Get the next move
        move = input("Enter your move as 'row col': ")
        row, col = map(int, move.split())

        if board[row][col] == -1:
            print("BOOM! You hit a mine. Game over!")
            revealed = [[True for _ in range(cols)] for _ in range(rows)]  # Reveal entire board
            print_board(board, revealed)
            break
        else:
            reveal_cell(board, revealed, row, col)
   
def greedy_sweeper(rows, cols, num_mines, move1):
    # Create the board and reveal the first move
    board = create_board(rows, cols, num_mines, move1)
    revealed = [[False for _ in range(cols)] for _ in range(rows)]
    reveal_cell(board, revealed, move1[0], move1[1])

    while True:
        print_board(board, revealed)
        # Update `p_board` to reflect the current revealed state
        p_board = get_current_board(board, revealed)

        # Check if player has won (all non-mine cells revealed)
        if all(revealed[i][j] or board[i][j] == -1 for i in range(rows) for j in range(cols)):
            print("Congratulations! You've won!")
            break

        # Calculate probabilities and get the next move
        probabilities = calculate_mine_probabilities(p_board, num_mines)
        print("Mine probabilities:")
        for row in probabilities:
            print(row)

        row, col = get_next_move(p_board, probabilities)
        print(f"AI selects cell ({row}, {col})")

        if board[row][col] == -1:
            print("BOOM! You hit a mine. Game over!")
            revealed = [[True for _ in range(cols)] for _ in range(rows)]  # Reveal entire board
            print_board(board, revealed)
            break
        else:
            reveal_cell(board, revealed, row, col)

def test_probability(h,w,m):
    board = create_board(h,w,m)
    move1 = (0, 0)
    revealed = [[False for _ in range(w)] for _ in range(h)]
    reveal_cell(board,revealed=revealed,row=move1[0],col=move1[1])
    bboard = get_current_board(board, revealed)  
  
    probabilities = calculate_mine_probabilities(bboard, 4)
    print("Board:")
    for row in bboard:
        print(row)
    print("Mine Probabilities:")
    for row in probabilities:
        print(row)

    r,c = get_next_move(bboard, probabilities)
    print(f"AI selects cell ({r}, {c})")


if __name__ == '__main__':
    rows, cols, num_mines = 16,30,90

    # # play_minesweeper(rows, cols, num_mines, move1)
    greedy_sweeper(rows, cols, num_mines, move1 = (0, 0))
   
    # start_time = time.time()
    # test_probability(rows, cols, num_mines)
    # end_time = time.time()

    # print(f"Execution time: {end_time - start_time} seconds")
