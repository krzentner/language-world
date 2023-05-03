
    # Steps:
    #  1. Put the gripper above the lid
    #  2. Drop the gripper around the lid
    #  3. Lift the lid up
    #  4. Place the lid down on the box
    # First, put the gripper roughly above the lid, so that we don't bang into it
    # while trying to grab it.
    if check("the robot's gripper is not above the lid"):
        robot.move_gripper("above the lid")
    # If the gripper isn't around the lid, put it around the lid.
    if check("the robot's gripper isn't around the lid and the robot's gripper is open"):
        robot.move_gripper("near the lid", close_gripper=True)
    # If the gripper is near the lid and closed, maybe we can grab it by lifting
    # it up.
    if check("the robot's gripper is above the lid and the robot's gripper is closed"):
        robot.move_gripper("above the box")
    # If the lid is above the box, we have the lid and can put it down on the
    # box.
    if check("the lid is above the box"):
        robot.move_gripper("above the lid")