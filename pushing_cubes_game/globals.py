#!/usr/bin/env python3
'''Use global variables to share data between the GUI and the pushing cubes game.

error defines whether or not Cozmo is making a mistake (False: no mistake).
push_cubes defines whether or not Cozmo will push each cube (False: doesn't push).
'''
def initialize():
    global push_cubes, mistakes
    mistakes = [False, False, False]
    push_cubes = [False, False, False]
