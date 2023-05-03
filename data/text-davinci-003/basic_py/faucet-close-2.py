
    if check("the faucet is not in line with the robot's gripper and the robot's gripper is below the faucet"):
        robot.move("to in line with faucet")
    if check("the robot's faucet is in line with the robot's gripper and the robot's gripper is not near the faucet"):
        robot.move("to near faucet")
    if check("the robot's gripper is near the faucet"):
        robot.turn("faucet right")