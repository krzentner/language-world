# plate-slide-back: slide the plate back into the target location
def plate_slide_back(robot):
    if check("the robot's gripper is not above the plate and the robot's gripper is not vertically aligned with the plate"):
        robot.put("the gripper above the plate")
    if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is not near plate"):
        robot.push("the gripper into the plate")
    if check("the robot's gripper is near the plate and the plate is below the robot's gripper"):
        robot.slide("the plate back to the target location")