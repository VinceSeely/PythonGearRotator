import random
import kivy
import Gear

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.button import Label


class GearMainApp:
    def __init__(self):
        self.gears = []
        self.generate_gears(8)
        self.gearChanger = GearChanger()

    def generate_gears(self, number_of_gears):
        for x in range(number_of_gears):
            self.gears.append(Gear(random.randint(0, 100), number_of_gears))
        print(self.gears)


class GearChanger(App):
    def build(self):
        return Label()


gearApp = GearChanger()
gearApp.run()
