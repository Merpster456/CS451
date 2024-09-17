# Homework 1
### Ryan Quirk

---

## Geography Problem

* **State:** A list of 3 letter strings such as:
  * ["ABC", "CFG", "GFG"]
* **Initial State:** The initial 3 letter string put into fringe.
  *  In the homework cases the initial state was ["ABC"]
* **Goal Test:** The goal test for the geography problem checks if the last letter of the first node matches the 
  first letter of the node in front of it, and so on and so forth for the entire state. If this test succeeds then 
  it is a good state. If this test succeeds and the state matches the length of the original case, then the state 
  solves the problem.
  * **SUCCESS:** ["ABC", "CFG"]
  * **FAIL:** ["ABC", "GKG"]
* **Successor Function:** The successor function is called if the state passes the goal test, and this successor 
  function is the same as the search function. It finds possible successors of the current state and adds these 
  successors to the fringe. The successor function/search function is breadth first search if the fringe is used as 
  a queue, and is depth first search if the fringe is used as a stack.
  * For the Geo problem, if the case was ["ABC", "CDE", "GFL"] and my state was ["ABC"] the successor function would 
    add ["ABC", "CDE"] and ["ABC", "GFL"] to the end of the fringe.

### Program Output

```
CASE 1 ~ BFS
CASE: ['ABC', 'CDE', 'CFG', 'EHE', 'EIJ', 'GHK', 'GLC']
Expanding state: ['ABC']
Expanding state: ['ABC', 'CDE']
Expanding state: ['ABC', 'CFG']
Expanding state: ['ABC', 'CDE', 'EHE']
Expanding state: ['ABC', 'CDE', 'EIJ']
Expanding state: ['ABC', 'CFG', 'GHK']
Expanding state: ['ABC', 'CFG', 'GLC']
Expanding state: ['ABC', 'CDE', 'EHE', 'EIJ']
Expanding state: ['ABC', 'CFG', 'GLC', 'CDE']
Expanding state: ['ABC', 'CFG', 'GLC', 'CDE', 'EHE']
Expanding state: ['ABC', 'CFG', 'GLC', 'CDE', 'EIJ']
Expanding state: ['ABC', 'CFG', 'GLC', 'CDE', 'EHE', 'EIJ']

FAILED!!
No solution

CASE 1 ~ DFS
CASE: ['ABC', 'CDE', 'CFG', 'EHE', 'EIJ', 'GHK', 'GLC']
Expanding state: ['ABC']
Expanding state: ['ABC', 'CFG']
Expanding state: ['ABC', 'CFG', 'GLC']
Expanding state: ['ABC', 'CFG', 'GLC', 'CDE']
Expanding state: ['ABC', 'CFG', 'GLC', 'CDE', 'EIJ']
Expanding state: ['ABC', 'CFG', 'GLC', 'CDE', 'EHE']
Expanding state: ['ABC', 'CFG', 'GLC', 'CDE', 'EHE', 'EIJ']
Expanding state: ['ABC', 'CFG', 'GHK']
Expanding state: ['ABC', 'CDE']
Expanding state: ['ABC', 'CDE', 'EIJ']
Expanding state: ['ABC', 'CDE', 'EHE']
Expanding state: ['ABC', 'CDE', 'EHE', 'EIJ']

FAILED!!
No solution

CASE 2 ~ BFS
CASE: ['ABC', 'CDE', 'CFG', 'EHI', 'GJC', 'GKG']
Expanding state: ['ABC']
Expanding state: ['ABC', 'CDE']
Expanding state: ['ABC', 'CFG']
Expanding state: ['ABC', 'CDE', 'EHI']
Expanding state: ['ABC', 'CFG', 'GJC']
Expanding state: ['ABC', 'CFG', 'GKG']
Expanding state: ['ABC', 'CFG', 'GJC', 'CDE']
Expanding state: ['ABC', 'CFG', 'GKG', 'GJC']
Expanding state: ['ABC', 'CFG', 'GJC', 'CDE', 'EHI']
Expanding state: ['ABC', 'CFG', 'GKG', 'GJC', 'CDE']
Expanding state: ['ABC', 'CFG', 'GKG', 'GJC', 'CDE', 'EHI']

STATE: ABC CFG GKG GJC CDE EHI
SUCCESS!

CASE 2 ~ DFS
CASE: ['ABC', 'CDE', 'CFG', 'EHI', 'GJC', 'GKG']
Expanding state: ['ABC']
Expanding state: ['ABC', 'CFG']
Expanding state: ['ABC', 'CFG', 'GKG']
Expanding state: ['ABC', 'CFG', 'GKG', 'GJC']
Expanding state: ['ABC', 'CFG', 'GKG', 'GJC', 'CDE']
Expanding state: ['ABC', 'CFG', 'GKG', 'GJC', 'CDE', 'EHI']

STATE: ABC CFG GKG GJC CDE EHI
SUCCESS!
```

