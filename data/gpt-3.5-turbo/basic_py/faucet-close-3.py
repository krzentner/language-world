if check("the robot's gripper is not around faucet handle"):
        robot.grab("faucet handle")
    if check("the robot's gripper is around faucet handle"):
        robot.turn("faucet right")