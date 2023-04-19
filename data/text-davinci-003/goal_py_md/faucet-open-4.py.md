

The Steps that need to be taken are as follows:

1. Put the gripper above the faucet handle
2. Drop the gripper around the faucet handle 
3. Turn the faucet to the desired direction (in this case, left)

```
# faucet-open: turn the faucet left
# def faucet_open(robot):
    # Steps:
    #  1. Put gripper above the faucet handle
    #  2. Drop gripper around the faucet handle 
    #  3. Turn the faucet to the left
    # First, put the gripper mostly above the faucet handle.
    if check("the robot's gripper is not vertically aligned with faucet handle"):
        robot.move_gripper("vertically aligned with the faucet handle")
    # Once the gripper is lined up above the faucet handle, we should be able to
    # grab the faucet handle by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with faucet handle and the robot's gripper is not around faucet handle"):
        robot.move_gripper("around the faucet handle")
    # Once the gripper is around the faucet handle, we can just turn the faucet 
    # to the left.
    if check("the robot's gripper is around faucet handle"):
        robot.turn_gripper("left")
```