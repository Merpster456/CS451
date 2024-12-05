from random import randrange
from math import comb

class Cell:
    def __init__(self, value):
        self.value = value
        self.seen = False
        self.flag = False
        self.edge = False
        self.edgeCount = 0
        self.mineArr = 0
        self.prob = -1

    def __str__(self):
        return str(self.value)

class Board:

    def __init__(self, h, w, m, x0, y0):
        # Initial Values
        self.height = h
        self.width = w
        self.numMines = m
        self.mines = []
        self.board = []
        self.arrGrid = []
        self.edgeArr = []
        self.hundredCount = 0

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

    def freeCells(self):
        free = []
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                if self.board[y][x].prob == 0:
                    free.append((x,y))

        return free

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

    def findNextEdge(self, x, y):
        for i in range(y, len(self.board)):
            for j in range(x, len(self.board[0])):
                if self.board[i][j].edge and self.board[i][j].prob < 0:
                    return [j,i]
            y = 0
        return [j, i]

    def genArr(self, grid, indx):
        x = self.arrGrid[indx][0]
        y = self.arrGrid[indx][1]

        if self.canBeMine(grid, x, y):
            y_pattern = self.arrGrid.copy()
            y_pattern[indx][2] = True

            if indx < len(self.arrGrid) - 1:
                self.genArr(y_pattern, indx+1)
            else:
                self.edgeArr.append(y_pattern)

        if self.canNotBeMine(grid, x, y):
            n_pattern = self.arrGrid.copy()
            n_pattern[indx][2] = False
            if indx < len(self.arrGrid) - 1:
                self.genArr(n_pattern, indx+1)
            else:
                self.edgeArr.append(n_pattern)

    # Calculate probabilities from mine arrangements
    def probCalc(self):
        arrCount = 0
        nonEdge = self.nonEdgeCount()

        for y in range(len(self.edgeArr)):
            minesPlaced = 0
            for x in range(len(self.edgeArr[0])):
                if self.edgeArr[y][x][2]:
                    minesPlaced += 1

        remaingMines = self.numMines - minesPlaced - self.hundredCount

        if remaingMines >= 0 and remaingMines <= nonEdge:
            nonEdgeCombinations = comb(nonEdge, remaingMines)
            for x in range(len(self.edgeArr[0])):
                if self.edgeArr[y][x][2]:
                    self.board[self.edgeArr[1]][self.edgeArr[0]].mineArr += nonEdgeCombinations

            arrCount += nonEdgeCombinations

            for i in range(len(self.board)):
                for j in range(len(self.board[0])):
                    if not self.board[i][j].seen and not self.board[i][j].edge:
                        self.board[i][j].mineArr += remaingMines / nonEdge * nonEdgeCombinations

        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                if self.board[y][x].edge and self.board[y][x].prob < 0:
                    self.board[y][x].prob = round(self.board[y][x].mineArr / arrCount * 100)

                if not self.board[y][x].seen and not self.board[y][x].edge and self.board[y][x].prob < 0:
                    self.board[y][x].prob = round(self.board[y][x].mineArr / arrCount * 100)

    # How many nonmines can be placed around a cell when generating arrangements
    def noMineCount(self, grid, x, y):
        count = 0
        for i in range(len(grid)):
            if (y-1 <= grid[i][1] <= y+1 and x - 1 <= grid[i][0] <= x + 1):
                if not grid[i][3]:
                    count += 1

        return count

    def canNotBeMine(self, grid, x, y):
        # left
        if 0 <= x - 1 < self.width:
            if (self.board[y][x - 1].seen and self.board[y][x - 1].value >= self.board[y][x-1].edgeCount -
                    self.noMineCount(grid, x - 1, y) + self.probZeroCount(x - 1, y)):
                return False

        # upper left
        if 0 <= x - 1 < self.width and 0 <= y - 1 < self.height:
            if (self.board[y-1][x - 1].seen and self.board[y-1][x - 1].value >= self.board[y-1][x-1].edgeCount -
                    self.noMineCount(grid, x - 1, y-1) + self.probZeroCount(x - 1, y-1)):
                return False

        # up
        if 0 <= y - 1 < self.height:
            if (self.board[y-1][x].seen and self.board[y-1][x].value >= self.board[y-1][x].edgeCount -
                    self.noMineCount(grid, x, y-1) + self.probZeroCount(x, y-1)):
                return False

        # upper right
        if 0 <= x + 1 < self.width and 0 <= y - 1 < self.height:
            if (self.board[y-1][x+1].seen and self.board[y-1][x+1].value >= self.board[y-1][x+1].edgeCount -
                    self.noMineCount(grid, x+1, y-1) + self.probZeroCount(x+1, y-1)):
                return False

        # right
        if 0 <= x + 1 < self.width:
            if (self.board[y][x+1].seen and self.board[y][x+1].value >= self.board[y][x+1].edgeCount -
                    self.noMineCount(grid, x+1, y) + self.probZeroCount(x+1, y)):
                return False

        # bottom right
        if 0 <= x + 1 < self.width and 0 <= y + 1 < self.height:
            if (self.board[y+1][x+1].seen and self.board[y+1][x+1].value >= self.board[y+1][x+1].edgeCount -
                    self.noMineCount(grid, x+1, y+1) + self.probZeroCount(x+1, y+1)):
                return False

        # bottom
        if 0 <= y + 1 < self.height:
            if (self.board[y+1][x].seen and self.board[y+1][x].value >= self.board[y+1][x].edgeCount -
                    self.noMineCount(grid, x, y+1) + self.probZeroCount(x, y+1)):
                return False

        # bottom left
        if 0 <= x - 1 < self.width and 0 <= y + 1 < self.height:
            if (self.board[y+1][x-1].seen and self.board[y+1][x-1].value >= self.board[y+1][x-1].edgeCount -
                    self.noMineCount(grid, x-1, y+1) + self.probZeroCount(x-1, y+1)):
                return False

        return True

    # How many mines can be placed around a cell when generating arrangements
    def mineCount(self, grid, x, y):
        count = 0
        for i in range(len(grid)):
            if (y - 1 <= grid[i][1] <= y + 1 and x - 1 <= grid[i][0] <= x + 1):
                if grid[i][3]:
                    count += 1

        return count

    def canBeMine(self, grid, x, y):
        # left
        if 0 <= x - 1 < self.width:
            if (self.board[y][x - 1].seen and self.board[y][x-1].value <=
                    self.mineCount(grid, x-1, y) + self.probHundredCount( x-1, y)):
                return False

        # upper left
        if 0 <= x - 1 < self.width and 0 <= y - 1 < self.height:
            if (self.board[y-1][x - 1].seen and self.board[y-1][x-1].value <=
                    self.mineCount(grid, x-1, y-1) + self.probHundredCount( x-1, y-1)):
                return False

        # up
        if 0 <= y - 1 < self.height:
            if (self.board[y-1][x].seen and self.board[y-1][x].value <=
                    self.mineCount(grid, x, y-1) + self.probHundredCount(x, y-1)):
                return False

        # upper right
        if 0 <= x + 1 < self.width and 0 <= y - 1 < self.height:
            if (self.board[y-1][x+1].seen and self.board[y-1][x+1].value <=
                    self.mineCount(grid, x+1, y-1) + self.probHundredCount(x+1, y-1)):
                return False

        # right
        if 0 <= x + 1 < self.width:
            if (self.board[y][x+1].seen and self.board[y][x+1].value <=
                    self.mineCount(grid, x+1, y) + self.probHundredCount(x+1, y)):
                return False

        # bottom right
        if 0 <= x + 1 < self.width and 0 <= y + 1 < self.height:
            if (self.board[y+1][x+1].seen and self.board[y+1][x+1].value <=
                    self.mineCount(grid, x+1, y+1) + self.probHundredCount(x+1, y+1)):
                return False

        # bottom
        if 0 <= y + 1 < self.height:
            if (self.board[y+1][x].seen and self.board[y+1][x].value <=
                    self.mineCount(grid, x, y+1) + self.probHundredCount(x, y+1)):
                return False

        # bottom left
        if 0 <= x - 1 < self.width and 0 <= y + 1 < self.height:
            if (self.board[y + 1][x-1].seen and self.board[y + 1][x-1].value <=
                    self.mineCount(grid, x-1, y + 1) + self.probHundredCount(x-1, y + 1)):
                return False

        return True

    # Count how many cells aren't open or bordering open cells
    def nonEdgeCount(self):
        count = 0
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                if not self.board[y][x].seen and not self.board[y][x].edge:
                    count += 1

        return count

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
        if  0 <= x-1 < self.width:
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




