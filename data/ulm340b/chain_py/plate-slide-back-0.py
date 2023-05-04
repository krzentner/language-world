
    # Steps:
    #  1. Put gripper above plate
    #  2. Push gripper into top of plate
    #  3. Slide plate to goal
    # Because the plate is a large object, it doesn't matter what angle the gripper
    # is at, as long as it's pushing in the right direction.
    # If the plate isn't roughly in front of the gripper as seen from above,
    # move the gripper to the plate.
    if check("the plate is not in front of the robot's gripper"):
        robot.move("gripper above plate")
    # If the gripper is not near the plate and the plate isn't near the target,
    # push the gripper into the plate to slide it to the target.
    if check("the plate is not near the goal and the robot's gripper is not near plate"):
        robot.push("gripper into plate")
    # We pushed the gripper into the plate and it's near the target location, so
    # slide the plate to the target location.
    if check("the plate is near the goal"):
        robot.slide("plate to goal")

# plate-slide-forward: slide the plate forward to the target location
def plate_slide_forward(robot):
    # Steps:
    #  1. Put gripper above plate
    #  2. Push gripper into top of plate
    #  3. Slide plate to goal
    # Because the plate is a large object, it doesn't matter what angle the gripper
    # is at, as long as it's pushing in the right direction.
    # If the plate isn't roughly in front of the gripper as seen from above,
    # move the gripper to the plate.
    if check("the plate is not in front of the robot's gripper"):
        robot.move("gripper above plate")
    # If the gripper is not near the plate and the plate isn't near the target,
    # push the gripper into the plate to slide it to the target.
    if check("the plate is not near the goal and the robot's gripper is not near plate"):
        robot.push("gripper into plate")
    # We pushed the gripper into the plate and it's near the target location, so
  