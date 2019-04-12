from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, ListProperty
from GearManager import *
from AStarSearch import *
from HillClimbingSearch import *
from LimitedDepthFirstSearch import *
import time


class GearVisualizer(BoxLayout):
    number_of_gears = ObjectProperty()
    number_of_positions = ObjectProperty()
    time_taken = ObjectProperty()
    turns_done = ObjectProperty()
    turn_results = ObjectProperty()
    gear_initial_state = ObjectProperty()
    gear_goal_state = ObjectProperty()
    gear_manager = GearManager()
    data = []

    def execute_search(self, search):
        t0 = time.time()
        result = search.Run(self.gear_manager)
        t1 = time.time()
        self.turn_results.adapter.data = []
        if result is None:
            self.turns_done.text = "None"
        else:
            self.print_results(result)
            self.turns_done.text = ", ".join(map(str, [x + 1 for x in result]))
        self.time_taken.text = str(t1 - t0)

    def print_results(self, results):
        gearsCopy = self.gear_manager.get_copy_of_gears()
        for turn in results:
            gearsCopy = self.gear_manager.rotate_and_copy(gearsCopy, turn)
            self.turn_results.adapter.data.append("{}: {}".format(turn + 1, ", ".join(map(str, [x.get_position() for x in gearsCopy]))))

    def limited_depth_first_search(self):
        limited_depth_first = LimitedDepthFirstSearch()
        self.execute_search(limited_depth_first)

    def a_star(self):
        a_star_search = AStarSearch()
        self.execute_search(a_star_search)

    def hill_climb(self):
        hill_climb_search = HillClimbingSearch()
        self.execute_search(hill_climb_search)

    def generate_gears(self):
        number_of_gears = int(self.number_of_gears.text)
        number_of_positions = int(self.number_of_positions.text)

        self.gear_manager.generate_random_gears(number_of_gears, number_of_positions)
        self.gear_goal_state.text = self.gear_manager.get_goal_string()
        self.gear_initial_state.text = self.gear_manager.get_positions_string()

        self.time_taken.text = "N/A"
        self.turns_done.text = "N/A"

        self.turn_results.adapter.data = []
        pass
