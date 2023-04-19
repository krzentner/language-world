# faucet-close: turn the faucet right
# def faucet_close(robot):
if check("the robot's gripper is not near the faucet knob"):
    robot.move("to the faucet knob")
if check("the robot's gripper is near the faucet knob and the robot's gripper is not vertically aligned with the faucet knob"):
    robot.align("gripper to the faucet knob")
if check("the robot's gripper is vertically aligned with the faucet knob and the robot's gripper is not around the faucet knob"):
    robot.grab("the faucet knob")
if check("the robot's gripper is around the faucet knob and the robot's gripper is not turned right"):
    robot.push("the faucet knob to the right")