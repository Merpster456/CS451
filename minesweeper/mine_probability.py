import itertools
from math import comb
from simple_sweeper import *


def calculate_mine_probabilities(board, remaining_mines):
    # print("Calculating mine probabilities...")
    """
    Calculate mine probabilities for a Minesweeper board with the updated logic.
    
    Args:
        board: 2D list representing the Minesweeper board. 
               Numbers as strings represent clues; `'#'` represents unknown cells.
        remaining_mines: Total number of mines left to be placed.
    
    Returns:
        2D list of probabilities where each cell represents the probability of containing a mine.
    """
    rows, cols = len(board), len(board[0])
    probabilities = [[-1 if board[r][c] != '#' else 0 for c in range(cols)] for r in range(rows)]
    total_arrangements = 0

    # Step 1: Identify frontier cells and unbordered cells
    frontier_cells = set()
    unbordered_cells = set()
    
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == '#':  # Unknown cell
                adjacent_numbers = [
                    (r + dr, c + dc) 
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
                    if 0 <= r + dr < rows and 0 <= c + dc < cols and board[r + dr][c + dc] != '#'
                ]
                if adjacent_numbers:
                    frontier_cells.add((r, c))
                else:
                    unbordered_cells.add((r, c))

    # Convert to lists for indexing
    frontier_cells = list(frontier_cells)
    unbordered_cells = list(unbordered_cells)

    # Step 2: Backtracking to generate valid arrangements for frontier cells
    def validate_arrangement(board, mine_board):
        """Validate the current arrangement against the clues on the board."""
        for r in range(rows):
            for c in range(cols):
                if board[r][c].isdigit():
                    # Count mines around this cell
                    mines_count = sum(
                        mine_board[r + dr][c + dc]
                        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
                        if 0 <= r + dr < rows and 0 <= c + dc < cols
                    )
                    if mines_count != int(board[r][c]):
                        return False
        return True

    def backtrack(frontier_idx, placed_mines):
        """Backtracking function for valid frontier arrangements."""
        nonlocal total_arrangements
        if len(placed_mines) > remaining_mines:
            return
        if frontier_idx == len(frontier_cells):
            # Validate the current arrangement
            mine_board = [[0 for _ in range(cols)] for _ in range(rows)]
            for r, c in placed_mines:
                mine_board[r][c] = 1
            if validate_arrangement(board, mine_board):
                total_arrangements += 1
                # Update probabilities for the frontier
                for r, c in placed_mines:
                    probabilities[r][c] += 1
            return

        # Include the current cell as a mine
        backtrack(frontier_idx + 1, placed_mines + [frontier_cells[frontier_idx]])
        # Exclude the current cell
        backtrack(frontier_idx + 1, placed_mines)

    backtrack(0, [])

    # Step 3: Calculate probabilities for unbordered cells
    unbordered_prob = 0
    if total_arrangements > 0:
        remaining_unbordered_mines = remaining_mines - len(frontier_cells)
        if remaining_unbordered_mines > 0:
            unbordered_prob = (remaining_unbordered_mines / len(unbordered_cells)) * 100

    # Apply probabilities to unbordered cells
    for r, c in unbordered_cells:
        probabilities[r][c] = -1

    # Step 4: Normalize probabilities for frontier cells
    for r, c in frontier_cells:
        if total_arrangements > 0:
            probabilities[r][c] = (probabilities[r][c] / total_arrangements) * 100
            probabilities[r][c] = int(probabilities[r][c] + 0.5)  # Round to nearest integer 

    return probabilities


def get_next_move(board, probabilities):
    """
    Select the next move based on the mine probabilities.

    Args:
        board: 2D list representing the Minesweeper board.
        probabilities: 2D list of probabilities where each cell represents the probability of containing a mine.

    Returns:
        The row and column of the cell with the lowest mine probability.
    """
    flat_probs = [(r, c, p) for r, row in enumerate(probabilities) for c, p in enumerate(row)]
    # find smallest probability that is not -1
    min = 101
    for r, c, p in flat_probs:
        if p < min and p != -1:
            min = p
    if min == 101:
        return None
    for r, c, p in flat_probs:
        if p == min:
            return r, c

if __name__ == "__main__":
    # Example usage
    board = [['0', '0', '1', '#'],
             ['1', '1', '2', '#'],
             ['#', '#', '2', '#'],
             ['#', '#', '#', '#']]
    remaining_mines = 6
    probabilities = calculate_mine_probabilities(board, remaining_mines)
    print("Mine Probabilities:")
    for row in probabilities:
        print(row)
    
    next_move = get_next_move(board, probabilities)
    if next_move:
        print(f"Next move should be at row {next_move[0]}, column {next_move[1]}")
    else:
        print("No valid next move found.")
