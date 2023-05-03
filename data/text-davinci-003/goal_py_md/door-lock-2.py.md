

## Answer

```
# door-lock: turn the dial on the door
def door_lock(robot):
    # Steps:
    #  1. Put gripper above dial
    #  2. Line up with the dial
    #  3. Turn the dial
    #  The robot can turn the dial by aligning the gripper with the dial and
    #  pushing it in the right direction.
    # If the gripper is not above the dial, it needs to be moved to the dial.
    if check("the robot's gripper is not vertically aligned with dial"):
        robot.move_gripper("vertically aligned with the dial")
    # If the gripper is above the dial and the dial isn't lined up with the
    # robot's gripper, the robot needs to move its gripper to the dial to align
    # it.
    if check("the robot's gripper is vertically aligned with dial and the dial is not aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the dial", close_gripper=True)
    # Once the dial is lined up, the robot can turn it by pushing.
    if check("the robot's gripper is forward aligned with the dial"):
        robot.move_gripper("around the dial")