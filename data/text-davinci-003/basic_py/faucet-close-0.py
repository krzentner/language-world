
    if check("the faucet handle is to the left of the robot's gripper and the robot's gripper is below the faucet handle"):
        robot.move("gripper to right of faucet handle")
    if check("the robot's gripper is above the faucet handle and the robot's gripper is close to the faucet handle"):
        robot.align("gripper to faucet handle")
    if check("the robot's gripper is level with the faucet handle"):
        robot.turn("faucet right")