
    # Steps:
    #  1. Put gripper below plate
    #  2. Push gripper up into plate
    #  3. Slide plate to goal
    # The robot can slide the plate by trapping it by pushing up on it from
    # below and moving the gripper.
    # If the plate isn't above the gripper as seen from above, move the gripper
    # below the plate.
    if check("the robot's gripper is not below plate and the robot's gripper is not vertically aligned with plate"):
        robot.move_gripper("vertically aligned with the plate")
    # If the gripper is aligned with the plate but not near it, move the gripper
    # up to the plate to slide it.
    if check("the robot's gripper is vertically aligned with plate and the robot's gripper is not above plate"):
        robot.move_gripper("below the plate")
    # If the gripper is below the plate, we've probably trapped the plate and
    # can slide it to the target location.
    if check("the robot's gripper is above the plate and the plate is above the robot's gripper"):
        robot.move_gripper("below the target location")

# plate-slide-back: slide the plate out from the target location
def plate_slide_back(robot):
    # Steps:
    #  1. Put gripper above plate
    #  2. Push gripper into back of plate
    #  3. Slide plate out from goal
    # If the plate isn't below the gripper as seen from above, move the gripper
    # above the plate.
    if check("the robot's gripper is not above plate and the robot's gripper is not vertically aligned with plate"):
        robot.move_gripper("vertically aligned with the plate")
    # If the gripper is aligned with the plate but not near it, move the gripper
    # down to the plate to slide it.
    if check("the robot's gripper is vertically aligned with plate and the robot's gripper is not near plate"):
        robot.move_gripper("above the plate")
    # If the gripper is near the plate, we've probably trapped the plate and
    # can slide it to the target location.
    if