

and write your code underneath.
"""

import random
import numpy as np
from collections import Counter
import copy

from robot_lang import RobotLanguage, RobotLanguageEnv
from functools import partial

from . import data

class Task:
    def __init__(self, name, env=None,
                 task_desc=None, task_desc_raw=None, raw_goal=None,
                 train_scenes=None, val_scenes=None, test_scenes=None, 
                 sample_goal_size=1, num_repeats=None,
                 task_fns=None):
        self.name = name
        self.env = env
        self.task_desc = task_desc
        self.task_desc_raw = task_desc_raw
        self.raw_goal = raw_goal
        self.train_scenes = train_scenes
        self.val_scenes = val_scenes
        self.test_scenes = test_scenes
        self.sample_goal_size = sample_goal_size
        self.num_repeats = num_repeats or (1 if env is None else env.max_steps//(len(train_scenes)+1))
        self.task_fns = task_fns or []
        assert len(self.task_fns) > 0

    def sample_goal(self, rand_state=None, batch_size=None):
        if rand_state is not None:
            rand_state = copy.deepcopy(rand_state)
        return sample_scenes(env=self.env, goal=self.raw_goal,
                             scenes=self.train_scenes,
                             batch_size=batch_size,
                             rand_state=rand_state,
                             sample_goal_size=self.sample_goal_size,
                             goal_selection_fn=lambda e,gs: self.task_desc(e, gs)[0].item() > .5)

    def reset_environment(self, env):
        if env is None:
            return None
        env.reset(start_state=None,
                  goal_state=self.raw_goal,
                  train_scenes=self.train_scenes,
                  sample_goal_size=self.sample_goal_size)

    def sample_step_fn(self, state, goal, step_idx):
        return sample_step(self.env,
                           state, goal,
                           task_fns=self.task_fns,
                           step_idx=step_