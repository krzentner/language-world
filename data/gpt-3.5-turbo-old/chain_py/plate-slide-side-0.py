# Steps:
    #  1. Put gripper above roughly the center of the plate
    #  2. Grab the plate with the gripper
    #  3. Move the plate to the target location
    # Because the plate is flat, we can just put the gripper above roughly the
    # center of the plate in order to grab it.
    if check("the robot's gripper is not above roughly the center of the plate"):
        robot.place("gripper above roughly the center of the plate")
    # If the gripper is not holding the plate, grab it.
    if check("the plate is not in the gripper's grasp"):
        robot.grab("plate")
    # If the gripper is now holding the plate, slide it sideways to the target
    # location.
    if check("the plate is in the gripper's grasp"):
        robot.slide("plate sideways to the target location")