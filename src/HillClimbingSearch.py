

class HillClimbingSearch:
    def __init__(self):
        self.result = []
        self.displacementValues = []
        self.visitedHeuristic = {}

    def Run(self, gear_manager):
        self.CalcGearDisplacementValues(gear_manager)
        result = self.HillClimbingSearch(gear_manager)
        return result

    def CalcGearDisplacementValues(self, gear_manager):
        matrix = gear_manager.get_matrix()
        self.displacementValues = [0] * len(matrix)
        for gear in range(len(matrix)):
            for rotation in range(len(matrix[gear])):
                self.displacementValues[gear] += matrix[gear][rotation]

    def HillClimbingSearch(self, gear_manager):
        gearCopy = gear_manager.get_copy_of_gears()
        result = []
        goal = gear_manager.get_goal()
        if gear_manager.get_positions() == goal:
            return []
        while True:
            nextLevel = []
            nextLevelHeuristicValue = []
            lowestHeuristicValue = None
            key = "".join(map(str, [x.position for x in gearCopy]))
            if key in self.visitedHeuristic:
                self.visitedHeuristic[key] += 1
            else:
                self.visitedHeuristic[key] = 1
            for gearToBeRotated in range(len(gearCopy)):
                gearCopyTemp = gear_manager.rotate_and_copy(gearCopy, gearToBeRotated)
                value = self.calcHeuristicValue(gearCopyTemp, goal)
                nextLevel.append(gearCopyTemp)
                nextLevelHeuristicValue.append(value)

            for index in range(len(nextLevelHeuristicValue)):
                if lowestHeuristicValue is None or nextLevelHeuristicValue[index] < lowestHeuristicValue:
                    lowestHeuristicValue = nextLevelHeuristicValue[index]

            nextLevelIndex = nextLevelHeuristicValue.index(lowestHeuristicValue)
            if lowestHeuristicValue == 0.0:
                result.append(nextLevelIndex)
                break
            else:
                result.append(nextLevelIndex)
            gearCopy = nextLevel[nextLevelIndex]
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
