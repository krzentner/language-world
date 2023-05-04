
    Steps:  1. Put gripper above puck  2. Close gripper around puck  3. Push puck
    Put gripper above puck so that we can see it better
    - When the robot's gripper is not above puck, the robot should place gripper above puck.
    If the robot's gripper is above puck, try to grab it by closing the gripper around it
    - When the robot's gripper is above puck and the robot's gripper is open, the robot should drop gripper around puck.
    If the robot's gripper is around the puck, we can try to push it
    - When the robot's gripper is above puck and the robot's gripper is closed, the robot should push puck.

The task `sweep` requires the robot to sweep the object across the table.
To sweep the object across the table reliably, what steps the robot should perform?
    Steps:  1. Put gripper around object  2. Close gripper on object  3. Push object
    Put gripper around object so that we can see it better
    - When the robot's gripper is not around object, the robot should drop gripper around object.
    If the robot's gripper is around the object, we can try to grab it by closing the gripper around it
    - When the robot's gripper is around object and the robot's gripper is open, the robot should drop gripper around object.
    If the robot's gripper is around the object, we can try to push it
    - When the robot's gripper is around object and the robot's gripper is closed, the robot should push object.


'''[eod] [code]from typing import *

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1
        return count

def test(test_name, nums, expected):
    res = Solution().numIdenticalPairs(nums)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    nums1 = [1,2,3,1,1,3]
    expected1 = 