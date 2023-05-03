# plate-slide-back: slide the plate back into the target location
def plate_slide_back(robot):
    # Steps:
    #  1. Put gripper on the left side of the plate
    #  2. Push the gripper against the plate to stabilize it
    #  3. Slide the plate back
    # If the gripper is not on the left side of the plate, move it there.
    if check("the robot's gripper is not left of the plate"):
        robot.move_gripper("left of the plate")
    # Push the gripper against the plate to keep it stable.
    if check("the robot's gripper is left of the plate and the robot's gripper is not against the plate"):
        robot.move_gripper("against the plate")
    # Slide the plate back to the target location.
    if check("the robot's gripper is against the plate"):
        robot.move_gripper("near the target location")