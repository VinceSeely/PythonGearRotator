

class LimitedDepthFirstSearch:
    def __init__ (self):
        self.closed = []

    def _LimitedSearch(self, gears, currentLevel, maxLevel, goalState):
        
        if currentLevel > maxLevel:
            return None

        gearPositions = []    
        for gear in gears:
            gearPositions.append(gear.possition)

        if self.closed.__contains__(gearPositions):
            return None

        self.closed.append(gearPositions)

        if gearPositions is goalState:
            return []

        for gearToBeRotated in range(gears.Length):
            gearCopy = gears.copy()
            self._Rotate(gearCopy, gearToBeRotated)
            result = self._LimitedSearch(gearCopy, currentLevel + 1, maxLevel, goalState)
            if result is not None:
                return result.append(gearToBeRotated)
            
        return None 

    def _Rotate (self, gearCopy, gearRotating):
        for gear in range(gearCopy):
            if gear is not gearRotating:
                gearCopy[gear].turn(gearCopy[gearRotating].rotations[gear])


