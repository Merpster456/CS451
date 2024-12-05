from random import randrange

class Cell:
    def __init__(self, value):
        self.value = value
        self.seen = False
        self.flag = False
        self.edge = False
        self.edgeCount = 0
        self.prob = -1

    def __str__(self):
        return str(self.value)

class Board:

    def __init__(self, h, w, m, x0, y0):
        # Initial Values
        self.height = h
        self.width = w
        self.mines = []
        self.board = []

        safezone = [(x0, y0), (x0, y0 - 1), (x0 + 1, y0 - 1), (x0 + 1, y0), (x0 + 1, y0 + 1),
                    (x0, y0 + 1), (x0 - 1, y0 + 1), (x0 - 1, y0), (x0 - 1, y0 - 1)]

        # Create grid for the board
        for row in range(h):
            self.board.append([])
            for col in range(w):
                self.board[row].append(0)

        # Add mines to random locations on the board
        x, y = 0, 0
        for _ in range(m):
            while True:
                x = randrange(w)
                y = randrange(h)
                print(f"x,y = ({x}, {y})")

                # If cell is already a mine redo
                if type(self.board[y][x]) == Cell and self.board[y][x].value == -1:
                    continue

                # Make sure first move is always safe
                elif (x, y) in safezone:
                    continue
                else:
                    self.board[y][x] = Cell(-1)
                    self.mines.append((x, y))
                    break

        for row in range(h):
            for col in range(w):
                c = self.board[row][col]
                if type(c) == Cell and c.value == -1:
                    continue

                else:
                    n = self.mineCheck(col, row)
                    print(f"x,y = ({col}, {row}) ~ n = {n}")
                    self.board[row][col] = Cell(n)

        self.board[y0][x0].seen = True
        self.reveal(x0, y0)

    def __str__(self):
        string = ""
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                c_str = str(self.board[y][x].value)
                if not self.board[y][x].seen:
                    c_str = "#"
                if self.board[y][x].prob == 100:
                    c_str="!"
                if self.board[y][x].prob == 0:
                    c_str="$"
                string += c_str + " "
            string += "\n"
        return string

    def reveal(self, x, y, fringe=[]):
        # upper
        nx = x
        ny = y - 1

        if 0 <= nx < self.width and 0 <= ny < self.height:
            if self.board[ny][nx].value >= 0 and not self.board[ny][nx].seen:
                self.board[ny][nx].seen = True
                if self.board[ny][nx].value == 0:
                    fringe.append((nx, ny))

        # left
        nx = x - 1
        ny = y

        if 0 <= nx < self.width and 0 <= ny < self.height:
            if self.board[ny][nx].value >= 0 and not self.board[ny][nx].seen:
                self.board[ny][nx].seen = True
                if self.board[ny][nx].value == 0:
                    fringe.append((nx, ny))

        # lower
        nx = x
        ny = y + 1

        if 0 <= nx < self.width and 0 <= ny < self.height:
            if self.board[ny][nx].value >= 0 and not self.board[ny][nx].seen:
                self.board[ny][nx].seen = True
                if self.board[ny][nx].value == 0:
                    fringe.append((nx, ny))

        # right
        nx = x + 1
        ny = y

        if 0 <= nx < self.width and 0 <= ny < self.height:
            if self.board[ny][nx].value >= 0 and not self.board[ny][nx].seen:
                self.board[ny][nx].seen = True
                if self.board[ny][nx].value == 0:
                    fringe.append((nx, ny))

        # upper right
        nx = x + 1
        ny = y - 1

        if 0 <= nx < self.width and 0 <= ny < self.height:
            if self.board[ny][nx].value != -1 and not self.board[ny][nx].seen:
                self.board[ny][nx].seen = True
                if self.board[ny][nx].value == 0:
                    fringe.append((nx, ny))

        # upper left
        nx = x - 1
        ny = y - 1

        if 0 <= nx < self.width and 0 <= ny < self.height:
            if self.board[ny][nx].value >= 0 and not self.board[ny][nx].seen:
                self.board[ny][nx].seen = True
                if self.board[ny][nx].value == 0:
                    fringe.append((nx, ny))

        # lower left
        nx = x - 1
        ny = y + 1

        if 0 <= nx < self.width and 0 <= ny < self.height:
            if self.board[ny][nx].value >= 0 and not self.board[ny][nx].seen:
                self.board[ny][nx].seen = True
                if self.board[ny][nx].value == 0:
                    fringe.append((nx, ny))

        # lower right
        nx = x + 1
        ny = y + 1

        if 0 <= nx < self.width and 0 <= ny < self.height:
            if self.board[ny][nx].value >= 0 and not self.board[ny][nx].seen:
                self.board[ny][nx].seen = True
                if self.board[ny][nx].value == 0:
                    fringe.append((nx, ny))

        if fringe:
            (x,y) = fringe.pop()
            self.reveal(x, y, fringe)


    def mineCheck(self, x, y):
        mines = 0
        nx = x
        ny = y - 1

        print("MINECHECK")
        print(x, y)

        if 0 <= nx < self.width and 0 <= ny < self.height:
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

    def edgeCount(self):
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                count = 0
                if self.board[y][x].seen:
                    self.board[y][x].edge = False

                    # left
                    if 0 <= x - 1 < self.width:
                        if not self.board[y][x - 1].seen:
                            self.board[y][x - 1].edge = True
                            count += 1

                    # upper left
                    if 0 <= x - 1 < self.width and 0 <= y - 1 < self.height:
                        if not self.board[y - 1][x - 1].seen:
                            self.board[y - 1][x - 1].edge = True
                            count += 1

                    # up
                    if 0 <= y - 1 < self.height:
                        if not self.board[y - 1][x].seen:
                            self.board[y - 1][x].edge = True
                            count += 1

                    # upper right
                    if 0 <= x + 1 < self.width and 0 <= y - 1 < self.height:
                        if not self.board[y - 1][x + 1].seen:
                            self.board[y - 1][x + 1].edge = True
                            count += 1

                    # right
                    if 0 <= x + 1 < self.width:
                        if not self.board[y][x + 1].seen:
                            self.board[y][x + 1].edge = True
                            count += 1

                    # bottom right
                    if 0 <= x + 1 < self.width and 0 <= y + 1 < self.height:
                        if not self.board[y+1][x + 1].seen:
                            self.board[y+1][x + 1].edge = True
                            count += 1

                    # bottom
                    if 0 <= y + 1 < self.height:
                        if not self.board[y + 1][x].seen:
                            self.board[y + 1][x].edge = True
                            count += 1

                    # bottom left
                    if 0 <= x - 1 < self.width and 0 <= y + 1 < self.height:
                        if not self.board[y + 1][x - 1].seen:
                            self.board[y + 1][x - 1].edge = True
                            count += 1

                self.board[y][x].edgeCount = count

    def seenCount(self, x, y):
        # Counts the number of seen cells around cell
        count = 0

        # left
        if 0 <= x - 1 < self.width:
            if self.board[y][x - 1].seen:
                count += 1

        # upper left
        if 0 <= x - 1 < self.width and 0 <= y - 1 < self.height:
            if self.board[y - 1][x - 1].seen:
                count += 1

        # up
        if 0 <= y - 1 < self.height:
            if self.board[y - 1][x].seen:
                count += 1

        # upper right
        if 0 <= x + 1 < self.width and 0 <= y - 1 < self.height:
            if self.board[y - 1][x + 1].seen:
                count += 1

        # right
        if 0 <= x + 1 < self.width:
            if self.board[y][x + 1].seen:
                count += 1

        # bottom right
        if 0 <= x + 1 < self.width and 0 <= y + 1 < self.height:
            if self.board[y + 1][x + 1].seen:
                count += 1

        # bottom
        if 0 <= y + 1 < self.height:
            if self.board[y + 1][x].seen:
                count += 1

        # bottom left
        if 0 <= x - 1 < self.width and 0 <= y + 1 < self.height:
            if self.board[y + 1][x - 1].seen:
                count += 1

        return count

    def probHundredCount(self, x, y):
        count = 0

        # left
        if 0 <= x - 1 < self.width:
            if self.board[y][x - 1].prob == 100:
                count += 1

        # upper left
        if 0 <= x - 1 < self.width and 0 <= y - 1 < self.height:
            if self.board[y - 1][x - 1].prob == 100:
                count += 1

        # up
        if 0 <= y - 1 < self.height:
            if self.board[y - 1][x].prob == 100:
                count += 1

        # upper right
        if 0 <= x + 1 < self.width and 0 <= y - 1 < self.height:
            if self.board[y - 1][x + 1].prob == 100:
                count += 1

        # right
        if 0 <= x + 1 < self.width:
            if self.board[y][x + 1].prob == 100:
                count += 1

        # bottom right
        if 0 <= x + 1 < self.width and 0 <= y + 1 < self.height:
            if self.board[y + 1][x + 1].prob == 100:
                count += 1

        # bottom
        if 0 <= y + 1 < self.height:
            if self.board[y + 1][x].prob == 100:
                count += 1

        # bottom left
        if 0 <= x - 1 < self.width and 0 <= y + 1 < self.height:
            if self.board[y + 1][x - 1].prob == 100:
                count += 1

        return count

    def probZeroCount(self, x, y):
        count = 0

        # left
        if  0 <= x -1 < self.width:
            if self.board[y][x-1].prob == 0:
                count += 1

        # upper left
        if 0 <= x - 1 < self.width and 0 <= y -1  < self.height:
            if self.board[y-1][x-1].prob == 0:
                count += 1

        # up
        if 0 <= y -1  < self.height:
            if self.board[y-1][x].prob == 0:
                count += 1

        # upper right
        if 0 <= x + 1 < self.width and 0 <= y -1  < self.height:
            if self.board[y-1][x+1].prob == 0:
                count += 1

        # right
        if 0 <= x + 1 < self.width:
            if self.board[y][x+1].prob == 0:
                count += 1

        # bottom right
        if 0 <= x + 1 < self.width and 0 <= y +1  < self.height:
            if self.board[y+1][x+1].prob == 0:
                count += 1

        # bottom
        if 0 <= y+1  < self.height:
            if self.board[y+1][x].prob == 0:
                count += 1

        # bottom left
        if 0 <= x - 1 < self.width and 0 <= y +1  < self.height:
            if self.board[y+1][x-1].prob == 0:
                count += 1

        return count




