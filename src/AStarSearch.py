import copy
import Gear


class AStarSearch:
    def __init__(self):
        self.knownStatesPath = {}
        self.knownStatesCost = {}
        self.heuristicStates = {}
        self.newStates = []
        self.goalState = []
        self.displacementValues = []

    def Run(self, gears, goal):
        self.goalState = goal
        self.CalcGearDisplacementValues(gears)
        result = self.AStarSearch(gears)
        return result

    def AStarSearch(self, gears):
        gearInUse = copy.deepcopy(gears)
        while True:
            for gearToBeRotated in range(len(gearInUse)):
                    gearCopyTemp = copy.deepcopy(gearInUse)
                    Gear.Rotate(gearCopyTemp, gearToBeRotated)
                    value = self.calcHeuristicValue(gearCopyTemp)
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
                return self.knownStatesPath["".join(map(str, self.goalState))]
            else:
                gearInUse = copy.deepcopy(self.newStates.pop(popPos))

    def CalcGearDisplacementValues(self, gears):
        self.displacementValues = [0] * len(gears)
        for gear in range(len(gears)):
            for gear2 in range(len(gears)):
                self.displacementValues[gear] += gears[gear].rotations[gear2] if gear2 is not gear else 1

    def calcHeuristicValue(self, gears):
        heuristic = 0
        for index in range(len(gears)):
            value = self.goalState[index] - gears[index].position
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
        key = ""
        for gear in gears:
            key += "{}".format(gear.position)
        return key



if __name__ == "__main__":
    astar = AStarSearch()
    gear1 = Gear.Gear(8, 3)
    gear2 = Gear.Gear(8, 3)
    gear3 = Gear.Gear(8, 3)
    gear1.goal = 6
    gear2.goal = 0
    gear3.goal = 5
    gear1.position = 6
    gear2.position = 5
    gear3.position = 5
    gear1.rotations = [1, 1, 1]
    gear2.rotations = [1, 1, 0]
    gear3.rotations = [0, 1, 1]
    astar.goalState = [6,0,5]
    astar.calcHeuristicValue([gear1,gear2,gear3])