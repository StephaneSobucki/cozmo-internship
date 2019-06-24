#!/usr/bin/env python3

import asyncio

import cozmo
from tkinter import *

from pushing_cubes_game import *
import globals

async def cozmo_program(robot: cozmo.robot.Robot):
    await PushingCubesGame(robot).start()

class GuiApp():
    '''The GUI is used to change the settings of our game.'''
    def __init__(self,master):
        self._canvas = Canvas(width = 400, height = 150)
        self._canvas.pack()
        
        self._frame = Frame(master)
        self._frame.pack()
        
        self._init_ui(master)

    def _add_checkbuttons(self):
        '''Add checkbuttons to the UI that acts like switch (checked = 1, unchecked = 0).'''
        self._cube1_value = IntVar()
        self._cube1_checkbutton = Checkbutton(self._frame, text="Cube 1", variable = self._cube1_value, onvalue = 1, offvalue = 0, command = self._on_check)
        self._cube1_checkbutton.grid(row=0, column=0)

        self._cube1_value2 = IntVar()
        self._cube1_checkbutton2 = Checkbutton(self._frame, text="Mistake", variable = self._cube1_value2, onvalue = 1, offvalue = 0, command = self._on_check)
        self._cube1_checkbutton2.grid(row=1, column=0)

        self._cube2_value = IntVar()
        self._cube2_checkbutton = Checkbutton(self._frame, text="Cube 2", variable=self._cube2_value, onvalue=1, offvalue=0, command = self._on_check)
        self._cube2_checkbutton.grid(row=0, column=1)
        
        self._cube2_value2 = IntVar()
        self._cube2_checkbutton2 = Checkbutton(self._frame, text="Mistake", variable = self._cube2_value2, onvalue = 1, offvalue = 0, command = self._on_check)
        self._cube2_checkbutton2.grid(row=1, column=1)

        self._cube3_value = IntVar()
        self._cube3_checkbutton = Checkbutton(self._frame, text="Cube 3", variable = self._cube3_value, onvalue = 1, offvalue = 0, command = self._on_check)
        self._cube3_checkbutton.grid(row=0, column=2)

        self._cube3_value2 = IntVar()
        self._cube3_checkbutton2 = Checkbutton(self._frame, text="Mistake", variable = self._cube3_value2, onvalue = 1, offvalue = 0, command = self._on_check)
        self._cube3_checkbutton2.grid(row=1, column=2)

    def _add_button(self, master):
        '''Trigger method _on_start when clicked on.'''
        self._button = Button(master,text = "Start")
        self._button.config(command = self._on_start)
        self._button.pack()

    def _add_canvas_images(self):
        self._cube1_img = PhotoImage(file = "images/cube1.png")
        self._canvas.create_image(20,20, anchor = 'nw',image=self._cube1_img)

        self._cube2_img = PhotoImage(file = "images/cube2.png")
        self._canvas.create_image(150, 20, anchor='nw', image=self._cube2_img)

        self._cube3_img = PhotoImage(file = "images/cube3.png")
        self._canvas.create_image(280, 20, anchor='nw', image=self._cube3_img)

    def _init_ui(self, master):
        self._add_checkbuttons()
        self._add_button(master)
        self._add_canvas_images()

    def _on_check(self):
        '''Update the value of push_cubes (resp. mistakes) when the state of a checkbutton associated with push_cubes (resp. mistakes) has been changed.'''
        globals.push_cubes[0] = self._cube1_value.get()
        globals.push_cubes[1] = self._cube2_value.get()
        globals.push_cubes[2] = self._cube3_value.get()

        globals.mistakes[0] = self._cube1_value2.get()
        globals.mistakes[1] = self._cube2_value2.get()
        globals.mistakes[2] = self._cube3_value2.get()

    def _on_start(self):
        '''Start the program when the button "start" has been clicked on.'''
        cozmo.run_program(cozmo_program)

