# Steps:
    #  1. Put gripper above box lid
    #  2. Drop gripper around box lid
    #  3. Close gripper around box lid
    #  4. Move box lid to box
    #  5. Align box lid with box
    #  6. Push box lid onto box
    # First, put the gripper roughly above the box lid.
    if check("the robot's gripper is not above the box lid"):
        robot.place("gripper above box lid")
    # If the gripper isn't around the box lid, put it around the box lid.
    if check("the robot's gripper is not around box lid and the robot's gripper is open"):
        robot.drop("gripper around box lid")
    # If the gripper is near the box lid and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near box lid and the robot's gripper is open"):
        robot.close("gripper around box lid")
    # We closed the gripper, and the box lid is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the box lid to the box.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above box lid and the robot's gripper is closed"):
        robot.reach("box")
    # If the box lid isn't above the box, move it there.
    if check("the box lid is not above the box"):
        robot.move("box lid above box")
    # If the box lid is above the box but not aligned, align it.
    if check("the box lid is above the box but not aligned"):
        robot.align("box lid to box")
    # If the box lid is aligned with the box, push it onto the box.
    if check("the box lid is aligned with the box"):
        robot.push("box lid onto box")