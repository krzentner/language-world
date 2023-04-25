

The following code will turn the faucet open:

```
# faucet-open: turn the faucet left
# def faucet_open(robot):
    # Steps:
    #  1. Put gripper near the top of the faucet handle
    #  2. Push faucet handle to the left
    # First, put the gripper near the top of the faucet handle.
    if check("the robot's gripper is not above the faucet handle"):
        robot.move_gripper("above the faucet handle")
    # If the gripper is near the faucet handle but not lined up with it, line
    # it up.
    if check("the robot's gripper is not horizontally aligned with the faucet handle"):
        robot.move_gripper("horizontally aligned with the faucet handle")
    # Once the gripper is lined up with the faucet handle, push the handle to
    # the left.
    if check("the robot's gripper is horizontally aligned with the faucet handle"):
        robot.move_gripper("slightly left of the faucet handle")
```