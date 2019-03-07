from tkinter import *


class GUI:

    def __init__(self):
        self.root = Tk()
        self.root.title("Gear Puzzle Solver")
        self.root.geometry('{}x{}'.format(500, 350))
        self.root.resizable(width=False, height=False)
        # self.root.protocol("WM_DELETE_WINDOW", self.closing)

        self.gearValues = Listbox(self.root, width=20, height=20)
        self.gearValues.pack(side=LEFT, padx=10)

        self.infoPanel = Frame(self.root)

        self.turnsLabel = Label(self.infoPanel, text="Turn order:", width=30, anchor=W)
        self.turnsList = Label(self.infoPanel, text="N/A", width=30, anchor = W)
        self.turnsLabel.pack(side=TOP)
        self.turnsList.pack(side=TOP)

        self.timeLabel = Label(self.infoPanel, text="Time Elapsed:", width=30, anchor=W)
        self.timeText = Label(self.infoPanel, text="N/A", width=30, anchor=W)
        self.timeLabel.pack(side=TOP)
        self.timeText.pack(side=TOP)

        self.infoPanel.pack(side=LEFT)

        self.buttonPanel = Frame(self.root)

        self.idfsButton = Button(self.buttonPanel, text="Iterative Depth First", width=20)
        self.idfsButton.pack(side=TOP)

        self.aStarButton = Button(self.buttonPanel, text="A*", width=20)
        self.aStarButton.pack(side=TOP)

        self.bfsButton = Button(self.buttonPanel, text="Best First", width=20)
        self.bfsButton.pack(side=TOP)

        self.buttonPanel.pack(side=LEFT)


if __name__ == "__main__":
    tk = GUI()
    tk.root.mainloop()
    
    # tk.initBindings
