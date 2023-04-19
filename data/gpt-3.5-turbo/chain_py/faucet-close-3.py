# Steps:
#  1. Put gripper around the faucet knob
#  2. Turn the knob right
# First, put the gripper around the faucet knob.
if check("the robot's gripper is not around the faucet knob"):
    robot.drop("gripper around faucet knob")
# Turn the faucet knob to the right.
if check("the robot's gripper is around faucet knob"):
    robot.turn("faucet knob right")