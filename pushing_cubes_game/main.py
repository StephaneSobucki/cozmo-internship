#!/usr/bin/env python3

from tkinter import *

import globals
from pushing_cubes_game import *
from gui_app import *


def launch():
    root = Tk()
    root.title("Pushing Cubes Game")
    root.resizable(width=FALSE, height=FALSE)
    GuiApp(root)
    root.mainloop()

if __name__ == '__main__':
    globals.initialize()
    launch()
