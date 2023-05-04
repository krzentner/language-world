

You will also need to provide an example test:

```
# test door-unlock
```

Then describe how to `door-unlock` in the test and your solution.

(We provide some sample code in `robot_code_template.py`. You can edit that code if you want.)
"""

"""
Door-unlock

-Steps:
1.Put the gripper near the dial.
2.Line up the gripper with the dial.
3.Grab the dial.
4.Turn the dial in the right direction.

"""

# door-unlock: turn the dial on the door
def door_unlock(robot):
    # If the robot's gripper is not near the dial, move the gripper to the dial
    if check("the robot's gripper is not close to the door's dial"):
        robot.move_gripper("near the door's dial")
    # If the gripper is near the door's dial, put the gripper near the door's dial.
    if check("the robot's gripper is near the door's dial and the robot's gripper is not almost vertically aligned with door's dial"):
        robot.move_gripper("near the door's dial")
    # If the robot's gripper is near the door's dial, move it around the door's dial.
    if check("the robot's gripper is near the door's dial and the robot's gripper is not around the door's dial"):
        robot.move_gripper("around the door's dial")
    # If the gripper is around the door's dial, move the door's dial by moving the gripper.
    if check("the robot's gripper is around the door's dial"):
        robot.move_gripper("vertically aligned with the door's dial")

# test door-unlock
test_door_unlock_1 = [  # start state
    (138.13446044921875, -12.479935646057129, 16.98980140686035, 1.5707963519305967, 0, 0, 0),
]
test_door_unlock_2 = [  # start state
    (139.78187561035156, -2