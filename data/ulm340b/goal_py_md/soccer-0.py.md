

If you can't complete the entire program, please fill in as many `if`/`check` statements as you can.
`soccer` and `football` are different names for the same sport.
*/

# Step 1. Move the gripper to the top of the ball, since the robot doesn't have any objects to grab
# Step 2. Push the gripper into the top of the ball, since the gripper doesn't have any objects to slide
# Step 3. Slide the ball to the goal

# soccer: push the soccer ball into the target location
def soccer(robot):
    if check("the robot's gripper is not above the soccer ball"):
        robot.move_gripper("above the soccer ball")
    if check("the soccer ball is not below the robot's gripper and the robot's gripper is not near the soccer ball"):
        robot.move_gripper("vertically aligned with the soccer ball", close_gripper=True)
    if check("the robot's gripper is near the soccer ball and the soccer ball is below the robot's gripper"):
        robot.move_gripper("above the target location")[eod] [code]#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   18.44.电话号码的字母组合.py
@Time    :   2020/08/04 18:13:47
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
# https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (56.89%)
# Likes:    896
# Dislikes: 0
# Total Accepted:    136.4K
# Total Submissions: 239.1K
# Testcase Example:  '"23"'
#
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
#
# 给出数字到字