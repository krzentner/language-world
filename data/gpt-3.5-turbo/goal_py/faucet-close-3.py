# Steps:
    #  1. Put gripper around the faucet handle
    #  2. Turn the handle right to close the faucet
    # If the gripper is not around the faucet handle, move it there.
    if check("the robot's gripper is not around the faucet handle"):
        robot.move_gripper("around the faucet handle")
    # Once the gripper is around the faucet handle, turn it to the right to close
    # the faucet.
    if check("the robot's gripper is around the faucet handle"):
        robot.move_gripper("turned to the right")