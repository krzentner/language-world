

The steps are as follows:

1. Put the gripper in front of the faucet handle
2. Grip the handle and turn it counter-clockwise 

```
# faucet-open: turn the faucet left
# def faucet_open(robot):
    # Steps:
    #  1. Put gripper in front of the faucet handle
    #  2. Grip the handle and turn it counter-clockwise
    if check("the robot's gripper is not in front of the faucet handle"):
        robot.move_gripper("in front of the faucet handle", close_gripper=True)
    # If the gripper is in front of the faucet handle and the gripper is open, 
    # grab the handle to start turning the faucet.
    if check("the robot's gripper is in front of the faucet handle and the robot's gripper is open"):
        robot.move_gripper("above the faucet handle")
    # If the gripper is around the handle and closed, turn the handle 
    # counter-clockwise to start the flow of water.
    if check("the robot's gripper is around the faucet handle and the robot's gripper is closed"):
        robot.move_gripper("turned counter-clockwise")
```