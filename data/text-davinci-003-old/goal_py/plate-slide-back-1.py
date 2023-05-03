
    # Steps:
    #  1. Put gripper near the plate
    #  2. slide the plate back into its original position
    # If the plate is not in front of the gripper, move the gripper near the
    # plate to slide it back.
    if check("the plate is not in front of the robot's gripper and the robot's gripper is not near the plate"):
        robot.move_gripper("near the plate")
    # Now that the plate is in front of the gripper, slide it back towards its
    # original position.
    if check("the robot's gripper is near the plate"):
        robot.move_gripper("near the target location")