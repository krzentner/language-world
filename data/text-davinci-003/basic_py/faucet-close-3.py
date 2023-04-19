
    if check("the robot's gripper is not above the faucet"):
        robot.put("gripper above faucet")
    if check("the robot's gripper is above the faucet and the faucet is on"):
        robot.turn("faucet right")