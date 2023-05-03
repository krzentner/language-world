# Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Slide the plate back into the target location
    # First, line up the gripper above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.put("gripper above plate")
    # Once the gripper is lined up, grab the plate.
    if check("the robot's gripper is above the plate and the robot's gripper is open"):
        robot.grab("plate")
    # With the plate in the gripper, slide it back into the target location.
    if check("the plate is in the robot's gripper"):
        robot.slide("plate back into target location")