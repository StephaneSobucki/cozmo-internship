#!/usr/bin/env python3

import asyncio

import cozmo
from cozmo.util import distance_mm, degrees, speed_mmps
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id

from blinky_cube import * 
import globals

'''Cozmo looks around and push cubes based on the game master input in the GUI.

After that the cubes with blink and the subject will have 15s to tap
on the cube(s) where he thinks Cozmo made a mistake.

The subject starts with 3 points. Tapping on the wrong cube or failing
to find a mistake grant minus 1 point.
'''

class PushingCubesGame():
    '''The game logic of Pushing Cubes.'''
    def __init__(self,robot: cozmo.robot.Robot):
        '''
        The constructor for PushingCubes class

        Parameters:
            robot (cozmo.robot.Robot): instance of the robot connected from run_program
        '''
        self._robot = robot 
        self._NUM_CUBES = 3 
        self._cube1 = self._robot.world.get_light_cube(cozmo.objects.LightCube1Id)
        self._cube2 = self._robot.world.get_light_cube(cozmo.objects.LightCube2Id)
        self._cube3 = self._robot.world.get_light_cube(cozmo.objects.LightCube3Id)
        self._cubes_seen = [False, False, False]
        self._starting_pose = None

    async def _push_cube(self, cube):
        '''Cozmo drives to a cube and push it.

        Args:
            cube(cozmo.objects.LightCube): a light cube
        '''
        await self._robot.dock_with_cube(cube, num_retries = 3).wait_for_completed()
        await self._robot.drive_straight(distance = distance_mm(80), speed = speed_mmps(80)).wait_for_completed()
        await self._robot.drive_straight(distance = distance_mm(-20), speed = speed_mmps(80)).wait_for_completed()
        await self._robot.turn_in_place(angle = degrees(180), speed = degrees(90)).wait_for_completed()
        await self._robot.go_to_pose(self._starting_pose).wait_for_completed()

    async def _action_on_cube(self, cube):
        '''Decide what to do with a cube based on game master GUI input.

        After that, the cube is set as seen.

        Args:
            cube(cozmo.objects.LightCube): a light cube
        '''
        if globals.push_cubes[cube.cube_id-1]:
            await self._push_cube(cube)
        self._cubes_seen[cube.cube_id-1] = True

    async def start(self):
        '''Defines the game execution.

        Cozmo looks for a cube and deals with it based on the game settings,
        then it goes back to its starting position and reiterates for each cube
        '''
        self._starting_pose = self._robot.pose
        cube_counter = 0
        while cube_counter < 3:
            look_around = self._robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
            while True:
                cube = await self._robot.world.wait_for_observed_light_cube(include_existing = False)
                if self._cubes_seen[cube.cube_id-1] is False:
                    break
            look_around.stop()
            cube_counter += 1
            await self._action_on_cube(cube)
        self._cube1.start_light_chaser(0.1)
        self._cube2.start_light_chaser(0.1)
        self._cube3.start_light_chaser(0.1)
        await asyncio.gather(self._cube1.change_color(),self._cube2.change_color(),self._cube3.change_color())
        await asyncio.sleep(5)



