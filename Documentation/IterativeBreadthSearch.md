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

[back](../README.md)
