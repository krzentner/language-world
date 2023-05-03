
    # Steps:
    #  1. Put gripper above faucet handle
    #  2. Drop gripper around faucet handle
    #  3. Turn the faucet clockwise
    # First, put the gripper above the faucet handle.
    if check("the robot's gripper is not almost vertically aligned with faucet handle"):
        robot.move_gripper("almost vertically aligned with the faucet handle", close_gripper=True)
    # If the gripper is not lined up with the faucet handle from the front,
    # move the gripper to the front.
    if check("the robot's gripper is vertically aligned with the faucet handle and the robot's gripper is not forward aligned with the faucet handle"):
        robot.move_gripper("forward aligned with the faucet handle", close_gripper=True)
    # If the gripper is forward aligned with the faucet handle, turn the faucet
    # clockwise to close it.
    if check("the robot's gripper is forward aligned with the faucet handle"):
        robot.move_gripper("right of the faucet handle")