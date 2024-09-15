# Geo Problem
case = ["ABC", "CDE", "CFG", "EHI", "GJC", "GKG"]
fringe = []
solution = []

fringe.append(case.pop(0))

i = 0
while True:
    i += 1
    state = fringe.pop(0) # Take state
    solution.append(state) # Add state to solution
    letter = state[-1]

    # Search algorithm?
    success = False
    for node in case:
        if node[0] == letter:
            fringe.append(node)
            case.remove(node)
            success = True
            break

    if not success and case and not fringe:
        for node in case:
            j = 0
            for state in solution:
                if node[0] == state[-1]:
                    solution = solution[0:j+1]
                    case.extend(solution[j+2:-1])
                    fringe.append(node)
                    success = True
                    break
                else:
                    j += 1
            if success:
                break



    if len(solution) == 7:
        # Win condition
        print(*solution)
        print("\nSUCCESS!")
        break

    elif not fringe:


        # Fail condition
        print(f"SOLUTION: {solution}")
        print(f"FRINGE: {fringe}")
        print(f"CASE: {case}")
        print("\nFAILED")
        break

    print(i)
    print(f"SOLUTION: {solution}")
    print(f"FRINGE: {fringe}\n\n")
