
    a. 1. Put gripper to left of window handle  2. Start pushing against the window handle to open the window  3. Push the window open harder
    b. 1. Put gripper on window handle  2. Start pulling the window open  3. Slide the window open
    c. 1. Put gripper right of window handle  2. Start pulling on window handle to open the window  3. Pull the window open harder
    d. 1. Put gripper right of window handle  2. Start pulling on the window handle to open the window  3. Open the window
    If the window handle is not left of the robot's gripper, put it to the left.
    - When the window handle is not left of the robot's gripper and the robot's gripper is not near the window handle, the robot should put gripper to left of window handle.
    If the robot's gripper is near the window handle and is not in front of the window handle we can probably start sliding the window.
    - When the robot's gripper is near the window handle and the robot's gripper is not in front of the window handle, the robot should start sliding window to left.
    If the robot's gripper is left of the window handle and the robot's gripper is not in front of the window handle then it's time to pull harder.
    - When the robot's gripper is left of the window handle and the robot's gripper is not in front of the window handle, the robot should pull the window open harder.
"""
[eod] [code]from __future__ import division
import math

def mean(data):
    sum = 0
    for el in data:
        sum += el
    mean = sum / len(data)
    return round(mean, 2)

def median(data):
    if len(data) % 2 == 0:
        return mean([data[len(data) / 2], data[len(data) / 2 - 1]])
    else:
        return data[len(data) // 2]

def mode(data):
    def counter(el):
        c = 0
        for i in data:
            if i == el:
                c += 1
        return c
    return max(data, key=counter)

def weighted_average(values, weights):
    s1 = sum(values)
    s2 = sum(weights)
    avg = s1 / s2
    return