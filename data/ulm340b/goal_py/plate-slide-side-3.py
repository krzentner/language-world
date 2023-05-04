
    # Steps:
    #  1. Put gripper above plate
    #  2. Push gripper into side of plate
    #  3. Slide plate to goal
    # If the plate isn't below the gripper as seen from above, move the gripper
    # above the plate.
    if check("the robot's gripper is not above plate and the robot's gripper is not vertically aligned with plate"):
        robot.move_gripper("vertically aligned with plate")
    # If the gripper is lined up with the plate but not touching the side of the
    # plate, move the gripper to the plate to slide it.
    if check("the robot's gripper is near the plate"):
        robot.move_gripper("above the plate", close_gripper=True)
    # If the gripper is near the side of the plate, we can slide the plate to
    # the target location.
    # Close the gripper to make sure we don't lose control of the plate.
    if check("the robot's gripper is near the plate"):
        robot.move_gripper("above the target location")

# plate-slide-topdown: slide the plate top-down into the target location
def plate_slide_topdown(robot):
    # Steps:
    #  1. Put gripper above plate
    #  2. Push gripper into top of plate
    #  3. Slide plate to goal
    # If the plate isn't below the gripper as seen from above, move the gripper
    # above the plate.
    if check("the robot's gripper is not above plate and the robot's gripper is not vertically aligned with plate"):
        robot.move_gripper("vertically aligned with plate")
    # If the gripper is lined up with the plate but not touching the top of the
    # plate, move the gripper to the plate to slide it.
    if check("the robot's gripper is above the plate"):
        robot.move_gripper("above the plate", close_gripper=True)
    # If the gripper is near the top of the plate, we can slide the plate to
    # the target location.
    # Close the gripper to make sure we don't lose control of the plate.
    if check("the robot'