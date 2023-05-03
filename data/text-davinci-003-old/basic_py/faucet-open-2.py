
    if check("the robot's gripper is not vertically aligned with faucet handle and the robot's gripper is not above the faucet handle"):
        robot.put("gripper above faucet handle")
    if check("the robot's gripper is vertically aligned with faucet handle and the robot's gripper is not in front of faucet handle"):
        robot.grab("faucet handle")
    if check("the robot's gripper is in front of the faucet handle"):
        robot.turn("faucet handle left")