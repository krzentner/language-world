if check("the robot's gripper is not above the faucet handle"):
        robot.move("gripper above faucet handle")
    if check("the robot's gripper is above the faucet handle and the faucet handle is turned left"):
        robot.turn("faucet right")