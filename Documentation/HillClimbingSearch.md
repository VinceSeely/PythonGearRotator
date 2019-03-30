# Hill Climbing Search

## Algorithm Description

This algorithm takes in the current state of gears and generates the next potential states the gears could be in. It calculates a heuristic value for each future state by subtracting the goal state's gears' positions by the future state's gears' positions. If the value happens to be negative, the program takes the absolute value of the heuristic value and adds the corresponding position of the goal state gear. The algorithm then choses the future state with the lowest heuristic value. If this future state is the goal state, then the algorithm returns the goal state, otherwise, it repeats the process with the selected future state.

## Pseudo Code

```
HillClimbingSearch(gears):
    result = []
    while true
        nextLevel, nextLevelHeuristicValue, lowestHeuristicValue = [], [], None

        for gearToBeRotated in range(gears.Length):
            Turn gear in position gearToBeRotated
            Append new gearsState to nextLevel
            Calculate new gearsState's Heuristic Value
            Append the Heuristic Value to nextLevelHeuristicValue

        for index = 0, index < self.nextLevelHeuristicValue.Length, index++:
            Set lowestHeuristicValue to equal the lowest Heuristic Value of the new states

        nextLevelIndex = nextLevelHeuristicValue.index(lowestHeuristicValue)

        if lowest Heuristic Value == 0:
            result.append(nextLevelIndex)
        else:
            result.append(nextLevelIndex)

    return result

calcHeuristicValue(gears):
    heuristic = 0
    for index = 0, index < gears.Length, index++:
        Add the distance the current gear is away from the goal gear state
    return heuristic
```

## Algorithm Properties

## Results
```
Inputs: [gear1, gear2, gear3], [goalGear1, goalGear1, goalGear1]       Note: The respective positions sets are [3, 1, 1] and [7, 1, 6]
Output: "None"
```
```
Inputs: [gear1, gear2, gear3], [goalGear1, goalGear1, goalGear1]      Note: The respective positions sets are [3, 7, 3] and [3, 4, 7]
Output: [3, 3, 3, 3, 2, 1, 1, 1]
```
```
Inputs: [gear1, gear2, gear3], [goalGear1, goalGear1, goalGear1]       Note: The respective positions sets are [1, 6, 2] and [2, 8, 5]
Output: [1, 2, 2, 3, 3]
```
[back](../README.md)