
    # Steps:
    #  1. Put gripper above box lid
    #  2. Drop gripper around box lid
    #  3. Close gripper around box lid
    #  4. Move box lid over box and place it on top
    # To start, put the gripper above the box lid.
    if check("the robot's gripper is not above the box lid"):
        robot.move_gripper("above the box lid")
    # If the gripper isn't wrapping around the box lid, move it around the lid.
    if check("the robot's gripper is not around box lid"):
        robot.move_gripper("around the box lid", close_gripper=True)
    # If the gripper is wrapped around the box lid, we can probably pick it up by
    # closing the gripper and moving to in front of the box.
    if check("the robot's gripper is around box lid and the robot's gripper is closed"):
        robot.move_gripper("in front of the box")
    # Once the gripper is in front of the box, just place the lid on the box.
    if check("the robot's gripper is in front of the box"):
        robot.move_gripper("above the box", open_gripper=True)