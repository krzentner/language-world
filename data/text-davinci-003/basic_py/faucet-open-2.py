
    if check("the robot's gripper is not vertically aligned with faucet handle"):
        robot.move("gripper above faucet handle")
    if check("the robot's gripper is near the faucet handle and the robot's gripper is open"):
        robot.put("gripper around faucet handle")
    if check("the robot's gripper is vertically aligned with the faucet handle"):
        robot.turn("left")