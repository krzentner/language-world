
    # Steps:
    #  1. Put gripper above plate
    #  2. Drop gripper onto plate
    #  3. Slide the plate to the goal
    # First, put the gripper above the plate, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above plate and the robot's gripper is not vertically aligned with plate"):
        robot.move("gripper above plate")
    # If the gripper isn't above the plate, put it above the plate.
    if check("the robot's gripper is above plate and the robot's gripper is open"):
        robot.drop("gripper onto plate")
    # If the gripper is near the plate and open, maybe we can grab it by closing
    # the gripper.
    # We can push the plate to the goal.
    if check("the robot's gripper is near plate and the robot's gripper is open"):
        robot.slide("plate to goal")

# plate-slide-side: slide the plate into the target location from the side
def plate_slide_side(robot):
    # Steps:
    #  1. Put gripper in front of plate
    #  2. Slide gripper into plate
    #  3. Slide the plate to the goal
    # First, put the gripper above the plate, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not in front of the plate and the robot's gripper is not vertically aligned with the plate"):
        robot.move("gripper in front of plate")
    # If the gripper isn't above the plate, put it above the plate.
    if check("the robot's gripper is in front of plate and the robot's gripper is open"):
        robot.slide("gripper into the plate")
    # If the gripper is near the plate and open, maybe we can grab it by closing
    # the gripper.
    # We can push the plate to the goal.
    if check("the robot's gripper is near plate and the robot's gripper is open"):
        robot.slide("plate to goal")

# plate-pick: pick up the plate and put it in the target location
def