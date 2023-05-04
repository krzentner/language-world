
    Steps: 

The task `plate-slide-forward` requires the robot to slide the plate forward into the target location.
To slide the plate forward into the target location reliably, what steps the robot should perform?
    Steps: 

The task `pick-place-goal` requires the robot to pick up the puck and put it into the goal.
To pick up the puck and put it into the goal reliably, what steps the robot should perform?
    Steps: 

The task `pick-place-goal-far` requires the robot to pick up the puck and put it into the goal.
To pick up the puck and put it into the goal reliably, what steps the robot should perform?
    Steps: 

The task `pick-place-box-far` requires the robot to pick up the puck and put it into the goal.
To pick up the puck and put it into the goal reliably, what steps the robot should perform?
    Steps: 

The task `pick-place-box` requires the robot to pick up the puck and put it into the goal.
To pick up the puck and put it into the goal reliably, what steps the robot should perform?
    Steps: 

The task `pick-place-basket-far` requires the robot to pick up the puck and put it into the basket.
To pick up the puck and put it into the basket reliably, what steps the robot should perform?
    Steps: 

The task `pick-place-basket` requires the robot to pick up the puck and put it into the basket.
To pick up the puck and put it into the basket reliably, what steps the robot should perform?
    Steps: 


"""
[eod] [code]'''
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#先对左子树进行深度优先遍历， 再对右子树进行深度优先遍历



class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root