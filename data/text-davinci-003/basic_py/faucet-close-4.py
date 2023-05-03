
    if check("the robot's gripper is not near faucet"):
        robot.grab("faucet")
    if check("the robot's gripper is near faucet and the faucet is not counter-clockwise"):
        robot.swivel("faucet counter-clockwise")