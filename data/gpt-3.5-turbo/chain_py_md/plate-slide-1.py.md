# plate-slide: slide the plate into the target location
# def plate_slide(robot):
    # Steps:
    #  1. Put gripper near the plate but not on it
    #  2. Move the gripper down to grab the plate
    #  3. If gripper is around the plate, slide it to the target location
    # First, move the gripper to be near the plate but not directly on it
    if check("the robot's gripper is not near the plate"):
        robot.put("gripper near the plate")
    # Once the gripper is near the plate, move it down to grab the plate
    if check("the robot's gripper is near the plate and the robot's gripper is open"):
        robot.down("to grab the plate")
    # If the gripper is around the plate, slide it to the target
    if check("the robot's gripper is around the plate"):
        robot.slide("the plate to the target location")