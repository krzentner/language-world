import collections

import clize
import os
from pprint import pprint
import random
from flax import linen as nn
from flax.metrics import tensorboard
from flax.training import train_state
import jax
import jax.numpy as jnp
import ml_collections
import numpy as np
import optax
import pickle
from tqdm import tqdm

import easy_process
from sample_utils import make_env, MT50_ENV_NAMES, sample_policy_with_noise_process
from run_utils import float_list, str_list
from ou_process import OUProcess
import jax_utils
import jax.numpy as jnp
import generate_metaworld_scene_dataset

# generate_metaworld_scene_dataset.np = jnp
from generate_metaworld_scene_dataset import (
    describe_obs,
    enumerate_descriptors,
    eval_conditions,
)
from metaworld_universal_policy import SawyerUniversalV2Policy
import embed_prompt


class ConditionEvaluator(nn.Module):
    def setup(self):
        self.cond_encoder = nn.Sequential(
            [
                nn.Dense(256),
                nn.relu,
                nn.Dense(256),
                nn.relu,
                nn.Dense(256),
                nn.relu,
                nn.Dense(128),
                nn.relu,
                nn.Dense(64),
                nn.relu,
                nn.Dense(64),
            ]
        )
        self.state_encoder = nn.Sequential(
            [
                nn.Dense(128),
                nn.relu,
                nn.Dense(128),
                nn.relu,
                nn.Dense(128),
                nn.relu,
                nn.Dense(128),
                nn.relu,
                nn.Dense(64),
                nn.relu,
                nn.Dense(64),
            ]
        )

    def __call__(self, low_dim, conditions, conditions_mask):
        conditions_enc = self.cond_encoder(conditions)
        state_enc = self.state_encoder(low_dim)
        base_results = jnp.einsum("ijkx,ix->ijk", conditions_enc, state_enc)
        conditions_weights = conditions_mask / conditions_mask.sum(
            axis=-1, keepdims=True
        )
        conjunction_results = jnp.einsum(
            "ijk,ijk->ij", base_results, conditions_weights
        )
        return conjunction_results


@jax.jit
def apply_model(state, low_dim, conditions, conditions_mask, targets):
    def loss_fn(params):
        logits = state.apply_fn(params, low_dim, conditions, conditions_mask)
        loss = jnp.mean(
            optax.sigmoid_binary_cross_entropy(
                jnp.stack([logits, -logits], axis=-1),
                jnp.stack([targets, 1 - targets], axis=-1),
            )
        )
        return loss, logits

    grad_fn = jax.value_and_grad(loss_fn, has_aux=True)
    (loss, logits), grads = grad_fn(state.params)
    accuracy = jnp.mean(targets * (logits > 0) + (1 - targets) * (logits < 0))
    return (
        grads,
        loss,
        {
            "accuracy": accuracy,
            "mean_truth_value": jnp.mean(logits),
            "var_truth_value": jnp.var(logits),
            "mean_abs_truth_values": jnp.mean(jnp.abs(logits)),
        },
    )


@easy_process.subprocess_func
def sample_process(*, env_name: str, noise_scales: [float], seed: int, parent):
    env = make_env(env_name, seed)
    policy = SawyerUniversalV2Policy(env_name=env_name)

    while True:
        random.shuffle(noise_scales)
        for noise_scale in noise_scales:
            ou_proc = OUProcess(dimensions=env.action_space.shape[0], sigma=noise_scale)
            episode = []
            found_nan = False
            for data in sample_policy_with_noise_process(env, policy, ou_proc):
                data["env_name"] = env_name
                data["noise_scale"] = noise_scale
                for (k, v) in data.items():
                    if isinstance(v, np.ndarray) and np.isnan(v).any():
                        print(f"Found NaN in {k!r}")
                        found_nan = True
                if found_nan:
                    break
                episode.append(data)
            if not found_nan:
                parent.sendrecv(episode)


DISC_DIM = 512


def worker_dataset(
    *,
    envs: str_list = MT50_ENV_NAMES,
    n_timesteps=1000,
    seed=jax_utils.DEFAULT_SEED,
    noise_scales: float_list = [0.1, 0.2, 0.3, 0.4],
):
    with easy_process.Scope():
        workers = [
            sample_process(env_name=env_name, seed=seed, noise_scales=noise_scales)
            for env_name in envs
        ]
        datapoints = []
        with tqdm(total=n_timesteps) as pbar:
            while len(datapoints) < n_timesteps:
                for worker in workers:
                    episode = worker.recv(block=False)
                    if episode:
                        datapoints.extend(episode)
                        pbar.update(len(episode))
    return datapoints


DESCRIPTOR_LISTS = {
    env_name: enumerate_descriptors(env_name) for env_name in MT50_ENV_NAMES
}

BASE_DESCRIPTOR_LISTS = {
    env_name: tuple([desc for desc in descriptors if " and " not in desc])
    for (env_name, descriptors) in DESCRIPTOR_LISTS.items()
}


def dup_to_len(descs, desired_len):
    assert desired_len <= len(descs)
    if len(descs) < desired_len:
        return descs + random.choices(descs, desired_len - len(descs))
    else:
        return descs


jit_eval_conditions = jax.jit(eval_conditions, static_argnames=["env_name", "conds"])


def preprocess(batch):
    observations = []
    descriptors_embeddings = []
    descriptors_targets = []
    for data in batch:
        observation = data["observation"]
        env_name = data["env_name"]
        N = 512
        base_conditions = BASE_DESCRIPTOR_LISTS[env_name]
        base_conditions_embed = [
            [embed_prompt.embed_condition(text)] for text in base_conditions
        ]
        base_targets = jit_eval_conditions(env_name, base_conditions, observation)
        pairs = [
            [
                random.randrange(len(base_conditions)),
                random.randrange(len(base_conditions)),
            ]
            for _ in range(512 - len(base_conditions))
        ]
        descriptors_embedded = base_conditions_embed + [
            [base_conditions_embed[i][0], base_conditions_embed[j][0]]
            for (i, j) in pairs
        ]
        targets = jnp.concatenate(
            [
                base_targets,
                jnp.array([base_targets[i] * base_targets[j] for (i, j) in pairs]),
            ]
        )
        observations.append(observation)
        descriptors_embeddings.append(descriptors_embedded)
        descriptors_targets.append(targets)
    obs_batch = np.stack(observations)
    assert len(obs_batch.shape) == 2
    assert obs_batch.shape[0] == len(descriptors_embeddings)
    descriptors_padded, desc_mask = jax_utils.pad_list_nd(descriptors_embeddings, 3)
    targets_padded, targets_mask = jax_utils.pad_list_nd(descriptors_targets, 2)
    return (obs_batch, descriptors_padded, desc_mask), targets_padded


def train_evaluator(
    *,
    envs: str_list = MT50_ENV_NAMES,
    n_epochs=50,
    n_timesteps=int(1e6),
    seed=jax_utils.DEFAULT_SEED,
    noise_scales: float_list = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],
    out_file,
):
    print("Gathering dataset:")
    data = worker_dataset(
        envs=envs, n_timesteps=n_timesteps, seed=seed, noise_scales=noise_scales
    )
    cond_evaluator = ConditionEvaluator()
    state = jax_utils.fit_model(
        cond_evaluator,
        data,
        apply_model,
        "evaluator",
        batch_size=4,
        preprocess=preprocess,
        seed=seed,
    )
    embed_prompt.save_cache()
    with open(out_file, "wb") as f:
        pickle.dump(state.params, f)


if __name__ == "__main__":
    clize.run(train_evaluator)
