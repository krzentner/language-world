# faucet-open: turn the faucet left
def faucet_open(robot):
    if check("the robot's gripper is not near the faucet handle"):
        robot.move("gripper to right of faucet handle")
    if check("the robot's gripper is near the faucet handle"):
        robot.grab("faucet handle")
    if check("the robot's gripper is around the faucet handle"):
        robot.turn("faucet left")