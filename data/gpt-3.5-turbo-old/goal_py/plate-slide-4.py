# Steps:
    # 1. Put gripper above the plate
    # 2. Grab the plate with the gripper
    # 3. Slide the plate towards the target location
    # First, put the gripper roughly above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.move_gripper("above the plate")
    # If the gripper isn't around the plate, put it around the plate.
    if check("the robot's gripper is not around plate and the robot's gripper is open"):
        robot.move_gripper("near the plate", close_gripper=True)
    # If the gripper is near the plate, we've probably trapped the plate and can
    # slide it to the target location.
    # Close the gripper to make sure we keep control of the plate.
    if check("the robot's gripper is near the plate and the plate is below the robot's gripper"):
        robot.move_gripper("near the target location")