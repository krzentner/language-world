

Then, the program would look like this:

```
# faucet-close: turn the faucet right
def faucet_close(robot):
    if check("the robot's gripper is not parallel with the faucet handle and the robot's gripper is below the faucet handle"):
        robot.move("gripper to right of faucet handle")
    if check("the robot's gripper is near the faucet handle"):
        robot.turn("faucet right")
    if check("the robot's gripper is in front of the faucet handle"):
        robot.push("faucet right harder")
```