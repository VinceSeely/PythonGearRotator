import copy


class HillClimbingSearch:
    def __init__(self, goalState):
        self.nextLevel = []
        self.nextLevelHeuristicValue = []
        self.lowestHeuristicValue = None
        self.goalState = goalState
    
    def Run(self, gears, goal):
        return self.HillClimbingSearch(gears)

    def HillClimbingSearch(self, gears):
        self.nextLevel.clear()
        self.lowestHeuristicValue = None
        self.nextLevelHeuristicValue.clear()

        for gearToBeRotated in range(len(gears)):
            gearCopy = copy.deepcopy(gears)
            self._Rotate(gearCopy, gearToBeRotated)
            value = self.calcHeuristicValue(gearCopy)
            self.nextLevel.append(gearCopy)
            self.nextLevelHeuristicValue.append(value)

        for index in range(len(self.nextLevelHeuristicValue)):
            if self.lowestHeuristicValue is None or self.nextLevelHeuristicValue[index] < self.lowestHeuristicValue:
                self.lowestHeuristicValue = self.nextLevelHeuristicValue[index]

        if self.lowestHeuristicValue is sum(self.goalState):#self.nextLevel[self.nextLevelHeuristicValue.index(self.lowestHeuristicValue)] == self.goalState:
            return self.goalState
        else:
            path = [self.nextLevelHeuristicValue.index(self.lowestHeuristicValue)]
            return path.append(self.HillClimbingSearch(self.nextLevel[self.nextLevelHeuristicValue.index(self.lowestHeuristicValue)]))

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


