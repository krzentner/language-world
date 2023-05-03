# plate-slide-side: slide the plate sideways into the target location
def plate_slide_side(robot):
    # Steps:
    #  1. Put gripper above plate
    #  2. Drop gripper around plate
    #  3. Push gripper into the side of the plate
    #  4. Slide plate sideways to goal
    # First, line up the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above plate")
    # Drop the gripper around the plate.
    if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is not around the plate"):
        robot.put("gripper around plate")
    # Push the gripper into the side of the plate.
    if check("the robot's gripper is around plate and the robot's gripper is not pushed into the side of the plate"):
        robot.push("gripper into side of plate")
    # Slide the plate sideways to the goal.
    if check("the robot's gripper is pushed into the side of the plate"):
        robot.slide("plate to goal sideways")