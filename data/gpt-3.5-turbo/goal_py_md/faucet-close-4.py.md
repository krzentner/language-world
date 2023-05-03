# faucet-close: turn the faucet right
def faucet_close(robot):
    # Steps:
    #  1. Put gripper right below the faucet lever
    #  2. Turn the faucet right
    # If the gripper is not vertically aligned with the faucet lever, move it
    # into position below the lever.
    if check("the robot's gripper is not vertically aligned with the faucet lever"):
        robot.move_gripper("vertically aligned with the faucet lever")
    # Once the gripper is below the lever, we can turn the faucet by moving the
    # gripper to the right.
    if check("the robot's gripper is below the faucet lever"):
        robot.move_gripper("right of the faucet lever")