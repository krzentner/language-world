# faucet-open: turn the faucet left
def faucet_open(robot):
    if check("the robot's gripper is not near the faucet handle"):
        robot.move("gripper to the right of the faucet handle")
    if check("the robot's gripper is near the faucet handle"):
        robot.put("gripper around the faucet handle")
    if check("the robot's gripper is around the faucet handle and the handle is in the off position"):
        robot.pull("the handle left")