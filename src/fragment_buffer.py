"""A replay buffer that can reconstruct episodes from fragments."""
from typing import Iterator
from itertools import chain

from numpy import dtype, isin
import torch


class EpisodeId(int):
    pass


class FragmentBuffer:
    """A replay buffer that can re-assemble episodes from timesteps, and can
    sample fragments of those episodes.

    FragmentBuffer attempts to be as agnostic as possible to the type of data
    being stored in it.
    Data will be stored in torch.Tensors when possible, and in lists otherwise.
    Args:
        n_episodes (int): Number of episodes to store at once.
        max_episode_length (int): Maximum episode length. If storing a trailing
        observation is desired, pass max_episode_length + 1.

    """

    def __init__(self, n_episodes: int, max_episode_length: int):
        self.buffers: dict[str, torch.Tensor or list] = {}
        self.episode_length_so_far: torch.Tensor = torch.zeros(
            n_episodes, dtype=torch.int64
        )
        self.episode_complete: torch.Tensor = torch.zeros(n_episodes, dtype=torch.bool)
        self._n_episodes = n_episodes
        self._max_episode_length = max_episode_length
        self._next_episode_id: EpisodeId = EpisodeId(1)
        self._next_allocation_index: int = 0
        self._episode_allocations: dict[EpisodeId, int] = {}
        self._rev_episode_allocations: dict[int, EpisodeId] = {}

    def start_episode(self, episode_id=None) -> EpisodeId:
        if episode_id is None:
            episode_id = self._next_episode_id
            self._next_episode_id = EpisodeId(self._next_episode_id + 1)
        episode_to_remove = self._rev_episode_allocations.get(
            self._next_allocation_index
        )
        if episode_to_remove is not None:
            del self._episode_allocations[episode_to_remove]
        self._rev_episode_allocations[self._next_allocation_index] = episode_id
        self._episode_allocations[episode_id] = self._next_allocation_index
        self.episode_length_so_far[self._next_allocation_index] = 0
        self.episode_complete[self._next_allocation_index] = False
        self._next_allocation_index = (
            1 + self._next_allocation_index
        ) % self._n_episodes
        return episode_id

    def end_episode(self, episode: EpisodeId):
        self.episode_complete[episode] = True

    def store_timestep(
        self, episode_id: EpisodeId, timestep: dict[str, torch.Tensor or object]
    ):
        timesteps = {}
        for k, v in timestep.items():
            if isinstance(v, torch.Tensor):
                timesteps[k] = v.unsqueeze(-1)
            else:
                timesteps[k] = [v]
        self.store_timesteps(episode_id, timesteps)

    def store_timesteps(
        self, episode_id: EpisodeId, timesteps: dict[str, torch.Tensor or list]
    ):
        assert timesteps
        assert not self.episode_complete[episode_id]
        allocation_index = self._episode_allocations[episode_id]
        start_step = self.episode_length_so_far[allocation_index]
        n_steps = None
        for k, v in timesteps.items():
            if n_steps is None:
                n_steps = len(v)
            else:
                assert n_steps == len(v)

            buffer = self.buffers.get(k)
            if isinstance(v, list):
                if buffer is None:
                    buffer = [
                        [None] * self._max_episode_length
                        for _ in range(self._n_episodes)
                    ]
                    self.buffers[k] = buffer
                else:
                    if not isinstance(buffer, list):
                        raise TypeError(
                            f"Expected a timestep sequence of type {type(buffer)} "
                            f"for {k} but got one of type {type(v)}"
                        )
            elif isinstance(v, torch.Tensor):
                if buffer is None:
                    buffer = torch.zeros(
                        (
                            self._n_episodes,
                            self._max_episode_length,
                        )
                        + v.shape[1:],
                        dtype=v.dtype,
                    )
                    self.buffers[k] = buffer
                else:
                    if not isinstance(buffer, torch.Tensor):
                        raise TypeError(
                            f"Expected a timestep sequence of type {type(buffer)} "
                            f"for {k} but got one of type {type(v)}"
                        )
            else:
                raise TypeError("Unsupported timestep sequence type {}", type(v))
            print(start_step, start_step + n_steps, v)
            buffer[allocation_index][start_step : start_step + n_steps] = v
        self.episode_length_so_far[allocation_index] += n_steps

    def valid_indices(self, fragment_length=1):
        all_allocations = []
        for allocation in self._episode_allocations.values():
            length = self.episode_length_so_far[allocation]
            last_valid_start = length - fragment_length
            if last_valid_start < 0:
                continue
            valid_indices = torch.stack(
                [
                    allocation * torch.ones(last_valid_start + 1, dtype=torch.int64),
                    torch.arange(last_valid_start + 1),
                ],
                dim=1,
            )
            all_allocations.append(valid_indices)
        return torch.cat(all_allocations)

    def index(
        self,
        start_indices: torch.tensor,
        lengths: torch.tensor or int = 1,
        extra_buffers: dict[str, list or torch.Tensor] = {},
    ) -> dict[str, list or torch.Tensor]:
        """Look up a set of fragments, using the provided start_indices.
        Output tensors will have shape (fragment_index, time_index, *)
        start_indices should be valid indices, with for a length passed here at most equal to the
        than the fragment_length passed to valid_indices.

        extra_buffers will be sampled from using the same indexing logic.
        """
        fragments = {}
        indices = None
        if isinstance(lengths, int):
            if lengths == 1:
                # This is an optimization to avoid the nested stack loop below.
                # We still want to produce a sequence of fragments (not a
                # sequence of steps), so add an indexing dimension
                indices = start_indices.unsqueeze(2)
            else:
                lengths = lengths * torch.ones(len(start_indices), dtype=torch.int64)
        max_lengths = self.episode_length_so_far[start_indices[:, 0]]
        end_indices, _ = torch.min(
            torch.stack([start_indices[:, 1] + lengths, max_lengths]), dim=0
        )
        clipped_lengths = end_indices - start_indices[:, 1]
        # If fragments are not all of equal length, then they cannot be stacked into a Tensor
        assert (clipped_lengths == lengths).all()
        if indices is None:
            assert isinstance(lengths, torch.Tensor)
            # There's does not appear to be a good way to do range indexing without a for loop.
            # https://stackoverflow.com/questions/61034839/pytorch-indexing-a-range-of-multiple-indices
            indices = torch.stack(
                [
                    torch.stack(
                        [
                            start_indices[i, 0]
                            * torch.ones((int(lengths[i]),), dtype=torch.int64),
                            torch.arange(start_indices[i, 1], end_indices[i]),
                        ]
                    )
                    for i in range(len(lengths))
                ]
            )
            # Dimensions: (expanded) index dim, episode, index in episode
            assert len(indices.shape) == 3
            assert len(indices) <= torch.sum(lengths)
        for k, v in chain(self.buffers.items(), extra_buffers.items()):
            if isinstance(v, list):
                fragments[k] = [
                    v[start_indices[i, 0]][start_indices[i, 1] : end_indices[i]]
                    for i in range(len(start_indices))
                ]
            else:
                # Ideally this would be: v[start_indices[:, 0], start_indices[:, 1]:end_indices]
                # But pytorch doesn't support range indexing from a tensor.
                fragments[k] = v[indices[:, 0], indices[:, 1]]
        return fragments


