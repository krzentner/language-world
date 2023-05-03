

The code for `faucet_close` should be:

```
# faucet-close: turn the faucet right
def faucet_close(robot):
    if check("the robot's gripper is not near the faucet handle"):
        robot.move("gripper near the faucet handle")
    if check("the robot's gripper is near the faucet handle"):
        robot.turn("faucet right")
```