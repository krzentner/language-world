

Then write the code:

```
# faucet-close: turn the faucet right
def faucet_close(robot):
    # Steps:
    #  1. Put gripper to the right of the faucet handle
    #  2. Grasp the faucet handle
    #  3. Turn the faucet handle to the right
    # First, put the gripper to the right of the faucet handle.
    if check("the robot's gripper is not right of the faucet handle"):
        robot.move_gripper("right of the faucet handle")
    # If the faucet handle is left of the robot's gripper, grab the handle.
    if check("the faucet handle is left of the robot's gripper"):
        robot.move_gripper("near the faucet handle", close_gripper=True)
    # If the gripper is around the faucet handle, turn the faucet handle to the
    # right.
    if check("the robot's gripper is around the faucet handle"):
        robot.move_gripper("right of the faucet handle")
```