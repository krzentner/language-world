

Here's the code for that task:

```
# faucet-close: turn the faucet right
def faucet_close(robot):
    # Steps:
    #  1. Put gripper above faucet handle
    #  2. Drop gripper around faucet handle
    #  3. Turn faucet to the right to close
    # First, put the gripper above the faucet handle.
    if check("the robot's gripper is not almost vertically aligned with faucet handle"):
        robot.move_gripper("almost vertically aligned with the faucet handle", close_gripper=True)
    # Once the gripper is lined up above the faucet handle, we should be able to
    # grab the faucet handle by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with faucet handle and the robot's gripper is not around faucet handle"):
        robot.move_gripper("around the faucet handle")
    # Once the gripper is around the faucet handle, turn it to the right to close it.
    if check("the robot's gripper is around faucet handle"):
        robot.move_gripper("right of the faucet handle")
```