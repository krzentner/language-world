
    if check("the robot's gripper is not horizontally aligned with faucet handle"):
        robot.turn("gripper to face faucet handle")
    if check("the robot's gripper is around the faucet handle and the faucet is not closed"):
        robot.rotate("faucet to the right")
    if check("faucet is close"):
        robot.stop("rotation")