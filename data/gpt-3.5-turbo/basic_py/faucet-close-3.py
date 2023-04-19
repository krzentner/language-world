if check("the robot's gripper is not above the faucet handle"):
        robot.move("gripper to faucet handle")
    if check("the robot's gripper is above the faucet handle"):
        robot.grab("faucet handle")
    if check("the faucet handle is not aligned to the right"):
        robot.turn("faucet handle to the right")