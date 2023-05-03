# plate-slide-back-side: slide the plate back sideways into the target location
def plate_slide_back_side(robot):
    # Steps:
    #  1. Put the gripper behind the plate
    #  2. Close the gripper around the plate
    #  3. Slide the plate back to the target location
    # The robot can slide the plate by grabbing it from behind, with the gripper
    # straddling the plate.
    # If the gripper is not behind the plate, move it there.
    if check("the robot's gripper is not behind the plate"):
        robot.move_gripper("behind the plate")
    # If the gripper is behind the plate but not around it, move it around
    # the plate and close the gripper.
    if check("the robot's gripper is behind the plate and the robot's gripper is not around the plate"):
        robot.move_gripper("around the plate", close_gripper=True)
    # If the gripper is around the plate and behind it, slide the plate back.
    if check("the robot's gripper is around the plate and the robot's gripper is behind the plate and the plate is not at the target location"):
        robot.move_gripper("horizontally aligned with the target location")