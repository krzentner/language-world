# faucet-close: turn the faucet right
def faucet_close(robot):
    if check("the robot's gripper is not vertically aligned with the faucet handle"):
        robot.put("gripper above faucet handle")
    if check("the robot's gripper is around faucet handle and the robot's gripper is closed"):
        robot.release("gripper around faucet handle")
    if check("the robot's gripper is near faucet handle and the robot's gripper is open"):
        robot.close("gripper around faucet handle")
    if check("the faucet handle is not pointing vertically downwards"):
        robot.turn("faucet handle right")