

"""

# Write your code here.
def coffee_pull(robot):
    # Steps:
    #  1. Put gripper above mug
    #  2. Drop gripper around mug
    #  3. Close gripper around mug
    #  4. Pull mug to goal
    if check("the robot's gripper is not above the mug"):
        robot.move_gripper("above the mug")
    # If the gripper isn't around the mug, put it around the mug.
    if check("the robot's gripper is not around mug and the robot's gripper is open"):
        robot.move_gripper("near the mug", close_gripper=True)
    # If the gripper is near the mug and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above mug and the robot's gripper is closed"):
        robot.move_gripper("near the target location")

"""
Now, I'm going to have you solve 20 test cases.

Some of them might require modifying the programs you've already written.
"""

"""
### Test 1

In this test case, the target for the reach-task is just in front of the robot.
"""

"""
### Test 2

In this test case, the target for the reach-task is just to the robot's left.
"""

"""
### Test 3

In this test case, the robot has to reach to the target on top of a tall pillar.
"""

"""
### Test 4

In this test case, the robot has to reach to the target inside a box.
"""

"""
### Test 5

In this test case, the robot has to move the drawer handle in front of it.
"""

"""
### Test 6

In this test case, the robot has to move the drawer handle slightly below it.
"""

"""
### Test 7

In this test case, the robot has to move the drawer handle above it.
"""

"""
### Test 8

In this test case, the robot has to move the door handle in front of it.
"""

"""
### Test 9

In this test case, the robot has to move the door handle slightly below it.
"""

"""
### Test 10

In this test case, the robot has to move the door handle above it.
"""

"""
