# Steps:
    #  1. Put gripper above plate
    #  2. Grab plate with gripper
    #  3. Slide plate to goal
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above plate")
    # If the gripper is above the plate, grab the plate with the gripper.
    if check("the robot's gripper is above plate"):
        robot.grab("plate")
    # If the gripper has the plate, slide it to the target location.
    if check("the robot's gripper is holding the plate"):
        robot.slide("plate to goal")