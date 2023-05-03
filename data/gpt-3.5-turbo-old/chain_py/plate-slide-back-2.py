# Steps:
    #  1. Put gripper above plate
    #  2. Grab the plate with gripper
    #  3. Slide plate back to target location
    # First put the gripper above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.put("gripper above plate")
    # If gripper is not around the plate, grab the plate.
    if check("the robot's gripper is not around the plate"):
        robot.grab("plate")
    # Once gripper is around the plate, slide the plate back to target location.
    if check("the robot's gripper is around the plate and the plate is not at target location"):
        robot.slide("plate back to target location")