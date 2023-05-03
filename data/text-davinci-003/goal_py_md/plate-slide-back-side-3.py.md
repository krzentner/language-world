

# plate-slide-back-side: slide the plate back sideways into the target location
def plate_slide_back_side(robot):
    # Steps:
    #  1. Put gripper above plate
    #  2. Drop gripper around plate
    #  3. Lock the plate
    #  4. Pull back on the plate to slide it sideways
    # First, put the gripper above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.move_gripper("above the plate")
    # If the gripper isn't around the plate, move the gripper around it.
    if check("the robot's gripper is not around the plate and the robot's gripper is open"):
        robot.move_gripper("near the plate", close_gripper=True)
    # If the gripper is near the plate and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above the plate and the robot's gripper is closed"):
        robot.move_gripper("left of the plate")
    # If the plate is left of the gripper as seen from in front, we can
    # pull the plate to slide it back.
    if check("the robot's gripper is left of plate"):
        robot.move_gripper("forward aligned with the plate")