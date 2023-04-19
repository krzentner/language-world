# plate-slide-side: slide the plate sideways into the target location
# def plate_slide_side(robot):
    if check("the robot's gripper is not vertically aligned with the plate and the robot's gripper is not near the plate"):
        robot.adjust("the gripper above the plate")
    if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is not around the plate"):
        robot.pickup("the gripper around the plate")
    if check("the robot's gripper is holding the plate and the plate is not in front of the target location"):
        robot.move("the plate towards the target location")
    if check("the plate is in front of the target location"):
        robot.slide("the plate sideways into the target location")