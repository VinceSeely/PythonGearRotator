import copy

class LimitedDepthFirstSearch:
    def __init__ (self):
        self.closed = []
        self.gears = []
    
    def Run(self, gears, goal):
        result = self.IterativeSearch(gears, 6, 500, goal)
        if result is not None:
            result.reverse()
        return result

    def IterativeSearch(self, gears, startLevel, MaxLevel, goalState):
        result = None
        self.gears = gears.copy()
        for layer in range(startLevel, MaxLevel):
            result = self._LimitedSearch(gears, 0, layer, goalState)
            if result is not None:
                break
            self.closed = []
        self.closed.sort()
        return result

    def _LimitedSearch(self, gears, currentLevel, maxLevel, goalState):
        
        if currentLevel > maxLevel:
            return None

        gearPositions = []    
        for gear in gears:
            gearPositions.append(gear.position)

        if self.closed.__contains__(gearPositions):
            return None

        self.closed.append(gearPositions)

        if self.closed.__contains__(goalState):
            return []

        for gearToBeRotated in range(len(gears)):
            gearCopy = copy.deepcopy(gears)
            self._Rotate(gearCopy, gearToBeRotated)
            result = self._LimitedSearch(gearCopy, currentLevel + 1, maxLevel, goalState)
            if result is not None:
                result.append(gearToBeRotated)
                return result
            
        return None 

    def _Rotate (self, gearCopy, gearRotating):
        gearCopy[gearRotating].turn(1)# = (gearCopy[gearRotating].position + 1) % 9
        for gear in range(len(gearCopy)):
            if gear is not gearRotating:
                gearCopy[gear].turn(gearCopy[gearRotating].rotations[gear])


