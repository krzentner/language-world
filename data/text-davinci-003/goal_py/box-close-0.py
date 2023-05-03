
    # Steps:
    #  1. Grab the box lid
    #  2. Put the li dback on the box
    # First, grab the box lid.
    # We need to get the gripper around the edge of the box lid, so move the
    # gripper around the edge until it is lined up with the box lid.
    if check("the robot's gripper is not around box lid"):
        robot.move_gripper("around box lid", close_gripper=True)
    # Now that the gripper is around the box lid, we can pick it up by lifting the
    # gripper up.
    if check("the robot's gripper is around box lid"):
        robot.move_gripper("above box")
    # If the gripper is lined up with the box, put the box lid back on the box.
    if check("the robot's gripper is above box and the box lid is not on box"):
        robot.move_gripper("above box lid", open_gripper=True)