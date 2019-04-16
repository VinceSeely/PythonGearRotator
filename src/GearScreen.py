from GearManager import gear_manager_instance
from AStarSearch import *
from HillClimbingSearch import *
from LimitedDepthFirstSearch import *
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, ListProperty
from kivy.clock import Clock


class GearScreen(Screen):
    current_gear_positions = ObjectProperty()
    gear_turning = ObjectProperty()

    def on_enter(self, *args):
        if self.current_gear_positions is not None:
            self.current_gear_positions.text = gear_manager_instance.get_positions_string()

    def rotate_gear(self):
        rotating = int(self.gear_turning.text)
        gear_manager_instance.rotate(rotating)
        self.current_gear_positions.text = gear_manager_instance.get_positions_string()
