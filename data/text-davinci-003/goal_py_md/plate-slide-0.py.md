

# plate-slide: slide the plate into the target location
# def plate_slide(robot):
    # Steps:
    #  1. Put gripper above the plate
    #  2. Push the plate to the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.move_gripper("above the plate")
    # If the plate isn't below the gripper as seen from above, move the gripper
    # above the plate and close it.
    if check("the robot's gripper is not vertically aligned with the plate and the robot's gripper is open"):
        robot.move_gripper("vertically aligned with the plate", close_gripper=True)
    # If the gripper is near the plate, we've probably trapped the plate and can
    # slide it to the target location.
    if check("the robot's gripper is near the plate and the plate is below the robot's gripper"):
        robot.move_gripper("above the target location")