# Iterative Depth Search

## Algorithm Description

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
