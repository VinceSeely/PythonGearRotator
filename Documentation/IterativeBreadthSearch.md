# Iterative Depth Search

## Algorithm Description

The Iterative depth first search looks at the current state of the system, and traverses the decisions by using a tree of all possible moves. it does this recursively looking down each branch and then traversing back up and down till it finds a solution or all possible positions have been visited. Then it returns an array of all the values for the order in which the gears were turned to get the final result of how the gears were turned.

## Pseudo Code

```
IterativeSearch(gears)
    solutionFound = false
    depth = 0
    goal = getGoal(gears)
    while !solutionFound and depth not greater than absoluteMax
        _limitedSearch(0, depth++, gears, goal)

_limitedSearch (currentLevel, maxLevel, gears, goalState)
    if currentLevel > maxLevel
       return none
    foreach gear in gears
       positions = gear.position

    if positions == goalState
       return []

    for each gear in gears
       rotatedGears = rotate(gears for gear.rotations value)
       _limitedSearch(currentLevel +1, maxLevel, rotatedGears, goalState)
```

## Algorithm Properties

This algorithm is complete and optimal since there is no weight applied to the edges of the state tree. The Time complexity is O(b^d) and Space complexity is O(bd), where b is the branching factor and d is the number of nodes. However, due to the nature of this problem it is possible for the Time and Space complexity to be infinite.

## Results
```
Inputs: 
    [
    {"min_turn"=0 "max_turn"=4 "position"=7 "goal"=5 "max_position"=8}, 
    {"min_turn"=0 "max_turn"=4 "position"=6 "goal"=1 "max_position"=8}, 
    {"min_turn"=0 "max_turn"=4 "position"=2 "goal"=3 "max_position"=8}
    ]
Output: 
   [1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3]
```
```
Inputs: 
    [
    {"min_turn"=0 "max_turn"=4 "position"=6 "goal"=3 "max_position"=8}, 
    {"min_turn"=0 "max_turn"=4 "position"=5 "goal"=2 "max_position"=8}, 
    {"min_turn"=0 "max_turn"=4 "position"=9 "goal"=5 "max_position"=8}
    ]
Output: 
   [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3]
```
```
Inputs: 
    [
    {"min_turn"=0 "max_turn"=4 "position"=9 "goal"=4 "max_position"=8}, 
    {"min_turn"=0 "max_turn"=4 "position"=5 "goal"=1 "max_position"=8}, 
    {"min_turn"=0 "max_turn"=4 "position"=9 "goal"=5 "max_position"=8}
    ]
Output: 
   [1, 1, 1, 2, 3]
```

[back](../README.md)
