

""",
    'hints': [
        'Try to get the robot to perform the first task first.',
        'Try writing code that uses some of the same steps as a previous task.',
        'This task is just like the `button-press-topdown` task, except that the robot has to approach the handle from the side, like the "drawer-open" task.'
    ]
}


def handle_press_side(robot):
    # Steps:
    #  1. Put gripper near the handle
    #  2. Push down on the handle from the side
    # We don't need to be careful about the direction, since the handle is
    # large and we're just pushing it (unlike when opening the drawer).
    if check("the robot's gripper is not forward aligned with handle"):
        robot.move_gripper("forward aligned with handle")
    # Now that the gripper is lined up, just push down on the handle.
    if check("the robot's gripper is forward aligned with handle"):
        robot.move_gripper("near handle")
[eod] [code]'''

The Fibonacci numbers, commonly denoted F(n) form a sequence,
called the Fibonacci sequence, such that each number is the sum of the two preceding ones,
starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.

Given N, calculate F(N).



Example 1:

Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.


Note:

0 ≤ N ≤ 30.


'''

class Solution:
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        a, b = 0, 1
        i = 0
        while i < N: