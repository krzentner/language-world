# faucet-open: turn the faucet left
def faucet_open(robot):
    # Steps:
    #  1. Put gripper around the faucet knob
    #  2. Keeping the gripper in place, rotate the faucet knob to the left
    # Place the gripper around the faucet knob.
    if check("the robot's gripper is not around the faucet knob"):
        robot.drop("gripper around faucet knob")
    # Keeping the gripper in place, rotate the faucet knob to the left
    # until the water starts flowing.
    if check("the robot's gripper is around the faucet knob"):
        robot.rotate("faucet knob to the left")
    # Once the water starts flowing, we're done.
    if check("water starts flowing from faucet"):
        robot.stop("turning faucet knob")