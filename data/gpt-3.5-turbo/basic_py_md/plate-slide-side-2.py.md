# plate-slide-side: slide the plate sideways into the target location
def plate_slide_side(robot):
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above plate")
    if check("the gripper is not around the plate and the gripper is open"):
        robot.drop("gripper around plate")
    if check("the robot's gripper is around the plate"):
        if check("the plate is to the right of the robot's gripper"):
            robot.move("gripper towards the plate")
        if check("the plate is in front of the robot's gripper"):
            robot.slide("the plate to the target location")