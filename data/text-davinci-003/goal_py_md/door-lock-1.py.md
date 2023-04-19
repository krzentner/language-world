

Here is the program to perform the task `door-lock`:

```
# door-lock: turn the dial on the door
# def door_lock(robot):
    # Steps:
    #  1. Put gripper near the lock's dial
    #  2. Turn the dial to the left
    #  3. Turn the dial to the right
    # We need to put the gripper near the lock's dial before we can turn it.
    if check("the robot's gripper is not near the dial"):
        robot.move_gripper("near the dial")
    # If the gripper is near the dial and orientated properly, turn the dial
    # to the left.
    if check("the robot's gripper is near the dial and it is in the correct orientation"):
        robot.move_gripper("left of the dial")
    # We don't know how far the dial needs to be turned, so turn it to the right
    # until the door unlocks.
    if check("the robot's gripper is right of the dial"):
        robot.move_gripper("right of the dial")

```