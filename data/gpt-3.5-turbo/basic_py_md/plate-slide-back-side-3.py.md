# plate-slide-back-side: slide the plate back sideways into the target location
def plate_slide_back_side(robot):
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above plate")
    if check("the plate is not left of the robot's gripper and the plate is not forward aligned with the robot's gripper"):
        robot.grab("plate")
    if check("the robot's gripper is forward aligned with the plate and the plate is not aligned with target location"):
        robot.move("plate to target location")
    if check("the plate is aligned with target location"):
        robot.slide("plate back")