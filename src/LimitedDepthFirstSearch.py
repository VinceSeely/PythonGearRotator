
import copy
import sys


class LimitedDepthFirstSearch:
    def __init__(self):
        self.closed = []
        self.visited = []

    def Run(self, gear_manager):
        result = self.IterativeSearch(gear_manager, 1, sys.maxsize)
        return result

    def IterativeSearch(self, gear_manager, startLevel, MaxLevel):
        result = None
        gearCopy = gear_manager.get_copy_of_gears()
        for layer in range(startLevel, MaxLevel, 3):
            result = self._LimitedSearch(gear_manager, layer, gearCopy)
            if result is not None:
                break
            if len(self.visited) == 0:
                break
        self.closed.sort()
        return result

    def _LimitedSearch(self, gear_manager, maxLevel, gears):
        nodes_to_visit = [[[], gears]]
        if len(self.visited) != 0:
            nodes_to_visit = copy.deepcopy(self.visited)
            self.visited = []
        while len(nodes_to_visit) != 0:
            currentNode = nodes_to_visit.pop()
            if len(currentNode[0]) > maxLevel:
                self.visited.append(currentNode)
                continue

            gearPositions = []    
            for gear in currentNode[1]:
                gearPositions.append(gear.position)

            if self.closed.__contains__(gearPositions):
                continue

            self.closed.append(gearPositions)

            if self.closed.__contains__(gear_manager.get_goal()):
                return currentNode[0]

            for gearToBeRotated in range(len(gears)):
                gearCopy = gear_manager.rotate_and_copy(currentNode[1], gearToBeRotated)
                nodeCopy = copy.deepcopy(currentNode[0])
                nodeCopy.append(gearToBeRotated)
                nodes_to_visit.append([nodeCopy, gearCopy])

        return None 

