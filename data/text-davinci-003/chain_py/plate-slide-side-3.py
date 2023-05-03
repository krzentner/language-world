
    # Steps:
    #  1. Put gripper above plate
    #  2. Grip the plate with the gripper
    #  3. Line the plate up with the target location
    #  4. Slide the plate sideways into the goal
    # If the gripper is not above the plate, put the gripper above the plate.
    if check("the robot's gripper is not above plate"):
        robot.put("gripper above plate")
    # If the gripper is above the plate, close the gripper to grip it.
    if check("the robot's gripper is above plate and the robot's gripper is open"):
        robot.grab("plate")
    # As long as the gripper is still above the plate and the plate isn't lined
    # up with the goal, keep trying to line the plate up with the goal.
    if check("the robot's gripper is above the plate and the plate is not horizontally aligned with goal"):
        robot.align("plate to goal")
    # If the plate is lined up with the goal, we can slide it in.
    if check("the plate is horizontally aligned with goal"):
        robot.slide("plate to goal")