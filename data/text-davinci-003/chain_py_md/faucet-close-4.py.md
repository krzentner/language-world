

Solution:
```
# faucet-close: turn the faucet right
def faucet_close(robot):
    # Steps:
    #  1. Put gripper above faucet handle
    #  2. Drop gripper around faucet handle
    #  3. Turn faucet to the right to close it
    # First, put the gripper mostly above the faucet handle.
    if check("the robot's gripper is not almost vertically aligned with faucet handle"):
        robot.put("gripper above faucet handle")
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is almost vertically aligned with the faucet handle and the robot's gripper is open"):
        robot.put("gripper around faucet handle")
    # Once the gripper is around the handle, we can rotate the faucet handle
    # clockwise or counterclockwise to close it.
    if check("the robot's gripper is around faucet handle"):
        robot.turn("right to close faucet")
```