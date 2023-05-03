if check("the robot's gripper is not around faucet handle"):
        robot.grab("faucet handle")
    if check("the robot's gripper is around faucet handle and the faucet is not turned off"):
        robot.turn("faucet right")