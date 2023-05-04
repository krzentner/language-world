
'''


# button-press-wall: push the button from the front with a short wall in the way
def button_press_wall(robot):
    # Steps:
    #  1. Put gripper left of the button
    #  2. Start pushing against the button
    #  3. Push the button harder
    # If the the button is right of the robot's gripper, we should move the
    # gripper near the button to start pushing
    if check("the button is right of the robot's gripper"):
        robot.move_gripper("left of the button")
    # If the robot's gripper is near the button we can probably push harder now.
    if check("the robot's gripper is near the button"):
        robot.move_gripper("forward aligned with the button")
[eod] [code]class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)

        if len(self.min_stack) == 0 or x <= self.min_stack[-1]:
            self.min_stack.append(x)
        self.min_stack.append(self.min_stack[-1])

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]
[eod] [code]#!/usr/bin/python2

import sys,os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from scipy.optimize import curve_fit

font = {'family':'serif',
        'serif':['Helvetica'],
        'size':14}
rc('font', **font)

def main():
  for fname in os.listdir("."):
    if ".pdf" in fname and not "fit" in fname:
      f,ax = plt.subplots()