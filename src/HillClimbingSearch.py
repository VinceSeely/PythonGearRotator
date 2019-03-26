import copy


class HillClimbingSearch:
    def __init__(self, goalState):
        self.goalState = goalState
    
    def Run(self, gears, goal):
        result = self.HillClimbingSearch(gears)
        return result

    def HillClimbingSearch(self, gears):
        result = []
        gearCopy = copy.deepcopy(gears)
        while True:
            nextLevel = []
            nextLevelHeuristicValue = []
            lowestHeuristicValue = None
            for gearToBeRotated in range(len(gearCopy)):
                gearCopyTemp = copy.deepcopy(gearCopy)
                self._Rotate(gearCopyTemp, gearToBeRotated)
                value = self.calcHeuristicValue(gearCopyTemp)
                nextLevel.append(gearCopyTemp)
                nextLevelHeuristicValue.append(value)

            for index in range(len(nextLevelHeuristicValue)):
                if lowestHeuristicValue is None or nextLevelHeuristicValue[index] < lowestHeuristicValue:
                    lowestHeuristicValue = nextLevelHeuristicValue[index]

            nextLevelIndex = nextLevelHeuristicValue.index(lowestHeuristicValue)
            if lowestHeuristicValue is 0:
                result.append(nextLevelIndex)
                break
            else:
                result.append(nextLevelIndex)
            gearCopy = nextLevel[nextLevelIndex]
        return result

    def calcHeuristicValue(self, gears):
        heuristic = 0
        for index in range(len(gears)):
            value = self.goalState[index] - gears[index].position
            if value < 0:
                value += self.goalState[index] + abs(value)
            heuristic += value
        return heuristic


    def _Rotate (self, gearCopy, gearRotating):
        gearCopy[gearRotating].turn(1)# = (gearCopy[gearRotating].position + 1) % 9
        for gear in range(len(gearCopy)):
            if gear is not gearRotating:
                gearCopy[gear].turn(gearCopy[gearRotating].rotations[gear])


