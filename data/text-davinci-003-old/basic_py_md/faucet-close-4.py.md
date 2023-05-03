

If check("the robot's gripper is not vertical aligned with the faucet handle"):
    robot.place("gripper above faucet handle")
If check("the robot's gripper is vertical aligned with the faucet handle and the robot's gripper is not around faucet handle"):
    robot.drop("gripper around faucet handle")
If check("the robot's gripper is around faucet handle"):
    robot.turn("right")