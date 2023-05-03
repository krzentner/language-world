# faucet-open: turn the faucet left
# def faucet_open(robot):
    if check("the robot's gripper is not vertically aligned with the faucet handle and the robot's gripper is not below the faucet handle"):
        robot.move("gripper below faucet handle")
    if check("the robot's gripper is not vertically aligned with the faucet handle and the robot's gripper is below the faucet handle"):
        robot.move("gripper above faucet handle")
    if check("the robot's gripper is vertically aligned with the faucet handle"):
        robot.turn("faucet left")