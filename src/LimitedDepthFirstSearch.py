
import copy
import Gear


class LimitedDepthFirstSearch:
    def __init__(self):
        self.closed = []

    def Run(self, gear_manager):
        result = self.IterativeSearch(gear_manager, 6, 500)
        return result

    def IterativeSearch(self, gear_manager, startLevel, MaxLevel):
        result = None
        gearCopy = gear_manager.get_copy_of_gears()
        for layer in range(startLevel, MaxLevel):
            result = self._LimitedSearch(gear_manager, 0, layer, gearCopy)
            if result is not None:
                break
            self.closed = []
        self.closed.sort()
        return result[0]

    def _LimitedSearch(self, gear_manager, currentLevel, maxLevel, gears):
        nodes_to_visit = [[[], gears]]
        while len(nodes_to_visit) != 0:
            currentNode = nodes_to_visit.pop()
            if len(currentNode[0]) > maxLevel:
                continue

            gearPositions = []    
            for gear in currentNode[1]:
                gearPositions.append(gear.position)

            if self.closed.__contains__(gearPositions):
                continue

            self.closed.append(gearPositions)

            if self.closed.__contains__(gear_manager.get_goal()):
                return currentNode

            for gearToBeRotated in range(len(gears)):
                gearCopy = gear_manager.rotate_and_copy(currentNode[1], gearToBeRotated)
                nodeCopy = copy.deepcopy(currentNode[0])
                nodeCopy.append(gearToBeRotated)
                nodes_to_visit.append([nodeCopy, gearCopy])

        return None 

