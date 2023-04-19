
    if check("the robot's gripper is not vertically aligned with faucet handle"):
        robot.put("gripper above faucet handle")
    if check("the robot's gripper is vertically aligned with the faucet handle and the faucet is closed"):
        robot.turn("faucet to the left")