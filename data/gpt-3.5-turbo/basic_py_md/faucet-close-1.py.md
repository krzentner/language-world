Here is a program to perform the `faucet-close` task:

```
# faucet-close: turn the faucet right
def faucet_close(robot):
    if check("the robot's gripper is not near the faucet handle"):
        robot.put("gripper above faucet handle")
    if check("the robot's gripper is around faucet handle and faucet is not off"):
        robot.turn("faucet right")
```

Note that this code assumes that the robot's gripper is able to turn the faucet handle clockwise to turn it off. 
Also, the function uses the `check` function to verify if the gripper is in the right position and if the faucet is still on or not.