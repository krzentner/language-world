

"""

# door-open: pull the door open
def door_open(robot):
    # Steps:
    #  1. Put gripper near door handle
    #  2. Grab the door handle
    #  3. Pull open the door
    # First, move the gripper near the door handle
    if check("the robot's gripper is not near the door handle"):
        robot.move_gripper("near the door handle")
    # If the door is aligned with the gripper as seen from in front, we can grab
    # the door handle.
    if check("the robot's gripper is forward aligned with the door handle"):
        robot.move_gripper("around the door handle")
    # Once the gripper is around the door handle, we can just pull the door open.
    if check("the robot's gripper is around the door handle"):
        robot.move_gripper("horizontally aligned with the door handle")


"""
Thank you, that will be all.
"""
[eod] [code]import unittest

from test_runner.helpers import get_input
from test_runner.helpers import check_result, run

# The input/output tests below were created based on a manual analysis
# of the example code.

INPUT_1 = '4,3,2,1,0'
OUTPUT_1 = '1,2,3,4,0,0,0,0,0'

INPUT_2 = '1,9,10,3,2,3,11,0,99,30,40,50'
OUTPUT_2 = '1,9,10,3,2,3,11,0,99,30,40,50,0,99,11,30,40,30,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0'


class TestPushswap(unittest.TestCase):
    def test_input1(self):
        input = get_input(INPUT_1)
        output = run(input)
        check_result(output, OUTPUT_1)

    def test_input2(self):
        input = get_input(INPUT_2)
        output = run(input)
       