### State Tracking Output

```
CASE 1 ~ BFS
CASE: ['ABC', 'CDE', 'CFG', 'EHE', 'EIJ', 'GHK', 'GLC']
Expanding state: ['ABC']
Expanding state: ['ABC', 'CDE']
Expanding state: ['ABC', 'CFG']
Visited state: ['ABC', 'EHE']
Visited state: ['ABC', 'EIJ']
Visited state: ['ABC', 'GHK']
Visited state: ['ABC', 'GLC']
Visited state: ['ABC', 'CDE', 'CFG']
Expanding state: ['ABC', 'CDE', 'EHE']
Expanding state: ['ABC', 'CDE', 'EIJ']
Visited state: ['ABC', 'CDE', 'GHK']
Visited state: ['ABC', 'CDE', 'GLC']
Visited state: ['ABC', 'CFG', 'CDE']
Visited state: ['ABC', 'CFG', 'EHE']
Visited state: ['ABC', 'CFG', 'EIJ']
Expanding state: ['ABC', 'CFG', 'GHK']
Expanding state: ['ABC', 'CFG', 'GLC']
Visited state: ['ABC', 'CDE', 'EHE', 'CFG']
Expanding state: ['ABC', 'CDE', 'EHE', 'EIJ']
Visited state: ['ABC', 'CDE', 'EHE', 'GHK']
Visited state: ['ABC', 'CDE', 'EHE', 'GLC']
Visited state: ['ABC', 'CDE', 'EIJ', 'CFG']
Visited state: ['ABC', 'CDE', 'EIJ', 'EHE']
Visited state: ['ABC', 'CDE', 'EIJ', 'GHK']
Visited state: ['ABC', 'CDE', 'EIJ', 'GLC']
Visited state: ['ABC', 'CFG', 'GHK', 'CDE']
Visited state: ['ABC', 'CFG', 'GHK', 'EHE']
Visited state: ['ABC', 'CFG', 'GHK', 'EIJ']
Visited state: ['ABC', 'CFG', 'GHK', 'GLC']
Expanding state: ['ABC', 'CFG', 'GLC', 'CDE']
Visited state: ['ABC', 'CFG', 'GLC', 'EHE']
Visited state: ['ABC', 'CFG', 'GLC', 'EIJ']
Visited state: ['ABC', 'CFG', 'GLC', 'GHK']
Visited state: ['ABC', 'CDE', 'EHE', 'EIJ', 'CFG']
Visited state: ['ABC', 'CDE', 'EHE', 'EIJ', 'GHK']
Visited state: ['ABC', 'CDE', 'EHE', 'EIJ', 'GLC']
Expanding state: ['ABC', 'CFG', 'GLC', 'CDE', 'EHE']
Expanding state: ['ABC', 'CFG', 'GLC', 'CDE', 'EIJ']
Visited state: ['ABC', 'CFG', 'GLC', 'CDE', 'GHK']
Expanding state: ['ABC', 'CFG', 'GLC', 'CDE', 'EHE', 'EIJ']
Visited state: ['ABC', 'CFG', 'GLC', 'CDE', 'EHE', 'GHK']
Visited state: ['ABC', 'CFG', 'GLC', 'CDE', 'EIJ', 'EHE']
Visited state: ['ABC', 'CFG', 'GLC', 'CDE', 'EIJ', 'GHK']
Visited state: ['ABC', 'CFG', 'GLC', 'CDE', 'EHE', 'EIJ', 'GHK']

FAILED!!
No solution

CASE 1 ~ DFS
CASE: ['ABC', 'CDE', 'CFG', 'EHE', 'EIJ', 'GHK', 'GLC']
Expanding state: ['ABC']
Visited state: ['ABC', 'GLC']
Visited state: ['ABC', 'GHK']
Visited state: ['ABC', 'EIJ']
Visited state: ['ABC', 'EHE']
Expanding state: ['ABC', 'CFG']
Expanding state: ['ABC', 'CFG', 'GLC']
Visited state: ['ABC', 'CFG', 'GLC', 'GHK']
Visited state: ['ABC', 'CFG', 'GLC', 'EIJ']
Visited state: ['ABC', 'CFG', 'GLC', 'EHE']
Expanding state: ['ABC', 'CFG', 'GLC', 'CDE']
Visited state: ['ABC', 'CFG', 'GLC', 'CDE', 'GHK']
Expanding state: ['ABC', 'CFG', 'GLC', 'CDE', 'EIJ']
Visited state: ['ABC', 'CFG', 'GLC', 'CDE', 'EIJ', 'GHK']
Visited state: ['ABC', 'CFG', 'GLC', 'CDE', 'EIJ', 'EHE']
Expanding state: ['ABC', 'CFG', 'GLC', 'CDE', 'EHE']
Visited state: ['ABC', 'CFG', 'GLC', 'CDE', 'EHE', 'GHK']
Expanding state: ['ABC', 'CFG', 'GLC', 'CDE', 'EHE', 'EIJ']
Visited state: ['ABC', 'CFG', 'GLC', 'CDE', 'EHE', 'EIJ', 'GHK']
Expanding state: ['ABC', 'CFG', 'GHK']
Visited state: ['ABC', 'CFG', 'GHK', 'GLC']
Visited state: ['ABC', 'CFG', 'GHK', 'EIJ']
Visited state: ['ABC', 'CFG', 'GHK', 'EHE']
Visited state: ['ABC', 'CFG', 'GHK', 'CDE']
Visited state: ['ABC', 'CFG', 'EIJ']
Visited state: ['ABC', 'CFG', 'EHE']
Visited state: ['ABC', 'CFG', 'CDE']
Expanding state: ['ABC', 'CDE']
Visited state: ['ABC', 'CDE', 'GLC']
Visited state: ['ABC', 'CDE', 'GHK']
Expanding state: ['ABC', 'CDE', 'EIJ']
Visited state: ['ABC', 'CDE', 'EIJ', 'GLC']
Visited state: ['ABC', 'CDE', 'EIJ', 'GHK']
Visited state: ['ABC', 'CDE', 'EIJ', 'EHE']
Visited state: ['ABC', 'CDE', 'EIJ', 'CFG']
Expanding state: ['ABC', 'CDE', 'EHE']
Visited state: ['ABC', 'CDE', 'EHE', 'GLC']
Visited state: ['ABC', 'CDE', 'EHE', 'GHK']
Expanding state: ['ABC', 'CDE', 'EHE', 'EIJ']
Visited state: ['ABC', 'CDE', 'EHE', 'EIJ', 'GLC']
Visited state: ['ABC', 'CDE', 'EHE', 'EIJ', 'GHK']
Visited state: ['ABC', 'CDE', 'EHE', 'EIJ', 'CFG']
Visited state: ['ABC', 'CDE', 'EHE', 'CFG']
Visited state: ['ABC', 'CDE', 'CFG']

FAILED!!
No solution

CASE 2 ~ BFS
CASE: ['ABC', 'CDE', 'CFG', 'EHI', 'GJC', 'GKG']
Expanding state: ['ABC']
Expanding state: ['ABC', 'CDE']
Expanding state: ['ABC', 'CFG']
Visited state: ['ABC', 'EHI']
Visited state: ['ABC', 'GJC']
Visited state: ['ABC', 'GKG']
Visited state: ['ABC', 'CDE', 'CFG']
Expanding state: ['ABC', 'CDE', 'EHI']
Visited state: ['ABC', 'CDE', 'GJC']
Visited state: ['ABC', 'CDE', 'GKG']
Visited state: ['ABC', 'CFG', 'CDE']
Visited state: ['ABC', 'CFG', 'EHI']
Expanding state: ['ABC', 'CFG', 'GJC']
Expanding state: ['ABC', 'CFG', 'GKG']
Visited state: ['ABC', 'CDE', 'EHI', 'CFG']
Visited state: ['ABC', 'CDE', 'EHI', 'GJC']
Visited state: ['ABC', 'CDE', 'EHI', 'GKG']
Expanding state: ['ABC', 'CFG', 'GJC', 'CDE']
Visited state: ['ABC', 'CFG', 'GJC', 'EHI']
Visited state: ['ABC', 'CFG', 'GJC', 'GKG']
Visited state: ['ABC', 'CFG', 'GKG', 'CDE']
Visited state: ['ABC', 'CFG', 'GKG', 'EHI']
Expanding state: ['ABC', 'CFG', 'GKG', 'GJC']
Expanding state: ['ABC', 'CFG', 'GJC', 'CDE', 'EHI']
Visited state: ['ABC', 'CFG', 'GJC', 'CDE', 'GKG']
Expanding state: ['ABC', 'CFG', 'GKG', 'GJC', 'CDE']
Visited state: ['ABC', 'CFG', 'GKG', 'GJC', 'EHI']
Visited state: ['ABC', 'CFG', 'GJC', 'CDE', 'EHI', 'GKG']
Expanding state: ['ABC', 'CFG', 'GKG', 'GJC', 'CDE', 'EHI']

STATE: ABC CFG GKG GJC CDE EHI
SUCCESS!

CASE 2 ~ DFS
CASE: ['ABC', 'CDE', 'CFG', 'EHI', 'GJC', 'GKG']
Expanding state: ['ABC']
Visited state: ['ABC', 'GKG']
Visited state: ['ABC', 'GJC']
Visited state: ['ABC', 'EHI']
Expanding state: ['ABC', 'CFG']
Expanding state: ['ABC', 'CFG', 'GKG']
Expanding state: ['ABC', 'CFG', 'GKG', 'GJC']
Visited state: ['ABC', 'CFG', 'GKG', 'GJC', 'EHI']
Expanding state: ['ABC', 'CFG', 'GKG', 'GJC', 'CDE']
Expanding state: ['ABC', 'CFG', 'GKG', 'GJC', 'CDE', 'EHI']

STATE: ABC CFG GKG GJC CDE EHI
SUCCESS!
```

