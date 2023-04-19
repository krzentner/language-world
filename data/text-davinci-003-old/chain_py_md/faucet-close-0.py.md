

Steps: 
1. Put gripper above faucet handle
2. Drop gripper around faucet handle
3. Turn the faucet handle to the right

```
# faucet-close: turn the faucet right
# def faucet_close(robot):
    # Steps:
    #  1. Put gripper above faucet handle
    #  2. Drop gripper around faucet handle
    #  3. Turn the faucet handle to the right
    # Put the gripper above the faucet handle.
    if check("the robot's gripper is not above the faucet handle"):
        robot.put("gripper above faucet handle")
    # If the gripper isn't around the faucet handle, put it around the faucet
    # handle.
    if check("the robot's gripper is not around faucet handle and the robot's gripper is open"):
        robot.drop("gripper around faucet handle")
    # If the gripper is near the faucet handle, we can turn it to the right to
    # close it.
    if check("the robot's gripper is near the faucet handle"):
        robot.turn("faucet handle to the right")