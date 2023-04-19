# Steps:
    #  1. Put gripper above plate
    #  2. Grab the plate with the gripper
    #  3. Slide the plate to the target location
    # First, put the gripper roughly above the plate
    if check("the robot's gripper is not above the plate"):
        robot.move_gripper("above the plate")
    # If the gripper isn't around the plate, put it around the plate.
    if check("the robot's gripper is not around the plate and the robot's gripper is open"):
        robot.move_gripper("near the plate", close_gripper=True)
    # If the gripper is around the plate, slide it to the target location.
    # We can assume the plate will stay level, so we can just move the gripper
    # around it. Close the gripper to make sure we keep control of the plate.
    if check("the robot's gripper is around the plate and the robot's gripper is not near the target location"):
        robot.move_gripper("above the target location")