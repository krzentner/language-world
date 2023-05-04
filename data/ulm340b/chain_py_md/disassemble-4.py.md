

and add lines to make the robot successfully perform the `disassemble` task.
*/

/**
 * Your code here
 */

# disassemble: pull the wrench off the peg
def disassemble(robot):
    # Steps:
    #  1. Put gripper around the wrench
    #  2. Close gripper around the wrench
    #  3. Pull wrench away from peg
    # First, put the gripper around the wrench.
    if check("the robot's gripper is not around wrench"):
        robot.grab("wrench")
    # If the gripper is mostly around the wrench, close the gripper all the way
    # to grab the wrench.
    # Since the peg is long, check if the gripper is forward aligned with it.
    if check("the robot's gripper is not forward aligned with wrench"):
        robot.close("gripper around wrench")
    # Once the robot has a grip on the wrench, we can pull it away from the peg.
    if check("the robot's gripper is vertically aligned with wrench"):
        robot.pull("wrench away from peg")

//# sourceMappingURL=15_control_robot.js.map[eod] [code]# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 17:57:57 2018

@author: zhu
"""
import time
import datetime
import numpy as np
from datetime import timedelta

def time_format(secs):
    '''
    secs:时间
    time:返回分钟数
    '''
    time = int(secs)
    timeArray = timedelta(seconds=secs)
    if time < 60:
        result = str(time) + '秒'
    else:
        result = str(time // 60) + '分' + str(time % 60) + '秒'
    return result

def testTime(start, end):
    # start = time.time()
    # end = time.time()
    print(start, end)
    # duration = end - start
    # print(duration)
    
    # print(start, end)
    duration = end - start
    print(duration)
    print(time_format(duration))
    
    
testTime(time.time(), time.time())
[eod] [code]from .base import