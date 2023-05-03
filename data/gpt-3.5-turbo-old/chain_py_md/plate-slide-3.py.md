# plate-slide: slide the plate into the target location
# def plate_slide(robot):
    # Steps:
    #  1. Position gripper above plate
    #  2. Close gripper around plate
    #  3. Move plate to target location
    # Place the gripper above the plate
    if check("the robot's gripper is not above the plate"):
        robot.place("gripper above plate")
    # Close the gripper around the plate
    if check("the robot's gripper is above plate and the robot's gripper is not closed around the plate"):
        robot.close("gripper around plate")
    # Move the plate to the target location
    if check("the robot's gripper is closed around plate and the robot's gripper is not at the target location"):
        robot.slide("plate to target location")