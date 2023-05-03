# faucet-open: turn the faucet left
def faucet_open(robot):
    if check("the robot's gripper is not near the faucet knob and the faucet knob is right of the robot's gripper"):
        robot.move("gripper to right of faucet knob")
    if check("the robot's gripper is near the faucet knob"):
        robot.rotate("faucet left")