# Steps:
    #  1. Put gripper above box lid
    #  2. Drop gripper around box lid
    #  3. Close gripper around box lid
    #  4. Move box lid to the box
    # First, put the gripper roughly above the box lid, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the box lid"):
        robot.move_gripper("above the box lid")
    # If the gripper isn't around the box lid, put it around the box lid.
    if check("the robot's gripper is not around the box lid and the robot's gripper is open"):
        robot.move_gripper("near the box lid", close_gripper=True)
    # If the gripper is near the box lid and closed, maybe we can grab it by lifting
    # the box lid.
    if check("the robot's gripper is around the box lid and lifted off the surface"):
        robot.move_gripper("above the box")
    # If the box lid is above the box, place it on top.
    if check("the robot's gripper is above the box and the box lid is above the box"):
        robot.move_gripper("on the box lid", close_gripper=False)