
    # Steps:
    #  1. Put gripper above box lid
    #  2. Drop gripper around box lid
    #  3. Close gripper around box lid
    #  4. Move box lid above box
    #  5. Lower box lid into box
    # The lid of the box is a small object, so it's easy for the robot to hold
    # it and manipulate it.
    # First, put the gripper above the box lid, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the box lid"):
        robot.place("gripper above box lid")
    # If the gripper isn't around the box lid, put it around the box lid.
    if check("the robot's gripper is not around the box lid and the robot's gripper is open"):
        robot.drop("gripper around box lid")
    # If the gripper is near the box lid and open, maybe we can grab it by
    # closing the gripper.
    if check("the robot's gripper is near box lid and the robot's gripper is open"):
        robot.close("gripper around box lid")
    # We closed the gripper, and the box lid is still near the gripper, so
    # maybe we grabbed it.
    # Try to move the box lid to the top of the box.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above box lid and the robot's gripper is closed"):
        robot.place("box lid above box")
    # If the box lid is above the box and the gripper is around it, maybe we
    # can lower it into the box.
    if check("the robot's gripper is around the box lid and the robot's gripper is above the box"):
        robot.lower("box lid into box")

# box-open: open the box by picking up the lid
def box_open(robot):
    # Steps:
    #  1. Put gripper above box lid
    #  2. Grab box lid with gripper
    #  3. Raise the box lid out of the box
    #  4. Lower