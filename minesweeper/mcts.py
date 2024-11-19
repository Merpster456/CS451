import random
import math

class MCTSAgent:
    def __init__(self, board):
        self.board = board
        self.max_depth = 5  
        self.simulation_count = 100  # Number of simulations per move

    def select_move(self):
        best_move = None
        best_value = -float('inf')

        for row in range(self.board.height):
            for col in range(self.board.width):
                cell = self.board.board[row][col]
                if not cell.seen and not cell.flag:
                    entropy = self.calculate_entropy(row, col)
                    value = self.simulate_move(row, col, entropy)

                    if value > best_value:
                        best_value = value
                        best_move = (row, col)

        return best_move

    def calculate_entropy(self, x, y):
        # This is a simple entropy heuristic based on surrounding unrevealed cells
        # A cell with more unknown neighbors is more uncertain (higher entropy).
        entropy = 0
        unknown_neighbors = 0

        for nx, ny in self.get_neighbors(x, y):
            neighbor = self.board.board[ny][nx]
            if not neighbor.seen:
                entropy += 1  # Increase entropy if the neighbor is not revealed
                unknown_neighbors += 1

        # Lower entropy is better, so return a scaled value.
        return entropy / max(1, unknown_neighbors)  # Avoid division by zero

    def get_neighbors(self, x, y):
        neighbors = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.board.width and 0 <= ny < self.board.height:
                neighbors.append((nx, ny))
        
        return neighbors

    def simulate_move(self, x, y, entropy):
        # Simulate the result of revealing the cell
        original_state = self.board.board[y][x].seen
        self.board.board[y][x].seen = True

        # A simple simulation could just check if it's a safe move.
        # This is where you can apply more advanced logic.
        result = 0
        if self.board.board[y][x].value == -1:  # Mine
            result = -100  # Bad result for hitting a mine
        else:
            result = entropy  # Otherwise, use the entropy as a proxy for safety

        # Restore the original state
        self.board.board[y][x].seen = original_state

        return result

    def backpropagate(self, move_result):
        # This is a placeholder for a real backpropagation mechanism
        # where we would adjust the values of nodes based on simulations.
        pass

