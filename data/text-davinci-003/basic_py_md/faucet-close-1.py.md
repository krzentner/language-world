

Then add the following lines of code:

```
    if check("the robot's gripper is not near faucet"):
        robot.grab("faucet handle")
    if check("the robot's gripper is near the faucet and the robot's gripper is not around faucet handle"):
        robot.put("gripper around faucet handle")
    if check("the robot's gripper is around faucet handle"):
        robot.turn("faucet right")
```