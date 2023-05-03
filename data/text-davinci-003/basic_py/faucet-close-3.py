
    if check("the robot's gripper is not vertically aligned with faucet Handle"):
        robot.put("gripper above faucet handle")
    if check("the robot's gripper is vertically aligned with the faucet handle and the robot's gripper is not around the faucet handle"):
        robot.put("gripper around faucet handle")
    if check("the robot's gripper is around the faucet handle"):
        robot.move("gripper clockwise around faucet handle")