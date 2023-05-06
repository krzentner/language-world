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
from constants import MT10_ENV_NAMES, MT50_ENV_NAMES
from run_utils import float_list, str_list
import pytorch_utils
from eval_callbacks import SingleProcEvalCallbacks, EvalCallbacks, RayEvalCallbacks
from datasets import single_env_dataset, grouped_env_dataset
from embed_prompt import embed_action
from generate_mt10_plans import MT50_TASK_DESCRIPTIONS


class MLPAgent(nn.Module):
    def __init__(self, use_language_embedding: bool):
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

    def forward(self, task_reprs, low_dim):
        if self.use_language_embedding:
            task_reprs = self.language_reencoder(task_reprs)
        info = {}
        inputs = torch.cat([low_dim, task_reprs], dim=-1)
        actions = self.layers(inputs)
        return actions, info

    def as_policy(self, env_name):
        return MLPAgentPolicy(env_name=env_name, agent=self)


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

        # for (k, v) in info.items():
        # print(k, v)

        return np.asarray(action), info


def loss_function(agent, env_names, low_dim, targets):
    actions, info = agent(env_names, low_dim)
    loss = F.mse_loss(actions, targets)
    return (
        loss,
        {
            "actions_mean": torch.mean(actions),
            "actions_var": torch.var(actions),
        },
    )


def zeroshot(
    *,
    train_envs: str_list = MT10_ENV_NAMES,
    test_envs: str_list = MT50_ENV_NAMES,
    seed=sample_utils.DEFAULT_SEED,
    n_timesteps=int(1e5),
    batch_size=4,
    use_noise=True,
    out_file,
):
    print("Gathering training dataset")
    if use_noise:
        data = grouped_env_dataset(envs=train_envs, n_timesteps=n_timesteps, seed=seed)
    else:
        data = grouped_env_dataset(
            envs=train_envs, n_timesteps=n_timesteps, seed=seed, noise_scales=[0.0]
        )
    agent = MLPAgent(use_language_embedding=True)

    def preprocess(batch):
        env_names = []
        observations = []
        actions = []
        for stack in batch:
            for data in stack:
                env_names.append(data["env_name"])
                observations.append(data["observation"])
                actions.append(data["action"])
        task_reprs = torch.stack(
            [
                torch.as_tensor(embed_action(MT50_TASK_DESCRIPTIONS[env_name]))
                for env_name in env_names
            ]
        )
        return (
            task_reprs,
            torch.tensor(np.asarray(observations), dtype=torch.float32),
        ), torch.tensor(np.asarray(actions), dtype=torch.float32)

    def create_model(example_inputs):
        with torch.no_grad():
            agent(*example_inputs)
        model = torch.jit.script(agent, example_inputs=[example_inputs])
        return model

    callbacks = RayEvalCallbacks(
        seed,
        test_envs,
        agent,
        output_filename=out_file,
        step_period=100,
    )
    pytorch_utils.fit_model(
        data=data,
        create_model=create_model,
        loss_function=loss_function,
        model_name="mlp_agent_zeroshot",
        batch_size=batch_size,
        preprocess=preprocess,
        seed=seed,
        n_epochs=1000,
        callbacks=callbacks,
        learning_rate=1e-5,
    )
    print("Done saving cache")


