#!/usr/bin/env python3

import math
import numpy as np

from PIL import Image as PIL_Image

import open3d as o3d

"""
Generates numpy rotation matrix from quaternion

@param quat: w-x-y-z quaternion rotation tuple

@return np_rot_mat: 3x3 rotation matrix as numpy array
"""


def quat2Mat(quat):
    if len(quat) != 4:
        print("Quaternion", quat, "invalid when generating transformation matrix.")
        raise ValueError

    # Note that the following code snippet can be used to generate the 3x3
    #    rotation matrix, we don't use it because this file should not depend
    #    on mujoco.
    """
    from mujoco_py import functions
    res = np.zeros(9)
    functions.mju_quat2Mat(res, camera_quat)
    res = res.reshape(3,3)
    """

    # This function is lifted directly from scipy source code
    # https://github.com/scipy/scipy/blob/v1.3.0/scipy/spatial/transform/rotation.py#L956
    w = quat[0]
    x = quat[1]
    y = quat[2]
    z = quat[3]

    x2 = x * x
    y2 = y * y
    z2 = z * z
    w2 = w * w

    xy = x * y
    zw = z * w
    xz = x * z
    yw = y * w
    yz = y * z
    xw = x * w

    rot_mat_arr = [
        x2 - y2 - z2 + w2,
        2 * (xy - zw),
        2 * (xz + yw),
        2 * (xy + zw),
        -x2 + y2 - z2 + w2,
        2 * (yz - xw),
        2 * (xz - yw),
        2 * (yz + xw),
        -x2 - y2 + z2 + w2,
    ]
    np_rot_mat = rotMatList2NPRotMat(rot_mat_arr)
    return np_rot_mat


"""
Generates numpy rotation matrix from rotation matrix as list len(9)

@param rot_mat_arr: rotation matrix in list len(9) (row 0, row 1, row 2)

@return np_rot_mat: 3x3 rotation matrix as numpy array
"""


def rotMatList2NPRotMat(rot_mat_arr):
    np_rot_arr = np.array(rot_mat_arr)
    np_rot_mat = np_rot_arr.reshape((3, 3))
    return np_rot_mat


"""
Generates numpy transformation matrix from position list len(3) and
    numpy rotation matrix

@param pos:     list len(3) containing position
@param rot_mat: 3x3 rotation matrix as numpy array

@return t_mat:  4x4 transformation matrix as numpy array
"""


def posRotMat2Mat(pos, rot_mat):
    t_mat = np.eye(4)
    t_mat[:3, :3] = rot_mat
    t_mat[:3, 3] = np.array(pos)
    return t_mat


"""
Generates Open3D camera intrinsic matrix object from numpy camera intrinsic
    matrix and image width and height

@param cam_mat: 3x3 numpy array representing camera intrinsic matrix
@param width:   image width in pixels
@param height:  image height in pixels

@return t_mat:  4x4 transformation matrix as numpy array
"""


def cammat2o3d(cam_mat, width, height):
    cx = cam_mat[0, 2]
    fx = cam_mat[0, 0]
    cy = cam_mat[1, 2]
    fy = cam_mat[1, 1]

    return o3d.camera.PinholeCameraIntrinsic(width, height, fx, fy, cx, cy)


#
# and combines them into point clouds
"""
Class that renders depth images in MuJoCo, processes depth images from
    multiple cameras, converts them to point clouds, and processes the point
    clouds
"""


