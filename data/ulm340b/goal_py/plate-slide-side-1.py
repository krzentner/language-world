
    # Steps:
    #  1. Put gripper above the plate
    #  2. Push the gripper into the plate
    #  3. Slide the plate sideways into the target location
    # Since we're pushing the plate sideways, we need to put the gripper above
    # the plate.
    if check("the robot's gripper is not above the plate"):
        robot.move_gripper("above the plate")
    # If the gripper is above the plate but not pushing on the plate, move the
    # gripper down onto the plate.
    if check("the robot's gripper is above the plate and the robot's gripper is not near the plate"):
        robot.move_gripper("almost vertically aligned with the plate")
    # If the gripper is near the plate, we've probably trapped the plate and can
    # slide it sideways.
    # Close the gripper to make sure we keep control of the plate.
    if check("the plate is left of the robot's gripper"):
        robot.move_gripper("below the target location")


# plate-slide-top: slide the plate forwards into the target location
def plate_slide_top(robot):
    # Steps:
    #  1. Push gripper into top of plate
    #  2. Slide plate to goal
    # Since we're pushing the plate forwards, we just need to push the gripper
    # into the plate.
    # If the gripper is above the plate but not pushing on the plate, move the
    # gripper down onto the plate.
    if check("the robot's gripper is not near the plate"):
        robot.move_gripper("vertically aligned with the plate")
    # If the gripper is near the plate, we've probably trapped the plate and can
    # slide it sideways.
    # Close the gripper to make sure we keep control of the plate.
    if check("the plate is left of the robot's gripper"):
        robot.move_gripper("horizontally aligned with the target location")

# plate-slide-bot: slide the plate forwards into the target location from behind
def plate_slide_bot(robot):
    # Steps:
    #  1. Push gripper into top of plate
    #  2. Slide plate