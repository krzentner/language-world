if check("the robot's gripper is not near the faucet handle"):
        robot.move("gripper to faucet handle")
    if check("the robot's gripper is around the faucet handle and the faucet is not turned off"):
        robot.turn("faucet handle to right")