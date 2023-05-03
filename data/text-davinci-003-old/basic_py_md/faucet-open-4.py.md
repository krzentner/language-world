

```
# faucet-open: turn the faucet left
# def faucet_open(robot):
    if check("the robot's gripper is not horizontally aligned with the faucet"):
        robot.put("gripper above faucet")
    if check("the robot's gripper is forward aligned with the faucet and the robot's gripper is not around the faucet"):
        robot.grab("faucet handle")
    if check("the robot's gripper is around the faucet"):
        robot.turn("faucet left")
```