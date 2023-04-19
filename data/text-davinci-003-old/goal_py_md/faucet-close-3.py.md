

# faucet-close: turn the faucet right
# def faucet_close(robot):
    # Steps:
    #  1. Put gripper left of the faucet handle
    #  2. Push the faucet handle right
    #  3. Push the faucet handle harder
    # First, put the gripper left of the faucet handle.
    if check("the robot's gripper is not left of the faucet handle"):
        robot.move_gripper("left of the faucet handle")
    # Now, push the faucet handle right.
    if check("the robot's gripper is left of the faucet handle"):
        robot.move_gripper("near the faucet handle")
    # If the faucet handle isn't all the way right, push it right harder.
    if check("the robot's gripper is near the faucet handle"):
        robot.move_gripper("right of the faucet handle")