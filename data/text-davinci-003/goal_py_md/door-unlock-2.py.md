

## Solution

```
# door-unlock: turn the dial on the door
# def door_unlock(robot):
    # Steps:
    #  1. Put gripper above dial
    #  2. Drop gripper around dial
    #  3. Rotate the dial
    # First, put the gripper above the dial.
    if check("the robot's gripper is not vertically aligned with dial"):
        robot.move_gripper("vertically aligned with the dial", close_gripper=True)
    # As long as the gripper is aligned with the dial, moving the gripper
    # slightly to the right of it should allow us to grab the dial.
    if check("the robot's gripper is vertically aligned with dial"):
        robot.move_gripper("right of the dial")
    # Once we have a grip on the dial, rotate it to the desired point.
    if check("the robot's gripper is around dial"):
        robot.rotate_gripper("to the desired point")
```