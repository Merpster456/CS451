"""
A.I. Homework 1
By Ryan Quirk <quirkrf@clarkson.edu>

Geography Problem

Goal Test: geoGoal(state)
    checks the state if it meets the goal of the
    geography problem, if it does return True, else
    return False

Successor Function: geoSearch(case, state, fringe)
    Uses the problem case and state to find possible
    successors to add to the fringe. Returns the fringe
    with all possible successors added.

Problem Function: solveGeo(case, bfs):
    Given a test case, attempts to solve the geography
    problem. set bfs to True if you want to use breadth
    first search, set to False if you want to use depth
    first search.
"""

def geoGoal(state):
    if len(state) == 1:
        return True

    for i in range(len(state)):
        if i == len(state) - 1:
            return True
        if state[i][-1] == state[i+1][0]:
            continue
        else:
            return False

def geoSearch(case, state, fringe):
    temp = [n for n in case]
    for n in state:
        if n in temp:
            temp.remove(n)

    for n in temp:
        succState = [sn for sn in state + [n]]
        fringe.append(succState)

    return fringe


def solveGeo(case, bfs):
    # If bfs is true, then breadth first search
    if bfs:
        KEY = 0
    else:
        # Else, depth first search
        KEY = -1
    solLen = len(case)
    fringe = []

    fringe.append(case[0])
    initial = True
    i = 0

    while True:
        if not fringe:
            print("\nFAILED!!\nNo solution\n")
            break
        i += 1
        if initial:
            initial = False
            state = [fringe.pop(0)]
        else:
            state = fringe.pop(KEY) # Take state


        if geoGoal(state):
            print("Expanding state:", state)
            if len(state) == solLen:
                # Win condition
                print("\nSTATE:", *state)
                print("SUCCESS!\n")
                break


            # Find successors
            fringe = geoSearch(case, state, fringe)
        else:
            pass
            #print("Visited state:", state)


case1 = ["ABC", "CDE", "CFG", "EHE", "EIJ", "GHK", "GLC"]
case2 = ["ABC", "CDE", "CFG", "EHI", "GJC", "GKG"]
print("CASE 1 ~ BFS")
print("CASE:", case1)
solveGeo(case1, True)
print("CASE 1 ~ DFS")
print("CASE:", case1)
solveGeo(case1, False)
print("CASE 2 ~ BFS")
print("CASE:", case2)
solveGeo(case2, True)
print("CASE 2 ~ DFS")
print("CASE:", case2)
solveGeo(case2, False)

"""
PCP Problem

Goal Test: pcp(state)
checks the state if it meets the goal of the
PCP problem, if it does return True, else
return False

Successor Function: pcpSearch(case, state, fringe)
Uses the problem case and state to find possible
successors to add to the fringe. Returns the fringe
with all possible successors added.

Problem Function: solvePCP(case, bfs):
Given a test case, attempts to solve the PCP
problem. set bfs to True if you want to use breadth
first search, set to False if you want to use depth
first search.
"""

def pcpGoal(state):
    top = state[0]
    bottom = state[1]

    l = len(min(top, bottom))
    if top[:l] == bottom[:l]: return True
    else: return False

def pcpSearch(case, state, fringe):
    for n in case:
        succState = (state[0] + n[0], state[1] + n[1])
        fringe.append(succState)

    return fringe

def solvePCP(case, bfs):
    # If bfs is true, then breadth first search
    if bfs:
        KEY = 0
    else:
        # Else, depth first search
        KEY = -1

    fringe = []
    fringe.append(case[0])
    i = 0

    while True:
        i+=1
        if i > 50:
            print("\nFAILED!!")
            print("No solution... Infinite states\n")
            break
        if not fringe:
            print("\nFAILED!!\nNo solution\n")
            break

        state = fringe.pop(KEY)

        if pcpGoal(state):
            print("Expanding state:", state)
            if state[0] == state[1]:
                # Win condition
                print("\nSTATE:", state)
                print("SUCCESS!\n")
                break

            # Finds successors
            fringe = pcpSearch(case, state, fringe)
        else:
            pass
            #print("Visiting state:", state)

case1 = [("MOM", "M"), ("O", "OMOMO")]
case2 = [("AA", "A")]
print("CASE 1 ~ BFS")
print("CASE:", case1)
solvePCP(case1, True)
print("CASE 1 ~ DFS")
print("CASE:", case1)
solvePCP(case1, False)
print("CASE 2 ~ BFS")
print("CASE:", case2)
solvePCP(case2, True)
print("CASE 2 ~ DFS")
print("CASE:", case2)
solvePCP(case2, False)