
    # Steps:
    #  1. Put gripper above the faucet handle
    #  2. Move the gripper to the right
    # First, put the gripper above the faucet handle.
    if check("the robot's gripper is not vertically aligned with the faucet handle"):
        robot.move_gripper("vertically aligned with the faucet handle")
    # If the gripper is lined up with the handle, move the gripper to the right
    # to turn the faucet off.
    if check("the robot's gripper is vertically aligned with the faucet handle"):
        robot.move_gripper("right of the faucet handle")