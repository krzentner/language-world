# faucet-close: turn the faucet right
def faucet_close(robot):
    if check("the robot's gripper is not around faucet handle and the robot's gripper is vertically aligned with faucet handle"):
        robot.put("gripper around faucet handle")
    if check("the robot's gripper is around faucet handle"):
        robot.turn("faucet to right")