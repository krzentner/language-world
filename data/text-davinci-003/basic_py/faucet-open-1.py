
    if check("the robot's gripper is not almost vertically aligned with faucet handle"):
        robot.put("gripper above faucet handle")
    if check("the robot's gripper is almost vertically aligned with faucet handle and the robot's gripper is open"):
        robot.put("gripper around faucet handle")
    if check("the robot's gripper is vertically aligned with the faucet handle"):
        robot.turn("faucet left")