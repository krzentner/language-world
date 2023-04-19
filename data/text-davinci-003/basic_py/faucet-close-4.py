
    if check("the robot's gripper is not near the faucet handle"):
        robot.grab("faucet handle")
    if check("the robot's gripper is near the faucet handle"):
        robot.rotate("faucet handle clockwise")