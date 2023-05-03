

The steps for this task are:

1. Put gripper around faucet handle
2. Turn the faucet to the left

# faucet-open: turn the faucet left
# def faucet_open(robot):
    # Steps:
    #  1. Put gripper around faucet handle
    #  2. Turn the faucet to the left
    # Put the gripper around the faucet handle in order to grab it.
    if check("the robot's gripper is not around the faucet handle"):
        robot.grab("faucet handle")
    # If the gripper is still around the faucet handle, turn the faucet handle
    # left to open the faucet.
    if check("the robot's gripper is around the faucet handle"):
        robot.turn("faucet left")