# faucet-open: turn the faucet left
# def faucet_open(robot):
if check("the robot's gripper is not aligned with the faucet knob"):
    robot.reach("to the faucet knob")
if check("the robot's gripper is aligned with the faucet knob and the robot's gripper is not around the knob"):
    robot.drop("gripper around the knob")
if check("the robot's gripper is around the knob"):
    robot.twist("the knob to the left")