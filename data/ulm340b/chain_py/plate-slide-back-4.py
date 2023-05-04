
    # Steps:
    #  1. Put gripper above plate
    #  2. Push gripper into top of plate
    #  3. Slide plate to goal
    # We need to put the gripper above the plate before we can slide it, because
    # of the angle of the robot's gripper.
    if check("the robot's gripper is not above the plate"):
        robot.put("gripper above plate")
    # If the plate isn't near the gripper as seen from above, push the gripper
    # into the plate.
    if check("the robot's gripper is above the plate and the robot's gripper is not near plate"):
        robot.push("gripper into plate")
    # If the plate is near the gripper and still aligned with it, we can slide
    # it to the target location.
    if check("the robot's gripper is near plate and the robot's gripper is aligned with plate"):
        robot.slide("plate to goal")

# plate-slide-side: slide the plate sideways into the target location
def plate_slide_side(robot):
    # Steps:
    #  1. Put gripper above plate
    #  2. Push gripper into top of plate
    #  3. Slide plate to goal
    # We need to put the gripper above the plate before we can slide it, because
    # of the angle of the robot's gripper.
    if check("the robot's gripper is not above the plate"):
        robot.put("gripper above plate")
    # If the plate isn't near the gripper as seen from above, push the gripper
    # into the plate.
    if check("the robot's gripper is above the plate and the robot's gripper is not near plate"):
        robot.push("gripper into plate")
    # If the plate is near the gripper and still aligned with it, we can slide
    # it to the target location.
    if check("the robot's gripper is near plate and the robot's gripper is aligned with plate"):
        robot.slide("plate to goal")

# drawer-close: push the drawer closed
def drawer_close(robot):
    # Steps:
    #  1. Put gripper around drawer handle
 