if check("the robot's gripper is not around faucet handle"):
        robot.grab("faucet handle")
    if check("the robot's gripper is around faucet handle and the faucet handle is not turned right"):
        robot.turn("faucet handle right")