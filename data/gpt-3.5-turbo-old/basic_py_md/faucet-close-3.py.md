# faucet-close: turn the faucet right
# def faucet_close(robot):
    if check("the robot's gripper is not near the faucet handle"):
        robot.move("gripper to the right of the faucet handle")
    if check("the robot's gripper is near the faucet handle"):
        robot.push("faucet handle right")
    if check("the faucet is no longer running"):
        robot.done("faucet is closed")