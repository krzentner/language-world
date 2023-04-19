# faucet-open: turn the faucet left
# def faucet_open(robot):
if check("the robot's gripper is not near the faucet handle"):
    robot.move("gripper to right of faucet handle")
if check("the robot's gripper is near the faucet handle and the faucet handle is not turned"):
    robot.push("faucet handle to the left")