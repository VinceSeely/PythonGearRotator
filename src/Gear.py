import random


class Gear:
    def random_stats(self, max_position):
        self.position = random.randint(0, max_position)
        self.goal = random.randint(0, max_position)
        self.max_position = max_position

    def __init__(self, max_position, current_position=None, goal_position=None):
        self.position = current_position
        self.goal = goal_position
        self.max_position = max_position
        if current_position is None or goal_position is None:
            self.random_stats(max_position)

    def turn(self, times):
        self.position = (self.position + times) % self.max_position

    def get_goal(self):
        return self.goal + 1

    def get_position(self):
        return self.position + 1


