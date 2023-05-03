# faucet-close: turn the faucet right
def faucet_close(robot):
    # Steps:
    #  1. Place the gripper around faucet handle
    #  2. Turn the handle right to close the faucet
    # First, put the gripper around the faucet handle.
    if check("the robot's gripper is not around the faucet handle"):
        robot.grab("faucet handle")
    # If the handle is not turned right enough to close the faucet, turn it more
    # right.
    if check("the faucet is not closed"):
        robot.turn("handle right")
