# plate-slide-back: slide the plate back into the target location
def plate_slide_back(robot):
    if check("the robot's gripper is not above the plate and the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above plate")
    if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is not near the plate"):
        robot.push("gripper into plate")
    if check("the robot's gripper is near the plate and the plate is below the robot's gripper"):
        robot.move("gripper to left of plate")
    if check("the robot's gripper is in front of the target location"):
        robot.push("plate back into target location")