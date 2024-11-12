from random import randrange

class Cell:
    def __init__(self, value):
        self.value = value
        self.seen = False

    def __str__(self):
        return str(self.value)

class Board:

    def __str__(self):
        string = ""
        for row in reversed(self.board):
            for cell in row:
                string += str(cell) + " "
            string += "\n"
        return string

    def mineCheck(self, x, y):
        mines = 0
        nx = x
        ny = y - 1

        print("MINECHECK")
        print(x, y)

        if 0 <= nx and nx < self.width and 0 <= ny and ny < self.height:
            print(type(self.board[ny][nx]))
            if type(self.board[ny][nx]) == Cell and self.board[ny][nx].value == -1:
                mines += 1

        nx = x - 1
        ny = y

        if 0 <= nx < self.width and 0 <= ny < self.height:
            if type(self.board[ny][nx]) == Cell and self.board[ny][nx].value == -1:
                mines += 1

        nx = x
        ny = y + 1

        if 0 <= nx < self.width and 0 <= ny < self.height:
            if type(self.board[ny][nx]) == Cell and self.board[ny][nx].value == -1:
                mines += 1

        nx = x + 1
        ny = y

        if 0 <= nx < self.width and 0 <= ny < self.height:
            if type(self.board[ny][nx]) == Cell and self.board[ny][nx].value == -1:
                mines += 1

        nx = x + 1
        ny = y - 1

        if 0 <= nx < self.width and 0 <= ny < self.height:
            if type(self.board[ny][nx]) == Cell and self.board[ny][nx].value == -1:
                mines += 1

        nx = x - 1
        ny = y - 1

        if 0 <= nx < self.width and 0 <= ny < self.height:
            if type(self.board[ny][nx]) == Cell and self.board[ny][nx].value == -1:
                mines += 1

        nx = x - 1
        ny = y + 1

        if 0 <= nx < self.width and 0 <= ny < self.height:
            if type(self.board[ny][nx]) == Cell and self.board[ny][nx].value == -1:
                mines += 1

        nx = x + 1
        ny = y + 1

        if 0 <= nx < self.width and 0 <= ny < self.height:
            if type(self.board[ny][nx]) == Cell and self.board[ny][nx].value == -1:
                mines += 1

        return mines

    def __init__(self, h, w, m):
        # Initial Values
        self.height = h
        self.width = w
        self.mines = m
        self.board = []

        # Create grid for the board
        for row in range(h):
            self.board.append([])

            for col in range(w):
                self.board[row].append(0)

        # Add mines to random locations on the board
        x, y = 0, 0
        for _ in range(m):
            while True:
                x = randrange(w-1)
                y = randrange(h-1)
                print(f"x,y = ({x}, {y})")

                # If cell is already a mine redo
                if type(self.board[y][x]) == Cell and self.board[y][x].value == -1:
                    continue
                else:
                    self.board[y][x] = Cell(-1)
                    break

        print(self.__str__())
        print(self.mineCheck(x + 1, y))

        for row in range(h):
            x = 0
            for col in range(w):
                c = self.board[row][col]
                if type(c) == Cell and c.value == -1:
                    continue

                else:
                    n = self.mineCheck(x, y)
                    print(f"x,y = ({col}, {row}) ~ n = {n}")
                    self.board[row][col] = Cell(n)
                x += 1
            y += 1








b = Board(10, 25, 9)
print(b)

c = Cell(0)

print(type(c) == Cell)