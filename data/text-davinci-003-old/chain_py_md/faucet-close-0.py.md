

Steps:
  1. Put the gripper above the faucet handle
  2. Rotate the handle to the right

```
# faucet-close: turn the faucet right
# def faucet_close(robot):
    # Steps:
    #  1. Put gripper above the faucet handle
    #  2. Rotate the handle to the right
    if check("the robot's gripper is not vertically aligned with the faucet handle"):
        robot.put("gripper above faucet handle")
    # Now that the gripper is lined up, just rotate the handle to the right.
    if check("the robot's gripper is vertically aligned with the faucet handle"):
        robot.turn("right")
```