if check("the robot's gripper is not near the faucet handle"):
    robot.move("gripper to the faucet handle")
if check("the faucet handle is not turned right"):
    robot.turn("faucet handle right")