class PointCloudGenerator(object):
    """
    initialization function

    @param sim:       MuJoCo simulation object
    @param min_bound: If not None, list len(3) containing smallest x, y, and z
        values that will not be cropped
    @param max_bound: If not None, list len(3) containing largest x, y, and z
        values that will not be cropped
    """

    def __init__(
        self,
        sim,
        min_bound=None,
        max_bound=None,
        camera_names=None,
        *,
        width=640,
        height=480
    ):
        super(PointCloudGenerator, self).__init__()

        self.sim = sim

        self.img_width = width
        self.img_height = height

        if camera_names is None:
            self.cam_names = list(enumerate(self.sim.model.camera_names))
        else:
            cam_name_to_id = {
                name: i for (i, name) in enumerate(self.sim.model.camera_names)
            }
            self.cam_names = [(cam_name_to_id[name], name) for name in camera_names]

        self.target_bounds = None
        if min_bound != None and max_bound != None:
            self.target_bounds = o3d.geometry.AxisAlignedBoundingBox(
                min_bound=min_bound, max_bound=max_bound
            )

        # List of camera intrinsic matrices
        self.cam_mats = {}
        for (cam_id, cam_name) in self.cam_names:
            fovy = math.radians(self.sim.model.cam_fovy[cam_id])
            f = self.img_height / (2 * math.tan(fovy / 2))
            cam_mat = np.array(
                (
                    (f, 0, self.img_width / 2, 0),
                    (0, f, self.img_height / 2, 0),
                    (0, 0, 1, 0),
                    (0, 0, 0, 1),
                )
            )
            self.cam_mats[cam_id] = cam_mat

    def cam2World(self, cam_name, cam_id):
        cam_body_id = self.sim.model.cam_bodyid[cam_id]

        try:
            cam_pos = self.sim.data.get_camera_xpos(cam_name)
        except TypeError:
            cam_pos = self.sim.model.body_pos[cam_body_id]

        try:
            cam_mat = self.sim.data.get_camera_xmat(cam_name)
        except TypeError:
            cam_mat = self.sim.model.cam_mat0[cam_id]
        # c2b_r = rotMatList2NPRotMat(self.sim.model.cam_mat0[cam_id])
        c2b_r = rotMatList2NPRotMat(cam_mat)
        # In MuJoCo, we assume that a camera is specified in XML as a body
        #    with pose p, and that that body has a camera sub-element
        #    with pos and euler 0.
        #    Therefore, camera frame with body euler 0 must be rotated about
        #    x-axis by 180 degrees to align it with the world frame.
        b2w_r = quat2Mat([0, 1, 0, 0])
        c2w_r = np.matmul(c2b_r, b2w_r)
        c2w = posRotMat2Mat(cam_pos, c2w_r)
        return c2w

    def images2PointCloud(
        self,
        cam2world_mats,
        color_imgs,
        depth_imgs,
        cam_locations,
        estimate_normals=True,
    ):
        o3d_clouds = []
        for (cam_id, cam_name) in self.cam_names:
            color_img = color_imgs[cam_name]
            depth_img = depth_imgs[cam_name]
            c2w = cam2world_mats[cam_name]
            cam_pos = cam_locations[cam_name]

            # convert camera matrix and depth image to Open3D format, then
            #    generate point cloud
            od_cammat = cammat2o3d(
                self.cam_mats[cam_id], self.img_width, self.img_height
            )
            # od_rgb = o3d.geometry.Image(color_img)
            # od_rgb = o3d.geometry.Image(color_img.transpose(1, 0, 2)
            # .reshape(self.img_height, self.img_width, 3))
            # Open3D Image doesn't know how to handle views, make sure to use a copy
            od_rgb = o3d.geometry.Image(np.copy(color_img))
            od_depth = o3d.geometry.Image(np.copy(depth_img))
            od_rgbd = o3d.geometry.RGBDImage.create_from_color_and_depth(
                od_rgb,
                od_depth,
                depth_scale=1.0,
                depth_trunc=100.0,
                convert_rgb_to_intensity=False,
            )
            o3d_cloud = o3d.geometry.PointCloud.create_from_rgbd_image(
                od_rgbd, od_cammat
            )

            # Compute world to camera transformation matrix
            transformed_cloud = o3d_cloud.transform(c2w)

            # If both minimum and maximum bounds are provided, crop cloud to fit
            #    inside them.
            if self.target_bounds != None:
                transformed_cloud = transformed_cloud.crop(self.target_bounds)

            # Estimate normals of cropped cloud, then flip them based on camera
            #    position.
            transformed_cloud.estimate_normals(
                search_param=o3d.geometry.KDTreeSearchParamHybrid(
                    radius=0.03, max_nn=250
                )
            )
            cam_body_id = self.sim.model.cam_bodyid[cam_id]
            transformed_cloud.orient_normals_towards_camera_location(cam_pos)

            o3d_clouds.append(transformed_cloud)

        combined_cloud = o3d.geometry.PointCloud()
        for cloud in o3d_clouds:
            combined_cloud += cloud
        return combined_cloud

    def generateObservation(self):
        color_imgs = {}
        depth_imgs = {}
        cam2world_mats = {}
        cam_locations = {}
        for (cam_id, cam_name) in self.cam_names:
            color_img, depth_img = self.captureImage(cam_name)
            color_imgs[cam_name] = color_img
            depth_imgs[cam_name] = depth_img
            cam_locations[cam_name] = self.sim.data.get_camera_xpos(cam_name).astype(
                np.float32
            )
            cam2world_mats[cam_name] = self.cam2World(cam_name, cam_id).astype(
                np.float32
            )
        return {
            "cam2world_mats": cam2world_mats,
            "cam_locations": cam_locations,
            "color_imgs": color_imgs,
            "depth_imgs": depth_imgs,
        }

    def observationToPointCloud(self, observation, estimate_normals=True):
        cam2world_mats = observation["cam2world_mats"]
        cam_locations = observation["cam_locations"]
        color_imgs = observation["color_imgs"]
        depth_imgs = observation["depth_imgs"]
        return self.images2PointCloud(
            cam2world_mats, color_imgs, depth_imgs, cam_locations, estimate_normals
        )

    def generateCroppedPointCloud(self, save_img_dir=None):
        obs = self.generateObservation()
        if save_img_dir != None:
            cam2world_mats, color_imgs, depth_imgs = observation
            for (cam_id, cam_name) in self.cam_names:
                self.saveImg(
                    depth_imgs[cam_name], save_img_dir, "depth_test_" + str(cam_id)
                )
                self.saveImg(
                    color_imgs[cam_name], save_img_dir, "color_test_" + str(cam_id)
                )
        return self.observationToPointCloud(obs)

    # https://github.com/htung0101/table_dome/blob/master/table_dome_calib/utils.py#L160
    def depthimg2Meters(self, depth):
        extent = self.sim.model.stat.extent
        near = self.sim.model.vis.map.znear * extent
        far = self.sim.model.vis.map.zfar * extent
        image = near / (1 - depth * (1 - near / far))
        return image

    def verticalFlip(self, img):
        return np.flip(img, axis=0)

    # Render and process an image
    def captureImage(self, cam_name):
        img, depth = self.sim.render(
            self.img_width, self.img_height, camera_name=cam_name, depth=True
        )
        # Rendered images appear to be flipped about vertical axis
        depth = self.verticalFlip(depth)
        img = self.verticalFlip(img)
        real_depth = self.depthimg2Meters(depth)

        return img, real_depth

    # Normalizes an image so the maximum pixel value is 255,
    # then writes to file
    def saveImg(self, img, filepath, filename):
        normalized_image = img / img.max() * 255
        normalized_image = normalized_image.astype(np.uint8)
        im = PIL_Image.fromarray(normalized_image)
        im.save(filepath + "/" + filename + ".jpg")
