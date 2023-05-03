# Steps:
    #  1. Put gripper around faucet handle
    #  2. Turn handle left to open
    # First, put the gripper around the faucet handle.
    if check("the robot's gripper is not around faucet handle"):
        robot.grab("faucet handle")
    # Then turn the handle left to open the faucet.
    if check("the robot's gripper is around faucet handle"):
        robot.turn("faucet left")

# faucet-close: turn the faucet right
def faucet_close(robot):
    # Steps:
    #  1. Put gripper around faucet handle
    #  2. Turn handle right to close
    # First, put the gripper around the faucet handle.
    if check("the robot's gripper is not around faucet handle"):
        robot.grab("faucet handle")
    # Then turn the handle right to close the faucet.
    if check("the robot's gripper is around faucet handle"):
        robot.turn("faucet right")