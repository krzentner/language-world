
    # Steps:
    #  1. Put gripper above the plate
    #  2. Push gripper into top of plate
    #  3. Slide the plate back to the target location
    # The robot can slide the plate by trapping it by pushing down on it from
    # above and moving the gripper.
    # If the plate isn't below the gripper as seen from above, move the gripper
    # above the plate.
    if check("the robot's gripper is not almost vertically aligned with the plate"):
        robot.move_gripper("above the plate")
    # If the gripper is aligned with the plate but not near it, move the gripper
    # down to the plate to slide it.
    if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is not near the plate"):
        robot.move_gripper("around the plate", close_gripper=True)
    # If the gripper is near the plate, we've probably trapped the plate and can
    # slide it to the target location.
    # Close the gripper to make sure we keep control of the plate.
    if check("the robot's gripper is near the plate and the robot's gripper is open"):
        robot.move_gripper("around the target location")

# plate-slide-forward-side: slide the plate forward sideways into the target location
def plate_slide_forward_side(robot):
    # Steps:
    #  1. Put gripper above the plate
    #  2. Push gripper into top of plate
    #  3. Slide the plate back to the target location
    # The robot can slide the plate by trapping it by pushing down on it from
    # above and moving the gripper.
    # If the plate isn't below the gripper as seen from above, move the gripper
    # above the plate.
    if check("the robot's gripper is not almost vertically aligned with the plate"):
        robot.move_gripper("above the plate")
    # If the gripper is aligned with the plate but not near it, move the gripper
    # down to the plate to slide it.
    if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is not near the plate"):
       