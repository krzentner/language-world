# plate-slide-side: slide the plate sideways into the target location
# def plate_slide_side(robot):
    if check("the robot's gripper is not vertically aligned with the plate and the robot's gripper is not near the plate"):
        robot.put("gripper above plate")
    if check("the robot's gripper is near the plate and the robot's gripper is not around the plate"):
        robot.grab("plate")
    if check("the robot's gripper is around the plate and the plate is not at the target location"):
        robot.slide("plate sideways to the goal")