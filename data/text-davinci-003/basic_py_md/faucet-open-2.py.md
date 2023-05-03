

Then, fill in the function:

```
# faucet-open: turn the faucet left
def faucet_open(robot):
    if check("the robot's gripper is not above the faucet handle"):
        robot.put("gripper above faucet handle")
    if check("the robot's gripper is not around the faucet handle"):
        robot.drop("gripper around faucet handle")
    if check("the robot's gripper is around the faucet handle"):
        robot.turn("faucet left")
```