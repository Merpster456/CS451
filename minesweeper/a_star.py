"""
Filename: a_star.py
Authors: Ryan Quirk

"""

from board import Board, Cell

zeroCount = 0

def rule1(grid):
    """
    Label cells that must be a mine by basic logic
    """
    ret = False
    hundredCount = 0

    for y in range(len(grid.board)):
        for x in range(len(grid.board[0])):
            if (grid.board[y][x].edgeCount > 0 and grid.board[y][x].value == grid.board[y][x].edgeCount - grid.probZeroCount(x, y)):
                # left
                if 0 <= x - 1 < grid.width:
                    if (grid.board[y][x - 1].edge and grid.board[y][x-1].prob < 0):
                        grid.board[y][x - 1].prob = 100
                        hundredCount += 1
                        ret = True

                # upper left
                if 0 <= x - 1 < grid.width and 0 <= y - 1 < grid.height:
                    if (grid.board[y-1][x - 1].edge and grid.board[y-1][x - 1].prob < 0):
                        grid.board[y-1][x - 1].prob = 100
                        hundredCount += 1
                        ret = True

                # up
                if 0 <= y - 1 < grid.height:
                    if (grid.board[y - 1][x].edge and grid.board[y - 1][x].prob < 0):
                        grid.board[y - 1][x].prob = 100
                        hundredCount += 1
                        ret = True

                # upper right
                if 0 <= x + 1 < grid.width and 0 <= y - 1 < grid.height:
                    if (grid.board[y - 1][x+1].edge and grid.board[y - 1][x+1].prob < 0):
                        grid.board[y - 1][x+1].prob = 100
                        hundredCount += 1
                        ret = True

                # right
                if 0 <= x + 1 < grid.width:
                    if (grid.board[y][x + 1].edge and grid.board[y][x + 1].prob < 0):
                        grid.board[y][x + 1].prob = 100
                        hundredCount += 1
                        ret = True

                # bottom right
                if 0 <= x + 1 < grid.width and 0 <= y + 1 < grid.height:
                    if (grid.board[y+1][x + 1].edge and grid.board[y+1][x + 1].prob < 0):
                        grid.board[y+1][x + 1].prob = 100
                        hundredCount += 1
                        ret = True

                # bottom
                if 0 <= y + 1 < grid.height:
                    if (grid.board[y + 1][x].edge and grid.board[y + 1][x].prob < 0):
                        grid.board[y + 1][x].prob = 100
                        hundredCount += 1
                        ret = True

                # bottom left
                if 0 <= x - 1 < grid.width and 0 <= y + 1 < grid.height:
                    if (grid.board[y + 1][x - 1].edge and grid.board[y + 1][x - 1].prob < 0):
                        grid.board[y + 1][x - 1].prob = 100
                        hundredCount += 1
                        ret = True

    grid.hundredCount += hundredCount
    return ret

def rule2(grid):
    """
    Label cells that can't be a mine by basic logic
    """
    ret = False

    for y in range(len(grid.board)):
        for x in range(len(grid.board[0])):
            if (grid.board[y][x].edgeCount > 0 and grid.board[y][x].value == grid.probHundredCount(x, y)):
                # left
                if 0 <= x - 1 < grid.width:
                    if (grid.board[y][x - 1].edge and grid.board[y][x - 1].prob < 0):
                        grid.board[y][x - 1].prob = 0
                        ret = True

                # upper left
                if 0 <= x - 1 < grid.width and 0 <= y - 1 < grid.height:
                    if (grid.board[y - 1][x - 1].edge and grid.board[y - 1][x - 1].prob < 0):
                        grid.board[y - 1][x - 1].prob = 0
                        ret = True

                # up
                if 0 <= y - 1 < grid.height:
                    if (grid.board[y - 1][x].edge and grid.board[y - 1][x].prob < 0):
                        grid.board[y - 1][x].prob = 0
                        ret = True

                # upper right
                if 0 <= x + 1 < grid.width and 0 <= y - 1 < grid.height:
                    if (grid.board[y - 1][x + 1].edge and grid.board[y - 1][x + 1].prob < 0):
                        grid.board[y - 1][x + 1].prob = 0
                        ret = True

                # right
                if 0 <= x + 1 < grid.width:
                    if (grid.board[y][x + 1].edge and grid.board[y][x + 1].prob < 0):
                        grid.board[y][x + 1].prob = 0
                        ret = True

                # bottom right
                if 0 <= x + 1 < grid.width and 0 <= y + 1 < grid.height:
                    if (grid.board[y + 1][x + 1].edge and grid.board[y + 1][x + 1].prob < 0):
                        grid.board[y + 1][x + 1].prob = 0
                        ret = True

                # bottom
                if 0 <= y + 1 < grid.height:
                    if (grid.board[y + 1][x].edge and grid.board[y + 1][x].prob < 0):
                        grid.board[y + 1][x].prob = 0
                        ret = True

                # bottom left
                if 0 <= x - 1 < grid.width and 0 <= y + 1 < grid.height:
                    if (grid.board[y + 1][x - 1].edge and grid.board[y + 1][x - 1].prob < 0):
                        grid.board[y + 1][x - 1].prob = 0
                        ret = True
    return ret

