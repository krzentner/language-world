import json
from dataclasses import dataclass

from torch.nn.modules import loss
import clize
from functools import partial

import torch
from torch import nn
from torch.nn import functional as F
import numpy as np

from tqdm import tqdm

# import sys

# sys.path.append("src")

import sample_utils
from sample_utils import MT10_ENV_NAMES, MT50_ENV_NAMES
from run_utils import float_list, str_list
import pytorch_utils
from eval_callbacks import SingleProcEvalCallbacks, EvalCallbacks, RayEvalCallbacks
from datasets import single_env_dataset, grouped_env_dataset
from embed_prompt import embed_action
from generate_mt10_plans import MT50_TASK_DESCRIPTIONS

from lightning.pytorch import LightningModule

class MLPAgent(LightningModule):

    def __init__(self, use_language_embedding: bool = True):
        super().__init__()
        self.use_language_embedding = use_language_embedding
        self.layers = nn.Sequential(
            nn.LazyLinear(128),
            nn.ReLU(),
            nn.LazyLinear(128),
            nn.ReLU(),
            nn.LazyLinear(128),
            nn.ReLU(),
            nn.LazyLinear(64),
            nn.ReLU(),
            nn.LazyLinear(32),
            nn.ReLU(),
            nn.LazyLinear(4),
        )
        if self.use_language_embedding:
            self.language_reencoder = nn.Sequential(
                nn.LazyLinear(64),
                nn.ReLU(),
                nn.LazyLinear(64),
                nn.ReLU(),
                nn.LazyLinear(64),
            )
        else:
            self.language_reencoder = nn.ReLU()

@dataclass
class MLPAgentPolicy:

    env_name: str or None
    agent: MLPAgent

    def get_action(self, low_dim, env_name=None):
        env_name = env_name or self.env_name
        assert env_name
        actions, infos = self.get_actions(np.array([low_dim]), [env_name])
        return actions[0], {k: v[0] for (k, v) in infos.items()}

    def get_actions(self, observations, env_names=None):
        if env_names is None:
            env_names = [self.env_name] * len(observations)
        if self.agent.use_language_embedding:
            task_reprs = torch.stack(
                [
                    torch.as_tensor(embed_action(MT50_TASK_DESCRIPTIONS[env_name]))
                    for env_name in env_names
                ]
            )
        else:
            task_reprs = pytorch_utils.env_names_to_onehots(env_names)
        with torch.no_grad():
            action, info = self.agent(
                task_reprs,
                torch.as_tensor(np.asarray(observations), dtype=torch.float32),
            )

        return np.asarray(action), info
