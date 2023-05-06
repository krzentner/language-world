import numpy as np
import torch
from torch import nn
from torch.nn import functional as F

# from torch.utils import tensorboard
import tensorboardX
from tqdm import tqdm
import math
import os
import pickle
from os.path import expanduser
import sample_utils
from constants import MT10_ENV_NAMES, MT50_ENV_NAMES, N_EPOCHS


def pad_list(seq, max_len=None):
    if max_len is None:
        max_len = max(len(s) for s in seq)
    zero = torch.zeros(seq[0][0].shape)
    padded = torch.tensor(
        [[s[i] if len(s) > i else zero for i in range(max_len)] for s in seq]
    )
    mask = torch.tensor([[1 if len(s) > i else 0 for i in range(max_len)] for s in seq])
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
        sub_padded, sub_mask = zip(
            *[pad_list_nd_inner(s, target_lens[1:], mask_shape[1:]) for s in seq]
        )
        sub_padded = np.array(sub_padded)
        sub_mask = np.array(sub_mask)
    else:
        sub_padded = seq
        if mask_shape:
            sub_mask = np.ones([len(seq)] + mask_shape[1:])
        else:
            sub_mask = np.ones(())
    if len(sub_padded) < target_lens[0]:
        # If we're not supposed to be masking at this depth, something has probably
        # gone wrong
        assert mask_shape
        len_diff = target_lens[0] - len(sub_padded)
        sub_padded = np.concatenate(
            [sub_padded, np.zeros([len_diff] + target_lens[1:])]
        )
        sub_mask = np.concatenate([sub_mask, np.zeros([len_diff] + mask_shape[1:])])
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
        return np.array(seq_padded), np.array(seq_mask)
    else:
        zero = np.zeros(seq[0])
        padded = np.array([seq[i] if len(seq) > i else zero for i in range(max_len)])
        mask = np.array([1 if len(seq) > i else 0 for i in range(max_len)])
        return padded, mask


def approx_minibatches(dataset, batch_size, epoch_size=None):
    n_data_points = len(dataset)
    if epoch_size is None:
        epoch_size = n_data_points
    n_batches = int(math.ceil(epoch_size / batch_size))
    for _ in range(n_batches):
        indices = np.random.randint(size=(batch_size,), low=0, high=n_data_points)
        yield [dataset[i] for i in indices]


def multisource_approx_minibatch(sources, source_repeats, epoch_size=None):
    assert len(sources) == len(source_repeats)
    n_data_points = max(
        [repeats * len(source) for (source, repeats) in zip(sources, source_repeats)]
    )
    if epoch_size is None:
        epoch_size = n_data_points
    batch_size = sum(source_repeats)
    n_batches = int(math.ceil(epoch_size / batch_size))
    for _ in range(n_batches):
        batch = []
        for source, reps in zip(sources, source_repeats):
            indices = np.random.randint(size=(reps,), low=0, high=len(source))
            for i in indices:
                batch.append(source[i])
        assert len(batch) == batch_size
        yield batch


LAST_SAVED_PARAMS_STEP = {}


def save_params(workdir, step, agent, delete_prev=True):
    # print(f'Saving params to {workdir}/{step}.pkl')
    with open(f"{workdir}/{step}.pkl", "wb") as f:
        pickle.dump(agent.state_dict(), f)
    if delete_prev:
        try:
            if workdir in LAST_SAVED_PARAMS_STEP:
                last_step = LAST_SAVED_PARAMS_STEP[workdir]
                if last_step != step:
                    # print(f'Deleting old params from {workdir}/{last_step}.pkl')
                    os.remove(f"{workdir}/{last_step}.pkl")
        except FileNotFoundError:
            pass
    LAST_SAVED_PARAMS_STEP[workdir] = step


class FitCallbacks:
    def epoch_start(self, model):
        return {}

    def epoch_end(self, model):
        return {}

    def minibatch_start(self, model):
        return {}

    def minibatch_end(self, model):
        return {}

    def training_complete(self, model):
        return {}


DEFAULT_SEED = sample_utils.DEFAULT_SEED


def log_infos(summary_writer, infos, step):
    for (k, v) in infos.items():
        try:
            summary_writer.add_scalar(k, v, step)
        except ValueError:
            pass
        except TypeError:
            pass


