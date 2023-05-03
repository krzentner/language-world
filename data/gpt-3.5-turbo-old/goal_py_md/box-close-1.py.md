# box-close: pick up the box lid and place it on the box
# def box_close(robot):
    # Steps:
    #  1. Put gripper above the box lid
    #  2. Grab the box lid with the gripper
    #  3. Lift the box lid off the box
    #  4. Move the gripper over the box and verify that it is properly aligned
    #  5. Lower the box lid onto the box
    #  6. Release the box lid
    # First, put the gripper above the box lid.
    if check("the robot's gripper is not vertically aligned with the box lid"):
        robot.move_gripper("vertically aligned with the box lid")
    # If the gripper isn't around the box lid, put it around the box lid.
    if check("the robot's gripper is not around box lid and the robot's gripper is open"):
        robot.move_gripper("near the box lid", close_gripper=True)
    # If the gripper is around the box lid and vertical, lift it off the box.
    if check("the robot's gripper is around the box lid and the box lid is on the box and the box lid is not vertically aligned with the gripper"):
        robot.move_gripper("above the box lid")
    # If we have the box lid in the gripper, move it over the box.
    if check("the box lid is in the robot's gripper and the robot's gripper isn't over the box"):
        robot.move_gripper("over the box")
    # If the gripper is over the box, align it properly.
    if check("the robot's gripper is over the box and the box lid is not aligned with the box"):
        robot.move_gripper("aligned with the box", close_gripper=True)
    # If the gripper is aligned with the box, lower the box lid and release it.
    if check("the robot's gripper is aligned with the box and the robot's gripper is not near the box lid"):
        robot.move_gripper("near the box lid", close_gripper=False)