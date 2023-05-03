if check("the robot's gripper is not near the faucet handle"):
        robot.move("gripper towards faucet handle")
    if check("the robot's gripper is around faucet handle"):
        robot.turn("faucet left")