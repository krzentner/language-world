# Steps:
    #  1. Put the gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Move the plate back to the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.move_gripper("above the plate")
    # If the gripper isn't around the plate, put it around the plate.
    if check("the robot's gripper is not around plate and the robot's gripper is open"):
        robot.move_gripper("near the plate", close_gripper=True)
    # If the gripper is near the plate and closed around it, move the plate back to the target location.
    if check("the robot's gripper is around the plate and the robot's gripper is not above the target location"):
        robot.move_gripper("above the target location")