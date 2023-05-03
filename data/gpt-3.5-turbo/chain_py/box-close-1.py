# Steps:
    #  1. Put gripper above box lid
    #  2. Drop gripper around box lid
    #  3. Close gripper around box lid
    #  4. Move box lid towards box
    #  5. Lower box lid onto box
    # First, put the gripper roughly above the box lid.
    if check("the robot's gripper is not above the box lid"):
        robot.put("gripper above box lid")
    # If the gripper isn't around the box lid, put it around the box lid.
    if check("the robot's gripper is not around box lid and the robot's gripper is open"):
        robot.drop("gripper around box lid")
    # If the gripper is near the box lid and open, maybe we can grab it by
    # closing the gripper.
    if check("the robot's gripper is near box lid and the robot's gripper is open"):
        robot.close("gripper around box lid")
    # We closed the gripper, and the box lid is still near the gripper, so maybe
    # we grabbed it.
    # Try to move the box lid towards the box.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above box lid and the robot's gripper is closed"
             " and the box lid is not on top of the box"):
        robot.move("box lid towards box")
    # If the box lid is now on top of the box, lower it.
    if check("the box lid is on top of the box"):
        robot.push("box lid down onto box")