def test_indexing():
    buffer = FragmentBuffer(n_episodes=7, max_episode_length=5)
    for x in range(2):
        ep = buffer.start_episode()
        for i in range(x + 3):
            buffer.store_timestep(ep, {"t": torch.tensor(i)})
    indices = buffer.valid_indices(fragment_length=4)
    assert (indices == torch.tensor([[1, 0]])).all()
    indices = buffer.valid_indices(fragment_length=3)
    assert (indices == torch.tensor([[0, 0], [1, 0], [1, 1]])).all()
    indices = buffer.valid_indices(fragment_length=2)
    assert (indices == torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1], [1, 2]])).all()
    indices = buffer.valid_indices()
    assert (
        indices
        == torch.tensor([[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [1, 3]])
    ).all()
    assert len(buffer.index(indices)["t"].shape) == 2
    assert (
        buffer.index(indices)["t"] == torch.tensor([[0], [1], [2], [0], [1], [2], [3]])
    ).all()
    indices = buffer.valid_indices(fragment_length=2)
    assert (
        buffer.index(indices, lengths=2)["t"]
        == torch.tensor([[0, 1], [1, 2], [0, 1], [1, 2], [2, 3]])
    ).all()


def test_list():
    buffer = FragmentBuffer(n_episodes=7, max_episode_length=5)
    for x in range(2):
        ep = buffer.start_episode()
        for i in range(x + 3):
            buffer.store_timestep(ep, {"t": "abcd"[i]})
    indices = buffer.valid_indices(fragment_length=4)
    assert (indices == torch.tensor([[1, 0]])).all()
    indices = buffer.valid_indices(fragment_length=3)
    assert (indices == torch.tensor([[0, 0], [1, 0], [1, 1]])).all()
    indices = buffer.valid_indices(fragment_length=2)
    assert (indices == torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1], [1, 2]])).all()
    indices = buffer.valid_indices()
    assert (
        indices
        == torch.tensor([[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [1, 3]])
    ).all()
    assert buffer.index(indices)["t"] == [
        ["a"],
        ["b"],
        ["c"],
        ["a"],
        ["b"],
        ["c"],
        ["d"],
    ]
    indices = buffer.valid_indices(fragment_length=2)
    assert buffer.index(indices, lengths=2)["t"] == [
        ["a", "b"],
        ["b", "c"],
        ["a", "b"],
        ["b", "c"],
        ["c", "d"],
    ]
