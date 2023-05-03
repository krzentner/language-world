# faucet-close: turn the faucet right
def faucet_close(robot):
    if check("the robot's gripper is not near the faucet handle"):
        robot.move("gripper to left of faucet handle")
    if check("the robot's gripper is around faucet handle"):
        robot.turn("faucet right")