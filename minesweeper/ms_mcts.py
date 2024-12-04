import random
import numpy as np

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

class Minesweeper:
    def __init__(self, rows=5, cols=5, num_mines=5, move1=(0, 0)):
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        self.board = create_board(rows, cols, num_mines, move1)
        self.revealed = [[False for _ in range(cols)] for _ in range(rows)]
        reveal_cell(self.board, self.revealed, move1[0], move1[1])
        self.game_over = False
        self.result = 0  # 1 for win, -1 for loss

    def get_legal_actions(self):
        # Get the cells adjacent to the revealed ones
        adjacent_cells = set()
        for i in range(self.rows):
            for j in range(self.cols):
                if self.revealed[i][j]:
                    # Check all neighboring cells
                    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
                    for dx, dy in directions:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < self.rows and 0 <= ny < self.cols and not self.revealed[nx][ny]:
                            adjacent_cells.add((nx, ny))
        return list(adjacent_cells)

    def calculate_mine_probabilities(self):
        # Calculate the remaining mines (R)
        remaining_mines = self.num_mines - sum(1 for i in range(self.rows) for j in range(self.cols) if self.revealed[i][j] and self.board[i][j] == -1)
        
        # Get the unopened cells adjacent to revealed cells
        adjacent_cells = self.get_legal_actions()
        
        # Calculate the probability of a mine in each unopened cell
        mine_probabilities = {}
        for cell in adjacent_cells:
            R = remaining_mines
            U = len(self.get_adjacent_unrevealed_cells(cell))
            if U > 0:
                P = R / U
            else:
                P = 0  # No unopened neighboring cells
            mine_probabilities[cell] = P
        return mine_probabilities

    def get_adjacent_unrevealed_cells(self, cell):
        # Get all adjacent cells to a given cell that are not revealed
        x, y = cell
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        adjacent_unrevealed = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.rows and 0 <= ny < self.cols and not self.revealed[nx][ny]:
                adjacent_unrevealed.append((nx, ny))
        return adjacent_unrevealed

    def reveal(self, x, y):
        if self.revealed[x][y]:
            return self
        reveal_cell(self.board, self.revealed, x, y)
        if self.board[x][y] == -1:
            self.game_over = True
            self.result = -1  # Loss
        return self

    def is_game_over(self):
        return self.game_over

    def game_result(self):
        return self.result

    def move(self, action):
        x, y = action
        return self.reveal(x, y)

    def print_board(self):
        print_board(self.board, self.revealed)


class MCTS_Node:
    def __init__(self, state, parent=None, parent_action=None):
        self.state = state
        self.parent = parent
        self.parent_action = parent_action
        self.children = []
        self.number_of_visits = 0
        self.results = {1: 0, -1: 0}
        self.untried_actions = self.state.get_legal_actions()

    def expand(self):
        action = self.untried_actions.pop()
        next_state = self.state.move(action)
        child_node = MCTS_Node(next_state, parent=self, parent_action=action)
        self.children.append(child_node)
        return child_node

    def is_terminal_node(self):
        return self.state.is_game_over()

    def rollout(self):
        current_rollout_state = self.state
        while not current_rollout_state.is_game_over():
            possible_moves = current_rollout_state.get_legal_actions()
            action = self.rollout_policy(possible_moves)
            current_rollout_state = current_rollout_state.move(action)
        return current_rollout_state.game_result()

    def backpropagate(self, result):
        self.number_of_visits += 1
        self.results[result] += 1
        if self.parent:
            self.parent.backpropagate(result)

    def is_fully_expanded(self):
        return len(self.untried_actions) == 0

    def best_child(self, c_param=0.1):
        choices_weights = [(c.q() / c.n()) + c_param * np.sqrt((2 * np.log(self.n()) / c.n())) for c in self.children]
        return self.children[np.argmax(choices_weights)]

    def q(self):
        return self.results[1] - self.results[-1]

    def n(self):
        return self.number_of_visits

    def rollout_policy(self, possible_moves):
        # Choose a move with the lowest mine probability
        mine_probabilities = self.state.calculate_mine_probabilities()
        min_prob_move = min(possible_moves, key=lambda move: mine_probabilities.get(move, 0))
        return min_prob_move

    def tree_policy(self):
        current_node = self
        while not current_node.is_terminal_node():
            if not current_node.is_fully_expanded():
                return current_node.expand()
            else:
                current_node = current_node.best_child()
        return current_node

    def best_action(self):
        simulation_no = 1000
        for _ in range(simulation_no):
            v = self.tree_policy()
            reward = v.rollout()
            v.backpropagate(reward)
        return self.best_child(c_param=0.)

# Main simulation logic
def main():
    rows, cols, num_mines = 16, 30, 99  # Changed dimensions to 16x30 and 99 mines
    initial_move = (7, 15)  # Starting from the center roughly (adjusted)
    initial_state = Minesweeper(rows=rows, cols=cols, num_mines=num_mines, move1=initial_move)
    
    root = MCTS_Node(state=initial_state)
    move_count = 0
    while not root.state.is_game_over():
        # Print the board state after every move
        print(f"Move {move_count + 1}:")
        root.state.print_board()
        
        selected_node = root.best_action()
        print(f"AI chooses move: {selected_node.parent_action}")
        
        root = selected_node  # Move to the selected node
        move_count += 1
        
        if root.state.is_game_over():
            break
    
    # Final game result
    if root.state.game_result() == 1:
        print("Congratulations! You've won!")
    else:
        print("BOOM! You hit a mine. Game over!")
    root.state.print_board()

if __name__ == "__main__":
    main()
