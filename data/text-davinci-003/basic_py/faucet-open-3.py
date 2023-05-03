
    if check("the robot's gripper is not near the faucet handle"):
        robot.grab("faucet handle")
    if check("the robot's gripper is near the faucet handle and the faucet handle is not turned left"):
        robot.turn("faucet left")
    if check("the faucet handle is turned left"):
        robot.keep("turning the faucet left")