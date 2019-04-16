import Gear
import random
import copy


class GearManager:
    def __init__(self, gears=None, rotations_configuration=None):
        self.gears = []
        self.gearRotationsMatrix = []
        self.totalPositions = 0
        if gears is not None and rotations_configuration is not None:
            self.gears = gears
            self.gearRotationsMatrix = rotations_configuration
            self.totalPositions = gears[0].max_position

    def generate_random_gears(self, number_of_gears, number_of_positions):
        self.gearRotationsMatrix = []
        self.gears = []
        self.totalPositions = number_of_positions
        for index in range(number_of_gears):
            self.gears.append(Gear.Gear(number_of_positions))
            self.gearRotationsMatrix.append(self._generate_random_rotations(number_of_gears, number_of_positions, index))

    def get_positions_string(self):
        positions = ""
        for gear in self.gears:
            positions += '{}, '.format(gear.get_position())
        return positions[0:(len(positions) - 2)]

    def get_matrix(self):
        return self.gearRotationsMatrix

    def get_positions(self):
        position = []
        for gear in self.gears:
            position.append(gear.position)
        return position

    def get_goal(self):
        goal = []
        for gear in self.gears:
            goal.append(gear.goal)
        return goal

    def get_goal_string(self):
        goal = ""
        for gear in self.gears:
            goal += '{}, '.format(gear.get_goal())
        return goal[0:(len(goal) - 2)]

    @staticmethod
    def _generate_random_rotations(total_gears, number_of_positions, gear_index):
        other_gear_rotations = []
        for x in range(total_gears):
            if x == gear_index:
                other_gear_rotations.append(1)
            else:
                other_gear_rotations.append(random.randint(0, number_of_positions))
        return other_gear_rotations

    def get_copy_of_gears(self):
        return copy.deepcopy(self.gears)

    def rotate_and_copy(self, gear_rotating):
        deep_copy = copy.deepcopy(self.gears)
        for gear in range(len(deep_copy)):
            deep_copy[gear].turn(self.gearRotationsMatrix[gear_rotating][gear])
        return deep_copy

    def rotate_and_copy(self, gears, gear_rotating):
        gearCopy = copy.deepcopy(gears)
        for gear in range(len(gearCopy)):
            gearCopy[gear].turn(self.gearRotationsMatrix[gear_rotating][gear])
        return gearCopy

    def rotate(self, gear_rotating):
        for gear in range(len(self.gears)):
            self.gears[gear].turn(self.gearRotationsMatrix[gear_rotating][gear])


gear_manager_instance = GearManager()
