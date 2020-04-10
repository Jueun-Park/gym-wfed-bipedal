import gym
import numpy as np


class WfedBipedalEnv(gym.Env):
    def __init__(self, base_index):
        observation_space = gym.spaces.Box()  # TODO
        action_space = gym.spaces.Box(low=np.zeros((4,)), high=np.ones((4,)))

    def step(self, action):
        # action to weights
        # wfed with action
        # eval wfeded agent on selected bipedal env (selected by base index)
        # observation shaping and reward shaping
        pass

    def reset(self):
        pass

    def render(self):
        pass

    def close(self):
        pass

    def seed(self):
        pass
