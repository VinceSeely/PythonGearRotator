import copy
import multiprocessing
from multiprocessing import Process

import Gear

timeOut = 50


class HillClimbingSearch:
    def __init__(self):
        self.goalState = []
        self.result = []
        self.goalFound = False
    
    def Run(self, gears, goal):
        self.goalState = goal
        result_queue = multiprocessing.Queue()
        process = Process(target=self.HillClimbingSearch, args=(gears, result_queue,))
        process.start()
        process.join(timeout=50)
        process.terminate()
        if result_queue.empty():
            return None
        result = result_queue.get(False)
        return result

    def HillClimbingSearch(self, gears, result_queue):
        gearCopy = copy.deepcopy(gears)
        result = []
        while True:
            nextLevel = []
            nextLevelHeuristicValue = []
            lowestHeuristicValue = None
            for gearToBeRotated in range(len(gearCopy)):
                gearCopyTemp = copy.deepcopy(gearCopy)
                Gear.Rotate(gearCopyTemp, gearToBeRotated)
                value = self.calcHeuristicValue(gearCopyTemp)
                nextLevel.append(gearCopyTemp)
                nextLevelHeuristicValue.append(value)

            for index in range(len(nextLevelHeuristicValue)):
                if lowestHeuristicValue is None or nextLevelHeuristicValue[index] < lowestHeuristicValue:
                    lowestHeuristicValue = nextLevelHeuristicValue[index]

            nextLevelIndex = nextLevelHeuristicValue.index(lowestHeuristicValue)
            if lowestHeuristicValue is 0:
                result.append(nextLevelIndex)
                break
            else:
                result.append(nextLevelIndex)
            gearCopy = nextLevel[nextLevelIndex]
        result_queue.put(result)

    def calcHeuristicValue(self, gears):
        heuristic = 0
        for index in range(len(gears)):
            value = self.goalState[index] - gears[index].position
            if value < 0:
                value = self.goalState[index] + abs(value)
            heuristic += value
        return heuristic
