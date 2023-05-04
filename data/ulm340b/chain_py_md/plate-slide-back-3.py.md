
"""

plate_slide_back = """
# plate-slide-back: slide the plate back into the target location
def plate_slide_back(robot):
    # Steps:
    #  1. Put gripper above plate
    #  2. Close gripper around plate
    #  3. Slide plate to target location
    # The plate is a very small object, so put the gripper above the plate to
    # try to grab it without knocking it around.
    if check("the robot's gripper is not above the plate"):
        robot.place("gripper above plate")
    # If the gripper is roughly above the plate but not around it, close the
    # gripper to grab the plate.
    if check("the robot's gripper is above plate and the robot's gripper is not around plate and the robot's gripper is open"):
        robot.close("gripper around plate")
    # Now that the gripper is above the plate and we've closed the gripper, we
    # might have grabbed the plate.
    # Slide the plate to the target location, and go back to an earlier step
    # if we didn't grab it.
    if check("the robot's gripper is above plate and the robot's gripper is closed"):
        robot.place("plate at target location")
"""
[eod] [code]import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


def plot_image(x):
    plt.imshow(x, cmap=plt.cm.gray)


def plot_histogram(x):
    hist = cv.calcHist([x], [0], None, [256], [0, 256])
    plt.plot(hist)


# 将黑白图片的0到255的灰度值重新归一化到0~1
def gray_normalize(img):
    img = img.astype(np.float32) / 255.
    return img


def get_hist(img):
    img = img.astype(np.uint8)
    gray_hist = cv.calcHist([img], [0], None, [256], [0, 256])
    c_hist = cv.calcHist([img], [1], None, [256], [0, 256])
    m_hist =