# plate-slide: slide the plate into the target location
# def plate_slide(robot):
    # Steps:
    #   1. Put the gripper above the plate
    #   2. Close the gripper around the plate
    #   3. Move the gripper with the plate to the target location
    # To slide the plate into the target location, we need to pick it up, move it
    # to the target location, and then release it. 
    # First, put the gripper roughly above the plate. 
    if check("the robot's gripper is not above the plate"):
        robot.move_gripper("above the plate")
    # If the gripper isn't around the plate, put it around the plate.
    if check("the robot's gripper is not around plate and the robot's gripper is open"):
        robot.move_gripper("near the plate", close_gripper=True)
    # If the gripper is near the plate and closed, lift the plate and move it
    # to the target location.
    if check("the robot's gripper is near the plate and the robot's gripper is closed"):
        robot.move_gripper("above the target location")
    # If the gripper is above the target location, release the plate.
    if check("the robot's gripper is above the target location and the robot's gripper is not open"):
        robot.move_gripper("near the plate", open_gripper=True)