# Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Slide the plate sideways into the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate")
    # If the plate is not between the gripper's fingers, move the gripper near
    # the plate and close it around the plate.
    if check("the robot's gripper is above the plate and the plate is not between the robot's gripper's fingers"):
        robot.move_gripper("near the plate", close_gripper=True)
    # If the gripper is holding the plate, slide it sideways to the target
    # location.
    if check("the plate is between the robot's gripper's fingers and the robot's gripper is not near the target location"):
        robot.move_gripper("above the target location")