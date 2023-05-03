# plate-slide-side: slide the plate sideways into the target location
def plate_slide_side(robot):
    # Steps:
    #  1. Put gripper slightly to the side of the plate
    #  2. Lower gripper around the plate
    #  3. Grip the plate
    #  4. Slide the plate to the target location
    # First, put the gripper slightly to the side of the plate.
    if check("the robot's gripper is not to the side of the plate"):
        robot.put("gripper to the side of the plate")
    # Once the gripper is to the side of the plate, lower it around the plate.
    if check("the robot's gripper is to the side of the plate and the gripper is not around the plate"):
        robot.put("gripper around the plate")
    # Once the gripper is around the plate, grip it.
    if check("the gripper is around the plate and the gripper is open"):
        robot.close("gripper around the plate")
    # Once the plate is gripped, slide it to the target location.
    if check("the plate is gripped and the plate is not at the target location"):
        robot.slide("the plate to the target location sideways")