import numpy as np
import jax
from flax.metrics import tensorboard
from flax.training import train_state
from tqdm import tqdm
import math
import os
import random
import optax
import pickle
from os.path import expanduser
import jax.numpy as jnp


def pad_list(seq, max_len=None):
    if max_len is None:
        max_len = max(len(s) for s in seq)
    zero = jnp.zeros(seq[0][0].shape)
    padded = jnp.array(
        [[s[i] if len(s) > i else zero for i in range(max_len)] for s in seq]
    )
    mask = jnp.array([[1 if len(s) > i else 0 for i in range(max_len)] for s in seq])
    return padded, mask

def find_max_lens(seq):
  if isinstance(seq, list):
    sub_max_lens = [find_max_lens(s) for s in seq]
    max_lens = sub_max_lens[0]
    for sub_max in sub_max_lens:
      # We don't handle different levels of dimensions
      assert len(sub_max_lens[0]) == len(sub_max)
      for (i, m_len) in enumerate(sub_max):
        if m_len > max_lens[i]:
          max_lens[i] = m_len
    return [len(seq)] + max_lens
  else:
    return list(seq.shape)

def pad_list_nd_inner(seq, target_lens, mask_shape):
  if isinstance(seq, list):
    sub_padded, sub_mask = zip(*[pad_list_nd_inner(s, target_lens[1:], mask_shape[1:])
                                 for s in seq])
    sub_padded = jnp.array(sub_padded)
    sub_mask = jnp.array(sub_mask)
  else:
    sub_padded = seq
    if mask_shape:
      sub_mask = jnp.ones([len(seq)] + mask_shape[1:])
    else:
      sub_mask = jnp.ones(())
  if len(sub_padded) < target_lens[0]:
    # If we're not supposed to be masking at this depth, something has probably
    # gone wrong
    assert mask_shape
    len_diff = target_lens[0] - len(sub_padded)
    sub_padded = jnp.concatenate(
        [sub_padded, jnp.zeros([len_diff] + target_lens[1:])])
    sub_mask = jnp.concatenate(
        [sub_mask, jnp.zeros([len_diff] + mask_shape[1:])])
  return sub_padded, sub_mask

def pad_list_nd(seq, mask_depth):
  max_lens = find_max_lens(seq)
  mask_shape = max_lens[:mask_depth]
  padded, mask = pad_list_nd_inner(seq, max_lens, mask_shape)
  return padded, mask


def pad_list_single_pass(seq, new_len=None):
  if isinstance(seq[0], list):
    max_len = max(len(s) for s in seq)
    seq_padded = []
    seq_mask = []
    for (s_padded, s_mask) in (pad_list_nd(s, max_len) for s in seq):
      seq_padded.append(s_padded)
      seq_mask.append(s_mask)
    return jnp.array(seq_padded), jnp.array(seq_mask)
  else:
    zero = jnp.zeros(seq[0])
    padded = jnp.array(
        [seq[i] if len(seq) > i else zero for i in range(max_len)]
    )
    mask = jnp.array([1 if len(seq) > i else 0 for i in range(max_len)])
    return padded, mask


def approx_minibatches(key, dataset, batch_size, epoch_size=None):
  n_data_points = len(dataset)
  if epoch_size is None:
    epoch_size = n_data_points
  n_batches = int(math.ceil(epoch_size / batch_size))
  for _ in tqdm(range(n_batches)):
    key, next_key = jax.random.split(key)
    indices = jax.random.randint(key, (batch_size,), 0, n_data_points)
    yield ([dataset[i] for i in indices], key)
    key = next_key


LAST_SAVED_PARAMS_STEP = {}


def save_params(workdir, step, state, delete_prev=True):
  # print(f'Saving params to {workdir}/{step}.pkl')
  with open(f'{workdir}/{step}.pkl', 'wb') as f:
    pickle.dump(state.params, f)
  if delete_prev:
    try:
      if workdir in LAST_SAVED_PARAMS_STEP:
        last_step = LAST_SAVED_PARAMS_STEP[workdir]
        if last_step != step:
          # print(f'Deleting old params from {workdir}/{last_step}.pkl')
          os.remove(f'{workdir}/{last_step}.pkl')
    except FileNotFoundError:
      pass
  LAST_SAVED_PARAMS_STEP[workdir] = step

class FitCallbacks:

  def epoch_start(self, state):
    return state, {}

  def epoch_end(self, state):
    return state, {}

  def minibatch_start(self, state):
    return state, {}

  def minibatch_end(self, state):
    return state, {}

  def training_complete(self, state):
    return state, {}

DEFAULT_SEED = random.randrange(1000)

def log_infos(summary_writer, infos, step):
    for (k, v) in infos.items():
      summary_writer.scalar(k, v, step)

def fit_model(model, data, apply_model, model_name,
              preprocess,
              batch_size=16, n_epochs=5,
              seed=DEFAULT_SEED, learning_rate=1e-4,
              momentum=0.995, callbacks=FitCallbacks()):
  workdir = expanduser(f'~/data/fit_model={model_name}_seed={seed}')
  print('workdir:', workdir)
  summary_writer = tensorboard.SummaryWriter(workdir)
  summary_writer.hparams({
      'learning_rate': learning_rate,
      'momentum': momentum,
      'seed': seed,
      'n_datapoints': len(data),
      'batch_size': batch_size,
      'n_epochs': n_epochs,
  })

  @jax.jit
  def update_model(state, grads):
    return state.apply_gradients(grads=grads)

  rng = jax.random.PRNGKey(seed)

  rng, init_rng = jax.random.split(rng)
  params = model.init(init_rng, *preprocess(data[:1])[0])
  tx = optax.sgd(learning_rate, momentum)

  state = train_state.TrainState.create(
      apply_fn=model.apply, params=params, tx=tx)

  step = 0
  for epoch in range(n_epochs):
    print('Beginning epoch', epoch)
    state, infos = callbacks.epoch_start(state)
    log_infos(summary_writer, infos, step)
    first_step_in_epoch = True
    rng, minibatch_rng = jax.random.split(rng)
    for (minibatch, key) in approx_minibatches(minibatch_rng, data, batch_size):
      state, infos = callbacks.minibatch_start(state)
      log_infos(summary_writer, infos, step)
      if step % 1000 == 0:
        save_params(workdir, step, state,
                    delete_prev=not first_step_in_epoch)
        first_step_in_epoch = False
      inputs, targets = preprocess(minibatch)
      grads, loss, infos = apply_model(state, *inputs, targets)
      state = update_model(state, grads)
      log_infos(summary_writer, infos, step)
      state, infos = callbacks.minibatch_end(state)
      log_infos(summary_writer, infos, step)
      summary_writer.flush()
      step += 1
    state, infos = callbacks.epoch_end(state)
    log_infos(summary_writer, infos, step)
    save_params(workdir, epoch, state)
    summary_writer.flush()
  state, infos = callbacks.training_complete(state)
  log_infos(summary_writer, infos, step)
  summary_writer.flush()

  return state
