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

## Results
```
Inputs: [gear1, gear2, gear3], [goalGear1, goalGear1, goalGear1]       Note: The respective positions sets are [7, 6, 2] and [5, 1, 3]
Output: [1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3]
```
```
Inputs: [gear1, gear2, gear3], [goalGear1, goalGear1, goalGear1]       Note: The respective positions sets are [6, 5, 9] and [3, 2, 5]
Output: [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3]
```
```
Inputs: [gear1, gear2, gear3], [goalGear1, goalGear1, goalGear1]       Note: The respective positions sets are [9, 5, 9] and [4, 1, 5]
Output: [1, 1, 1, 2, 3]
```

[back](../README.md)
