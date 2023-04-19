# faucet-open: turn the faucet left
# def faucet_open(robot):
    # Steps:
    #  1. Put gripper right of the faucet handle
    #  2. Start pushing against the faucet handle to turn it left
    #  3. Turn the faucet left
    # If the robot's gripper is not vertically lined up with the faucet handle,
    # we should move the gripper near the faucet handle to start turning it.
    if check("the robot's gripper is not near the faucet handle"):
        robot.move_gripper("near the faucet handle")
    # If the robot's gripper is near the faucet handle we can probably turn the
    # faucet handle now by moving the gripper left.
    if check("the robot's gripper is in front of the faucet handle"):
        robot.move_gripper("almost vertically aligned with the faucet handle")
    # If the robot's gripper is starting to be behind the faucet handle,
    # turn the faucet handle left more.
    if check("the robot's gripper is in front of the faucet handle and the faucet is not fully open"):
        robot.move_gripper("behind the faucet handle")