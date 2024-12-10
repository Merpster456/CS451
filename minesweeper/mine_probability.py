import itertools
from math import comb
from simple_sweeper import *

# def calculate_mine_probabilities(board, remaining_mines):
#     print("calculating mine probabilities...")
#     """
#     Calculate mine probabilities for a Minesweeper board.
    
#     Args:
#         board: 2D list representing the Minesweeper board. 
#                Numbers as strings represent clues; `'#'` represents unknown cells.
#         remaining_mines: Total number of mines left to be placed.
    
#     Returns:
#         2D list of probabilities where each cell represents the probability of containing a mine.
#     """
#     rows, cols = len(board), len(board[0])
#     probabilities = [[0 for _ in range(cols)] for _ in range(rows)]
#     total_arrangements = 0

#     # Step 2: Find all unknown cells
#     unknown_cells = [(r, c) for r in range(rows) for c in range(cols) if board[r][c] == '#']

#     # Backtracking function to generate valid mine arrangements
#     def backtrack(placed_mines, idx):
#         nonlocal total_arrangements
#         if len(placed_mines) == remaining_mines:
#             # Validate the current arrangement against board clues
#             mine_board = [[0 for _ in range(cols)] for _ in range(rows)]
#             for (r, c) in placed_mines:
#                 mine_board[r][c] = 1
#             if validate_arrangement(board, mine_board):
#                 total_arrangements += 1
#                 # Update the probabilities for valid arrangement
#                 for r, c in placed_mines:
#                     probabilities[r][c] += 1
#             return
        
#         if idx >= len(unknown_cells):
#             return
        
#         # Try placing a mine at the current cell
#         backtrack(placed_mines + [unknown_cells[idx]], idx + 1)
#         # Skip placing a mine at the current cell
#         backtrack(placed_mines, idx + 1)

#     # Start backtracking with an empty list of placed mines and starting index 0
#     backtrack([], 0)

#     # Step 4: Normalize probabilities
#     for r in range(rows):
#         for c in range(cols):
#             if board[r][c] == '#':  # Only normalize for unknown cells
#                 if total_arrangements > 0:
#                     probabilities[r][c] = (probabilities[r][c] / total_arrangements) * 100
#                     # take the ceiling of the probability
#                     probabilities[r][c] = int(probabilities[r][c] + 0.5)
#                 else:
#                     probabilities[r][c] = 0  # If no valid arrangements, set to 0%

#     return probabilities


                
    
# def validate_arrangement(board, mine_board):
#     """
#     Check if a mine arrangement is valid based on board clues.

#     Args:
#         board: Original Minesweeper board with clues.
#         mine_board: Board with mines for the current arrangement.

#     Returns:
#         True if the arrangement satisfies all clues; False otherwise.
#     """
#     rows, cols = len(board), len(board[0])
#     for r in range(rows):
#         for c in range(cols):
#             if board[r][c] != '#':  # If it's a clue (not '#')
#                 clue = int(board[r][c])  # Convert clue from string to integer
#                 count_mines = 0
#                 # Check the 8 neighbors of the current cell
#                 for dr, dc in itertools.product([-1, 0, 1], [-1, 0, 1]):
#                     nr, nc = r + dr, c + dc
#                     if 0 <= nr < rows and 0 <= nc < cols:
#                         count_mines += mine_board[nr][nc]
#                 if count_mines != clue:
#                     return False
#     return True
def calculate_mine_probabilities(board, remaining_mines):
    print("Calculating mine probabilities...")
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
    probabilities = [[0 for _ in range(cols)] for _ in range(rows)]
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
        # probabilities[r][c] = int(unbordered_prob + 0.5)  # Round to nearest integer
        # probability is for each arrangement generated in the backtracking, how many mines were used -> m_used?
        # for each arrangement, probability of a mine being in a cell is (total mines - m_used) / total arrangements
        # so the probability of a mine being in a cell is (total mines - m_used) / total arrangements * 100
        # superimpose this probability on the existing probability of a mine being in a cell
        # probabilities[r][c] = int(unbordered_prob + 0.5)  # Round to nearest integer
        probabilities[r][c] = -1
        



    # Step 4: Normalize probabilities for frontier cells
    for r, c in frontier_cells:
        if total_arrangements > 0:
            probabilities[r][c] = (probabilities[r][c] / total_arrangements) * 100
            # probabilities[r][c] = int(probabilities[r][c] + 0.5)  # Round to nearest integer 

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
    # min_prob = float('inf')
    # next_move = None
    # for r in range(len(board)):
    #     for c in range(len(board[0])):
    #         if board[r][c] == '#' and probabilities[r][c] < min_prob:
    #             min_prob = probabilities[r][c]
    # return r, c

    # sort probabilities low to high return the first one
    # flatten the 2d array
    flat_probs = [p for row in probabilities for p in row]
    # sort the flat array
    sorted_probs = sorted(flat_probs)
    # get the first element
    min_prob = sorted_probs[0]
    # get the index of the first element
    min_index = flat_probs.index(min_prob)
    # get the row and column of the first element
    rows = len(board)
    cols = len(board[0])
    row = min_index // cols
    col = min_index % cols
    return row, col

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