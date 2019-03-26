class AStarSearch:
    def __init__(self, goalState):
        self.knownStates = {}
        self.goalState = goalState
        self.lowestCost

    def AStarSearch(self, gears):
        nextLevel = []
        nextLevelHeuristicValue = []

        for gearToBeRotated in range(gears.Length):
            gearCopy = gears.copy()
            result = self._Rotate(gearCopy, gearToBeRotated)
            value = self.calcHeuristicValue(result)
            nextLevel.append(result)
            nextLevelHeuristicValue.append(value)
            self.updateKnownValues(gears, result, gearToBeRotated)

        lowestCostIndex = 0
        for index in range(self.nextLevel.Length):
            cost = nextLevelHeuristicValue[index] + self.updateKnownValues[self.getKey(nextLevel[index])].Length
            if self.lowestCost is None:
                self.lowestCost = cost
            if cost < self.lowestCost:
                self.lowestCost = cost
                lowestCostIndex = index

        if self.goalState in self.knownStates:
            return self.knownStates[self.goalState]
        else:
            AStarSearch(self.nextLevel[lowestCostIndex])

    def calcHeuristicValue(self, gears):
        heuristic = 0
        for index in range(gears.Length):
            value = self.goalState[index].get_position() - gears[index].get_position()
            if value < 0:
                value += self.goalState[index].get_position() + abs(value)
            heuristic += value
        return heuristic

    def updateKnownValues(self, initialState, newState, gearTurned):
        previousKey = self.getKey(initialState)
        newKey = self.getKey(newState)

        if previousKey in self.knownStates:
            if self.knownStates[previousKey].append(gearTurned).Length < self.knownStates[newKey]:
                self.knownStates[newKey] = self.knownStates[previousKey].append(gearTurned)
        else:
            self.knownStates[newKey] = [gearTurned]

    def getKey(self, gears):
        key = ""
        for gear in gears:
            key += str(gear.position)
        return key

    def _Rotate (self, gearCopy, gearRotating):
        for gear in range(gearCopy):
            if gear is not gearRotating:
                return gearCopy[gear].turn(gearCopy[gearRotating].rotations[gear])
