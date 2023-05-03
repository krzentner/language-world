# Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Slide the plate sideways into the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate", close_gripper=True)
    # Once the gripper is on top of the plate, we can slide it to the target location.
    if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is not near the target location"):
        robot.move_gripper("horizontally aligned with the target location")