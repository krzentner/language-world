if check("the robot's gripper is not around the faucet handle"):
        robot.grab("faucet handle")
    if check("the robot's gripper is not aligned with the faucet handle"):
        robot.align("gripper with handle")
    if check("the faucet handle is not turned all the way to the left"):
        robot.turn("faucet left")