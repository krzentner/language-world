if check("the robot's gripper is not near the faucet handle"):
        robot.move("gripper to right of faucet handle")
    if check("the robot's gripper is around the faucet handle and the faucet is not turned on"):
        robot.turn("faucet left")
    if check("the faucet is turned on"):
        print("Water is now running from the faucet.")