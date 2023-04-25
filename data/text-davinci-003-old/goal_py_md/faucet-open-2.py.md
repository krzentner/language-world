

# faucet-open: turn the faucet left
# def faucet_open(robot):
    # Steps:
    #  1. Put gripper above the faucet handle
    #  2. Drop gripper around the faucet handle
    #  3. Rotate the faucet handle to the left
    # First, put the gripper above the faucet handle.
    if check("the robot's gripper is not vertically aligned with the faucet handle"):
        robot.move_gripper("vertically aligned with the faucet handle")
    # If the gripper isn't around the handle, put it around the handle.
    if check("the robot's gripper is not around faucet handle and the robot's gripper is open"):
        robot.move_gripper("near the faucet handle", close_gripper=True)
    # If the gripper is around the handle, rotate the handle to the left.
    if check("the robot's gripper is around faucet handle"):
        robot.move_gripper("left of the faucet handle")