

Steps:
1. Put gripper above the faucet handle
2. Grab the faucet handle with the gripper
3. Rotate the faucet handle clockwise

```
# faucet-close: turn the faucet right
# def faucet_close(robot):
    # Steps:
    #  1. Put gripper above the faucet handle
    #  2. Grab the faucet handle with the gripper
    #  3. Rotate the faucet handle clockwise
    if check("the robot's gripper is not above the faucet handle"):
        robot.put("gripper above faucet handle")
    if check("the robot's gripper is not around the faucet handle and the robot's gripper is open"):
        robot.grab("faucet handle")
    if check("the robot's gripper is around the faucet handle and the robot's gripper is closed"):
        robot.rotate("faucet handle clockwise")
```