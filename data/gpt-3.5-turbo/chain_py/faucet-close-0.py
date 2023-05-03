# Steps:
    #  1. Put gripper around the faucet handle
    #  2. Turn the handle to the right to close the faucet
    # We need to move the gripper around the faucet handle before we can turn
    # it.
    if check("the robot's gripper is not around faucet handle"):
        robot.put("gripper around faucet handle")
    # Once the gripper is around the faucet handle, we can turn the handle to 
    # the right to close the faucet.
    if check("the robot's gripper is around faucet handle"):
        robot.turn("faucet handle right to close")