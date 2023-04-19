# plate-slide-back: slide the plate back into the target location
# def plate_slide_back(robot):
    if check("the robot's gripper is not near the plate"):
        robot.reach("to the plate")
        robot.grab("the plate")
    if check("the robot's gripper is near the plate but not above it"):
        robot.put("the gripper above the plate")
    if check("the robot's gripper is above the plate and the plate is not in the target location"):
        robot.slide("the plate to the target location")