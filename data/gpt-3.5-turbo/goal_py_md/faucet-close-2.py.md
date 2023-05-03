```
# faucet-close: turn the faucet right
def faucet_close(robot):
    # Steps:
    #  1. Put gripper around the faucet handle
    #  2. Turn the handle right to close the faucet
    # First, put the gripper around the faucet handle.
    if check("the robot's gripper is not around the faucet handle"):
        robot.move_gripper("around the faucet handle")
    # Once the gripper is around the faucet handle, turn the handle right to
    # close the faucet.
    if check("the robot's gripper is around the faucet handle"):
        robot.move_gripper("horizontally aligned with the faucet handle")
```