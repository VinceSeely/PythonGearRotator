
import copy
import Gear


class LimitedDepthFirstSearch:
    def __init__ (self):
        self.closed = []

    def Run(self, gear_manager):
        result = self.IterativeSearch(gear_manager, 6, 500)
        if result is not None:
            result.reverse()
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
        return result

    def _LimitedSearch(self, gear_manager, currentLevel, maxLevel, gears):
        
        if currentLevel > maxLevel:
            return None

        gearPositions = []    
        for gear in gears:
            gearPositions.append(gear.position)

        if self.closed.__contains__(gearPositions):
            return None

        self.closed.append(gearPositions)

        if self.closed.__contains__(gear_manager.get_goal()):
            return []

        for gearToBeRotated in range(len(gears)):
            gearCopy = gear_manager.rotate_and_copy(gears, gearToBeRotated)
            result = self._LimitedSearch(gear_manager, currentLevel + 1, maxLevel, gearCopy)
            if result is not None:
                result.append(gearToBeRotated)
                return result
            
        return None 

