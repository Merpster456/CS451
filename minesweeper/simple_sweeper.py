import random

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


def export_game_state(board, revealed):
    return {
        "board": board,
        "revealed": revealed
    }
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

def rule_follower_ai(rows, cols, num_mines, move1):
    # Create board and reveal the first move
    board = create_board(rows, cols, num_mines, move1)
    revealed = [[False for _ in range(cols)] for _ in range(rows)]
    reveal_cell(board, revealed, move1[0], move1[1])

    def count_adjacent(board, revealed, row, col):
        """Count the number of hidden and revealed cells around a tile."""
        mines = 0
        hidden = 0
        for i in range(max(0, row - 1), min(rows, row + 2)):
            for j in range(max(0, col - 1), min(cols, col + 2)):
                if not revealed[i][j]:
                    hidden += 1
                elif board[i][j] == -1:
                    mines += 1
        return mines, hidden

    def get_random_adjacent_hidden(revealed, rows, cols):
        """Find a random hidden cell adjacent to a revealed cell."""
        candidates = []
        for r in range(rows):
            for c in range(cols):
                if revealed[r][c]:  # Look at revealed cells
                    for i in range(max(0, r - 1), min(rows, r + 2)):
                        for j in range(max(0, c - 1), min(cols, c + 2)):
                            if not revealed[i][j]:  # Adjacent hidden cell
                                candidates.append((i, j))
        return random.choice(candidates) if candidates else None

    def make_move(board, revealed):
        """Make a move based on Minesweeper rules."""
        for r in range(rows):
            for c in range(cols):
                if revealed[r][c] and board[r][c] > 0:
                    mines, hidden = count_adjacent(board, revealed, r, c)
                    
                    # Rule 1: If hidden cells == number of mines remaining, avoid hidden cells
                    if hidden == board[r][c] - mines:
                        continue  # Do nothing, as these cells are mines
                    
                    # Rule 2: If all mines are accounted for, reveal all remaining hidden cells
                    elif mines == board[r][c]:
                        for i in range(max(0, r - 1), min(rows, r + 2)):
                            for j in range(max(0, c - 1), min(cols, c + 2)):
                                if not revealed[i][j]:
                                    if board[i][j] == -1:
                                        return (False, board)  # Hit a mine
                                    reveal_cell(board, revealed, i, j)
                                    return (True, board)

        # Random adjacent move
        random_move = get_random_adjacent_hidden(revealed, rows, cols)
        if random_move:
            r, c = random_move
            if board[r][c] == -1:
                return (False, board)  # Hit a mine
            reveal_cell(board, revealed, r, c)
        return (True, board)

    while True:
        print_board(board, revealed)
        # Check for win condition: All non-mine cells revealed
        if all(revealed[i][j] or board[i][j] == -1 for i in range(rows) for j in range(cols)):
            print("AI has won!")
            break
        move_safe, board = make_move(board, revealed)
        if not move_safe:
            print("AI hit a mine! Game over!")
            revealed = [[True for _ in range(cols)] for _ in range(rows)]  # Reveal entire board
            print_board(board, revealed)
            break




if __name__ == '__main__':
    rows, cols, num_mines = 16, 30, 99
    # row, col = map(int, input("Enter your move as 'row col': ").split())
    row, col = 0, 0
    # create_board(rows, cols, num_mines, (row, col))
    # play_minesweeper(rows, cols, num_mines,(row, col))
    rule_follower_ai(rows, cols, num_mines, (row, col))




