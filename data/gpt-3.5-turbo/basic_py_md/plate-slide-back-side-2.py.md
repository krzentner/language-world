# plate-slide-back-side: slide the plate back sideways into the target location
def plate_slide_back_side(robot):
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above plate")
    if check("the plate is not below the robot's gripper and the plate is not left of the robot's gripper"):
        robot.move("gripper to left of plate")
    if check("the robot's gripper is near the plate and the plate is below the robot's gripper"):
        robot.grab("the plate with gripper")
    if check("the robot's gripper is holding the plate and the plate is not near the target location"):
        robot.move("the plate towards the target location")
    if check("the plate is near the target location and the target location is below the robot's gripper"):
        robot.put("the plate at the target location")