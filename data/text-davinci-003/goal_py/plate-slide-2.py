
    # Steps:
    #  1. Put gripper above the plate
    #  2. Put gripper onto the plate
    #  3. Slide the plate to the target location
    # We need to put the gripper onto the plate before we can slide it.
    # We don't need to be careful about the direction, since the plate is big and
    # we're just sliding it.
    if check("the robot's gripper is not forward aligned with the plate"):
        robot.move_gripper("forward aligned with the plate", close_gripper=True)
    # Once the gripper is above the plate, we just slide the plate to the target
    # location.
    if check("the robot's gripper is above plate"):
        robot.move_gripper("left of the plate")