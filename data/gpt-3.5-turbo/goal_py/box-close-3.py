# Steps:
    #  1. Put gripper above box lid
    #  2. Drop gripper around box lid
    #  3. Close gripper around box lid
    #  4. Move box lid to box
    # First, put the gripper roughly above the box lid, so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not above box lid"):
        robot.move_gripper("above the box lid")
    # If the gripper isn't around the box lid, put it around the box lid.
    if check("the robot's gripper is not around box lid and the robot's gripper is open"):
        robot.move_gripper("near the box lid", close_gripper=True)
    # If the gripper is near the box lid and closed, move it to the box and put
    # the lid on the box.
    if check("the robot's gripper is around box lid"):
        robot.move_gripper("near the box", close_gripper=False) # Open gripper to place the lid on the box.