
    # Steps:
    #  1. Put gripper above the box lid
    #  2. Grab the lid with the gripper
    #  3. Move the lid to the box
    #  4. Put the lid down onto the box
    # First, put the gripper roughly between the lid and the box.
    if check("the robot's gripper is not above the box lid"):
        robot.move_gripper("above the box lid")
    # If the gripper isn't around the lid, put it around the lid.
    if check("the robot's gripper is not around box lid and the robot's gripper is open"):
        robot.move_gripper("below the box lid", close_gripper=True)
    # Now that the gripper is around the lid, move it onto the box.
    if check("the robot's gripper is above the box lid and the robot's gripper is closed"):
        robot.move_gripper("on top of the box", open_gripper=True)