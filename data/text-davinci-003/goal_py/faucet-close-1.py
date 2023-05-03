
    # Steps:
    #  1. Put gripper above faucet handle
    #  2. Drop gripper around faucet handle
    #  3. Turn the faucet right
    # First, put the gripper above the faucet handle.
    if check("the robot's gripper is not vertically aligned with faucet handle"):
        robot.move_gripper("vertically aligned with the faucet handle")
    # If the gripper is above the faucet handle, we can grab it by moving the
    # gripper around the handle.
    if check("the robot's gripper is above the faucet handle and the robot's gripper is not around faucet handle"):
        robot.move_gripper("around the faucet handle")
    # Once we've got the faucet handle, turning it right should close the
    # faucet.
    if check("the robot's gripper is around the faucet handle"):
        robot.move_gripper("right of faucet handle")