

Steps:
  1. Put gripper above the faucet handle
  2. Line up the gripper with the faucet handle
  3. Turn the faucet right

```
# faucet-close: turn the faucet right
# def faucet_close(robot):
    # Steps:
    #  1. Put gripper above the faucet handle
    if check("the robot's gripper is not vertically aligned with faucet handle"):
        robot.put("gripper above faucet handle")
    #  2. Line up the gripper with the faucet handle
    if check("the robot's gripper is not vertically aligned with faucet handle"):
        robot.align("gripper with faucet handle")
    #  3. Turn the faucet right
    if check("the robot's gripper is vertically aligned with faucet handle"):
        robot.turn("faucet right")
```