# Steps:
    #  1. Put gripper above plate
    #  2. Grab plate with gripper
    #  3. Slide plate to goal
    # First, put the gripper above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.put("gripper above plate")
    # Once the gripper is lined up above the plate, grab the plate.
    if check("the robot's gripper is above the plate and the robot's gripper is open"):
        robot.grab("plate")
    # Once the plate is grabbed, slide it to the goal.
    if check("the robot's gripper is holding the plate"):
        robot.slide("the plate to the goal")