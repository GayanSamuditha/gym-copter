'''
gym-copter Environment class with simplified physics

Copyright (C) 2019 Simon D. Levy

MIT License
'''

from gym_copter.envs.env import CopterEnv
from gym import spaces
import numpy as np

class CopterSimple(CopterEnv):
    '''
    A simplified copter class for Q-Learning.
    Observation space: one state only
    Action space:      motors=0 or motors=1
    Reward             altitude
    '''

    TIMEOUT = 1

    def __init__(self):

        CopterEnv.__init__(self)

        self.action_space = spaces.Discrete(2)

        self.observation_space = spaces.Discrete(1)

    def step(self, action):

        # Convert discrete action index to array of floating-point number values
        motors = [float(action)]*4

        # Call parent-class step() to do basic update
        state, reward, done, info = CopterEnv.step(self, motors)

        # Dynamics uses NED coordinates, so negate to get altitude
        altitude = -state[4]

        # Only one state; reward is altitude
        return 0, altitude, done, info

    def reset(self):
        CopterEnv.reset(self)
        return 0

