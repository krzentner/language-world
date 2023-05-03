
    if check("the faucet handle is not left at six o'clock"):
        robot.turn("faucet handle right")
    if check("the faucet handle is forward aligned with the robot's gripper"):
        robot.push("faucet handle right")