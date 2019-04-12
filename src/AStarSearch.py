import copy


class AStarSearch:
    def __init__(self):
        self.knownStatesPath = {}
        self.knownStatesCost = {}
        self.heuristicStates = {}
        self.newStates = []
        self.displacementValues = []

    def Run(self, gear_manager):
        self.CalcGearDisplacementValues(gear_manager)
        result = self.AStarSearch(gear_manager)
        return result

    def CalcGearDisplacementValues(self, gear_manager):
        matrix = gear_manager.get_matrix()
        self.displacementValues = [0] * len(matrix)
        for gear in range(len(matrix)):
            for rotation in range(len(matrix[gear])):
                self.displacementValues[gear] += matrix[gear][rotation]

    def AStarSearch(self, gear_manager):
        gearInUse = gear_manager.get_copy_of_gears()
        goal = gear_manager.get_goal()
        if gear_manager.get_positions() == goal:
            return []
        while True:
            for gearToBeRotated in range(len(gearInUse)):
                gearCopyTemp = gear_manager.rotate_and_copy(gearInUse, gearToBeRotated)
                value = self.calcHeuristicValue(gearCopyTemp, goal)
                addedNewState = self.updateKnownValues(gearInUse, gearCopyTemp, value, gearToBeRotated)
                if addedNewState:
                    self.newStates.append(gearCopyTemp)

            lowestCostIndex = None
            popPos = None
            lowestHCostIndex = None
            for index in range(len(self.newStates)):
                key = self.getKey(self.newStates[index])
                curStateCost = self.knownStatesCost[key]
                if lowestCostIndex is None or curStateCost < lowestCostIndex:
                    lowestCostIndex = curStateCost            
                    popPos = index        
                curHCost = self.heuristicStates[key]
                if lowestHCostIndex is None or curHCost < lowestHCostIndex:
                    lowestHCostIndex = curHCost

            if popPos is None:
                return None
            if self.heuristicStates[self.getKey(self.newStates[popPos])] == 0.0:
                return self.knownStatesPath["".join(map(str, goal))]
            else:
                gearInUse = self.newStates.pop(popPos)

    def calcHeuristicValue(self, gears, goal):
        heuristic = 0.0
        for index in range(len(gears)):
            value = goal[index] - gears[index].position
            if value < 0:
                value += gears[0].max_position
            heuristic += (value / self.displacementValues[index])
        return heuristic

    def updateKnownValues(self, initialState, newState, hValue, gearTurned):
        prevStateKey = self.getKey(initialState)
        newStateKey = self.getKey(newState)

        self.heuristicStates[newStateKey] = hValue
        if prevStateKey not in self.knownStatesCost:
            self.knownStatesPath[newStateKey] = [gearTurned]
            self.knownStatesCost[newStateKey] = hValue + 1
            return True
        else:
            newStateCost = self.knownStatesCost[prevStateKey] + hValue + 1
            knownStateCost = self.knownStatesCost[newStateKey] if newStateKey in self.knownStatesCost else None
            if knownStateCost is None or newStateCost < knownStateCost:
                next = copy.deepcopy(self.knownStatesPath[prevStateKey])
                next.append(gearTurned)
                self.knownStatesPath[newStateKey] = next
                self.knownStatesCost[newStateKey] = newStateCost
                return True
        return False

    def getKey(self, gears):
        key = "".join(map(str, [x.position for x in gears]))
        return key
