

We are done!
"""

def box_close(robot):
    # Steps:
    #  1. Pick up the box lid
    #  2. Move the box lid to above the box
    #  3. Drop the box lid on the box
    # First, put the gripper above the lid so that we don't bump it while trying
    # to grab it.
    if check("the robot's gripper is not above the lid"):
        robot.move_gripper("above the lid")
    # Put the gripper around the lid.
    if check("the robot's gripper is not around the lid and the robot's gripper is open"):
        robot.move_gripper("near the lid", close_gripper=True)
    # Now that the gripper is near the lid, we might be able to grab it by
    # closing the gripper.
    if check("the robot's gripper is around the lid and the robot's gripper is closed"):
        robot.move_gripper("above the box")
    # Move the box lid over the box by moving the robot's gripper.
    if check("the robot's gripper is forward aligned with the box"):
        robot.move_gripper("above the box")
    # Place the lid on the box.
    if check("the robot's gripper is above the box"):
        robot.move_gripper("near the box")


[eod] [code]'''
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

'''


class Solution:
    def combinationSum(self, candidates: list, target: int) -> list:
        ans =