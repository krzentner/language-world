# faucet-open: turn the faucet left
def faucet_open(robot):
    # Steps:
    #  1. Put gripper around the faucet knob
    #  2. Turn the knob to the left
    # We need to first bring the gripper around the faucet knob.
    if check("the robot's gripper is not around the faucet knob"):
        robot.move_gripper("around the faucet knob")
    # Once the gripper is in position, we can turn the knob left.
    if check("the robot's gripper is around the faucet knob"):
        robot.move_gripper("left of the faucet knob")