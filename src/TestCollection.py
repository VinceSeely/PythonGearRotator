import random
import GearManager
import time
import csv
from HillClimbingSearch import *
from LimitedDepthFirstSearch import *
from AStarSearch import *


class testFrame():

    def __init__(self):
        self.GearManager = GearManager.GearManager()

    def GenerateGears(self):
            numGears = 4
            numPositions = 9
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
                    writer.writerow(["".join(map(str, [x for x in result])), len(result), totalTime, numberOfGears, searchtype,
                                     self.GearManager.totalPositions])
                    return True
                else:
                    writer.writerow(["None", '', totalTime, numberOfGears, searchtype])
            return False
                
    def run(self):
        with open('data.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(["turns", "numTurns", "time", "numGears", "type", "positions"])
        for x in range(1000):
            self.GenerateGears()
            search = AStarSearch()
            result_exists = self.runSearch(search, "A*")
            self.runSearch(search, "LDFS")
            search = LimitedDepthFirstSearch()
            if result_exists:  # skips hill climb if there will be no result for it as hill climb will never finish
                self.runSearch(search, "Hill Climb")
                search = HillClimbingSearch()



if __name__ ==  "__main__":
    test = testFrame()
    test.run()