---

## PCP Problem

* **State:** A tuple of two strings that represent the top and bottom of a domino.
  * I.E. ("MOMO", "MOM")
* **Initial State:** The initial top and bottom strings put into the fringe.
  *  In one of the homework cases the initial state was ("MOM", "M")
* **Goal Test:** The goal test takes the smaller string and iterates through every character of the smaller string 
  checking if it matches the characters of the longer string. If the smaller string matches the longer 
  string for all of its characters, then the test succeeds. If this test succeeds and the two strings have equivalent 
  lengths, then the state solves the problem
  * **SUCCESS:** ("MOMMOMO", "MOM")
  * **FAIL:** ("MOMMO", "MOMO")
* **Successor Function:** The successor function can be explained the same way as the geography problem. The successor 
  function is called if the state passes the goal test, and this successor function is the same as the search 
  function. It finds possible successors of the current state and adds these successors to the fringe. The 
  successor function/search function is breadth first search if the fringe is used as a queue, and is depth first 
  search if the fringe is used as a stack.
  * For the PCP problem, if the case was [("MOM", "M"), ("O", "OMOMO")] and my state was ("MOM", "M") the successor 
    function would add ("MOMMOM", "MM") and ("MOMO", "MOMOMO") to the fringe.

### Program Output

```
CASE 1 ~ BFS
CASE: [('MOM', 'M'), ('O', 'OMOMO')]
Expanding state: ('MOM', 'M')
Expanding state: ('MOMO', 'MOMOMO')
Expanding state: ('MOMOMOM', 'MOMOMOM')

STATE: ('MOMOMOM', 'MOMOMOM')
SUCCESS!

CASE 1 ~ DFS
CASE: [('MOM', 'M'), ('O', 'OMOMO')]
Expanding state: ('MOM', 'M')
Expanding state: ('MOMO', 'MOMOMO')
Expanding state: ('MOMOMOM', 'MOMOMOM')

STATE: ('MOMOMOM', 'MOMOMOM')
SUCCESS!

CASE 2 ~ BFS
CASE: [('AA', 'A')]
Expanding state: ('AA', 'A')
Expanding state: ('AAAA', 'AA')
Expanding state: ('AAAAAA', 'AAA')
Expanding state: ('AAAAAAAA', 'AAAA')
Expanding state: ('AAAAAAAAAA', 'AAAAA')
...
Expanding state: ('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')

FAILED!!
No solution... Infinite states

CASE 2 ~ DFS
CASE: [('AA', 'A')]
Expanding state: ('AA', 'A')
Expanding state: ('AAAA', 'AA')
Expanding state: ('AAAAAA', 'AAA')
Expanding state: ('AAAAAAAA', 'AAAA')
Expanding state: ('AAAAAAAAAA', 'AAAAA')
...
Expanding state: ('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')

FAILED!!
No solution... Infinite states
```

