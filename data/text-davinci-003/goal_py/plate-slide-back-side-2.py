
    # Steps:
    #  1. Put gripper near side of the plate
    #  2. Push the plate back sideways
    # First, put the gripper near the side of the plate.
    if check("the robot's gripper is not near side of the plate"):
        robot.move_gripper("near the side of the plate")
    # Now, we slide the plate back sideways.
    if check("the robot's gripper is near the side of the plate"):
        robot.move_gripper("vertically aligned with the plate")