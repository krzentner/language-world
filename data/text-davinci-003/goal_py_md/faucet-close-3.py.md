

Solution:

```
# faucet-close: turn the faucet right
# def faucet_close(robot):
    # Steps:
    #  1. Put gripper above faucet handle
    #  2. Drop gripper around faucet handle
    #  3. Turn faucet right
    # First, put the gripper above the faucet handle before we can grab it.
    if check("the robot's gripper is not vertically aligned with faucet handle"):
        robot.move_gripper("vertically aligned with the faucet handle")
    # If the faucet is not near the gripper, move the gripper to be near the
    # faucet.
    if check("the robot's gripper is vertically aligned with the faucet handle and the robot's gripper is not near the faucet handle"):
        robot.move_gripper("near the faucet handle")
    # Once the gripper is lined up above the faucet handle, we should be able to
    # grab the faucet handle by moving the gripper down around it.
    if check("the robot's gripper is near the faucet handle"):
        robot.move_gripper("around the faucet handle", close_gripper=True)
    # Once the gripper is around the faucet handle, we can just turn the faucet
    # right.
    if check("the robot's gripper is around the faucet handle"):
        robot.move_gripper("right of the faucet handle")
```