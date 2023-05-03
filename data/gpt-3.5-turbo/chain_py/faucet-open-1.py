# Steps:
    #  1. Put gripper around faucet handle
    #  2. Rotate the handle to the left
    # We need to move the gripper around the faucet handle first.
    if check("the robot's gripper is not around the faucet handle"):
        robot.grab("faucet handle")
    # Once the gripper is around the handle, we can just turn it to the left to
    # open the faucet.
    if check("the robot's gripper is around the faucet handle"):
        robot.rotate("faucet handle", "left")

# faucet-close: turn the faucet right
def faucet_close(robot):
    # Steps:
    #  1. Put gripper around faucet handle
    #  2. Rotate the handle to the right
    # We need to move the gripper around the faucet handle first.
    if check("the robot's gripper is not around the faucet handle"):
        robot.grab("faucet handle")
    # Once the gripper is around the handle, we can just turn it to the right to
    # close the faucet.
    if check("the robot's gripper is around the faucet handle"):
        robot.rotate("faucet handle", "right")