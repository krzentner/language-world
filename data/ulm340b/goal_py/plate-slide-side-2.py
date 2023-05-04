
    # Steps:
    #  1. Put gripper left of the plate
    #  2. Move gripper to the plate
    #  3. Slide the plate right
    # If the gripper is not near the plate, move it to near the plate.
    if check("the robot's gripper is not near the plate"):
        robot.move_gripper("forward aligned with the plate", close_gripper=True)
    # If the plate is near the gripper, we can move it right.
    if check("the plate is in front of the robot's gripper"):
        robot.move_gripper("vertically aligned with the plate")

# plate-slide-topdown: slide the plate towards us into the target location
def plate_slide_topdown(robot):
    # Steps:
    #  1. Put gripper above the plate
    #  2. Move gripper to the plate
    #  3. Slide the plate towards us
    # First, put the gripper above the plate, so that we can slide it.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate")
    # If the plate is above the gripper, we can slide the plate towards us.
    if check("the plate is left of the robot's gripper"):
        robot.move_gripper("around the plate")

# plate-slide-away: slide the plate away from us into the target location
def plate_slide_away(robot):
    # Steps:
    #  1. Put gripper below the plate
    #  2. Move gripper to the plate
    #  3. Slide the plate away from us
    # First, put the gripper below the plate, so that we can slide it.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate")
    # If the plate is below the gripper, we can slide the plate away from us.
    if check("the plate is right of the robot's gripper"):
        robot.move_gripper("around the plate")

# peg-unstack: pick up the top peg and drop it on the table
def peg_unstack(robot):
    # Steps: