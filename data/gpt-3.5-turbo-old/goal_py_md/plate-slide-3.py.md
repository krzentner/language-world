# plate-slide: slide the plate into the target location
# def plate_slide(robot):
    # Steps:
    #  1. Check if plate is in front of robot and nicely centered
    #  2. Move gripper above the plate
    #  3. Close the gripper around the plate
    #  4. Move the plate to the target location
    # If the plate is not in front of the robot and centered, move closer and center it
    if check("the plate is not in front of the robot and nicely centered"):
        robot.move_gripper("in front of the plate and center it")
    # If the gripper is not above the plate, move it above
    if check("the robot's gripper is not above the plate"):
        robot.move_gripper("above the plate")
    # If the gripper is above the plate but not closed, close the gripper
    if check("the robot's gripper is above the plate and the gripper is not closed"):
        robot.move_gripper("near the plate", close_gripper=True)
    # If the gripper is closed around the plate, move the plate to the target location
    if check("the gripper is closed around the plate"):
        robot.move_gripper("above the target location")