

# %%
"""
# plate-slide-back-side: slide the plate back sideways into the target location
def plate_slide_back_side(robot):
"""


# %%
# Steps:
#  1. Put gripper above plate
#  2. Close gripper around plate
#  3. Slide plate sideways into goal
# First, put the gripper roughly above plate.
if check("the robot's gripper is not vertically aligned with the plate"):
    robot.place("gripper above plate")
# Once the gripper is aligned above the plate, we can close the gripper to grab
# the plate.
if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is open"):
    robot.drop("gripper around plate")
# Now that we grabbed the plate, we can just slide it along the table to the
# goal.
if check("the robot's gripper is around plate and the robot's gripper is closed"):
    robot.slide("plate to the goal")


# %%
[eod] [code]import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("Lenna.png", cv.IMREAD_GRAYSCALE)

_, th1 = cv.threshold(img, 100, 255, cv.THRESH_BINARY)
_, th2 = cv.threshold(img, 100, 255, cv.THRESH_BINARY_INV)
_, th3 = cv.threshold(img, 100, 255, cv.THRESH_TRUNC)
_, th4 = cv.threshold(img, 100, 255, cv.THRESH_TOZERO)
_, th5 = cv.threshold(img, 100, 255, cv.THRESH_TOZERO_INV)

titles = ["Original", "BINARY", "BINARY_INV", "TRUNC", "TOZERO", "TOZERO_INV"]
images = [img, th1, th2, th3, th4, th5]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()[eod] [code]#!/usr/bin/env python
# -*- coding: utf-