# plate-slide-side: slide the plate sideways into the target location
def plate_slide_side(robot):
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above plate")
    if check("the gripper is not around the plate and is not holding onto another object"):
        robot.grab("plate")
    if check("the robot's gripper is forward aligned with the target location"):
        robot.put("plate at target")
    if check("the robot's gripper is not at the target location"):
        robot.slide("the plate sideways to the target location")