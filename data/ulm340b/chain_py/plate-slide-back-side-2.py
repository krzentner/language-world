
    # Steps:
    #  1. Put gripper right of plate
    #  2. Grab the plate with the gripper
    #  3. Line the plate up with the target location
    #  4. Slide the plate sideways into the target location
    # If the robot's gripper is to the right of the plate, we should move the
    # gripper to the left of the plate to start moving the plate right.
    if check("the robot's gripper is to the right of the plate and the robot's gripper is not near the plate"):
        robot.move("gripper left of plate")
    # If the robot's gripper is near the plate and the plate isn't aligned with
    # the target location, we should align it with the target location.
    if check("the robot's gripper is near the plate and the plate is not horizontally aligned with the goal"):
        robot.align("plate to goal")
    # If the plate is horizontally aligned with the goal we can slide it into
    # the goal.
    if check("the plate is horizontally aligned with the goal"):
        robot.insert("plate into goal")

# plate-push: slide the plate to the target location
def plate_push(robot):
    # Steps:
    #  1. Put gripper above plate
    #  2. Push gripper into top of plate
    #  3. Slide plate to goal
    # We need to put the gripper above the plate before we can grab it.
    # If the plate isn't below the gripper as seen from above, move the gripper
    # above the plate.
    if check("the plate is not below the robot's gripper"):
        robot.put("the gripper above the plate")
    # If the gripper is aligned with the plate but not near it, move the gripper
    # down to the plate to slide it.
    if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is not near plate"):
        robot.push("the gripper into the plate")
    # If the gripper is near the plate, we can slide it to the target location.
    if check("the robot's gripper is near the plate and the plate is below the robot's gripper"):
        robot.slide("the plate to the