

Then fill in the rest of the code to perform the push-back task.
"""

# push-back: slide the puck backwards to the target location
def push_back(robot):
    if check("the robot's gripper is not below the puck and the robot's gripper is not near the puck"):
        robot.grab("the puck")
    if check("the robot's gripper is near the puck and the puck is above the robot's gripper"):
        robot.slide("the puck to the goal")

[eod] [code]import numpy as np


def load_matrix(filename: str) -> np.ndarray:
    matrix = []
    with open(filename) as file:
        for line in file:
            matrix.append([int(num) for num in line.strip()])

    return np.array(matrix)
[eod] [code]# -*- coding: utf-8 -*-
"""
Created on Tue Nov 01 19:37:16 2016

@author: admin
"""
import os
import sys
import numpy as np
import tensorflow as tf
import cv2
import random

def gen_random_rotation_matrix(angle):
    c = np.cos(angle)
    s = np.sin(angle)
    return np.array([[c,-s],[s,c]])

def rotate_image(img, angle, zoom=0.5):
    c = np.cos(angle)
    s = np.sin(angle)
    x0,y0 = img.shape[0]/2,img.shape[1]/2
    x1 = int((x0 - y0*s)*zoom+x0)
    y1 = int((x0 + y0*c)*zoom+y0)
    x2 = int((x0 + y0*s)*zoom+x0)
    y2 = int((y0 - x0*c)*zoom+y0)
    x3 = int((x0 - y0*s)*zoom+x0+0.5)
    y3 = int((y0 + x0*c)*zoom+y0+0.5)
    x4 = int((x0 + y0*s)*zoom+x0+0.5)
    y4 = int((y0 - x0*c)*zoom+y0+0.5)
    warp_matrix = np.array([[x1, y1], [x2, y2], [x3, y3], [x4, y