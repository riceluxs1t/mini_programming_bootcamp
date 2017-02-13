from Tkinter import *
from view import GUI

class RockPaperScissorsController:
    def __init__(self, master):
        self.root = master
        self.view = GUI(self.root)

    def run(self):
        self.view.display()





class model2ViewAdapter:
    def __init__(self):
        pass

class view2ModelAdapter:
    def __init__(self):
        pass
