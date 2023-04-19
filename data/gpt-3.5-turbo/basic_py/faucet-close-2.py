if check("the robot's gripper is not above the faucet handle"):
        robot.move("gripper above faucet handle")
    if check("the robot's gripper is above the faucet handle"):
        robot.turn("faucet right")