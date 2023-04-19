# faucet-close: turn the faucet right
# def faucet_close(robot):
    if check("the robot's gripper is not near faucet knob"):
        robot.move("gripper to faucet knob")
    if check("the robot's gripper is near the faucet knob and the robot's gripper is not around it"):
        robot.grab("faucet knob")
    if check("the robot's gripper is around faucet knob"):
        robot.turn("faucet right")