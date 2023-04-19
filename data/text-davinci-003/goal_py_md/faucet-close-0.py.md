

The robot should turn the faucet clockwise (right) to close the faucet.

```
# faucet-close: turn the faucet right
# def faucet_close(robot):
    # Steps:
    #  1. Put gripper above the handle of faucet
    #  2. Drop the gripper to hold the handle
    #  3. Push the handle right to close the faucet
    # First, put the gripper above the handle of the faucet.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move_gripper("vertically aligned with the handle", close_gripper=True)
    # If the robot's gripper is lined up with the handle but not near it, drop
    # the gripper to hold the handle.
    if check("the robot's gripper is vertically aligned with the handle and the robot's gripper is not around the handle"):
        robot.move_gripper("around the handle")
    # Once the gripper is around the handle, push the handle right to close the
    # faucet.
    if check("the robot's gripper is around the handle and the handle is not right of the robot's gripper"):
        robot.move_gripper("right of the handle")
```