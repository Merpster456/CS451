# Homework 1
### Ryan Quirk

---

## Free Cell Problem

* **State:** A tuple with 4 values. First, a list of 3 lists that represent each pile in the free cell game. Then the next 3 values are the f, n, and g values corresponding to the state.
  * I.E. ([[1], [2,3], [5,4,6]], f=8, n=6, g=2)
* **Initial State:** The initial setup of the free cell game. G would be 0 so f = h.
  *  In the homework case the initial state was ([[], [], [4,5,1,2,6,7,10,9,3,8]], 10, 10, 0)
* **Goal Test:** The goal test for the free cell problem is whether n equals 0. If n = 0 then every card has been 
 discarded and the game has been won.
* **Successor Function:**  The successor function calls the search algorithm and finds all successors of the current 
 state, and adds these successors to the fringe. The search algorithm used if A*
* **Heuristic Functions** Below you can find the two heuristics used for this problem
  * Heuristic 1: h equals n
  * Heuristic 2: h equals n, plus the cards in front of card n
    * I.E. [[4,2,3], [1], []] if n = 4, h = 4 + 2, h = 6
   

### Program Output
```
CASE 1 ~ H1
GAME WON!!
Solution:[[], [], []]
States expanded: 306
Path cost: 16


CASE 1 ~ H2
GAME WON!!
Solution:[[], [], []]
States expanded: 224
Path cost: 16


CASE 2 ~ H1
FAILED!!
NO SOLUTION

CASE 2 ~ H2
FAILED!!
NO SOLUTION
```
## Parking Lot Problem

* **State:** A tuple with 3 values, the first element being a list containing the player_car and a list of all other cars.
 The second element is the f-value, and the last element being the path cost.
  * I.E. ([cars, player_car], f=8, g=2)
* **Initial State:** The initial setup of the parking lot game. G would be 0 so f = h.
* **Goal Test:** The goal test for the parking lot problem is checking if the starting coordinate or the finishing
 coordinate of the player car matches the goal coordinate.
* **Successor Function:**  The successor function calls the search algorithm and finds all successors of the current 
 state, and adds these successors to the fringe. The search algorithm used if A*
* **Heuristic Functions** Below you can find the two heuristics used for this problem
  * Heuristic 1: Manhattan Distance between the player car and the goal
  * Heuristic 2: H1, but h is increased by one for every car in between the player car and the goal.
   

### Program Output
```
CASE 1 ~ H1
States Expanded: 35785
Path Cost: 8
Solution:
['0', '1', '1', '1', '0']
['0', '1', '0', '1', '0']
['0', '1', '0', '1', '0']
['0', '0', '0', '*', '*']
['0', '0', '0', '0', '0']

GAME WON!!

CASE 1 ~ H2
States Expanded: 6245
Path Cost: 8
Solution:
['0', '1', '1', '1', '0']
['0', '1', '0', '1', '0']
['0', '1', '0', '1', '0']
['0', '0', '0', '*', '*']
['0', '0', '0', '0', '0']

GAME WON!!!

CASE 2 ~ H1
FAILED!!
NO SOLUTION

CASE 2 ~ H2
FAILED!!
NO SOLUTION
```