# faucet-close: turn the faucet right
# def faucet_close(robot):
    # Steps:
    # 1. Put gripper around faucet knob
    # 2. Turn knob to the right until it stops
    # First, the robot should position the gripper around the faucet knob.
    if check("the robot's gripper is not around the faucet knob"):
        robot.drop("gripper around faucet knob")
    # Now, the robot should turn the knob until the faucet stops.
    while check("the faucet is not turned all the way right"):
        robot.turn_knob("right")