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
    return state

  def epoch_end(self, state):
    return state

  def minibatch_start(self, state):
    return state

  def minibatch_end(self, state):
    return state

  def training_complete(self, state):
    return state


def fit_model(model, data, apply_model, model_name,
              preprocess,
              batch_size=16, n_epochs=5,
              seed=random.randrange(1000), learning_rate=1e-4,
              momentum=0.995, callbacks=FitCallbacks()):
  workdir = expanduser(f'~/data/fit_model={model_name}_seed={seed}')
  print('workdir:', workdir)
  summary_writer = tensorboard.SummaryWriter(workdir)
  summary_writer.hparams(dict(locals()))

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
    state = callbacks.epoch_start(state)
    first_step_in_epoch = True
    rng, minibatch_rng = jax.random.split(rng)
    for (minibatch, key) in approx_minibatches(minibatch_rng, data, batch_size):
      state = callbacks.minibatch_start(state)
      if step % 1000 == 0:
        save_params(workdir, step, state,
                    delete_prev=not first_step_in_epoch)
        first_step_in_epoch = False
      inputs, targets = preprocess(minibatch)
      grads, loss, infos = apply_model(state, inputs, targets)
      state = update_model(state, grads)
      for (k, v) in infos.items():
        summary_writer.scalar(k, v, step)
      summary_writer.flush()
      step += 1
      state = callbacks.minibatch_end(state)
    state = callbacks.epoch_end(state)
    save_params(workdir, epoch, state)
  state = callbacks.training_complete(state)

  return state
