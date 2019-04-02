from Gear import *
import random
import time
import csv
from HillClimbingSearch import *
from LimitedDepthFirstSearch import *
from AStarSearch import *

def GenerateGears():
        Gears = []
        numGears = random.randint(0, 45)
        numPositions = random.randint(0, 45)
        for entry in range(numGears):
            Gears.append(Gear.Gear(numPositions, numGears))
        return Gears

def runSearch(search, Gears):    
        goal = []
        for gear in Gears:
            goal.append(gear.goal)
        t0 = time.time()
        result = search.Run(Gears, goal)
        t1 = time.time()
        totalTime = t1 - t0
        #print to file
        with open('data.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, demlimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        if result is not None:
            writer.writerow([result,len(result),time])
        else:
            writer.writerow(["None",'',time])



if __name__ ==  "__main__":    
    with open('data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, demlimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["turns","numTurns","time"])
    for x in range(100):
        gears = GenerateGears()
        search = HillClimbingSearch()
        runSearch(search,gears)
        search = LimitedDepthFirstSearch()
        runSearch(search,gears)
        search = AStarSearch()
        runSearch(search,gears)
        