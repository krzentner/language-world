# faucet-close: turn the faucet right
def faucet_close(robot):
    # Steps:
    #  1. Put gripper near the faucet handle
    #  2. Turn the handle to close the faucet
    # If the the faucet handle is not near the robot's gripper, we should move the
    # gripper near the faucet handle.
    if check("the faucet handle is not near the robot's gripper"):
        robot.move("gripper near the faucet handle")
    # If the robot's gripper is near the faucet handle, we can turn the handle to
    # close the faucet.
    if check("the robot's gripper is near the faucet handle"):
        robot.turn("faucet handle right to close")