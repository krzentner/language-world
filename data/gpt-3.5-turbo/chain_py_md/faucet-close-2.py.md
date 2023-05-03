# faucet-close: turn the faucet right
def faucet_close(robot):
    # Steps:
    #  1. Put gripper around the faucet knob
    #  2. Turn right to close the faucet
    # First, put the gripper around the faucet knob
    if check("the robot's gripper is not around the faucet knob and the robot's gripper is open"):
        robot.drop("gripper around faucet knob")
    # If the gripper is around the faucet knob, turn right to close the faucet
    if check("the robot's gripper is around the faucet knob"):
        robot.turn("faucet right to close")