
    # Steps:
    #  1. Put gripper left of the plate
    #  2. Slide the plate to the left into the goal
    # First, put the gripper roughly left of the plate.
    if check("the robot's gripper is not left of the plate"):
        robot.move_gripper("near the plate")
    # If the plate is right of the robot's gripper, slide the plate to the
    # left.
    if check("the robot's gripper is forward aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate")

# plate-slide-back: slide the plate back into the target location
def plate_slide_back(robot):
    # Steps:
    #  1. Put gripper left of the plate
    #  2. Slide the plate to the left into the goal
    # First, put the gripper roughly left of the plate.
    if check("the robot's gripper is not left of the plate"):
        robot.move_gripper("near the plate")
    # If the plate is right of the robot's gripper, slide the plate to the
    # left.
    if check("the robot's gripper is forward aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate")

# plate-slide: slide the plate sideways into the target location
def plate_slide(robot):
    # Steps:
    #  1. Put gripper right of the plate
    #  2. Slide the plate to the right into the goal
    # First, put the gripper roughly left of the plate.
    if check("the robot's gripper is not right of the plate"):
        robot.move_gripper("near the plate")
    # If the plate is left of the robot's gripper, slide the plate to the right.
    if check("the robot's gripper is forward aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate")

# plate-press-side: push the plate from the side until it's inserted into the
# goal
def plate_press_side(robot):
    # Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate
    #  3.