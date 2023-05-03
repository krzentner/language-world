# faucet-close: turn the faucet right
def faucet_close(robot):
    # Steps:
    #  1. Put gripper near the faucet
    #  2. Turn the faucet right
    # As long as the gripper is not near the faucet, move it there.
    if check("the robot's gripper is not near the faucet"):
        robot.move_gripper("near the faucet")
    # Once the gripper is near the faucet, turn the faucet right.
    if check("the robot's gripper is near the faucet"):
        robot.move_gripper("right of the faucet")