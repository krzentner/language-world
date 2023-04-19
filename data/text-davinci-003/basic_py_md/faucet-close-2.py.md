

Solution: 

```
# faucet-close: turn the faucet right
# def faucet_close(robot):
    if check("the robot's gripper is not above the faucet handle"):
        robot.place("gripper above faucet handle")
    if check("the robot's gripper is not around the faucet handle"):
        robot.drop("gripper around faucet handle")
    if check("the robot's gripper is near the faucet handle"):
        robot.close("gripper around faucet handle")
    if check("the robot's gripper is almost vertically aligned with faucet handle"):
        robot.turn("faucet right")
```