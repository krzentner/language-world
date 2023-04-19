
    # Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Reach towards the target location
    #  4. Slide the plate sideways into the target
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above plate")
    # If the plate becomes left of the gripper, go back to putting the gripper
    # above the plate.
    # Because the plate is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("plate is not left of the robot's gripper and plate is not forward aligned with the robot's gripper"):
        robot.grab("plate")
    # Reach towards the target location.
    if check("the robot's gripper is not near the target location"):
        robot.reach("to target location")
    # Now that the gripper is near the target location, we can slide the plate
    # sideways into the target.
    if check("the robot's gripper is near the target location"):
        robot.slide("plate sideways into target")