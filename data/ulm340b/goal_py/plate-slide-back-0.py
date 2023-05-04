
    # Steps:
    #  1. Put gripper above plate
    #  2. Grab plate
    #  3. Slide plate backwards
    # We have to put the gripper above the plate first, so we can grab the
    # plate.
    if check("the robot's gripper is not above the plate"):
        robot.move_gripper("vertically aligned with the plate")
    # If we have the plate, we can slide it backwards to the target location.
    # However, if we don't have the plate and the gripper isn't lined up with
    # the plate, put it above the plate.
    if check("the plate is behind the robot's gripper"):
        robot.move_gripper("vertically aligned with the plate")
    # If we have the plate, pull it to the target location.
    if check("the plate is in front of the robot's gripper"):
        robot.move_gripper("behind the target location")

# plate-slide-side: slide the plate side into the target location
def plate_slide_side(robot):
    # Steps:
    #  1. Put gripper left of the plate
    #  2. Grab plate
    #  3. Slide plate side
    # If we don't have the plate, put the gripper left of it to grab it.
    if check("the plate is not left of the robot's gripper"):
        robot.move_gripper("vertically aligned with the plate")
    # If we have the plate, pull it to the target location.
    if check("the plate is left of the robot's gripper"):
        robot.move_gripper("horizontally aligned with the plate")

# peg-insert-front: grab the peg and insert it into the hole from the front
def peg_insert_front(robot):
    # Steps:
    #  1. Put gripper above peg
    #  2. Drop gripper around peg
    #  3. Line the peg up with the hole
    #  4. Push the peg forwards into the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("above the peg")
    # As