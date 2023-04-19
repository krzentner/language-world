
    if check("the faucet handle is not front aligned with the robot's gripper"):
        robot.align("gripper to the faucet handle")
    if check("the robot's gripper is around the faucet handle"):
        robot.turn("faucet left")