

and finish the function with a program that performs the following steps:

1. Put gripper left of the window handle
2. Push against the window handle to pull it open
3. Keep pulling the window open

### Hint

1. Start with something simple, like moving the gripper right of the window handle.
2. Add steps to make it more robust.
3. Try out your program on several tasks, especially the task you're trying to solve.



"""


"""

# window-open: slide the window open to the left
def window_open(robot):
    """
    if check("the window handle is left of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move("gripper to right of window handle")
    if check("the robot's gripper is near the window handle"):
        robot.slide("window left")
    """
    
    if check("the window handle is right of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move("gripper to left of window handle")
    if check("the robot's gripper is near the window handle"):
        robot.slide("window left")
    if check("the robot's gripper is left of the window handle"):
        robot.slide("window left harder")


[eod] [code]#!/usr/bin/python
"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path
such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: sum: the sum
    @return: true if have root-to-leaf path with given sum else false
    """

    def hasPathSum(self, root, sum):
        if root is None