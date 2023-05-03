

We want the robot to turn the faucet clockwise to close it.

```
# faucet-close: turn the faucet right
def faucet_close(robot):
    # Steps:
    #  1. Put the gripper below the faucet handle
    #  2. Grab the faucet handle with the gripper
    #  3. Turn the faucet handle clockwise
    # First, put the gripper below the faucet handle.
    if check("the robot's gripper is not below the faucet handle"):
        robot.put("gripper below faucet handle")
    # If the faucet handle is not in the gripper, try to grab it by moving the
    # gripper downwards.
    if check("the robot's gripper is below the faucet handle and the robot's gripper is not around the faucet handle"):
        robot.grab("faucet handle")
    # If the faucet handle is in the gripper, turn it clockwise.
    if check("the robot's gripper is around the faucet handle"):
        robot.turn("faucet handle clockwise")
```