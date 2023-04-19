# Steps:
    #  1. Put gripper around faucet knob
    #  2. Turn the knob right to close the faucet
    # First, put the gripper around the faucet knob.
    if check("the robot's gripper is not around the faucet knob"):
        robot.move_gripper("around the faucet knob")
    # If the gripper is around the knob, we can turn it to the right to close
    # the faucet.
    if check("the robot's gripper is around the faucet knob"):
        robot.move_gripper("right of the faucet knob")