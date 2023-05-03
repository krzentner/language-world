# plate-slide-back: slide the plate back into the target location
def plate_slide_back(robot):
    # Steps:
    #  1. Put gripper above the plate
    #  2. Push gripper into the plate
    #  3. Slide the plate back into the target location
    # The robot can slide the plate back into the target location by trapping it 
    # by pushing down on it from above and moving the gripper.
    # If the plate isn't below the gripper as seen from above, move the gripper
    # above the plate.
    if check("the robot's gripper is not above the plate and the plate is not at the target location"):
        robot.put("the gripper above the plate")
    # If the gripper is aligned with the plate but not near it, move the gripper
    # down to the plate to slide it.
    if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is not near the plate"):
        robot.push("the gripper into the plate")
    # If the gripper is near the plate, we've probably trapped the plate and can
    # slide it back to the target location.
    # Close the gripper to make sure we keep control of the plate.
    # If the plate is below the gripper, we should push it back to the target location.
    if check("the robot's gripper is near the plate and the plate is below the robot's gripper"):
        if check("the plate is not at the target location"):
            robot.slide("the plate back to the target location")