

Then continue by writing code:

```
# faucet-close: turn the faucet right
# def faucet_close(robot):
    # Steps:
    #  1. Put gripper above faucet
    #  2. Drop gripper around the faucet handle
    #  3. Turn the faucet handle to the right
    # First, put the gripper above the faucet handle.
    if check("the robot's gripper is not above the faucet"):
        robot.move_gripper("above the faucet")
    # If the gripper isn't around the faucet, put it around the faucet.
    if check("the robot's gripper is not around faucet and the robot's gripper is open"):
        robot.move_gripper("near the faucet", close_gripper=True)
    # If the gripper is near the faucet and open, close the gripper so that we
    # have control of the faucet handle.
    if check("the robot's gripper is near the faucet and the robot's gripper is closed"):
        robot.move_gripper("right of the faucet")
    # Once we're lined up with the faucet, rotate it to the right.
    if check("the robot's gripper is right of the faucet"):
        robot.move_gripper("right of the faucet handle")
```