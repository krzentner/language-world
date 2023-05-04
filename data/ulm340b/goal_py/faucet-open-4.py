
    # Steps:
    #  1. Put gripper above the faucet handle
    #  2. Move the gripper around the faucet handle
    #  3. Twist the faucet handle left
    # First, we need to put the gripper above the faucet handle, so that we can
    # twist it.
    if check("the robot's gripper is not vertically aligned with faucet handle"):
        robot.move_gripper("vertically aligned with the faucet handle", close_gripper=True)
    # If the gripper is aligned with the faucet handle but not around it, move
    # the gripper around the faucet handle.
    if check("the robot's gripper is vertically aligned with faucet handle and the robot's gripper is not around faucet handle"):
        robot.move_gripper("around the faucet handle")
    # Now that the gripper is around the faucet handle, we can twist it by
    # moving the gripper left.
    if check("the robot's gripper is almost horizontally aligned with faucet handle"):
        robot.move_gripper("left of the faucet handle", close_gripper=True)

# faucet-close: turn the faucet right
def faucet_close(robot):
    # Steps:
    #  1. Put gripper above the faucet handle
    #  2. Move the gripper around the faucet handle
    #  3. Twist the faucet handle right
    # First, we need to put the gripper above the faucet handle, so that we can
    # twist it.
    if check("the robot's gripper is not vertically aligned with faucet handle"):
        robot.move_gripper("vertically aligned with the faucet handle", close_gripper=True)
    # If the gripper is aligned with the faucet handle but not around it, move
    # the gripper around the faucet handle.
    if check("the robot's gripper is vertically aligned with faucet handle and the robot's gripper is not around faucet handle"):
        robot.move_gripper("around the faucet handle")
    # Now that the gripper is around the faucet handle, we can twist it by
    # moving the gripper right.
    if check("the robot's gripper is almost horizontally aligned with faucet handle"):
        robot.move_gripper("right of the faucet handle", close_gripper=True)

# push-