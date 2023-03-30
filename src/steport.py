import torch
import torch.nn as nn
import torch.nn.functional as F

import numpy as np

import itertools


class Steport(nn.Module):
    def __init__(
        self,
        grid_shape=(64, 64, 64),
        center_crop_shape=(8, 8, 8),
        path_layers=6,
        n_voxel_features=5,
        output_size=4,
    ):
        super().__init__()
        self._feature_count = 8 + np.arange(10)
        self._grid_shape = grid_shape
        self._center_crop_shape = center_crop_shape
        self._n_voxel_features = n_voxel_features
        self._pre_transport_layers = nn.Sequential(
            nn.Conv3d(n_voxel_features, self._feature_count[0], 2, 1, padding="same"),
            nn.Tanh(),
            nn.Conv3d(self._feature_count[0], self._feature_count[1], 1, 1),
        )
        self._center_crop_layers = nn.Sequential(
            nn.Conv3d(n_voxel_features, self._feature_count[0], 2, 1, padding="same"),
            nn.Tanh(),
            nn.Conv3d(self._feature_count[0], self._feature_count[1], 1, 1),
        )
        path_stack = []
        last_feature_count = self._feature_count[1]
        for i in range(path_layers):
            path_stack.extend(
                [
                    nn.Conv3d(last_feature_count, self._feature_count[i + 1], 2, 2),
                    nn.Tanh(),
                ]
            )
            last_feature_count = self._feature_count[i + 1]
        self._path_stack = nn.Sequential(*path_stack)
        self._final_readout = nn.Linear(last_feature_count, output_size)
        self._output_size = output_size

    def forward(self, feature_grid):
        # Allow only batch size 1
        if len(feature_grid.shape) == 5:
            assert feature_grid.shape[0] == 1
            return self.forward(feature_grid.squeeze(0)).unsqueeze(0)

        assert feature_grid.shape == self._grid_shape + (self._n_voxel_features,)
        # Grid is X, Y, Z, C
        cc_idx = [
            (
                int((self._grid_shape[i] - self._center_crop_shape[i]) / 2),
                int((self._grid_shape[i] + self._center_crop_shape[i]) / 2),
            )
            for i in range(3)
        ]
        center_crop = feature_grid[
            cc_idx[0][0] : cc_idx[0][1],
            cc_idx[1][0] : cc_idx[1][1],
            cc_idx[2][0] : cc_idx[2][1],
        ]
        # Grid is X, Y, Z, C
        # Need 1, C, X, Y, Z
        feature_grid_cxyz = feature_grid.permute(3, 0, 1, 2).unsqueeze(0)
        cc_cxyz = center_crop.permute(3, 0, 1, 2).unsqueeze(0)

        pre_transport = self._pre_transport_layers(feature_grid_cxyz)
        pre_transport_cc = self._center_crop_layers(cc_cxyz)

        # CC is 1, C, X, Y, Z
        # Need C, C, X, Y, Z
        cc_weight = pre_transport_cc.expand(pre_transport.shape[1], -1, -1, -1, -1)
        # PyTorch can't batch this, so the whole method may as well not be batched.
        transport_out = F.conv3d(pre_transport, weight=cc_weight, padding="same")
        path_out = self._path_stack(transport_out)
        # path_out is 1, C, 1, 1, 1
        # Need C
        flat_path_out = path_out.squeeze()
        # If this assert fails, path_layers needs to be adjusted (assuming the
        # grid size is all a power of 2)
        # If the grid size isn't a power of 2, a flatten may be needed here,
        # along with a change to the final_readout layer
        assert len(flat_path_out.shape) == 1, "Adjust path_layers"

        result = self._final_readout(flat_path_out)
        assert result.shape == (self._output_size,)
        return result


def test_smoke():
    from metaworld_3d_env import MetaWorldVoxelEnv

    env = MetaWorldVoxelEnv(env_name="reach", seed=1000)
    obs = env.reset()
    feature_grid = env.obsToNumpyVoxels(obs)
    feature_grid_torch = torch.from_numpy(feature_grid)

    steport = Steport()
    steport(feature_grid_torch)
    steport(feature_grid_torch.unsqueeze(0))


if __name__ == "__main__":
    test_smoke()
