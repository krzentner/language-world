# plate-slide-back: slide the plate back into the target location
# def plate_slide_back(robot):
    # Steps:
    #  1. Put gripper above plate
    #  2. Push gripper into plate
    #  3. Slide plate back into target location
    # The robot can slide the plate back by trapping it by pushing down on it from
    # above and moving the gripper.
    # If the plate isn't below the gripper as seen from above, move the gripper
    # above the plate.
    if check("the robot's gripper is not above the plate and the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate")
    # If the gripper is aligned with the plate but not near it, move the gripper
    # down to the plate to slide it.
    if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is not near the plate"):
        robot.move_gripper("above the plate", close_gripper=True)
    # If the gripper is near the plate, we've probably trapped the plate and can
    # slide it back to the target location.
    # Close the gripper to make sure we keep control of the plate.
    if check("the robot's gripper is near the plate and the plate is below the robot's gripper"):
        robot.move_gripper("above the target location", open_gripper=True)