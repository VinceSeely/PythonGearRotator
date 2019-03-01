[gears]: ./images/gearsOrientation.jpg
[gearChart]: ./images/GearDecision.jpg
[implementationInfo]: https://github.com/VinceSeely/PythonGearRotator/blob/master/Documentation/Implemntation.md

# PythonGearRotator

## Problem Description

When a person turns a gear there is a number of other gears that can turn an unknown number of times. Each gear can cause every other gear to turn differently. The goal is to get all the gears to a specified position per gear. For a given gear it could be any value that can exist in the gear, for this we will use numbers, say each gear has 5 positions it can be in and we have 3 gears,  1, 2, and 3, where gear 1 needs to be in position 3, gear 2 in position 4, and gear 3 in position 1. The goal is to get the gear from its initial state to the goal state in the fewest number of moves.

## Problem Modeling

### Options

1. Turn Gear 1 to right
2. Turn Gear 1 to left
3. Turn Gear 2 to right
4. Turn Gear 2 to left

### Gear Orientation 

![alt text][gears]

### Gear Turning Decisions

![alt text][gearChart]

## [Implementation Details][implementationInfo]
