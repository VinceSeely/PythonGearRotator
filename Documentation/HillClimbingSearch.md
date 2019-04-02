# Hill Climbing Search

## Heuristic Description

The heurstic is the sum of each gear's goal position minus each gear's current position. If the difference is negative the absolute value of the difference is taken plus the maximum gear position possible and is added instead.

$ \sum_{\forall i}{x_i^{2}} $

$ \sum_{i=1}^{10} t_i goal + (goal - pos) : If goal - pos < 0 else goal - pos $
```
$ \sum_{i=1}^{10} t_i goal + (goal - pos) : If goal - pos < 0 else goal - pos $
```

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

This algorithm is greedy in which case it is not complete or admissibile. It does have irrevocability. This is not optimal for this problem because the tree grows infinitely. It's complexity is also potentially infinite.

## Results
```
Inputs: 
    [
    {"min_turn"=0 "max_turn"=4 "position"=2 "goal"=6 "max_position"=8 "rotations"=[1, 1, 1]}, 
    {"min_turn"=0 "max_turn"=4 "position"=0 "goal"=0 "max_position"=8 "rotations"=[1, 1, 0]}, 
    {"min_turn"=0 "max_turn"=4 "position"=0 "goal"=5 "max_position"=8 "rotations"=[0, 1, 1]}
    ]
Output: 
    "None"
```
```
Inputs: 
    [
    {"min_turn"=0 "max_turn"=4 "position"=3 "goal"=3 "max_position"=8 "rotations"=[0, 0, 0]}, 
    {"min_turn"=0 "max_turn"=4 "position"=4 "goal"=6 "max_position"=8 "rotations"=[0, 0, 0]}, 
    {"min_turn"=0 "max_turn"=4 "position"=2 "goal"=7 "max_position"=8 "rotations"=[1, 1, 0]}
    ]
Output: 
    "None"
```
```
Inputs: 
    [
    {"min_turn"=0 "max_turn"=4 "position"=7 "goal"=7 "max_position"=8 "rotations"=[1, 0, 0]}, 
    {"min_turn"=0 "max_turn"=4 "position"=0 "goal"=2 "max_position"=8 "rotations"=[1, 0, 0]}, 
    {"min_turn"=0 "max_turn"=4 "position"=8 "goal"=7 "max_position"=8 "rotations"=[1, 0, 1]}
    ]
Output: 
    [2, 2, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1]
```
[back](../README.md)
