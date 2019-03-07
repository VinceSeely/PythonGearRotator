# Best First Search

## Algorithm Description

This algorithm takes in the current state of gears and generates the next potential states the gears could be in. It calculates a heuristic value for each future state by subtracting the goal state's gears' positions by the future state's gears' positions. If the value happens to be negative, the program takes the absolute value of the heuristic value and adds the corresponding position of the goal state gear. The algorithm then choses the future state with the lowest heuristic value. If this future state is the goal state, then the algorithm returns the goal state, otherwise, it repeats the process with the selected future state.

## Pseudo Code

```
BestFirstSearch(gears):
    Reset class variables (nextLevel, nextLevelHeuristicValue, lowestHeuristicValue)

    for gearToBeRotated in range(gears.Length):
        Turn gear in position gearToBeRotated
        Append new gearsState to nextLevel
        Calculate new gearsState's Heuristic Value
        Append the Heuristic Value to nextLevelHeuristicValue

    for index = 0, index < self.nextLevelHeuristicValue.Length, index++:
        Set lowestHeuristicValue to equal the lowest Heuristic Value of the new states

    if newGoalState with the lowest Heuristic Value == self.goalState:
        return the goalState
    else:
        return an array containing the current gears with the next level search of best next state

calcHeuristicValue(gears):
    heuristic = 0
    for index = 0, index < gears.Length, index++:
        Add the distance the current gear is away from the goal gear state
    return heuristic
```

## Algorithm Properties

## Results

[back](../README.md)