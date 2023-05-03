
    # Steps:
    #  1. Put gripper around faucet handle
    #  2. Rotate faucet handle clockwise to close faucet
    # First, put the gripper around the faucet handle, so it can grab it.
    if check("the robot's gripper is not around the faucet handle"):
        robot.put("gripper around faucet handle")
    # If the gripper is around the handle and not turned, just turn it clockwise
    # to close the faucet.
    if check("the robot's gripper is around the faucet handle and the faucet handle is not turned clockwise"):
        robot.rotate("faucet clockwise")