"""
A.I. Homework 2
By Ryan Quirk <quirkrf@clarkson.edu>

Free Cell Problem

Heuristics:
"""

case = [[2,3,1],[6,4,5], []]
n = 6


def h2(state, n):
    if n == 0: return 0
    for s in state:
        if n in s:
            cards = len(s) - (s.index(n) + 1)
            return n + cards


def cellSearch(state, fringe, h):
    tstate = state[0]
    n = state[2]
    g = state[3] + 1
    piles = len(tstate)

    for i in range(piles):
        full = [p.copy() for p in tstate]
        if full[i]:
            num = full[i].pop()
            tn = n
            if num == n:
                tn -= 1
                if h == 2:
                    h = h2(full, tn)
                else:
                    h = tn
                fringe.append((full, h + g, tn, g))
                continue
        else:
            continue

        for j in range(piles):
            if j == i:
                continue
            partial = [p.copy() for p in full]
            if not partial[j] or partial[j][-1] == num - 1:
                partial[j].append(num)
                if h == 2:
                    h = h2(full, tn)
                else:
                    h = n
                fringe.append((partial, h + g, n, g))

    return fringe

def solveCell(case, n, heur):

    # Create heuristic for case
    # Create logic to assign heuristic to pile numbers
    # Choose lowest heuristic initially, but keep track of cost of action
    # Add action costs to heuristics, and choose smallest value
    """
    Possible heuristics:
    
    1. Heuristic is counter n
    2. Heuristic is counter n plus numbers in front of card n
    """

    # Heuristic 1
    g = 0
    h = n
    fringe = cellSearch((case, g + h, n, g), [], heur)

    j = 0
    while True:
        if not fringe:
            print("FAILED!!!\n\n")
            break

        if j > 9999:
            print("FAILED!!\nNO SOLUTION\n")
            break

        fcost = 100
        state = -1
        for i in range(len(fringe)):
            if fcost > fringe[i][1]:
                fcost = fringe[i][1]
                state = i

        state = fringe.pop(state)
        n = state[2]


        if n == 0:
            print("GAME WON!!")
            print(f"Solution:{state[0]}")
            print("States expanded:", j)
            print("Path cost:", state[3])
            print("\n")
            break

        """
        print("\nExpanding State...")
        print(f"Pile 1: {state[0][0]}\tPile 2: {state[0][1]}\tPile 3: {state[0][2]}")
        print(f"n: {n}\tf: {state[1]}")
        print("\n",fringe)
        """
        j += 1

        fringe = cellSearch(state, fringe, heur)


        """
        print(f"Pile 1: {case[0]}\tPile 2: {case[1]}\tPile 3: {case[2]}")
        s_pile = int(input(f"Press [1] to choose: pile 1\tPress [2] to choose: pile 2\tPress [3] to choose: pile 3\n")) - 1
        card = case[s_pile].pop()
        if card == n:
            print(f"{card} acquired, decrementing counter...")
            n += -1
            if n == 0:
                print("\n\nGAME WON!!")
                break
            continue

        t_pile = int(input(f"Move {card} to what pile? [1] [2] or [3]")) - 1
        if case[t_pile]:
            if case[t_pile][-1] == card - 1:
                case[t_pile].insert(len(case[t_pile]), card)
            else:
                print("Cannot move card to pile!")
                case[s_pile].append(card)
        else:
            case[t_pile].append(card)
        """

case1 = [[], [], [4,5,1,2,6,7,10,9,3,8]]
n = 10
"""
print("CASE 1 ~ H1")
solveCell(case1, n, 1)

print("CASE 1 ~ H2")
solveCell(case1, n, 2)

case2 = [[2,11,4], [3,12,6,1],[7,8,9], [10,5]]
n = 12
print("CASE 2 ~ H1")
solveCell(case2, n, 1)
print("CASE 2 ~ H2")
solveCell(case2, n, 2)
"""
from random import randint

def genGrid(cars, me, goal, n):
    grid = []
    for _ in range(n):
        row = []
        for __ in range(n):
            row.append('0')
        grid.append(row)

    print(cars)
    for car in cars:
        start_x = car[0][0] - 1
        start_y = car[0][1] - 1
        fin = car[1]
        if car[2]:
            grid[start_y][start_x] = '1'
            while start_x != (fin[0] - 1):
                print("inside1")
                start_x += 1
                grid[start_y][start_x] = '1'
        else:
            grid[start_y][start_x] = '1'
            while start_y != (fin[1] - 1):
                print("inside2")
                start_y += 1
                grid[start_y][start_x] = '1'

    m_x = me[0][0] - 1
    m_y = me[0][1] - 1
    fin = me[1]

    if me[2]:
        grid[m_y][m_x] = '*'
        while m_x != (fin[0]- 1):
            m_x += 1
            grid[m_y][m_x] = '*'
    else:
        grid[m_y][m_x] = '*'
        while m_y != (fin[1] - 1):
            m_y += 1
            grid[m_y][m_x] = '*'

    grid[goal[1] - 1][goal[0] - 1] = "X"

    return grid

def pH1():
    pass

def parkSearch(case):
    pass

def solvePark(n, cars, me, goal):
    """
    Heuristic 1: Manhattan distance from player car to goal
    Heuristic 2: Distance lengthwise from player car to goal

    """

    temp = []
    for car in cars:
        start = car[0]
        fin = car[-1]

        if start[0] == fin[0]:
            # Mark car as vertical with '0'
            temp.append([start, fin, 0])

        elif start[1] == fin[1]:
            # Mark car as horizontal with '1'
            temp.append([start, fin, 1])

        else:
            print("Something wrong here:\t", car)
            break

    cars = temp


    m_start = me[0]
    m_fin = me[-1]

    if m_start[0] == m_fin[0]:
        me = [m_start, m_fin, 0]

    if m_start[1] == m_fin[1]:
        me = [m_start, m_fin, 1]

    grid = genGrid(cars, me, goal, n)
    for row in reversed(grid):
        print(row)


    g = 0
    fringe = parkSearch([cars, me, goal, n], g)
    while True:
        if not fringe:
            print("\n\nFAILED!!!")
            break



# case 1

solvePark(5,[[(4,5),(5,5)], [(4,1),(4,2),(4,3)] ,[(2,4),(2,5)]], [(1,2), (2,2)], (5,2))