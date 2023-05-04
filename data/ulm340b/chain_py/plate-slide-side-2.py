
    # Steps:
    #  1. Put gripper left of plate
    #  2. Push gripper into the plate
    #  3. Slide the plate into the goal
    # First, the robot's gripper needs to be left of the plate.
    if check("the robot's gripper is not left of plate"):
        robot.put("gripper left of plate")
    # The robot needs to grip the plate from the side.
    # Then it can slide the plate to the right into the target location.
    # As long as the gripper is to the left of the plate and near it, we should
    # be able to grip it to slide it.
    if check("the robot's gripper is left of plate and the robot's gripper is near plate"):
        robot.push("the robot's gripper into the plate")
    # If the gripper is aligned with the plate and touching it, push it into the
    # goal.
    if check("the robot's gripper is near plate"):
        robot.slide("the plate into the goal")

# plate-slide-topdown: slide the plate into the goal
def plate_slide_topdown(robot):
    # Steps:
    #  1. Put gripper above plate
    #  2. Push gripper down on plate
    #  3. Slide the plate into the goal
    # First, the robot's gripper needs to be above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.put("gripper above plate")
    # The robot needs to grip the plate from above.
    # Then it can slide the plate into the target location.
    # As long as the gripper is above the plate and not touching it, we should
    # be able to grip it to slide it.
    if check("the robot's gripper is above the plate and the robot's gripper is not near plate"):
        robot.push("the gripper into the plate")
    # If the gripper is aligned with the plate and touching it, push it into the
    # goal.
    if check("the robot's gripper is above the plate and the robot's gripper is near plate"):
        robot.slide("the plate into the goal")

# peg-insert-topdown