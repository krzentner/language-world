
    if check("the robot's gripper is not near the faucet handle"):
        robot.move("gripper near faucet handle")
    if check("the robot's gripper is near faucet handle and the robot's gripper is not around faucet handle"):
        robot.grab("faucet handle")
    if check("the robot's gripper is around faucet handle"):
        robot.turn("faucet left")