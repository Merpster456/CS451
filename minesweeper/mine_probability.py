import itertools
from math import comb

def calculate_mine_probabilities(board, remaining_mines):
    """
    Calculate mine probabilities for a Minesweeper board.
    
    Args:
        board: 2D list representing the Minesweeper board. 
               Numbers represent clues; `-1` represents unknown cells.
        remaining_mines: Total number of mines left to be placed.
    
    Returns:
        2D list of probabilities where each cell represents the probability of containing a mine.
    """
    rows, cols = len(board), len(board[0])
    probabilities = [[0 for _ in range(cols)] for _ in range(rows)]
    total_arrangements = 0

    # Step 2: Find all unknown cells
    unknown_cells = [(r, c) for r in range(rows) for c in range(cols) if board[r][c] == -1]

    # Step 3: Generate all possible arrangements
    for arrangement in itertools.combinations(range(len(unknown_cells)), remaining_mines):
        # Generate one arrangement
        mine_set = set(arrangement)
        mine_board = [[0 for _ in range(cols)] for _ in range(rows)]
        for i, (r, c) in enumerate(unknown_cells):
            if i in mine_set:
                mine_board[r][c] = 1

        # Validate the arrangement against board clues
        if validate_arrangement(board, mine_board):
            # Add valid arrangement probabilities
            total_arrangements += 1
            for i, (r, c) in enumerate(unknown_cells):
                if i in mine_set:
                    probabilities[r][c] += 1

    # Step 4: Normalize probabilities
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == -1 and total_arrangements > 0:
                probabilities[r][c] = (probabilities[r][c] / total_arrangements) * 100

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
            if board[r][c] >= 0:  # If it's a clue
                count_mines = 0
                for dr, dc in itertools.product([-1, 0, 1], [-1, 0, 1]):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        count_mines += mine_board[nr][nc]
                if count_mines != board[r][c]:
                    return False
    return True

# Example Usage
board = [
    [1, -1, -1],
    [2, -1, -1],
    [1, -1, -1]
]
remaining_mines = 3
probabilities = calculate_mine_probabilities(board, remaining_mines)

# Display probabilities
for row in probabilities:
    print(["{:.2f}%".format(cell) if cell > 0 else "0.00%" for cell in row])
