
    if check("the robot's gripper is not vertically aligned with the faucet knob"):
        robot.put("gripper above faucet knob")
    if check("the robot's gripper is vertically aligned with the faucet knob and the robot's gripper is not around the faucet knob"):
        robot.grab("faucet knob")
    if check("the robot's gripper is around the faucet knob and the faucet is off"):
        robot.turn("faucet left")

# faucet-close: turn the faucet right
# def faucet_close(robot):
    if check("the robot's gripper is not vertically aligned with the faucet knob"):
        robot.put("gripper above faucet knob")
    if check("the robot's gripper is vertically aligned with the faucet knob and the robot's gripper is not around the faucet knob"):
        robot.grab("faucet knob")
    if check("the robot's gripper is around the faucet knob and the faucet is on"):
        robot.turn("faucet right")