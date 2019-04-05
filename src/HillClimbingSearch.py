import copy
import sys
import multiprocessing
from multiprocessing import Process

import Gear

timeOut = 50


class HillClimbingSearch:
    def __init__(self):
        self.goalState = []
        self.result = []
        self.displacementValues = []
        self.goalFound = False
    
    def Run(self, gears, goal):
        self.goalState = goal
        self.CalcGearDisplacementValues(gears)
        result = self.HillClimbingSearch(gears)
        return result

    def CalcGearDisplacementValues(self, gears):
        self.displacementValues = [0] * len(gears)
        for gear in range(len(gears)):
            for gear2 in range(len(gears)):
                self.displacementValues[gear] += gears[gear].rotations[gear2] if gear2 is not gear else 1

    def HillClimbingSearch(self, gears):
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
            if lowestHeuristicValue == 0.0:
                result.append(nextLevelIndex)
                break
            else:
                result.append(nextLevelIndex)
            gearCopy = nextLevel[nextLevelIndex]
        return result

    def calcHeuristicValue(self, gears):
        heuristic = 0
        heuristic2 = 0.0
        for index in range(len(gears)):
            turnsToGoal = self.simulateTurnToGoal(gears, index)
            #print(turnsToGoal)
            affectDivisor = self.GetEffectDivisor(turnsToGoal)
            #print(affectDivisor)
            heuristic2 += len(turnsToGoal) / affectDivisor
            print("{}:{}".format(index, len(turnsToGoal) / affectDivisor))
            value = self.goalState[index] - gears[index].position
            if value < 0:
               value += gears[0].max_position
            heuristic += value
        return heuristic2

    def GetEffectDivisor(self, turns):
        if len(turns) is not 0:
            average = 0
            for turn in turns:
                average += self.displacementValues[turn]
            average = average / len(turns)
            return average
        return 1

    def simulateTurnToGoal(self, gears, gearToGetToGoal):
        gearCopy = copy.deepcopy(gears)
        rotatedOrder = []
        while gearCopy[gearToGetToGoal].position is not gearCopy[gearToGetToGoal].goal:
            bestRotation = sys.maxsize
            bestRotationPos = gearToGetToGoal
            for gear in range(len(gearCopy)):
                loopCopy = copy.deepcopy(gearCopy)
                Gear.Rotate(loopCopy, gear)
                distanceFromGoal = loopCopy[gearToGetToGoal].goal - loopCopy[gearToGetToGoal].position
                if distanceFromGoal < 0:
                    distanceFromGoal += gears[0].max_position
                if distanceFromGoal < bestRotation:
                    bestRotation = distanceFromGoal
                    bestRotationPos = gear
            Gear.Rotate(gearCopy, bestRotationPos)
            rotatedOrder.append(bestRotationPos)
        return rotatedOrder
