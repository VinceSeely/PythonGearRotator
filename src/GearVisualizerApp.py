from GearVisualizer import *

from kivy.app import App


class GearVisualizerApp(App):
    def build(self):
        return GearVisualizer()


if __name__ == "__main__":
    print("better GUI to come")
    gearApp = GearVisualizerApp()
    gearApp.run()
