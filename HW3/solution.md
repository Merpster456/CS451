## Part 1

1. How many states are expanded for BFS in the worst case, in terms of n. 
- Theoretically this should be $n!$ because it is possible that, in the worst case, where all words could be connected to the initial word they all need to be expanded. 

2. How many states are stored in BFS in the worst case, in terms of n.
- The worst case all states are stored and expanded: O(n)

3. Is BFS complete for this problem?
- Yes. BFS will explore all the nodes.

4. Same as part A for DFS 
- DFS can also expand all possible states leading to n! expansions

5. Same as part B for DFS 
- Worst case all nodes are stored and expanded: O(n)
6. Same as part C for DFS
- DFS is complete as long as there are no cycles.
7. Same as part A for iterative deepening
- If iterative deepening explores up to the max depth it should be O(n * n!)
8. Same as part B for iterative deepening
-  Worst case is O(n)
9. Same as part c for iterative deepening
- Yes. Tt will eventually explore all possible paths and find a solution if one exists.



## Part 3

### A.

**Breadth First Search**

Output:
```
Position: 1
Pathway: 3, 5

Position: 3
Pathway: 2, 4

Position: 5
Pathway: 3, 8

Position: 2
Pathway: 3, 6

Position: 4
Pathway: 2, 3

SUCCESS!!
Goal: 8, Position: 8
States Expanded: 6
Tree: 1 --> 3 --> 5 --> 2 --> 4 --> 8
```

### B.

**Depth First Search**

Output:
```
Position: 1
Pathway: 3, 5

Position: 5
Pathway: 3, 8

SUCCESS!!
Goal: 8, Position: 8
States Expanded: 3
Tree: 1 --> 5 --> 8
```
### C.

**Iterative Deepening Search**

Iterative depth = 2

Output:
```
Position: 1
Pathway: 3, 5

Position: 5
Pathway: 3, 8

Position: 3
Pathway: 2, 4

Position: 4
Pathway: 2, 3

Position: 2
Pathway: 3, 6

SUCCESS!!
Goal: 8, Position: 8
States Expanded: 6
Tree: 1 --> 5 --> 3 --> 4 --> 2 --> 8
```
### D.

**A Star**

#### Heuristic:

Knowing that one move can only get closer to the goal by at most 4, 
the heuristic chosen is however many multiples 4 away the position is from the goal.

If the position is less than 4 away from the goal, than the heuristic would be 0.

**For example:**

    If the position is 2, and the goal is 11 then the h-value would be 2

    Because:

    Distance = 11 - 2 = 9

    Distance / 4 = 9/4 = 2.25
    
    Since the distance divided by 4 is over 2, the heuristic will be 2.


Output:
```
Position: 1
Pathway: 3, 5

Position: 5
Pathway: 3, 8

Position: 3
Pathway: 2, 4

Position: 4
Pathway: 2, 3

Position: 2
Pathway: 3, 6

SUCCESS!!
Goal: 8, Position: 8
States Expanded: 6
Tree: 1 --> 5 --> 3 --> 4 --> 2 --> 8
```

### E.

**A Star**

Heuristic is the same as **D**

Output:
```
Position: 1
Pathway: 3, 5

Position: 5
Pathway: 3, 8

Position: 3
Pathway: 2, 4

SUCCESS!!
Goal: 8, Position: 8
States Expanded: 4
Tree: 1, (f: 1) --> 5, (f: 2) --> 3, (f: 3) --> 8, (f: 3
```


## Part 5 
Think of a solution to the Geography problem as a mapping from a word to
its position in the solved list of words.  For example, if the Geography problem
was {cat,toy,treat}, then the solution would be that cat has the value 1, toy has
the value 3, and treat has the value 2.

A. Given the above representation, suppose you were to solve Geography using 
local search. 

What would be the definition of state?  
    - State can be a list of word positions ex `[cat=1, treat=2, toy=3]`
What would be a suitable definition of neighbor?  
    - A neighboring state could be a list with the same words but a change in order ex. `[cat=1, toy=2, treat=3]`

What is a good objective function?
    - Should evaluate how close word order is to the solution. 
    - Use the number of adjacent word pairs where the last letter matches the first of the next word
    - Target: maximize that value

B. Given the above representation, suppose you were to solve Geography as a
CSP.  
What would the variables be?  
- position of words in the list 
What would the domain be?  
- set of all possible integer positions in the list 
What are the constraints?
- Each word's position is unique. 
- Any two consecutive words follow geography rules last letter matches first.