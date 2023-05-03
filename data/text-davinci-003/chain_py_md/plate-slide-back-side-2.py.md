

# plate-slide-back-side: slide the plate back sideways into the target location
def plate_slide_back_side(robot):
    # Steps:
    #  1. Put gripper in front of plate
    #  2. Push plate backwards
    #  3. Slide plate sideways into target location
    # First, put the gripper in front of the plate.
    if check("the robot's gripper is not forward aligned with the plate"):
        robot.put("gripper in front of plate")
    # If the robot's gripper is forward aligned with the plate, it should be
    # ready to push the plate backwards.
    if check("the robot's gripper is forward aligned with the plate"):
        robot.push("plate backwards")
    # Once the plate is pushed back, we can slide the plate sideways into the
    # target location.
    if check("the robot's gripper is sideways aligned with the plate and the robot's gripper is near the plate"):
        robot.slide("plate sideways")