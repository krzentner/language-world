

Solution:
```
# faucet-close: turn the faucet right
# def faucet_close(robot):
    if check("the robot's gripper is not near the faucet handle"):
        robot.move("gripper above faucet handle")
    if check("the robot's gripper is near the faucet handle and the robot's gripper is not around the faucet handle"):
        robot.grab("faucet handle")
    if check("the robot's gripper is around the faucet handle"):
        robot.turn("faucet right until closed")
```