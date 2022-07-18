import numpy as np
import jax
import tensorflow as tf
from tqdm import tqdm
import math
import os


def gen():
  for i in range(100):
    yield i, [1, 2, 3]


def approx_minibatches(key, dataset, batch_size, epoch_size=None):
  n_data_points = len(dataset)
  if epoch_size is None:
    epoch_size = n_data_points
  n_batches = int(math.ceil(epoch_size / batch_size))
  for _ in tqdm(range(n_batches)):
    key, next_key = random.split(key)
    indices = jax.random.randint(key, (batch_size,), 0, n_data_points)
    yield ([dataset[i] for i in indices], key)
    key = next_key

LAST_SAVED_PARAMS_STEP = {}

def save_params(workdir, step, state, delete_prev=True):
  with open(f'{workdir}/{step}.pkl', 'wb') as f:
    pickle.dump(state.params, f)
  if delete_prev:
    try:
      if workdir in LAST_SAVED_PARAMS_STEP:
        last_step = LAST_SAVED_PARAMS_STEP[workdir]
        os.remove(f'{workdir}/{last_step}.pkl')
    except FileNotFoundError:
      pass
  LAST_SAVED_PARAMS_STEP[workdir] = step


def fit_model(model, data, apply_model, work_dir, batch_size=16, n_epochs=5,
              seed=np.random.randrange(1000), learning_rate=1e-4, momentum=0.99):
  summary_writer = tensorboard.SummaryWriter(workdir)
  summary_writer.hparams(dict(locals()))

  @jax.jit
  def update_model(state, grads):
    return state.apply_gradients(grads=grads)

  rng = jax.random.PRNGKey(seed)

  rng, init_rng = jax.random.split(rng)
  params = model.init(init_rng, data[0])
  tx = optax.sgd(learning_rate, momentum)

  state = train_state.TrainState.create(
      apply_fn=model.apply, params=params, tx=tx)

  step = 0
  for epoch in range(n_epochs):
    print('Beginning epoch', epoch)
    first_step_in_epoch = True
    for (minibatch, key) in approx_minibatches(rng, data, batch_size):
      if step % 100 == 0:
        save_params(workdir, epoch, state,
                    delete_prev=not first_step_in_epoch)
        first_step_in_epoch = False
      grads, loss, infos = apply_model(state, minibatch)
      state = update_model(state, grads)
      for (k, v) in infos.items():
        summary_writer.scalar(k, v, step)
      summary_writer.flush()
      step += 1
    save_params(workdir, epoch, state)

  return state
