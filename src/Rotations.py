from kivy.uix.listview import ListItemLabel


class DataItem(object):
    def __init__(self, text='', is_selected=False):
        self.text = text
        self.is_selected = is_selected


class Rotations(ListItemLabel):
    pass

