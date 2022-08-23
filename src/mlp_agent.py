import json
from dataclasses import dataclass
import clize
from functools import partial

from flax import linen as nn
from flax.training import train_state
import jax
import jax.numpy as jnp
import numpy as np
import optax

from tqdm import tqdm

import sys

sys.path.append("src")

from sample_utils import MT10_ENV_NAMES, MT50_ENV_NAMES
from run_utils import float_list, str_list
import jax_utils
from eval_callbacks import SingleProcEvalCallbacks, EvalCallbacks
from datasets import single_env_dataset, grouped_env_dataset


def env_names_to_onehots(env_names, all_names=MT50_ENV_NAMES):
  return jax.nn.one_hot([all_names.index(env_name)
                         for env_name in env_names],
                        len(all_names))


class MLPAgent(nn.Module):
    def setup(self):
        self.layers = nn.Sequential(
            [
                nn.Dense(128),
                nn.relu,
                nn.Dense(128),
                nn.relu,
                nn.Dense(128),
                nn.relu,
                nn.Dense(64),
                nn.relu,
                nn.Dense(32),
                nn.relu,
                nn.Dense(4),
            ]
        )

    def __call__(self, env_names, low_dim):
        info = {}
        one_hots = env_names_to_onehots(env_names)
        inputs = jnp.concatenate([low_dim, one_hots], axis=-1)
        actions = self.layers(inputs)
        return actions, info

    def as_policy(self, env_name, state):
        return MLPAgentPolicy(env_name=env_name, state=state, agent=self)


@dataclass
class MLPAgentPolicy:

    env_name: str or None
    state: train_state.TrainState
    agent: MLPAgent

    def get_action(self, low_dim, env_name=None):
        env_name = env_name or self.env_name
        assert env_name
        actions, infos = self.get_actions(np.array([low_dim]), [env_name])
        return actions[0], {k: v[0] for (k, v) in infos.items()}

    def get_actions(self, observations, env_names):
        action, info = run_agent(self.state, tuple(env_names), observations)

        # for (k, v) in info.items():
        # print(k, v)

        return np.asarray(action), info


@partial(jax.jit, static_argnames=["env_names"])
def run_agent(state, env_names, observations):
    return state.apply_fn(state.params, env_names, observations)


@partial(jax.jit, static_argnames=["env_names"])
def apply_model(state, env_names, low_dim, targets):
    def loss_fn(params):
        actions, info = state.apply_fn(params, env_names, low_dim)
        loss = jnp.mean(optax.l2_loss(actions, targets))
        return loss, actions

    grad_fn = jax.value_and_grad(loss_fn, has_aux=True)
    (loss, actions), grads = grad_fn(state.params)
    return (
        grads,
        loss,
        {
            "actions_mean": jnp.mean(actions),
            "actions_var": jnp.var(actions),
        },
    )


def preprocess(batch):
    env_names = []
    observations = []
    actions = []
    for stack in batch:
        for data in stack:
            env_names.append(data["env_name"])
            observations.append(data["observation"])
            actions.append(data["action"])
    return (tuple(env_names), jnp.array(observations)), jnp.array(actions)


def zeroshot(
    *,
    train_envs: str_list = MT10_ENV_NAMES,
    test_envs: str_list = MT50_ENV_NAMES,
    seed=jax_utils.DEFAULT_SEED,
    n_timesteps=1e5,
    batch_size=4,
    noise_scale=0.1,
    out_file,
):
    agent = MLPAgent()
    callbacks = EvalCallbacks(
        seed, train_envs + test_envs, agent, output_filename=out_file
    )
    jax_utils.fit_model(
        agent,
        data,
        apply_model,
        "mlp_agent",
        batch_size=batch_size,
        preprocess=preprocess,
        seed=seed,
        n_epochs=1000,
        callbacks=callbacks,
        learning_rate=1e-5,
    )
    print("Done saving cache")


def fewshot(
    *,
    train_envs: str_list = MT10_ENV_NAMES,
    target_env: str,
    seed=jax_utils.DEFAULT_SEED,
    n_timesteps=1e5,
    fewshot_timesteps=500,
    language_space_mixing=True,
    out_file,
):
    agent = MLPAgent()
    callbacks = SingleProcEvalCallbacks(
        seed,
        [target_env],
        agent,
        base_infos={
            "target_task": target_env,
        },
        output_filename=out_file,
    )
    train_and_evaluate_fewshot_with_callbacks(
        callbacks=callbacks,
        agent=agent,
        train_envs=train_envs,
        target_env=target_env,
        seed=seed,
        n_timesteps=n_timesteps,
        fewshot_timesteps=fewshot_timesteps,
    )


def train_and_evaluate_fewshot_with_callbacks(
    *,
    callbacks,
    agent,
    train_envs: str_list = MT10_ENV_NAMES,
    target_env: str,
    seed=jax_utils.DEFAULT_SEED,
    n_timesteps=1e5,
    fewshot_timesteps=500,
):
    # batch_size is basically source_repeats[0] * train_envs + source_repeats[1]
    source_repeats = [2, 20]

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
        return (tuple(env_names), jnp.array(observations)), jnp.array(actions)

    base_data = grouped_env_dataset(envs=train_envs, n_timesteps=n_timesteps, seed=seed)
    target_data = single_env_dataset(
        env_name=target_env, n_timesteps=fewshot_timesteps, seed=seed
    )
    jax_utils.fit_model_multisource(
        model=agent,
        sources=[base_data, target_data],
        source_repeats=source_repeats,
        apply_model=apply_model,
        model_name=f"mlp_agent_fewshot_task={target_env}",
        preprocess=preprocess_fewshot,
        seed=seed,
        n_epochs=500,
        callbacks=callbacks,
        learning_rate=1e-5,
    )


if __name__ == "__main__":
    # import multiprocessing as mp

    # mp.set_start_method("spawn")
    clize.run(zeroshot, fewshot)
