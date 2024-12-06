import itertools
from math import comb
from simple_sweeper import create_board, print_board, reveal_cell

def calculate_mine_probabilities(board, revealed, remaining_mines):
    rows, cols = len(board), len(board[0])
    probabilities = [[0 for _ in range(cols)] for _ in range(rows)]
    total_arrangements = 0

    # Focus only on cells adjacent to revealed ones
    frontier = set()
    for r in range(rows):
        for c in range(cols):
            if revealed[r][c] and board[r][c] >= 0:
                for dr, dc in itertools.product([-1, 0, 1], [-1, 0, 1]):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and not revealed[nr][nc]:
                        frontier.add((nr, nc))

    # If no frontier cells are available, make a random move
    if not frontier:
        return probabilities

    # Convert frontier to a list for indexing
    frontier = list(frontier)
    frontier_indices = range(len(frontier))

    # Ensure remaining_mines does not exceed the number of available frontier cells
    if remaining_mines > len(frontier):
        remaining_mines = len(frontier)

    # Generate mine arrangements only for frontier cells
    for arrangement in itertools.combinations(frontier_indices, remaining_mines):
        mine_set = set(arrangement)
        mine_board = [[0 for _ in range(cols)] for _ in range(rows)]
        for i, (r, c) in enumerate(frontier):
            if i in mine_set:
                mine_board[r][c] = 1

        # Validate arrangement
        if validate_arrangement(board, mine_board, revealed):
            total_arrangements += 1
            for i, (r, c) in enumerate(frontier):
                if i in mine_set:
                    probabilities[r][c] += 1

    # Normalize probabilities
    for r, c in frontier:
        if total_arrangements > 0:
            probabilities[r][c] = (probabilities[r][c] / total_arrangements) * 100

    return probabilities



def validate_arrangement(board, mine_board, revealed):
    rows, cols = len(board), len(board[0])
    for r in range(rows):
        for c in range(cols):
            if revealed[r][c] and board[r][c] >= 0:  # If it's a clue
                count_mines = 0
                for dr, dc in itertools.product([-1, 0, 1], [-1, 0, 1]):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        count_mines += mine_board[nr][nc]
                if count_mines != board[r][c]:
                    return False
    return True

def greedy_minesweeper_solver(rows, cols, total_mines, move1):
    # Step 1: Initialize the game
    board = create_board(rows, cols, total_mines, move1)
    revealed = [[False for _ in range(cols)] for _ in range(rows)]
    reveal_cell(board, revealed, move1[0], move1[1])

    while True:
        print_board(board, revealed)

        # Step 2: Calculate probabilities
        remaining_mines = max(0, total_mines - sum(row.count(True) for row in revealed))
        probabilities = calculate_mine_probabilities(board, revealed, remaining_mines)

        # Step 3: Find the safest cell
        safest_cell = None
        min_probability = float('inf')
        for r in range(rows):
            for c in range(cols):
                if not revealed[r][c] and probabilities[r][c] < min_probability:
                    min_probability = probabilities[r][c]
                    safest_cell = (r, c)

        if safest_cell is None:
            print("No safe moves left!")
            break

        r, c = safest_cell
        print(f"Clicking cell ({r}, {c}) with probability {min_probability:.2f}%")

        # Step 4: Simulate the click
        if board[r][c] == -1:
            print(f"BOOM! You hit a mine at ({r}, {c}). Game over!")
            revealed = [[True for _ in range(cols)] for _ in range(rows)]  # Reveal all cells
            print_board(board, revealed)
            break
        else:
            reveal_cell(board, revealed, r, c)

        # Step 5: Check win condition
        if all(revealed[i][j] or board[i][j] == -1 for i in range(rows) for j in range(cols)):
            print("Congratulations! You've won!")
            break

if __name__ == "__main__":
    rows, cols, total_mines = 8, 8, 10
    move1 = (0, 0)
    greedy_minesweeper_solver(rows, cols, total_mines, move1)