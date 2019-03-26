class HillClimbingSearch:
    def __init__(self, goalState):
        self.nextLevel = []
        self.nextLevelHeuristicValue = []
        self.lowestHeuristicValue = None
        self.goalState = goalState
    def Run(self, gears, goal):
        self.HillClimbingSearch(gears)
    def HillClimbingSearch(self, gears):
        self.nextLevel.clear()
        self.lowestHeuristicValue = None
        self.nextLevelHeuristicValue.clear()

        for gearToBeRotated in range(gears.Length):
            gearCopy = gears.copy()
            result = self._Rotate(gearCopy, gearToBeRotated)
            value = self.calcHeuristicValue(result)
            self.nextLevel.append(result)
            self.nextLevelHeuristicValue.append(value)

        for index in range(len(self.nextLevelHeuristicValue)):
            if self.nextLevelHeuristicValue[index] < self.lowestHeuristicValue or self.lowestHeuristicValue is None:
                self.lowestHeuristicValue = self.nextLevelHeuristicValue[index]

        if self.nextLevel[self.nextLevelHeuristicValue.index(self.lowestHeuristicValue)] == self.goalState:
            return self.goalState
        else:
            path = [self.nextLevelHeuristicValue.index(self.lowestHeuristicValue)]
            return path.append(HillClimbingSearch(self.nextLevel[self.nextLevelHeuristicValue.index(self.lowestHeuristicValue)]))

    def calcHeuristicValue(self, gears):
        heuristic = 0
        for index in range(gears.Length):
            value = self.goalState[index].get_position() - gears[index].get_position()
            if value < 0:
                value += self.goalState[index].get_position() + abs(value)
            heuristic += value
        return heuristic


    def _Rotate (self, gearCopy, gearRotating):
        for gear in range(gearCopy):
            if gear is not gearRotating:
                return gearCopy[gear].turn(gearCopy[gearRotating].rotations[gear])
