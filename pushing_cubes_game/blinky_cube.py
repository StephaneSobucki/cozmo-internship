#!/usr/bin/env python3

import asyncio

import cozmo
from cozmo.lights import blue_light, Color, green_light, Light, red_light, white_light, off_light
from cozmo.util import degrees, distance_mm, radians, speed_mmps

import globals

yellow_light = Light(Color(name = 'yellow', rgb = (255, 255, 0)))

rainbow_colors = [blue_light, red_light, green_light, yellow_light]

class BlinkyCube(cozmo.objects.LightCube):
    '''Same as a normal cube, plus extra methods specific to Quick Tap.'''
    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
        self._chaser = None
        self.mistake = globals.mistakes[self.cube_id-1]
		    
    def start_light_chaser(self, pause_time):
        '''Rotates four colors around the cube light corners in a continuous loop.

        Args:
            pause_time (float): the time awaited before moving the rotating lights
        '''
        if self._chaser:
            raise ValueError('Light chaser already running')
        async def _chaser():
            while True:
                for i in range(4):
                    self.set_light_corners(*rainbow_colors)
                    await asyncio.sleep(pause_time, loop = self._loop)
                    light = rainbow_colors.pop(0)
                    rainbow_colors.append(light)
        self._chaser = asyncio.ensure_future(_chaser(), loop = self._loop)

    def stop_light_chaser(self):
        '''Ends the _chaser loop.'''
        if self._chaser:
            self._chaser.cancel()
            self._chaser = None
        self.set_lights_off()

    async def change_color(self):
        '''On cube tapping event or timeout, turn off blinking and change to 'color' the cube's lights.'''
        try: 
            evt_tapped = await self.wait_for_tap(timeout=15)
            if evt_tapped is not None:
                self.stop_light_chaser()
                if self.mistake:
                    color = green_light
                else:
                    color = red_light
                self.set_lights(color)
        except asyncio.TimeoutError:
            self.stop_light_chaser()
            if self.mistake:
                color = red_light
            else:
                color = green_light
            self.set_lights(color)


# Make sure World knows how to instantiate the BlinkyCube subclass
cozmo.world.World.light_cube_factory = BlinkyCube
