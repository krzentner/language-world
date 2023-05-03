if check("the robot's gripper is not near the faucet handle"):
        robot.move("gripper to the right of the faucet handle")
    if check("the robot's gripper is near the faucet handle and the handle is turned right"):
        robot.turn("faucet left until water flows")