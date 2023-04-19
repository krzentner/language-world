
    # Steps:
    #  1. Gripper above the faucet
    #  2. Grasp the faucet handle
    #  3. Push the faucet handle left
    # First, line up the gripper with the faucet handle.
    if check("the robot's gripper is not vertically aligned with the faucet handle"):
        robot.move_gripper("vertically aligned with the faucet handle")
    # To grasp the faucet handle, the robot needs to move the gripper down.
    if check("the robot's gripper is vertically aligned with the faucet handle and the robot's gripper is not around the faucet handle and the robot's gripper is open"):
        robot.move_gripper("around the faucet handle", close_gripper=True)
    # If the gripper is around the faucet handle, the robot can push it open.
    if check("the robot's gripper is around the faucet handle"):
        robot.move_gripper("left of the faucet handle")