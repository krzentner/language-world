# Steps:
    #  1. Put gripper above the plate
    #  2. Slide the plate towards the target
    # First, put the gripper above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.put("gripper above plate")
    # If the gripper is above the plate, we can just slide the plate towards the target location.
    if check("the robot's gripper is above the plate"):
        robot.slide("plate to the target")