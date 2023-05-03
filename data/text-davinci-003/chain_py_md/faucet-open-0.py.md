

The robot will need to open a faucet.

Steps:
 1. Put the gripper above the faucet handle
 2. Drop the gripper around the faucet handle
 3. Turn the faucet left

```
# faucet-open: turn the faucet left
def faucet_open(robot):
    # Steps:
    #  1. Put gripper above faucet handle
    #  2. Drop gripper around faucet handle
    #  3. Turn the faucet left
    # First, put the gripper roughly above the faucet handle.
    if check("the robot's gripper is not vertically aligned with the faucet handle"):
        robot.put("gripper above faucet handle")
    # If the gripper isn't around the faucet handle, put it around the faucet
    # handle.
    if check("the robot's gripper is not around faucet handle and the robot's gripper is open"):
        robot.drop("gripper around faucet handle")
    # Assuming the gripper is near the faucet handle and closed, turn the faucet
    # left.
    if check("the robot's gripper is near faucet handle and the robot's gripper is closed"):
        robot.turn("faucet left")
```