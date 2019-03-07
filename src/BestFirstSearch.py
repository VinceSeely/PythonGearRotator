#This is not finished

class BestFirstSearch:
    def __init__(self, goalState):
        self.nextLevel = []
        self.nextLevelHeuristicValue = []
        self.lowestHeuristicValue = 200
        self.goalState = goalState

    def BestFirstSearch(self, gears):
        self.nextLevel.clear()
        self.nextLevelHeuristicValue.clear()
        self.lowestHeuristicValue = 200

        for gearToBeRotated in range(gears.Length):
            gearCopy = gears.copy()
            result = self._Rotate(gearCopy, gearToBeRotated)
            value = self.calcHeuristicValue(result)
            self.nextLevel.append(result)
            self.nextLevelHeuristicValue.append(value)

        for index in range(self.nextLevelHeuristicValue.Length):
            if self.nextLevelHeuristicValue[index] < self.lowestHeuristicValue:
                self.lowestHeuristicValue = self.nextLevelHeuristicValue[index]

        if self.nextLevel[self.nextLevelHeuristicValue.index(self.lowestHeuristicValue)] == self.goalState:
            return self.goalState
        else:
            path = [gears]
            return path.append(BestFirstSearch(self.nextLevel[index]))

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
