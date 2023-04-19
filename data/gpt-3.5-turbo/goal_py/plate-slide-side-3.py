# Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Slide the plate sideways into the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate")
    # If the plate becomes left of the gripper or far away from it, go back to
    # putting the gripper above the plate.
    if check("plate is not left of the robot's gripper and plate is not near the robot's gripper"):
        robot.move_gripper("near the plate", close_gripper=True)
    # If the plate is near the gripper, we can slide it into the target location
    # by moving the gripper sideways.
    if check("the robot's gripper is above the plate and the plate is not horizontally aligned with the target location"):
        robot.move_gripper("horizontally aligned with the target location")