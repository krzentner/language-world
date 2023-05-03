

Then add the code:

```
    # Steps:
    #  1. Put gripper left of the faucet handle
    #  2. Grip the faucet handle with the gripper
    #  3. Push the handle to the right
    # First, make sure the gripper is to the left of the faucet handle.
    if check("the robot's gripper is not left of the faucet handle"):
        robot.move_gripper("left of the faucet handle")
    # Once the gripper is to the left, close the gripper to hold the handle.
    if check("the robot's gripper is left of the faucet handle and the robot's gripper is open"):
        robot.move_gripper("above the faucet handle", close_gripper=True)
    # With the gripper closed, push the handle to the right to turn it off.
    if check("the robot's gripper is left of the faucet handle and the robot's gripper is closed"):
        robot.move_gripper("right of the faucet handle")
```