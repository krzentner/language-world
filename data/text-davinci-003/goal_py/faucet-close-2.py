
    # Steps:
    #  1. Put gripper above faucet handle
    #  2. Drop gripper around faucet handle
    #  3. Turn faucet to the right
    # First, line the gripper up so that the gripper can grab the faucet handle.
    if check("the robot's gripper is not above faucet handle and the robot's gripper is not around faucet handle"):
        robot.move_gripper("above the faucet handle")
    # If the gripper is lined up as seen from in front, we can grab the handle.
    if check("the robot's gripper is never around faucet handle and the robot's gripper is forward aligned with faucet handle"):
        robot.move_gripper("around the faucet handle")