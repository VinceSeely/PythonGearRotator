from Gear import *
import random
import time
import csv
from HillClimbingSearch import *
from LimitedDepthFirstSearch import *
from AStarSearch import *


class testFrame():

    def GenerateGears(self):
            Gears = []
            numGears = random.randint(0, 45)
            numPositions = random.randint(0, 45)
            for entry in range(numGears):
                Gears.append(Gear.Gear(numPositions, numGears))
            return Gears

    def runSearch(self,search, Gears,searchtype):    
            goal = []
            for gear in Gears:
                goal.append(gear.goal)
            t0 = time.time()
            result = search.Run(Gears, goal)
            print("result Found")
            t1 = time.time()
            totalTime = t1 - t0
            #print to file
            with open('data.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
                if result is not None:
                    writer.writerow([result,len(result),totalTime,len(Gears),searchtype,Gears[0].max_position])
                else:
                    writer.writerow(["None",'',totalTime,len(Gears),searchtype])
                
    def run(self):
        with open('data.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(["turns","numTurns","time","numGears","type","positions"])
        for x in range(100):
            gears = self.GenerateGears()
            search = HillClimbingSearch()
            self.runSearch(search,gears, "Hill Climb")
            search = LimitedDepthFirstSearch()
            self.runSearch(search,gears, "LDFS")
            search = AStarSearch()
            self.runSearch(search,gears,"A*")



if __name__ ==  "__main__":    
    test = testFrame()
    test.run()