def fit_model(
    data,
    create_model,
    loss_function,
    model_name,
    preprocess,
    batch_size=16,
    n_epochs=N_EPOCHS,
    seed=DEFAULT_SEED,
    learning_rate=1e-4,
    momentum=0.995,
    callbacks=FitCallbacks(),
):
    workdir = expanduser(f"~/data/fit_model={model_name}_seed={seed}")
    print("workdir:", workdir)
    summary_writer = tensorboardX.SummaryWriter(workdir)
    summary_writer.add_hparams(
        {
            "learning_rate": learning_rate,
            "momentum": momentum,
            "seed": seed,
            "n_datapoints": len(data),
            "batch_size": batch_size,
            "n_epochs": n_epochs,
        },
        {},
    )

    torch.manual_seed(seed)
    model = create_model(preprocess(data[:1])[0])
    opt = torch.optim.SGD(model.parameters(), learning_rate, momentum)

    step = 0
    for epoch in tqdm(range(n_epochs)):
        # print("Beginning epoch", epoch)
        infos = callbacks.epoch_start(model)
        log_infos(summary_writer, infos, step)
        first_step_in_epoch = True
        for minibatch in approx_minibatches(data, batch_size):
            infos = callbacks.minibatch_start(model)
            log_infos(summary_writer, infos, step)
            if step % 1000 == 0:
                save_params(workdir, step, model, delete_prev=not first_step_in_epoch)
                first_step_in_epoch = False
            inputs, targets = preprocess(minibatch)
            loss, infos = loss_function(model, *inputs, targets)
            opt.zero_grad()
            loss.backward()
            opt.step()
            log_infos(summary_writer, infos, step)
            infos = callbacks.minibatch_end(model)
            log_infos(summary_writer, infos, step)
            summary_writer.flush()
            step += 1
        infos = callbacks.epoch_end(model)
        log_infos(summary_writer, infos, step)
        save_params(workdir, epoch, model)
        summary_writer.flush()
    infos = callbacks.training_complete(model)
    log_infos(summary_writer, infos, step)
    summary_writer.flush()

    return model


def fit_model_multisource(
    sources,
    source_repeats,
    create_model,
    loss_function,
    model_name,
    preprocess,
    n_epochs=5,
    seed=DEFAULT_SEED,
    learning_rate=1e-4,
    momentum=0.995,
    callbacks=FitCallbacks(),
):
    workdir = expanduser(f"~/data/fit_model_multisource={model_name}_seed={seed}")
    print("workdir:", workdir)
    print("Setting up SummaryWriter... ", end="", flush=True)
    summary_writer = tensorboardX.SummaryWriter(workdir)
    summary_writer.add_hparams(
        {
            "learning_rate": learning_rate,
            "momentum": momentum,
            "seed": seed,
            "source_lengths": [len(source) for source in sources],
            "source_repeats": source_repeats,
            "n_epochs": n_epochs,
        },
        {},
    )
    print("done")

    torch.manual_seed(seed)
    first_batch = next(multisource_approx_minibatch(sources, source_repeats))
    model = create_model(preprocess(first_batch)[0])
    opt = torch.optim.SGD(model.parameters(), learning_rate, momentum)

    step = 0
    for epoch in tqdm(range(n_epochs)):
        # print("Beginning epoch", epoch)
        infos = callbacks.epoch_start(model)
        log_infos(summary_writer, infos, step)
        first_step_in_epoch = True
        for minibatch in multisource_approx_minibatch(sources, source_repeats):
            infos = callbacks.minibatch_start(model)
            log_infos(summary_writer, infos, step)
            if step % 1000 == 0:
                save_params(workdir, step, model, delete_prev=not first_step_in_epoch)
                first_step_in_epoch = False
            inputs, targets = preprocess(minibatch)
            loss, infos = loss_function(model, *inputs, targets)
            opt.zero_grad()
            loss.backward()
            opt.step()
            log_infos(summary_writer, infos, step)
            infos = callbacks.minibatch_end(model)
            log_infos(summary_writer, infos, step)
            summary_writer.flush()
            step += 1
        infos = callbacks.epoch_end(model)
        log_infos(summary_writer, infos, step)
        save_params(workdir, epoch, model)
        summary_writer.flush()
    infos = callbacks.training_complete(model)
    log_infos(summary_writer, infos, step)
    summary_writer.flush()

    return model


def env_names_to_onehots(env_names, all_names=MT50_ENV_NAMES):
    return F.one_hot(
        torch.tensor([all_names.index(env_name) for env_name in env_names]),
        len(all_names),
    )
