from metaworld.envs import ALL_V2_ENVIRONMENTS_GOAL_OBSERVABLE
import numpy as np

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

def get_camera_mat(env, width, height, camera_name):
    pos = env.sim.data.get_camera_xpos(camera_name)
    rot = env.sim.data.get_camera_xmat(camera_name).reshape(3, 3).T
    # HMM, how to get cam_id from camera_name
    # fov = env.sim.model.cam_fovy[cam_id]
    # print(env.sim.model.cam_fovy)
    # Just hard code the camera fov
    assert camera_name == 'corner4'
    fov = 30

    # Translation matrix (4x4).
    translation = np.eye(4)
    translation[0:3, 3] = -pos
    # Rotation matrix (4x4).
    rotation = np.eye(4)
    rotation[0:3, 0:3] = rot
    # Focal transformation matrix (3x4).
    focal_scaling = (1./np.tan(np.deg2rad(fov)/2)) * height / 2.0
    focal = np.diag([-focal_scaling, focal_scaling, 1.0, 0])[0:3, :]
    # Image matrix (3x3).
    image = np.eye(3)
    image[0, 2] = (width - 1) / 2.0
    image[1, 2] = (height - 1) / 2.0
    camera_matrix = image @ focal @ rotation @ translation
    return camera_matrix

import pylab as pl
from mayavi import mlab

def mlab_imshowColor(im, alpha=255, **kwargs):
    """
    Plot a color image with mayavi.mlab.imshow.
    im is a ndarray with dim (n, m, 3) and scale (0->255]
    alpha is a single number or a ndarray with dim (n*m) and scale (0->255]
    **kwargs is passed onto mayavi.mlab.imshow(..., **kwargs)
    """
    try:
        alpha[0]
    except:
        alpha = pl.ones(im.shape[0] * im.shape[1]) * alpha
    if len(alpha.shape) != 1:
        alpha = alpha.flatten()

    # The lut is a Nx4 array, with the columns representing RGBA
    # (red, green, blue, alpha) coded with integers going from 0 to 255,
    # we create it by stacking all the pixles (r,g,b,alpha) as rows.
    myLut = pl.c_[im.reshape(-1, 3), alpha]
    myLutLookupArray = pl.arange(im.shape[0] * im.shape[1]).reshape(im.shape[0], im.shape[1])

    #We can display an color image by using mlab.imshow, a lut color list and a lut lookup table.
    theImshow = mlab.imshow(myLutLookupArray, colormap='binary', **kwargs) #temporary colormap
    theImshow.module_manager.scalar_lut_manager.lut.table = myLut
    mlab.draw()

    return theImshow

if __name__ == '__main__':
    render_env('reach')
