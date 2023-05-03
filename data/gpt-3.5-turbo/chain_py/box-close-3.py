# Steps:
    #  1. Put gripper above box lid
    #  2. Drop gripper around box lid
    #  3. Close gripper around box lid
    #  4. Put gripper above box
    #  5. Drop gripper around box
    #  6. Slide box lid onto box
    # First, put the gripper roughly above the box lid, so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not above the box lid"):
        robot.place("gripper above box lid")
    # If the gripper is not around the box lid yet, move it around the box lid.
    if check("the robot's gripper is not around box lid and the robot's gripper is open"):
        robot.drop("gripper around box lid")
    # If the gripper is near the box lid and is open, maybe we can grab it by
    # closing the gripper.
    if check("the robot's gripper is near box lid and the robot's gripper is open"):
        robot.close("gripper around box lid")
    # If the gripper is holding the box lid, move it towards the box.
    # If we didn't grab the box lid, we'll just go back to an earlier step.
    if check("the robot's gripper is closed around box lid"):
        robot.place("gripper above box")
    # If the gripper isn't around the box yet, move it there.
    if check("the robot's gripper is not around box and the robot's gripper is closed"):
        robot.drop("gripper around box")
    # If the gripper is near the box and closed, put the box lid on the box by
    # sliding it.
    if check("the robot's gripper is near box and the robot's gripper is closed around box lid"):
        robot.slide("box lid onto box")