# faucet-close: turn the faucet right
def faucet_close(robot):
    # Steps:
    #  1. Put gripper around the faucet knob
    #  2. Turn the faucet right
    # First, put the gripper around the faucet knob.
    if check("the robot's gripper is not around the faucet knob"):
        robot.grab("faucet knob")
    # Once the gripper is around the faucet knob, turn the knob right to close
    # the faucet.
    if check("the robot's gripper is around the faucet knob"):
        robot.rotate("knob right")