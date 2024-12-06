import itertools
from math import comb

def calculate_mine_probabilities(board, remaining_mines):
    """
    Calculate mine probabilities for a Minesweeper board.
    
    Args:
        board: 2D list representing the Minesweeper board. 
               Numbers as strings represent clues; `'#'` represents unknown cells.
        remaining_mines: Total number of mines left to be placed.
    
    Returns:
        2D list of probabilities where each cell represents the probability of containing a mine.
    """
    rows, cols = len(board), len(board[0])
    probabilities = [[0 for _ in range(cols)] for _ in range(rows)]
    total_arrangements = 0

    # Step 2: Find all unknown cells
    unknown_cells = [(r, c) for r in range(rows) for c in range(cols) if board[r][c] == '#']

    # Backtracking function to generate valid mine arrangements
    def backtrack(placed_mines, idx):
        nonlocal total_arrangements
        if len(placed_mines) == remaining_mines:
            # Validate the current arrangement against board clues
            mine_board = [[0 for _ in range(cols)] for _ in range(rows)]
            for (r, c) in placed_mines:
                mine_board[r][c] = 1
            if validate_arrangement(board, mine_board):
                total_arrangements += 1
                # Update the probabilities for valid arrangement
                for r, c in placed_mines:
                    probabilities[r][c] += 1
            return
        
        if idx >= len(unknown_cells):
            return
        
        # Try placing a mine at the current cell
        backtrack(placed_mines + [unknown_cells[idx]], idx + 1)
        # Skip placing a mine at the current cell
        backtrack(placed_mines, idx + 1)

    # Start backtracking with an empty list of placed mines and starting index 0
    backtrack([], 0)

    # Step 4: Normalize probabilities
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == '#':  # Only normalize for unknown cells
                if total_arrangements > 0:
                    probabilities[r][c] = (probabilities[r][c] / total_arrangements) * 100
                else:
                    probabilities[r][c] = 0  # If no valid arrangements, set to 0%

    return probabilities

def validate_arrangement(board, mine_board):
    """
    Check if a mine arrangement is valid based on board clues.

    Args:
        board: Original Minesweeper board with clues.
        mine_board: Board with mines for the current arrangement.

    Returns:
        True if the arrangement satisfies all clues; False otherwise.
    """
    rows, cols = len(board), len(board[0])
    for r in range(rows):
        for c in range(cols):
            if board[r][c] != '#':  # If it's a clue (not '#')
                clue = int(board[r][c])  # Convert clue from string to integer
                count_mines = 0
                # Check the 8 neighbors of the current cell
                for dr, dc in itertools.product([-1, 0, 1], [-1, 0, 1]):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        count_mines += mine_board[nr][nc]
                if count_mines != clue:
                    return False
    return True

def select_next_move(board, probabilities):
    """
    Select the next move based on the mine probabilities.

    Args:
        board: 2D list representing the Minesweeper board.
        probabilities: 2D list of probabilities where each cell represents the probability of containing a mine.

    Returns:
        The row and column of the cell with the lowest mine probability.
    """
    min_prob = float('inf')
    next_move = None
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == '#' and probabilities[r][c] < min_prob:
                min_prob = probabilities[r][c]
                next_move = (r, c)
    return next_move

# Example Usage
board = [
    ['0', '1', '#'],
    ['1', '3', '#'],
    ['#', '#', '#']
]
remaining_mines = 3
probabilities = calculate_mine_probabilities(board, remaining_mines)

# Display probabilities
for row in probabilities:
    print(["{:.2f}%".format(cell) if cell > 0 else "0.00%" for cell in row])

# Select the next move based on probabilities
next_move = select_next_move(board, probabilities)
print("Next move:", next_move)