### State Tracking Output

```
CASE 1 ~ BFS
CASE: [('MOM', 'M'), ('O', 'OMOMO')]
Expanding state: ('MOM', 'M')
Visiting state: ('MOMMOM', 'MM')
Expanding state: ('MOMO', 'MOMOMO')
Expanding state: ('MOMOMOM', 'MOMOMOM')

STATE: ('MOMOMOM', 'MOMOMOM')
SUCCESS!

CASE 1 ~ DFS
CASE: [('MOM', 'M'), ('O', 'OMOMO')]
Expanding state: ('MOM', 'M')
Expanding state: ('MOMO', 'MOMOMO')
Visiting state: ('MOMOO', 'MOMOMOOMOMO')
Expanding state: ('MOMOMOM', 'MOMOMOM')

STATE: ('MOMOMOM', 'MOMOMOM')
SUCCESS!

CASE 2 ~ BFS
CASE: [('AA', 'A')]
Expanding state: ('AA', 'A')
Expanding state: ('AAAA', 'AA')
Expanding state: ('AAAAAA', 'AAA')
Expanding state: ('AAAAAAAA', 'AAAA')
Expanding state: ('AAAAAAAAAA', 'AAAAA')
...
Expanding state: ('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')

FAILED!!
No solution... Infinite states

CASE 2 ~ DFS
CASE: [('AA', 'A')]
Expanding state: ('AA', 'A')
Expanding state: ('AAAA', 'AA')
Expanding state: ('AAAAAA', 'AAA')
Expanding state: ('AAAAAAAA', 'AAAA')
Expanding state: ('AAAAAAAAAA', 'AAAAA')
...
Expanding state: ('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')

FAILED!!
No solution... Infinite states
```