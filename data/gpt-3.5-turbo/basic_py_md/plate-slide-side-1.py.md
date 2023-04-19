# plate-slide-side: slide the plate sideways into the target location
# def plate_slide_side(robot):
def plate_slide_side(robot):
    if check("the robot's gripper is not vertically aligned with the plate and the robot's gripper is not near the plate"):
        robot.move("gripper to right of the plate")
    if check("the robot's gripper is near the plate"):
        robot.slide("plate to the left")
    if check("the plate is in front of the robot's gripper"):
        robot.push("plate left harder")