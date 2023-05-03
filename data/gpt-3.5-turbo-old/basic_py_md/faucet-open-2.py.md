# faucet-open: turn the faucet left
# def faucet_open(robot):
if check("the robot's gripper is not near the faucet handle"):
    robot.move("gripper to right of faucet handle")
if check("the robot's gripper is in front of the faucet handle"):
    robot.push("faucet left")
    robot.push("faucet left")
if check("water is flowing"):
    robot.say("water is flowing")
else:
    robot.say("faucet is stuck")