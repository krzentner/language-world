

# plate-slide-side: slide the plate sideways into the target location
def plate_slide_side(robot):
    # Steps:
    #  1. Put gripper above the plate
    #  2. Line the plate up with the goal using the gripper
    #  3. Slide the plate sideways into the goal
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above plate")
    # As long the gripper is still mostly around the plate and the plate isn't lined
    # up with the goal, line up the plate with the goal.
    if check("the robot's gripper is forward aligned with the plate and the plate is not horizontally aligned with goal"):
        robot.align("plate to goal")
    # If the plate is lined up with the goal to the side, slide it sideways.
    if check("plate is horizontally aligned with goal"):
        robot.slide("plate sideways into goal")