# Steps:
    #  1. Put gripper above plate
    #  2. Grab plate with the gripper
    #  3. Slide the plate back into the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate")
    # Move the gripper down to grab the plate.
    if check("the robot's gripper is above the plate and the robot's gripper is open"):
        robot.move_gripper("near the plate", close_gripper=True)
    # Slide the plate back to the target location.
    if check("the robot's gripper is near the target location"):
        robot.move_gripper("above the target location")