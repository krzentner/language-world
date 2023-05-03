
    if check("the robot's gripper is not vertically aligned with the faucet handle"):
        robot.put("gripper above faucet handle")
    if check("faucet handle is not left of the robot's gripper"):
        robot.grab("faucet handle")
    if check("faucet handle is left of the robot's gripper"):
        robot.turn("faucet left")

# faucet-close: turn the faucet right
# def faucet_close(robot):
    if check("the robot's gripper is not vertically aligned with the faucet handle"):
        robot.put("gripper above faucet handle")
    if check("faucet handle is not right of the robot's gripper"):
        robot.grab("faucet handle")
    if check("faucet handle is right of the robot's gripper"):
        robot.turn("faucet right")