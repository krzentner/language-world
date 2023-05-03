# Steps:
    #  1. Put gripper around faucet knob
    #  2. Turn knob right to close faucet
    # First, put the gripper around the faucet knob.
    if check("the robot's gripper is not around the faucet knob"):
        robot.drop("gripper around faucet knob")
    # Then turn the knob right to close the faucet.
    if check("the robot's gripper is around the faucet knob"):
        robot.turn("faucet knob right")