def train_and_evaluate_fewshot_with_callbacks(
    *,
    callbacks,
    agent,
    train_envs: str_list = MT10_ENV_NAMES,
    target_task: str,
    use_language_embedding,
    seed: int = sample_utils.DEFAULT_SEED,
    n_timesteps=int(1e5),
    fewshot_timesteps=500,
    use_noise=True,
):
    # batch_size is basically source_repeats[0] * train_envs + source_repeats[1]
    source_repeats = [2, 20]

    def create_model(example_inputs):
        with torch.no_grad():
            agent(*example_inputs)
        model = torch.jit.script(agent, example_inputs=[example_inputs])
        return model

    def preprocess_fewshot(batch):
        env_names = []
        observations = []
        actions = []
        base_stacks = batch[: source_repeats[0]]
        target_stack = batch[source_repeats[0] :]
        assert len(target_stack) == source_repeats[1]
        for stack in base_stacks + [target_stack]:
            for data in stack:
                env_names.append(data["env_name"])
                observations.append(data["observation"])
                actions.append(data["action"])
        if use_language_embedding:
            task_reprs = torch.stack(
                [
                    torch.as_tensor(embed_action(MT50_TASK_DESCRIPTIONS[env_name]))
                    for env_name in env_names
                ]
            )
        else:
            task_reprs = pytorch_utils.env_names_to_onehots(env_names)
        return (
            task_reprs,
            torch.tensor(np.asarray(observations), dtype=torch.float32),
        ), torch.tensor(np.asarray(actions), dtype=torch.float32)

    if use_noise:
        base_data = grouped_env_dataset(
            envs=train_envs, n_timesteps=n_timesteps, seed=seed
        )
        target_data = single_env_dataset(
            env_name=target_task, n_timesteps=fewshot_timesteps, seed=seed
        )
    else:
        base_data = grouped_env_dataset(
            envs=train_envs, n_timesteps=n_timesteps, seed=seed, noise_scales=[0.0]
        )
        target_data = single_env_dataset(
            env_name=target_task,
            n_timesteps=fewshot_timesteps,
            seed=seed,
            noise_scales=[0.0],
        )
    pytorch_utils.fit_model_multisource(
        create_model=create_model,
        sources=[base_data, target_data],
        source_repeats=source_repeats,
        loss_function=loss_function,
        model_name=f"mlp_agent_fewshot_task={target_task}",
        preprocess=preprocess_fewshot,
        seed=seed,
        n_epochs=500,
        callbacks=callbacks,
        learning_rate=1e-5,
    )


def oneshot(
    *,
    target_task: str,
    seed=sample_utils.DEFAULT_SEED,
    fewshot_timesteps=500,
    use_noise=False,
    use_language_embedding=True,
    out_file,
):
    def preprocess_oneshot(batch):
        env_names = []
        observations = []
        actions = []
        for data in batch:
            env_names.append(data["env_name"])
            observations.append(data["observation"])
            actions.append(data["action"])
        if use_language_embedding:
            task_reprs = torch.stack(
                [
                    torch.as_tensor(embed_action(MT50_TASK_DESCRIPTIONS[env_name]))
                    for env_name in env_names
                ]
            )
        else:
            task_reprs = pytorch_utils.env_names_to_onehots(env_names)
        return (
            task_reprs,
            torch.tensor(observations, dtype=torch.float32),
        ), torch.tensor(actions, dtype=torch.float32)

    agent = MLPAgent(use_language_embedding=use_language_embedding)

    def create_model(_example_inputs):
        return agent

    callbacks = SingleProcEvalCallbacks(
        seed,
        [target_task],
        agent,
        base_infos={
            "target_task": target_task,
        },
        output_filename=out_file,
        step_period=100,
    )
    batch_size = 32

    if use_noise:
        target_data = single_env_dataset(
            env_name=target_task, n_timesteps=fewshot_timesteps, seed=seed
        )
    else:
        target_data = single_env_dataset(
            env_name=target_task,
            n_timesteps=fewshot_timesteps,
            seed=seed,
            noise_scales=[0.0],
        )
    epoch_mult = int(9091 / 16)
    print(f"Running for {500 * epoch_mult} epochs")
    callbacks.step_period = callbacks.step_period * epoch_mult
    print(f"Eval every {callbacks.step_period} epochs")
    pytorch_utils.fit_model(
        create_model=create_model,
        data=target_data,
        batch_size=batch_size,
        loss_function=loss_function,
        model_name=f"mlp_agent_real_oneshot_task={target_task}_language_embed={use_language_embedding}",
        preprocess=preprocess_oneshot,
        seed=seed,
        n_epochs=500 * epoch_mult,
        callbacks=callbacks,
        learning_rate=1e-5,
    )


if __name__ == "__main__":
    # import multiprocessing as mp

    # mp.set_start_method("spawn")
    clize.run(zeroshot, oneshot)
