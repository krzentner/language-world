
    # Steps:
    #  1. Put gripper above the box lid
    #  2. Drop gripper around the box lid
    #  3. Close gripper around the box lid
    #  4. Move box lid to box
    # First, put the gripper above the box lid so we don't bump it while trying
    # to grab it.
    if check("the robot's gripper is not above the box lid"):
        robot.place("gripper above box lid")
    # If the gripper isn't around the box lid, put it around the box lid.
    if check("the robot's gripper is not around box lid and the robot's gripper is open"):
        robot.drop("gripper around box lid")
    # If the gripper is near the box lid and open, maybe we can grab it by
    # closing the gripper.
    if check("the robot's gripper is near box lid and the robot's gripper is open"):
        robot.close("gripper around box lid")
    # We closed the gripper, and the box lid is still near the gripper, so
    # hopefully we grabbed it.
    # Try to move the box lid to the box.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above box lid and the robot's gripper is closed"):
        robot.place("box lid onto box")