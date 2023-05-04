
    # Steps:
    #  1. Put gripper above box lid
    #  2. Drop gripper around box lid
    #  3. Close gripper around box lid
    #  4. Move box lid over box
    #  5. Put box lid above box
    # First, put the gripper roughly above box lid, so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not above the box lid"):
        robot.place("gripper above box lid")
    # If the gripper isn't around the box lid, put it around the box lid.
    if check("the robot's gripper is not around box lid and the robot's gripper is open"):
        robot.drop("gripper around box lid")
    # If the gripper is near the box lid and open, maybe we can grab it by
    # closing the gripper.
    if check("the robot's gripper is near box lid and the robot's gripper is open"):
        robot.close("gripper around box lid")
    # We closed the gripper, and the box lid is still near the gripper, so maybe
    # we grabbed it.
    # Try to move the box lid over the box.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above box lid and the robot's gripper is closed"):
        robot.move("box lid to box")
    # Once the box lid is roughly over the box, we can put it down.
    if check("box lid is over box"):
        robot.place("box lid on box")

# box-open: pick up the box lid from the box and hold it
def box_open(robot):
    # Steps:
    #  1. Put gripper above box lid
    #  2. Drop gripper around box lid
    #  3. Close gripper around box lid
    #  4. Move box lid away from box
    # First, put the gripper roughly above box lid, so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not above the box lid"):
        robot.place("gripper