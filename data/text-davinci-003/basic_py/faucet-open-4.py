
    if check("the robot's gripper is not near faucet handle"):
        robot.reach("to faucet handle")
    if check("the robot's gripper is near faucet handle and the faucet handle is not facing left"):
        robot.turn("faucet left")