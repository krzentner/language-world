# Steps:
    #  1. Put gripper above plate
    #  2. Grab the plate with gripper
    #  3. Slide the plate to target location
    # Similar to pushing the puck, the robot can slide the plate by trapping it
    # from above and moving the gripper.
    # First, put the gripper above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.place("gripper above plate")
    # If the gripper is not around the plate, put it around the plate.
    if check("the robot's gripper is not around plate and the robot's gripper is open"):
        robot.grab("gripper around plate")
    # If the gripper is around the plate and near the target location, we can
    # slide the plate to the target location.
    if check("the robot's gripper is around plate and the robot's gripper is near the target location"):
        robot.slide("plate to target location")