
    # Steps:
    #  1. Put gripper above and near plate
    #  2. Push gripper into top of plate
    #  3. Slide plate back to goal
    # The robot can slide the plate by trapping it by pushing down on it from
    # above and moving the gripper.
    # First, put the gripper above the plate.
    if check("the robot's gripper is not above plate"):
        robot.put("gripper above plate")
    # If the gripper is aligned with the plate but not near it, move the gripper
    # down to the plate to slide it.
    if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is not near plate"):
        robot.push("gripper into plate")
    # If the gripper is near the plate, we've probably trapped the plate and can
    # slide it back to the target location.
    if check("the robot's gripper is near plate and the robot's gripper is above the plate"):
        robot.slide("plate backwards to goal")

# plate-slide: slide the plate into the target location
def plate_slide(robot):
    # Steps:
    #  1. Put gripper above and near plate
    #  2. Push gripper into top of plate
    #  3. Slide plate to goal
    # The robot can slide the plate by trapping it by pushing down on it from
    # above and moving the gripper.
    # First, put the gripper above the plate.
    if check("the robot's gripper is not above plate"):
        robot.put("gripper above plate")
    # If the gripper is aligned with the plate but not near it, move the gripper
    # down to the plate to slide it.
    if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is not near plate"):
        robot.push("gripper into plate")
    # If the gripper is near the plate, we've probably trapped the plate and can
    # slide it to the target location.
    if check("the robot's gripper is near plate and the robot's gripper is above the plate"):
        robot.slide("plate forwards to goal")

# pick-place-topdown: