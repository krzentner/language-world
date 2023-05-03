# faucet-close: turn the faucet right
# def faucet_close(robot):
if check("the robot's gripper is not above the faucet handle"):
    robot.reach("to the faucet handle")
if check("the robot's gripper is not aligned with the faucet handle"):
    robot.align("gripper to faucet handle")
if check("the robot's gripper is aligned with the faucet handle and the faucet is not turned off"):
    robot.turn("the faucet handle to the right")