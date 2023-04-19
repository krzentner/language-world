
    # Steps:
    #  1. Put the gripper above the plate
    #  2. Push the gripper forward to grab the plate
    #  3. Slide the plate back into the location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.move_gripper("above the plate", close_gripper=True)
    # Now that the gripper is above the plate, we can slide the gripper forward
    # and grab the plate.
    if check("the robot's gripper is ahead of the plate"):
        robot.move_gripper("horizontally aligned with the plate")
    # Once the gripper is around the plate, we can slide the plate back.
    if check("the robot's gripper is horizontally aligned with the plate"):
        robot.move_gripper("above the target location")