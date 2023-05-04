
    # Steps:
    #  1. Put gripper above plate
    #  2. Push gripper into top of plate
    #  3. Slide plate to goal
    # The robot can slide the plate by trapping it by pushing down on it from
    # above and moving the gripper.
    # If the plate isn't below the gripper as seen from above, move the gripper
    # above the plate.
    if check("the robot's gripper is not above the plate and the robot's gripper is not vertically aligned with the plate"):
        robot.put("the gripper above the plate")
    # If the gripper is aligned with the plate but not near it, move the gripper
    # down to the plate to slide it.
    if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is not near plate"):
        robot.push("the gripper into the plate")
    # If the gripper is near the plate, we've probably trapped the plate and can
    # slide it to the target location.
    if check("the robot's gripper is near the plate and the plate is below the robot's gripper"):
        robot.slide("the plate to the goal")

# disc-slide: slide the disc to the target location
def disc_slide(robot):
    # Steps:
    #  1. Put gripper above disc
    #  2. Push gripper into top of disc
    #  3. Slide disc to goal
    # The robot can slide the disc by trapping it by pushing down on it from
    # above and moving the gripper.
    # If the disc isn't below the gripper as seen from above, move the gripper
    # above the disc.
    if check("the robot's gripper is not above the disc and the robot's gripper is not vertically aligned with the disc"):
        robot.put("the gripper above the disc")
    # If the gripper is aligned with the disc but not near it, move the gripper
    # down to the disc to slide it.
    if check("the robot's gripper is vertically aligned with the disc and the robot's gripper is not near disc"):
        robot.push("the gripper into the disc")
    # If the gripper is near the disc, we