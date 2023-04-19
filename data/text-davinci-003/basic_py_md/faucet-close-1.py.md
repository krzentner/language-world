

If check("the robot's gripper is not near the faucet handle"):
    robot.move("gripper to faucet handle")
if check("the robot's gripper is near the faucet handle and the gripper is open"):
    robot.grab("faucet handle")
if check("the robot's gripper is around the faucet handle and the faucet handle is not turned right"):
    robot.turn("faucet right")
if check("the faucet handle is turned right and the robot's gripper is around the faucet handle"):
    robot.release("faucet handle")