

Then add code to perform the task:

```
# faucet-close: turn the faucet right
def faucet_close(robot):
    # Steps:
    #  1. Put gripper right of the faucet handle
    #  2. Rotate the faucet handle clockwise
    # First, we need to put the gripper to the right of the faucet handle.
    # We should line it up from the side rather than from above, because the
    # faucet handle is round.
    if check("the robot's gripper is not side aligned with faucet handle"):
        robot.move_gripper("side aligned with the faucet handle", close_gripper=True)
    # Once the gripper is aligned with the faucet handle, rotate it clockwise
    # to turn the faucet off.
    if check("the robot's gripper is aligned with the faucet handle"):
        robot.move_gripper("clockwise around the faucet handle")
```