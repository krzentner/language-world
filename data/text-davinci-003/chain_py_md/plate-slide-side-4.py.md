

# plate-slide-side: slide the plate sideways into the target location
def plate_slide_side(robot):
    # Steps:
    #  1. Put gripper above plate
    #  2. Line up gripper with plate from the side
    #  3. Slide plate sideways into the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above plate")
    # As long as the gripper isn't lined up with the plate from the side, keep
    # adjusting it until it is.
    if check("the robot's gripper is not side aligned with the plate"):
        robot.align("gripper with plate from side")
    # If the gripper is side aligned with the plate, slide it sideways into the
    # target location.
    if check("the robot's gripper is side aligned with plate"):
        robot.slide("plate sideways into target")