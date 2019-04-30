import copy

class BeamSearch:
    def __init__(self):
        self.result = []
        self.displacementValues = []
        self.visitedHeuristic = {}
        self.knownStatesPath = {}
        self.queue = []
        self.numNodesKept = 2

    def Run(self, gear_manager):
        self.CalcGearDisplacementValues(gear_manager)
        result = self.BeamSearch(gear_manager)
        return result

    def CalcGearDisplacementValues(self, gear_manager):
        matrix = gear_manager.get_matrix()
        self.displacementValues = [0] * len(matrix)
        for gear in range(len(matrix)):
            for rotation in range(len(matrix[gear])):
                self.displacementValues[gear] += matrix[gear][rotation]

    def BeamSearch(self, gear_manager):
        gearCopy = gear_manager.get_copy_of_gears()
        result = []
        goal = gear_manager.get_goal()
        if gear_manager.get_positions() == goal:
            return []
        while True:
            nextLevel = []
            nextLevelHeuristicValue = []
            key = "".join(map(str, [x.position for x in gearCopy]))
            if key in self.visitedHeuristic:
                self.visitedHeuristic[key] += 1
            else:
                self.visitedHeuristic[key] = 1
            
            breakTime = False
            for gearToBeRotated in range(len(gearCopy)):
                gearCopyTemp = gear_manager.rotate_and_copy(gearCopy, gearToBeRotated)
                value = self.calcHeuristicValue(gearCopyTemp, goal)
                nextLevel.append(gearCopyTemp)
                nextLevelHeuristicValue.append(value)
                self.updateKnownValues(gearCopy, gearCopyTemp, gearToBeRotated)
                if value == 0:
                    breakTime = True

            if breakTime:
                goalKey = "".join(map(str, [x.position for x in gear_manager.get_goal()]))
                result = self.knownStatesPath[goalKey]
                break

            self.SelectionSort(nextLevel, nextLevelHeuristicValue)
            for index in range(self.numNodesKept):
                self.queue.append(nextLevel[index])
            gearCopy = copy.deepcopy(self.queue.pop(0))
                
        return result

    def calcHeuristicValue(self, gears, goal):
        heuristic = 0.0
        for index in range(len(gears)):
            value = goal[index] - gears[index].position
            if value < 0:
               value += gears[0].max_position
            heuristic += (value / self.displacementValues[index])
        key = "".join(map(str, [x.position for x in gears]))
        if key in self.visitedHeuristic:
            heuristic += self.visitedHeuristic[key]
        return heuristic

    def SelectionSort(self, nextLevel, nextLevelHeuristicValue):
        for goalIndex in range(len(nextLevel)-1):
            for curIndex in range(goalIndex+1, len(nextLevel), -1):
                curValue = nextLevelHeuristicValue[curIndex]
                nextValue = nextLevelHeuristicValue[curIndex-1]
                curGearSet = nextLevel[curIndex]
                nextGearSet = nextLevel[curIndex-1]
                if curValue < nextValue:
                    temp = curValue
                    nextLevelHeuristicValue[curIndex] = nextValue
                    nextLevelHeuristicValue[curIndex-1] = temp
                    temp = curGearSet
                    nextLevel[curIndex] = nextGearSet
                    nextLevel[curIndex-1] = temp
        
    def updateKnownValues(self, initialState, newState, gearTurned):
        prevStateKey = "".join(map(str, [x.position for x in initialState]))
        newStateKey = "".join(map(str, [x.position for x in newState]))

        if prevStateKey not in self.knownStatesPath:
            self.knownStatesPath[newStateKey] = [gearTurned]
        else:
            next = copy.deepcopy(self.knownStatesPath[prevStateKey])
            next.append(gearTurned)
            self.knownStatesPath[newStateKey] = next
