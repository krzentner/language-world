# Steps:
    #  1. Put gripper around the faucet handle
    #  2. Turn the handle to the right to close
    # If the gripper is not already around the faucet handle, move it there.
    if check("the robot's gripper is not around faucet handle"):
        robot.drop("gripper around faucet handle")
    # Once the gripper is around the faucet handle, turn it to the right to close.
    if check("the robot's gripper is around faucet handle"):
        robot.turn("faucet handle to the right")