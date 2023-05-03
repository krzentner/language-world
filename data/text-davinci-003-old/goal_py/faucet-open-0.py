
    # Steps:
    #  1. Put gripper above faucet handle
    #  2. Drop gripper around faucet handle
    #  3. Turn the faucet left
    # First, put the gripper above the faucet handle.
    if check("the robot's gripper is not vertically aligned with faucet handle"):
        robot.move_gripper("vertically aligned with the faucet handle")
    # Once the gripper is above the faucet handle, move it around the faucet
    # handle to grab it.
    if check("the robot's gripper is not around faucet handle"):
        robot.move_gripper("around the faucet handle")
    # Once the gripper is around the faucet handle, we can start turning it.
    if check("the robot's gripper is around faucet handle"):
        robot.move_gripper("left of the faucet handle")