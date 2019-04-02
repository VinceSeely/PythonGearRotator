import random


class Gear():
    def __init__(self, max_pos, total_gears):
        self.min_turn = 0
        self.max_turn = 4
        if max_pos < self.max_turn:
            self.max_turn = 1
        self.position = random.randint(0, max_pos)
        self.goal = random.randint(0, max_pos)
        self.max_position = max_pos
        self.rotations = self.random_gears(total_gears)

    def random_gears(self, total_gears):
        other_gear_rotations = []
        for x in range(total_gears):
            other_gear_rotations.append(random.randint(self.min_turn, self.max_turn))
        return other_gear_rotations

    def turn(self, times):
        self.position = (self.position + times) % self.max_position

    def get_position(self):
        return self.position + 1

def Rotate (gearCopy, gearRotating):
    gearCopy[gearRotating].turn(1)
    for gear in range(len(gearCopy)):
        if gear is not gearRotating:
            gearCopy[gear].turn(gearCopy[gearRotating].rotations[gear])
