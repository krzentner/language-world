

'''

# lever-pull: rotate the lever up
def lever_pull(robot):
    # Steps:
    #  1. Put gripper above lever
    #  2. Drop gripper around lever
    #  3. Pull the lever up
    # We need to put the gripper above the lever before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with the lever"):
        robot.put("gripper above lever")
    # Once the gripper is lined up above the lever, we should be able to
    # grab the lever by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with lever and the robot's gripper is not around lever"):
        robot.put("gripper around lever")
    # Once the gripper is around the lever, we can just pull the lever.
    if check("the robot's gripper is around lever"):
        robot.pull("lever up")
[eod] [code]class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs, key = lambda x: x[0])
        res = 0
        left = pairs[0][0]
        for i in range(1, len(pairs)):
            if pairs[i][0] >= left:
                res += 1
                left = pairs[i][1]
        return res
[eod] [code]class Solution:
    def __init__(self):
        self.res = -1
        
    def maxProduct(self, nums: List[int]) -> int:
        self.dfs(nums, [])
        return self.res
        
    def dfs(self, nums, temp):
        if len(nums) == 0:
            self.res = max(self.res, self._maxProduct(temp))
        
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i+1:], temp+[nums[i]])
        
    def _maxProduct(self, temp):
        m, res = 1, 1
        for x in temp:
            m = max(m*x, x)
            res = max(m, res)
        return res
[eod] [code]from setuptools import setup, find_packages

