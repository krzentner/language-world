

If check("the robot's gripper is not near the faucet"):
    robot.move("gripper to the faucet")
if check("the robot's gripper is near the faucet and the robot's gripper is not around the faucet handle"):
    robot.grab("faucet handle")
if check("the robot's gripper is around the faucet handle"):
    robot.turn("faucet right")