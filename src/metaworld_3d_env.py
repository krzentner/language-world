from metaworld.envs import ALL_V2_ENVIRONMENTS_GOAL_OBSERVABLE
import numpy as np
import gym.spaces as spaces
import gym

import plotly.express as px
import plotly.graph_objects as go

def render_env(env_name, seed=1000):
    env = ALL_V2_ENVIRONMENTS_GOAL_OBSERVABLE[f'{env_name}-v2-goal-observable'](seed)
    env.seeded_rand_vec = True
    env.reset()
    width = 64
    height = 48
    camera = "corner4"

    img, depth = env.sim.render(
        width,
        height,
        mode='offscreen',
        camera_name=camera,
        depth=True
    )
    obs = env._get_obs()
    mlab_imshowColor(img)
    # Pos Hand
    points3d(obs[0], obs[1], obs[2])
    # Pos obj
    points3d(obs[4], obs[5], obs[6], color=(0, 0, 1))
    points_pixel_space = np.mgrid[-1:1:(2/height), -1:1:(2/width)].astype(np.float32)
    print(points_pixel_space.shape)
    assert points_pixel_space.shape == (2, height, width)
    assert depth[None].shape == (1, height, width)
    points_with_depth = np.concatenate((points_pixel_space, depth[None]), axis=0)
    assert points_with_depth.shape == (3, height, width)
    mat = get_camera_mat(env, width, height, camera)
    points_in_3d = points_with_depth.T @ mat
    print(points_in_3d)
    assert points_in_3d.shape == (width, height, 4)
    assert points_in_3d.T.shape == (4, height, width)
    points_flat_3d = points_in_3d.T.reshape(4, -1)
    assert img.transpose(2, 0, 1).shape == (3, height, width)
    colors_flat_3d = img.transpose(2, 0, 1).reshape(3, -1)

    alpha = pl.ones(width * height)
    myLut = pl.c_[img.reshape(-1, 3), alpha]
    myLutLookupArray = pl.arange(width * height).reshape(width, height)

    points = mlab.points3d(points_flat_3d[0], points_flat_3d[1],  points_flat_3d[2], colormap='binary')
    points.module_manager.scalar_lut_manager.lut.table = myLut

    # mlab.points3d(points_in_3d[:, :, 0] / 100, points_in_3d[:, :, 1] / 100, points_in_3d[:, :, 2] / 100)

    mlab.show()

def points3d(x, y, z, *args, **kwargs):
    return mlab.points3d(100 * x, 100 * y, 100 * z, *args, **kwargs)

from mj_pc.mj_point_clouds import PointCloudGenerator
import open3d as o3d

def render_env_mj_pc(env_name, seed=1000):
    env = MetaWorldVoxelEnv(env_name=env_name, seed=seed)
    obs = env.reset()
    assert env.observation_space['imgs']['depth_imgs'].contains(obs['imgs']['depth_imgs'])
    assert env.observation_space['imgs']['color_imgs'].contains(obs['imgs']['color_imgs'])
    assert env.observation_space['imgs']['cam_locations'].contains(obs['imgs']['cam_locations'])
    assert env.observation_space['imgs']['cam2world_mats'].contains(obs['imgs']['cam2world_mats'])
    # Don't check low_dim, since it's broken anyways
    env.obsToNumpyVoxels(obs)

