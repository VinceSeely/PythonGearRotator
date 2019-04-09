import random
import GearManager
import time
import csv
from HillClimbingSearch import *
from LimitedDepthFirstSearch import *
from AStarSearch import *


class testFrame():

    def __init__(self):
        self.GearManager = GearManager.GearManager([],[])

    def GenerateGears(self):
            numGears = random.randint(1, 45)
            numPositions = random.randint(1, 45)
            self.GearManager.generate_random_gears(numGears, numPositions)

    def runSearch(self,search, searchtype):
            t0 = time.time()
            result = search.Run(self.GearManager)
            print("result Found")
            t1 = time.time()
            totalTime = t1 - t0
            #print to file
            with open('data.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
                numberOfGears = len(self.GearManager.get_copy_of_gears())
                if result is not None:
                    writer.writerow([result, len(result), totalTime, numberOfGears, searchtype,
                                     self.GearManager.totalPositions])
                else:
                    writer.writerow(["None", '', totalTime, numberOfGears, searchtype])
                
    def run(self):
        with open('data.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(["turns","numTurns","time","numGears","type","positions"])
        for x in range(100):
            self.GenerateGears()
            search = HillClimbingSearch()
            self.runSearch(search, "Hill Climb")
            search = LimitedDepthFirstSearch()
            self.runSearch(search, "LDFS")
            search = AStarSearch()
            self.runSearch(search,"A*")



if __name__ ==  "__main__":    
    test = testFrame()
    test.run()
