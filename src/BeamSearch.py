import copy
import heapq

class GearTuple:
    def __init__(self, gears, heuristic, turns):
        self.gearroatations = gears
        self.heuristic = heuristic
        self.turns = turns

    def __ge__(self, other):
        if isinstance(other, GearTuple):
            return self.heuristic >= other.heuristic
        else:
            return False

    def __le__(self, other):
        if isinstance(other, GearTuple):
            return self.heuristic <= other.heuristic
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, GearTuple):
            return self.heuristic > other.heuristic
        else:
            return False

    def __le__(self, other):
        if isinstance(other, GearTuple):
            return self.heuristic < other.heuristic
        else:
            return False


class BeamSearch:
    def __init__(self):
        self.displacementValues = []
        self.visitedHeuristic = {}
        self.knownStatesPath = {}

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
        gearCopy = GearTuple(gear_manager.get_copy_of_gears(), None, [])
        queue = []
        numNodesKept = 2
        goal = gear_manager.get_goal()
        if gear_manager.get_positions() == goal:
            return []
        while True:
            nextLevel = []
            key = "".join(map(str, [x.position for x in gearCopy.gearroatations]))
            if key in self.visitedHeuristic:
                self.visitedHeuristic[key] += 1
            else:
                self.visitedHeuristic[key] = 1

            uptonowturns = gearCopy.turns
            for gearToBeRotated in range(len(gearCopy.gearroatations)):
                gearCopyTemp = gear_manager.rotate_and_copy(gearCopy.gearroatations, gearToBeRotated)
                nextTurn = copy.deepcopy(uptonowturns)
                nextTurn.append(gearToBeRotated)
                value = self.calcHeuristicValue(gearCopyTemp, goal)
                nextLevel.append(GearTuple(gearCopyTemp, value, nextTurn))
                if value == 0:
                    return nextTurn


            keptconfigs = heapq.nsmallest(numNodesKept, nextLevel)
            for index in keptconfigs:
                queue.append(index)
            gearCopy = copy.deepcopy(queue.pop(0))
                
        return None

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
