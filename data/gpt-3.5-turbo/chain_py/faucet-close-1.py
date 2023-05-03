# Steps:
    #  1. Put gripper around faucet handle
    #  2. Turn the handle right to close the faucet
    # We need to position the gripper to fit around the faucet handle first.
    if check("the robot's gripper is not around the faucet handle"):
        robot.move("gripper around faucet handle")
    # Once the gripper is around the handle, we can turn it right to close the
    # faucet.
    if check("the robot's gripper is around the faucet handle"):
        robot.turn("faucet handle right")