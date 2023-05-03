# plate-slide-side: slide the plate sideways into the target location
# def plate_slide_side(robot):
    if check("the robot's gripper is not above the plate and the plate is not near the target location"):
        robot.put("the gripper above the plate")
    if check("the robot's gripper is above the plate and the plate is not near the target location"):
        robot.grab("the plate")
    if check("the plate is almost aligned with the target location"):
        robot.slide("the plate sideways into the target location")