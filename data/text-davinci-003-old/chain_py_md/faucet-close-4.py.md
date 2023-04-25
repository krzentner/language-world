

Steps:
1. Put gripper above the faucet handle
2. Drop gripper around the faucet handle
3. Turn the gripper right to close the faucet

```
# faucet-close: turn the faucet right
# def faucet_close(robot):
    # Steps:
    #  1. Put gripper above the faucet handle
    #  2. Drop gripper around the faucet handle
    #  3. Turn the gripper right to close the faucet
    if check("the robot's gripper is not vertically aligned with the faucet handle"):
        robot.put("gripper above faucet handle")
    if check("the robot's gripper is vertically aligned with the faucet handle and the robot's gripper is not around faucet handle"):
        robot.drop("gripper around faucet handle")
    if check("the robot's gripper is around faucet handle"):
        robot.turn("gripper right")
```