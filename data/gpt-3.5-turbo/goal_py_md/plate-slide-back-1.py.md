# plate-slide-back: slide the plate back into the target location
def plate_slide_back(robot):
    # Steps:
    #  1. Put gripper above plate
    #  2. Push gripper into top of plate
    #  3. Slide plate back to target location
    # We can slide the plate by pushing down on it from above and moving the gripper.
    # First, move the gripper above the plate if it isn't already there.
    if check("the robot's gripper is not above plate and the robot's gripper is not vertically aligned with plate"):
        robot.move_gripper("vertically aligned with the plate")
    # If the gripper is aligned with the plate but not near it, move the gripper down to the plate to slide it.
    if check("the robot's gripper is vertically aligned with plate and the robot's gripper is not near plate"):
        robot.move_gripper("above the plate", close_gripper=True)
    # If the gripper is near the plate, we've probably trapped the plate and can slide it back to the target location.
    # Close the gripper to make sure we keep control of the plate.
    if check("the robot's gripper is near the plate and the plate is below the robot's gripper"):
        robot.move_gripper("behind the plate", close_gripper=True)
    # Once the gripper is behind the plate, gently push forward to slide the plate back to the target location.
    if check("the robot's gripper is around plate and the plate is between the robot's gripper and target location"):
        robot.move_gripper("above the target location")