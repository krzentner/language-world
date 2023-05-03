# faucet-close: turn the faucet right
def faucet_close(robot):
    if check("the robot's gripper is not vertically aligned with faucet handle"):
        robot.put("gripper above faucet handle")
    if check("the robot's gripper is not around faucet handle and the robot's gripper is open"):
        robot.grab("faucet handle")
    if check("the robot's gripper is around the faucet handle and the faucet handle is not horizontal"):
        robot.align("faucet handle to right")
    if check("faucet handle is horizontal"):
        robot.push("faucet handle to off position")