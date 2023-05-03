

# faucet-open: turn the faucet left
def faucet_open(robot):
    # Steps:
    #  1. Put gripper in front of faucet handle
    #  2. Rotate the handle left
    # First, put the gripper in front of the faucet handle.
    if check("the robot's gripper is not forward aligned with faucet handle"):
        robot.move_gripper("forward aligned with the faucet handle")
    # As long as the gripper is still forward aligned with the handle, rotate
    # it to the left.
    if check("the robot's gripper is forward aligned with faucet handle"):
        robot.move_gripper("left of the faucet handle")