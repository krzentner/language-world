```
# faucet-close: turn the faucet right
# def faucet_close(robot):
    if check("the robot's gripper is not near faucet handle"):
        robot.move("gripper to the right of faucet handle")
    if check("the robot's gripper is near faucet handle"):
        robot.push("faucet handle right")
```