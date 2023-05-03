# plate-slide-side: slide the plate sideways into the target location
def plate_slide_side(robot):
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above plate")
    if check("plate is not beside the robot's gripper and the robot's gripper is not near the plate"):
        robot.move("gripper to side of plate")
    if check("the robot's gripper is near the plate"):
        robot.slide("plate to the target location")