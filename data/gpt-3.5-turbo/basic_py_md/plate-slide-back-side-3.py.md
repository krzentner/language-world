# plate-slide-back-side: slide the plate back sideways into the target location
# def plate_slide_back_side(robot):
    if check("the robot's gripper is not above the plate and the robot's gripper is not vertically aligned with the plate"):
        robot.put("the gripper above the plate")
    if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is not near the plate"):
        robot.slide("the gripper towards the plate")
    if check("the robot's gripper is near the plate and the plate is below the robot's gripper and the gripper is open"):
        robot.close("the gripper around the plate")
    if check("the robot's gripper is above the target location and the gripper is closed"):
        robot.slide("the plate sideways into the target location")