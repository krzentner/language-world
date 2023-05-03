# plate-slide-back: slide the plate back into the target location
def plate_slide_back(robot):
    # Steps:
    #  1. Move gripper above the plate
    #  2. Push gripper into the plate from above
    #  3. Slide the plate to the target location
    # First, line up the gripper from above with the plate.
    # We want to make sure the gripper is not already holding the plate, so we
    # only proceed if the gripper is not near the plate.
    if check("the robot's gripper is not near the plate"):
        robot.put("the gripper above the plate")
    # Once the gripper is above the plate, we can push down on it from above to
    # trap it under the gripper.
    if check("the robot's gripper is above the plate"):
        robot.push("the gripper into the plate")
    # With the plate trapped between the gripper and the table, we can slide it
    # back to the target location.
    if check("the plate is trapped under gripper and gripper and target location are horizontally aligned"):
        robot.slide("the plate to the target location")