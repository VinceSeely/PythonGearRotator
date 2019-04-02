from tkinter import *
from Gear import *
import time
from HillClimbingSearch import *
from LimitedDepthFirstSearch import *
from AStarSearch import *


class GUI:

    def __init__(self):
        self.root = Tk()
        self.root.title("Gear Puzzle Solver")
        self.root.geometry('{}x{}'.format(575, 400))
        self.root.resizable(width=False, height=False)
        self.root.wm_iconbitmap('..\images\gearlogo.ico')
        # self.root.protocol("WM_DELETE_WINDOW", self.closing)

        self.toolbar = Frame(self.root)

        self.numGearsLabel = Label(self.toolbar, text="Number of Gears:")
        self.numGearsEntry = Entry(self.toolbar, width=7)
        self.numGearsEntry.insert(END, '3')
        self.numGearsLabel.pack(side=LEFT, anchor=W)
        self.numGearsEntry.pack(side=LEFT, anchor=W)

        self.numPositionsLabel = Label(self.toolbar, text="Number of positions:")
        self.numPositionsEntry = Entry(self.toolbar, width=7)
        self.numPositionsEntry.insert(END, '9')
        self.numPositionsLabel.pack(side=LEFT, anchor=W)
        self.numPositionsEntry.pack(side=LEFT, anchor=W)
        self.generateButton = Button(self.toolbar, text="Generate", bg="#e50b83")
        self.generateButton.pack(side=LEFT, padx=10)

        self.matrixButton = Button(self.toolbar, text="Display Gear Turn Matrix", width=25)
        self.matrixButton.pack(side=LEFT, padx=10)

        self.toolbar.pack(side=TOP, anchor=W, padx=10)

        self.gearValues = Listbox(self.root, width=20, height=22)
        self.gearValues.pack(side=LEFT, padx=(10, 0))

        self.scrollbar = Scrollbar(orient="vertical")
        self.scrollbar.config(command=self.gearValues.yview)
        self.scrollbar.pack(side="left", fill="y", pady=10)
        # self.bottomScroll = Scrollbar(orient="horizontal")
        # self.bottomScroll.config(command=self.gearValues.yview)
        # self.bottomScroll.pack(side="left")

        self.gearValues.config(yscrollcommand=self.scrollbar.set)

        self.infoPanel = Frame(self.root)

        self.startingLabel = Label(self.infoPanel, text="Initial State: ", anchor=W, width=20)
        self.startState = Label(self.infoPanel, text="None", anchor=W, width=20, justify=LEFT, wraplength=150)
        self.startingLabel.pack(side=TOP)
        self.startState.pack(side=TOP)

        self.goalLabel = Label(self.infoPanel, text="Goal State: ", anchor=W, width=20)
        self.goalState = Label(self.infoPanel, text="None", anchor=W, width=20, justify=LEFT, wraplength=150)
        self.goalLabel.pack(side=TOP)
        self.goalState.pack(side=TOP)

        self.turnsLabel = Label(self.infoPanel, text="Turn order:", width=20, anchor=W)
        self.turnsList = Label(self.infoPanel, text="", width=20, anchor=W, justify=LEFT, wraplength=150)
        self.turnsLabel.pack(side=TOP)
        self.turnsList.pack(side=TOP)

        self.timeLabel = Label(self.infoPanel, text="Time Elapsed:", width=20, anchor=W)
        self.timeText = Label(self.infoPanel, text="N/A", width=20, anchor=W)
        self.timeLabel.pack(side=TOP)
        self.timeText.pack(side=TOP)

        self.infoPanel.pack(side=LEFT)

        self.buttonPanel = Frame(self.root)

        self.turnFrame = Frame(self.buttonPanel)

        self.gearTurnBox = Spinbox(self.turnFrame, from_=1, to=3, width=10)
        self.gearTurnBox.pack(side=LEFT,padx=10)

        self.rotateGear = Button(self.turnFrame, text="Rotate Gear", bg="red")
        self.rotateGear.pack(side=LEFT, padx=10)

        self.turnFrame.pack(side=TOP, pady=10)

        self.idfsButton = Button(self.buttonPanel, text="Iterative Depth First", width=20)
        self.idfsButton.pack(side=TOP, pady=10)

        self.hillClimbButton = Button(self.buttonPanel, text="Hill Climb", width=20)
        self.hillClimbButton.pack(side=TOP, pady=10)

        self.aStarButton = Button(self.buttonPanel, text="A*", width=20)
        self.aStarButton.pack(side=TOP, pady=10)

        self.buttonPanel.pack(side=LEFT, padx=20)
        gear1 = Gear.Gear(8, 3)
        gear2 = Gear.Gear(8, 3)
        gear3 = Gear.Gear(8, 3)
        gear1.goal = 6
        gear2.goal = 0
        gear3.goal = 5
        gear1.position = 2
        gear2.position = 0
        gear3.position = 0
        gear1.rotations = [1, 1, 1]
        gear2.rotations = [1, 1, 0]
        gear3.rotations = [0, 1, 1]

        gear1 = Gear.Gear(9, 3)
        gear2 = Gear.Gear(9, 3)
        gear3 = Gear.Gear(9, 3)
        gear1.goal = 7
        gear2.goal = 2
        gear3.goal = 7
        gear1.position = 7
        gear2.position = 0
        gear3.position = 8
        gear1.rotations = [1, 0, 0]
        gear2.rotations = [1, 0, 0]
        gear3.rotations = [1, 0, 1]

        self.Gears = [gear1, gear2, gear3]
        positions = ""
        for gear in self.Gears:
            positions += '{}, '.format(gear.get_position())
        self.goal = []
        for gear in self.Gears:
            self.goal.append(gear.goal)
        self.gearValues.delete(0, END)
        self.startState["text"] = positions[0:(len(positions) - 2)]
        self.goalState["text"] = ", ".join(map(str, [x + 1 for x in self.goal]))

    def initBindings(self):
        self.idfsButton.bind("<Button-1>", self.idfs_Handler)
        self.hillClimbButton.bind("<Button-1>", self.hillClimbing_Handler)
        self.aStarButton.bind("<Button-1>", self.aStar_Handler)
        self.generateButton.bind("<Button-1>", self.GenerateGears)
        self.matrixButton.bind("<Button-1>", self.DisplayMatrix)
        self.rotateGear.bind("<Button-1>", self.RotateGear)


        self.root.bind("i", self.idfs_Handler)
        self.root.bind("h", self.hillClimbing_Handler)
        self.root.bind("a", self.aStar_Handler)
        self.root.bind("g", self.GenerateGears)
        self.root.bind("m", self.DisplayMatrix)

    def RotateGear(self, button):
        Gear.Rotate(self.Gears, int(self.gearTurnBox.get()) - 1)        
        self.startState["text"] = self.getPositionsString(self.Gears)

    def GenerateGears(self, button):
        self.Gears = []
        numGears = int(self.numGearsEntry.get())
        numPositions = int(self.numPositionsEntry.get()) - 1
        self.gearTurnBox["to"] = numGears
        for entry in range(numGears):
            self.Gears.append(Gear.Gear(numPositions, numGears))
        self.goal = []
        for gear in self.Gears:
            self.goal.append(gear.goal)

        self.gearValues.delete(0, END)
        self.startState["text"] = self.getPositionsString(self.Gears)
        self.goalState["text"] = ", ".join(map(str, [x + 1 for x in self.goal]))

    def DisplayMatrix(self, button):
        window = Toplevel()
        window.wm_title("Gear Rotation Matrix")
        window.geometry('{}x{}'.format(300, 375))

        matixDisplay = Listbox(window)
        matixDisplay.pack(side=LEFT, padx=(10, 0), pady=10, expand=True, fill='both')

        matrixScrollbar = Scrollbar(window, orient="vertical")
        matrixScrollbar.config(command=matixDisplay.yview)
        matrixScrollbar.pack(side="left", fill="y", padx=(0,10), pady=10)
        
        
        matrix = []
        for x in self.Gears:
            matrix.append("[{}]".format(", ".join(map(str, [y for y in x.rotations]))))
        
        for turn in matrix:
           matixDisplay.insert(END, turn)


        


    def idfs_Handler(self, button):
        idfs = LimitedDepthFirstSearch()
        self.runAny(idfs)

    def runAny(self, methodToBeRun):
        t0 = time.time()
        result = methodToBeRun.Run(self.Gears, self.goal)
        t1 = time.time()        
        self.gearValues.delete(0, END)
        if result is None:
            self.turnsList['text'] = "None"
        else:
            self.printResults(result)
            self.turnsList['text'] = ", ".join(map(str, [x + 1 for x in result]))
        self.timeText['text'] = t1 - t0

    def printResults(self, results):
        gearsCopy = copy.deepcopy(self.Gears)
        for turn in results:
            Gear.Rotate(gearsCopy, turn)
            self.gearValues.insert(END, "{}: {}".format(turn + 1, self.getPositionsString(gearsCopy)))

    def getPositionsString(self, gearsCopy):
        gearPositions = ""
        for gear in gearsCopy:
            gearPositions += '{}, '.format(gear.get_position())
        return gearPositions[0:(len(gearPositions) - 2)]

    def hillClimbing_Handler(self, button):
        hillClimbing = HillClimbingSearch()
        self.runAny(hillClimbing)

    def aStar_Handler(self, button):
        astar = AStarSearch()
        self.runAny(astar)


if __name__ == "__main__":
    tk = GUI()
    tk.initBindings()
    tk.root.mainloop()
