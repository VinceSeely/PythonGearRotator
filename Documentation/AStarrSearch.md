# A* Search

## Algorithm Description

This algorithm takes in the current state of gears and generates the next potential states the gears could be in. It calculates a heuristic value for each future state by subtracting the goal state's gears' positions by the future state's gears' positions. If the value happens to be negative, the program takes the absolute value of the heuristic value and adds the corresponding position of the goal state gear. The algorithm also calculates the total cost to get to the potential new states by taking the previous state's cost and adding the currently selected state's heuristic cost and 1. At the same time, the path of the potential new state is created by appending the previous state's path and the new gear turned to get to the selected potential new state. If the potnetial new state has never been seen before or if it is better than the preiously known way to get to it, then add it to the list of new new states to explore. Of the new states, the algorithm selects the lowest costing state and if the state's heuristic value is zero, then we will know we've found the goal state and can return the path to get to the goal state. Otherwise, the algorithm uses the lowest costing state as the new base state. However, as a safety measure, if the list of new states is empty and the goal state isn't found, then the algorithm returns None.

## Pseudo Code

```
    AStarSearch(gears):
        Make a deep copy of gears as gearInUse
        while True:
            foreach gear in gearInUse
                    Make a temporary deep copy of gearInUse
                    Rotate the Gear
                    Calculate the Heuristic of the new Gear state
                    Keep a record of the total cost to get to this state and the turns needed to do so
                    If this is a completely new state, then add it to a list of unexplored states
            
            Initialize lowestCost, popPos, and lowestHCost to None
            foreach gears in newStates:
                Get the gears' key
                Get the gears' current cost
                if lowestCost is None or curStateCost < lowestCost:
                    lowestCost = curStateCost            
                    popPos = index        
                curHCost = self.heuristicStates[key]
                if lowestHCost is None or curHCost < lowestHCost:
                    lowestHCost = curHCost

            if popPos is None:
                return None
            if lowestHCost is 0:
                return the path to the goal state
            else:
                Make a deep copy of gearInUse as the lowest costing state
```

## Algorithm Properties

This algorithm is complete because the problem has a finite branching factor, as well as it is optimal. It has abmissibility and irrevocability. The algorithm's complexity increases exponentially based on the heuristic values.

## Results
```
Inputs: 
    [
    {"min_turn"=0 "max_turn"=4 "position"=4 "goal"=4 "max_position"=8}, 
    {"min_turn"=0 "max_turn"=4 "position"=6 "goal"=3 "max_position"=8}, 
    {"min_turn"=0 "max_turn"=4 "position"=1 "goal"=8 "max_position"=8}
    ]
Output: 
    [2, 2, 2, 2, 2, 3]
```
```
Inputs: 
    [
    {"min_turn"=0 "max_turn"=4 "position"=7 "goal"=6 "max_position"=8}, 
    {"min_turn"=0 "max_turn"=4 "position"=4 "goal"=9 "max_position"=8}, 
    {"min_turn"=0 "max_turn"=4 "position"=1 "goal"=2 "max_position"=8}
    ]
Output: 
    "None"
```
```
Inputs: 
    [
    {"min_turn"=0 "max_turn"=4 "position"=7 "goal"=5 "max_position"=8}, 
    {"min_turn"=0 "max_turn"=4 "position"=6 "goal"=1 "max_position"=8}, 
    {"min_turn"=0 "max_turn"=4 "position"=2 "goal"=3 "max_position"=8}
    ]
Output: 
    [1, 2, 2, 1, 1, 1, 3, 3, 3, 3, 3]
```
[back](../README.md)