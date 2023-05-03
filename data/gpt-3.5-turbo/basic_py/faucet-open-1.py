if check("the robot's gripper is not near faucet handle"):
        robot.move("gripper to right of faucet handle")
    if check("the robot's gripper is around faucet handle"):
        robot.turn("faucet left")

# faucet-close: turn the faucet right
def faucet_close(robot):
    if check("the robot's gripper is not near faucet handle"):
        robot.move("gripper to right of faucet handle")
    if check("the robot's gripper is around faucet handle"):
        robot.turn("faucet right")