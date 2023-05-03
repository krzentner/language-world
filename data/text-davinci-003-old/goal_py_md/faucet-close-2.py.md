

Steps:
1. Put gripper above faucet handle
2. Grab faucet handle with the gripper
3. Start turning the faucet right to close it
4. Turn the faucet harder to close it

```
# faucet-close: turn the faucet right
# def faucet_close(robot):
    # Steps:
    #  1. Put gripper above faucet handle
    #  2. Grab faucet handle with the gripper
    #  3. Start turning the faucet right to close it
    #  4. turn the faucet harder to close it
    # First, we need to the put the gripper above the faucet handle.
    if check("the robot's gripper is not above the faucet handle"):
        robot.move_gripper("above the faucet handle")
    # If we've got the gripper above the faucet handle, grab it by moving the
    # gripper around it and closing the gripper.
    if check("the robot's gripper is above the faucet handle"):
        robot.move_gripper("around the faucet handle", close_gripper=True)
    # Now that the gripper is above the handle and grabbing it, we can start to
    # turn the faucet right.
    if check("the robot's gripper is around the faucet handle"):
        robot.move_gripper("right of the faucet handle")
    # Once the faucet is lined up, we have to push a bit harder to turn it all
    # the way.
    if check("the robot's gripper is right of the faucet handle"):
        robot.move_gripper("behind the faucet handle")
```