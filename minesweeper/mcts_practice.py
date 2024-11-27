import numpy as np

class MCTS_Node:
    def __init__(self, state, parent=None, parent_action=None):  # Node constructor
        '''
        state:  For our game it represents the board state.
                Generally the board state is represented by an array.
                For nxn minesweeper it is the nxn board array

        parent: It is None for the root node and for other nodes it is equal to the node it is derived from.
                For the first turn as you have seen from the game it is None.

        children: It contains all possible actions from the current node.
                  For the second turn in our game this is 9 or 8 depending on where you make your move.

        parent_action: None for the root node and for other nodes it is equal to the action which it’s parent carried out.

        number_of_visits: Number of times current node is visited

        results: It’s a dictionary

        untried_actions: Represents the list of all possible actions

        action: Move which has to be carried out.

        '''
        self.state = state  # will be the minesweeper board
        self.parent = parent
        self.parent_action = parent_action
        self.children = []
        self.number_of_visits = 0
        self.results[1] = 0
        self.results[-1] = 0
        self.untried_actions = None
        self.untried_actions = self.untried_actions()
        return

    def untried_actions(self):
        self.untried_actions = self.state.get_legal_actions()
        return self.untried_actions
    
    def q(self):
        return self.results[1] - self.results[-1] # win loss differential
    
    def n(self):
        return self.number_of_visits
    
    def expand(self): # node expansion function
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
    
    def backpropigate(self, result): # update node stats
        self.number_of_visits += 1 
        self.results[result] += 1
        if self.parent:
            self.parent.backpropagate(result)
    
    def is_fully_expanded(self):
        return len(self.untried_actions) == 0
    
    def best_child(self, c_param = 0.1 ):
        choices_weights = [(c.q() / c.n()) + c_param * np.sqrt((2 * np.log(self.n()) / c.n())) for c in self.children]
        return self.children[np.argmax(choices_weights)]

    def rollout_policy(self, possible_moves): # currently random, will choose a better scheme
        return possible_moves[np.random.randint(len(possible_moves))]
    
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
        for i in range(simulation_no):
            v = self.tree_policy()
            reward = v.rollout()
            v.backpropigate(reward)
        return self.best_child(c_param=0.)
    
    def get_legal_actions(self):
        '''
        This is an opportunity to set our search space. 
        It is possible we can reduce legal moves to "reasonable moves"
        (limit island clicks and whatnot)
        
        returns: a list of possible move
        '''
        # Search space should be "island" with a 1 square buffer 
        legal_moves = []

        for y in range(self.height):
            for x in range(self.width):
                cell = self.board[y][x]
                if isinstance(cell, Cell) and (cell.seen or cell.flag):
                    continue

                # unrevealed cells are "reasonable" if they touch a revealed cell
                for dx in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        neighbor = self.board[ny][nx]
                        if isinstance(neighbor, Cell) and neighbor.seen:
                            legal_moves.append((x, y))
                            break
                else:
                    continue
                break

    return legal_moves


    def is_game_over(self):
        '''
        returns true if game is over else false
        '''

        
        pass

    def game_result(self):
        '''
        return 1 or -1 for win or loss. 
        (minesweeper has no tie condition)
        '''

        pass

    def move(self, action):
        '''
        update state based on moves. 
        returns the new game state.
        '''
        
        pass

    def main():
        root = MCTS_Node(state=initial_state)
        selected_node = root.best_action()
        return 