class MetaWorldVoxelEnv(gym.Env):

    def __init__(self,
                 *,
                 env_name,
                 seed,
                 camera_names=('corner4', 'behindGripper'),
                 img_width=128,
                 img_height=72):
        self.img_width = img_width
        self.img_height = img_height
        self.env = ALL_V2_ENVIRONMENTS_GOAL_OBSERVABLE[f'{env_name}-v2-goal-observable'](seed)
        self.env.seeded_rand_vec = True
        self.pc_gen = PointCloudGenerator(self.env.sim,
                                          min_bound=(-1., -1., -1.),
                                          max_bound=(1., 1., 1.),
                                          camera_names=camera_names,
                                          width=img_width,
                                          height=img_height)
        self.action_space = self.env.action_space
        self.observation_space = spaces.Dict({
            'low_dim': self.env.observation_space,
            'imgs': spaces.Dict({
                'cam2world_mats': spaces.Dict({
                    cam_name: spaces.Box(low=-np.inf, high=np.inf, shape=(4, 4))
                    for cam_name in camera_names
                }),
                'cam_locations': spaces.Dict({
                    cam_name: spaces.Box(low=-np.inf, high=np.inf, shape=(3,))
                    for cam_name in camera_names
                }),
                'color_imgs': spaces.Dict({
                    cam_name: spaces.Box(low=0, high=255,
                                         shape=(self.img_height, self.img_width, 3),
                                         dtype=np.uint8)
                    for cam_name in camera_names
                }),
                'depth_imgs': spaces.Dict({
                    cam_name: spaces.Box(low=0, high=np.inf,
                                         shape=(self.img_height, self.img_width),
                                         dtype=np.float32)
                    for cam_name in camera_names
                }),
            })
        })

    def _wrap_obs(self, low_dim_obs):
        return {'low_dim': low_dim_obs,
                'imgs': self.pc_gen.generateObservation()}

    def reset(self):
        obs = self.env.reset()
        return self._wrap_obs(obs)

    def step(self, action):
        obs, reward, done, info = self.env.step(action)
        return self._wrap_obs(obs), reward, done, info

    def visualize(self, obs):
        point_cloud = self.pc_gen.observationToPointCloud(obs['imgs'],
                                                          estimate_normals=True)
        voxel_grid = o3d.geometry.VoxelGrid.create_from_point_cloud(point_cloud,
                                                                    voxel_size=0.01)
        o3d.visualization.draw_geometries([point_cloud, voxel_grid])

    VOXEL_FEATURES = 5 # RGB + Count + Ones

    def obsToNumpyVoxels(self, obs, grid_shape=(64, 64, 64), grid_dims=(1., 1., 1.)):
        """

        Args:
            obs (dict): Observation to turn into a voxel grid.
            grid_shape (int, int, int): Shape of grid (not counting feature dimensions).
            grid_dims (float, float, float): Bounds to clip the points to

        Returns:
            np.ndarray: The featurized voxel grid. Has shape grid_shape + (VOXEL_FEATUES,)

        """
        gripper_location = obs['low_dim'][:3]
        point_cloud = self.pc_gen.observationToPointCloud(obs['imgs'],
                                                          estimate_normals=False)
        # Center the gripper
        # That's right, it's serious egocentrism time :sunglasses:
        point_cloud = point_cloud.translate(-gripper_location)

        min_bound = (-grid_dims[0] / 2, -grid_dims[1] / 2, -grid_dims[2] / 2)
        max_bound = (grid_dims[0] / 2, grid_dims[1] / 2, grid_dims[2] / 2)
        target_bounds = o3d.geometry.AxisAlignedBoundingBox(
            min_bound=min_bound, max_bound=max_bound)
        point_cloud = point_cloud.crop(target_bounds)

        locations = np.asarray(point_cloud.points)
        colors = np.asarray(point_cloud.colors, dtype=np.float32) / 255.0
        indices = np.trunc((locations - min_bound) * grid_shape).astype(np.uint32)
        count_grid = np.zeros(shape=grid_shape, dtype=np.uint32)
        color_grid = np.zeros(shape=grid_shape + (3,), dtype=np.float32)
        for i in range(indices.shape[0]):
            count_grid[indices[i, 0], indices[i, 1], indices[i, 2]] += 1
            color_grid[indices[i, 0], indices[i, 1], indices[i, 2]] += colors[i]

        divisor = np.maximum(np.expand_dims(count_grid, -1).astype(np.float32), 1.)
        color_grid /= divisor

        # X, Y, Z = np.mgrid[min_bound[0]:max_bound[0]:(grid_shape[0] * 1j),
                           # min_bound[1]:max_bound[1]:(grid_shape[1] * 1j),
                           # min_bound[2]:max_bound[2]:(grid_shape[2] * 1j)]
        # ds = count_grid.flatten()
        # X = X.flatten()[ds > 0]
        # Y = Y.flatten()[ds > 0]
        # Z = Z.flatten()[ds > 0]
        # C = color_grid.reshape(-1, 3)[ds > 0]
        # # values = np.sin(X*Y*Z) / (X*Y*Z)
        # # vol = (X - 1)**2 + (Y - 1)**2 + Z**2

        # fig = go.Figure(data=[go.Scatter3d(
            # x=X.flatten(),
            # y=Y.flatten(),
            # z=Z.flatten(),
            # mode='markers',
            # marker=dict(
                # size=grid_shape[0],
                # color=255 * C,
                # opacity=1.0,
            # )
        # )])

        # fig.write_html('first_figure.html', auto_open=True)

        count_feature_grid = count_grid.astype(np.float32) / 16
        feature_grid = np.concatenate((color_grid,
                                       np.expand_dims(count_grid, -1),
                                       np.ones(grid_shape + (1,))),
                                      axis=-1,
                                      dtype=np.float32)

        assert feature_grid.dtype == np.float32
        assert feature_grid.shape == grid_shape + (VOXEL_FEATURES,)
        return feature_grid


if __name__ == '__main__':
    render_env_mj_pc('reach')