def rule3(grid):
    """
    Find isolated cells and give neighbors their independent mine probability
    """
    for y in range(len(grid.board)):
        for x in range(len(grid.board[0])):

            # This control loop checks for isolated cells
            if grid.board[y][x].edgeCount > 2:
                count = 0

                # left
                if 0 <= x - 1 < grid.width:
                    if (grid.board[y][x - 1].edge and grid.seenCount(x-1, y) == 1):
                        count += 1

                # upper left
                if 0 <= x - 1 < grid.width and 0 <= y - 1 < grid.height:
                    if (grid.board[y - 1][x - 1].edge and grid.seenCount(x-1, y-1) == 1):
                        count += 1

                # up
                if 0 <= y - 1 < grid.height:
                    if (grid.board[y - 1][x].edge and grid.seenCount(x, y-1) == 1):
                        count += 1

                # upper right
                if 0 <= x + 1 < grid.width and 0 <= y - 1 < grid.height:
                    if (grid.board[y - 1][x + 1].edge and grid.seenCount(x+1, y-1) == 1):
                        count += 1

                # right
                if 0 <= x + 1 < grid.width:
                    if (grid.board[y][x + 1].edge and grid.seenCount(x+1, y) == 1):
                        count += 1

                # bottom right
                if 0 <= x + 1 < grid.width and 0 <= y + 1 < grid.height:
                    if (grid.board[y + 1][x + 1].edge and grid.seenCount(x+1, y+1) == 1):
                        count += 1

                # bottom
                if 0 <= y + 1 < grid.height:
                    if (grid.board[y + 1][x].edge and grid.seenCount(x, y +1) == 1):
                        count += 1

                # bottom left
                if 0 <= x - 1 < grid.width and 0 <= y + 1 < grid.height:
                    if (grid.board[y + 1][x - 1].edge and grid.seenCount(x-1, y+1) == 1):
                        count += 1

                if count == grid.board[y][x].edgeCount:
                    probability = round((grid.board[y][x].value / grid.board[y][x].edgeCount) * 100)

                    # left
                    if 0 <= x - 1 < grid.width:
                        grid.board[y][x-1].prob = probability

                    # upper left
                    if 0 <= x - 1 < grid.width and 0 <= y - 1 < grid.height:
                        grid.board[y-1][x-1].prob = probability

                    # up
                    if 0 <= y - 1 < grid.height:
                        grid.board[y-1][x].prob = probability

                    # upper right
                    if 0 <= x + 1 < grid.width and 0 <= y - 1 < grid.height:
                        grid.board[y-1][x+1].prob = probability

                    # right
                    if 0 <= x + 1 < grid.width:
                        grid.board[y][x+1].prob = probability

                    # bottom right
                    if 0 <= x + 1 < grid.width and 0 <= y + 1 < grid.height:
                        grid.board[y+1][x+1].prob = probability

                    # bottom
                    if 0 <= y + 1 < grid.height:
                        grid.board[y+1][x].prob = probability

                    # bottom left
                    if 0 <= x - 1 < grid.width and 0 <= y + 1 < grid.height:
                        grid.board[y+1][x-1].prob = probability


def main(grid):

    for y in range(len(grid.board)):
        for x in range(len(grid.board[0])):
            grid.board[y][x].mineArr = 0
            grid.board[y][x].prob = -1
            grid.board[y][x].edgeCount = 0
            grid.board[y][x].edge = False

    grid.hundredCount = 0
    grid.arrGrid = []
    grid.edgeArr = []

    grid.edgeCount()

    ret1 = True
    ret2 = True
    i = 0
    while(ret1 or ret2):
        ret1 = rule1(grid)
        ret2 = rule2(grid)
        i+=1

    rule3(grid)

    indx = grid.findNextEdge(0,0)
    x = indx[0]
    y = indx[1]

    while y > -1:

        # Appending the list [x, y, isMine]
        grid.arrGrid.append([x,y, None])
        if x == grid.width - 1:
            indx = grid.findNextEdge(0,y+1)
            x = indx[0]
            y = indx[1]
        else:
            indx = grid.findNextEdge(x+1, y)
            x = indx[0]
            y = indx[1]

    if len(grid.arrGrid) > 0:
        grid.genArr(grid.arrGrid, 0)
        grid.probCalc()

    else:
        nonEdge = grid.nonEdgeCount()
        remaining_mines = grid.numMines - grid.hundredCount
        for y in range(len(grid.board)):
            for x in range(len(grid.board[0])):
                if not grid.board[y][x].seen and not grid.board[y][x]:
                    grid.board[y][x].prob = round((remaining_mines / nonEdge) * 100)

    return grid.moves()


if __name__ == "__main__":
    main(Board(16,30,99,5,5))