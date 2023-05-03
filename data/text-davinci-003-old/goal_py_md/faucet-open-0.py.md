

Then, the program should provide instructions for the robot:
   
    # Steps:
    #  1. Put gripper above faucet handle
    #  2. Drop gripper around faucet handle
    #  3. Turn the faucet handle to the left
    # First, put the gripper above the faucet handle.
    if check("the robot's gripper is not vertically aligned with the faucet handle"):
        robot.move_gripper("vertically aligned with the faucet handle")
    # If the gripper isn't around the faucet handle, put it around the faucet handle.
    if check("the robot's gripper is not around faucet handle and the robot's gripper is open"):
        robot.move_gripper("near the faucet handle", close_gripper=True)
    # If the gripper is near the faucet handle, turn the faucet handle to the left.
    if check("the robot's gripper is around the faucet handle"):
        robot.move_gripper("left of the faucet handle")