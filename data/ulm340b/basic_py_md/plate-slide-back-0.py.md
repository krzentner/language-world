

This method should be similar to the `push` method, except that it should slide the plate from behind.

Please fill in the following blank with the appropriate code:

"""

# ANSWER

# def plate_slide_back(robot):
#     if check("the robot's gripper is not vertically aligned with plate"):
#         robot.put("gripper behind plate")
#     if check("the robot's gripper is near plate and the robot's gripper is behind plate"):
#         robot.push("plate back")
#     if check("the robot's gripper is near plate and plate is below the robot's gripper"):
#         robot.slide("plate to goal")

# EXPLANATION

# The robot should be placed behind the plate to begin. It will
# then push the plate back toward the goal until the plate is
# behind the robot, and then slide the plate to the goal.
[eod] [code]import numpy as np
from numpy.testing import assert_almost_equal, assert_equal
from numpy.testing import assert_array_almost_equal, assert_array_equal

from skimage import transform
from skimage.io import imread
from skimage._shared.testing import assert_warns


def test_matrix_transform():
    arr = np.array([[0, 0, 0],
                    [0, 1, 0],
                    [0, 0, 0]])

    transform._matrix_transform(arr, np.eye(2))
    assert_array_equal(arr, np.zeros((3, 3)))

    transform._matrix_transform(arr, 0.5 * np.eye(2))
    assert_almost_equal(arr[1, 1], 0.5)

    transform._matrix_transform(arr, [[1, 0], [0.5, 1]], order=0)
    assert_equal(arr[1, 0], 0.5)
    assert_equal(arr[1, 1], 1)
    transform._matrix_transform(arr, [[1, 0], [0.5, 1]], order=1)
    assert_almost_equal(arr[1, 0], 0.25)
    assert_almost_equal(arr[1, 1], 1)


def test_matrix_transform_keep_range():
    a = transform._matrix_transform_keep_range(np.arange(10).reshape(2, 5),
                               