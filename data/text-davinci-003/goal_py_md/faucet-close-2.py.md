

Here's the solution: 
```
# faucet-close: turn the faucet right
def faucet_close(robot):
    # Steps:
    #  1. Put gripper above faucet handle
    #  2. Drop gripper around faucet handle
    #  3. Turn the faucet clockwise
    # First, put the gripper above the faucet handle.
    if check("the robot's gripper is not almost vertically aligned with the faucet handle"):
        robot.move_gripper("almost vertically aligned with the faucet handle", close_gripper=True)
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is vertically aligned with the faucet handle"):
        robot.move_gripper("clockwise around the faucet handle")
    # If it's lined up clockwise, turn it to the right.
    if check("the robot's gripper is clockwise around the faucet handle"):
        robot.move_gripper("above the faucet handle")
```