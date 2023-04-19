# Steps:
    #  1. Put gripper above plate
    #  2. Grab the plate with the gripper
    #  3. Slide the plate to the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate")
    # If the gripper is above the plate, grab the plate with the gripper.
    if check("the robot's gripper is above the plate and the robot's gripper is not around the plate"):
        robot.move_gripper("around the plate")
    # With the plate in the gripper, we can now slide it towards the target
    # location.
    if check("the robot's gripper is near the target location"):
        robot.move_gripper("vertically aligned with the target location")