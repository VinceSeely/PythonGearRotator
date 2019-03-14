class A-StarSearch:
    def __init__(self, goalState):
        self.nextLevel = []
        self.nextLevelHeuristicValue = []
        self.lowestCost
        self.goalState = goalState
        self.knownStates = {}

    def A-StarSearch(self, gears):
        self.nextLevel.clear()
        self.nextLevelHeuristicValue.clear()

        for gearToBeRotated in range(gears.Length):
            gearCopy = gears.copy()
            result = self._Rotate(gearCopy, gearToBeRotated)
            value = self.calcHeuristicValue(result)
            self.nextLevel.append(result)
            self.nextLevelHeuristicValue.append(value)
            self.updateKnownValues(gears, result, gearToBeRotated)

        for index in range(self.nextLevel.Length):
            cost = self.nextLevelHeuristicValue[index] + self.updateKnownValues[self.getKey(self.nextLevel[index])].Length
            if cost < self.lowestCost:
                self.lowestCost = cost

        if self.nextLevel[self.nextLevelHeuristicValue.index(self.lowestHeuristicValue)] == self.goalState:
            return self.goalState
        else:
            path = [gears]
            return path.append(A-StarSearch(self.nextLevel[index]))

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

    def getKey(self, gears)
        key = ""
        for gear in gears:
            key += str(gear.position)
        return key


    def _Rotate (self, gearCopy, gearRotating):
        for gear in range(gearCopy):
            if gear is not gearRotating:
                return gearCopy[gear].turn(gearCopy[gearRotating].rotations[gear])