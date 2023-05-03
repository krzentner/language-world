# plate-slide-side: slide the plate sideways into the target location
# def plate_slide_side(robot):
    if check("the robot's gripper is not vertically aligned with the plate and the gripper is not next to the plate"):
        robot.move("gripper next to plate")
    if check("the gripper is next to the plate and the gripper is not around the plate"):
        robot.grab("plate")
    if check("the gripper is around the plate"):
        robot.slide("plate towards target location")
    if check("the plate is at the target location"):
        robot.release("the plate at the target location")