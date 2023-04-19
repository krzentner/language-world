# Steps:
    #  1. Put gripper around the faucet handle
    #  2. Turn the handle left
    # This task involves more precise manipulation than some others, so we will
    # have more steps to get into the right position.
    # First, we need to align the gripper with the faucet handle by moving the
    # gripper above it.
    if check("the robot's gripper is not above the faucet handle"):
        robot.move_gripper("above the faucet handle")
    # Now we need to get the gripper around the faucet handle by opening it and
    # then positioning it around the handle.
    if check("the robot's gripper is not open and not around the faucet handle"):
        robot.move_gripper("around the faucet handle", open_gripper=True)
    # Once the gripper is around the faucet handle, we can turn it left. We may
    # need to adjust the position of the gripper as we turn the handle.
    if check("the robot's gripper is around the faucet handle"):
        robot.move_gripper("around the faucet handle", angle=-90)

# faucet-close: turn the faucet right
# def faucet_close(robot):
    # Steps:
    #  1. Put gripper around the faucet handle
    #  2. Turn the handle right
    # This is very similar to faucet-open, with the only change being the angle we
    # turn the handle.
    if check("the robot's gripper is not above the faucet handle"):
        robot.move_gripper("above the faucet handle")
    if check("the robot's gripper is not around the faucet handle"):
        robot.move_gripper("around the faucet handle", open_gripper=True)
    if check("the robot's gripper is around the faucet handle"):
        robot.move_gripper("around the faucet handle", angle=90)