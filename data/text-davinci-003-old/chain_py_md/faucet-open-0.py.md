

The steps for this task are: 

1. Put gripper above the faucet handle
2. Drop gripper around the faucet handle
3. Turn the faucet handle left

```
# faucet-open: turn the faucet left
# def faucet_open(robot):
    # Steps:
    #  1. Put gripper above the faucet handle
    #  2. Drop gripper around the faucet handle
    #  3. Turn the faucet handle left
    # First, put the gripper roughly above the faucet handle.
    if check("the robot's gripper is not vertically aligned with faucet handle"):
        robot.put("gripper above faucet handle")
    # Once the gripper is lined up above the faucet handle, we should be able to
    # grab the faucet handle by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with faucet handle and the robot's gripper is not around faucet handle"):
        robot.drop("gripper around faucet handle")
    # Once the gripper is around the faucet handle, we can just turn it left.
    if check("the robot's gripper is around faucet handle"):
        robot.turn("faucet left")
```