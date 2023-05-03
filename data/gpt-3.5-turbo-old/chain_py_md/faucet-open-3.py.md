# faucet-open: turn the faucet left
# def faucet_open(robot):
    # Steps:
    #  1. Put gripper around faucet knob
    #  2. Turn the knob to the left
    # First, put the gripper around the faucet knob, making sure it's in a position to turn.
    if check("the robot's gripper is not around the faucet knob"):
        robot.grab("faucet knob")
    # Turn the knob to the left.
    if check("the robot's gripper is around the faucet knob"):
        robot.turn("knob to the left")