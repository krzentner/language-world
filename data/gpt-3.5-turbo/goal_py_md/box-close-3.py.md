# box-close: pick up the box lid and place it on the box
# def box_close(robot):
    # Steps:
    #  1. Put gripper above the box lid
    #  2. Grab the lid with the gripper
    #  3. Move the gripper over to the box and put the lid on top
    # First, put the gripper above the box lid.
    if check("the robot's gripper is not vertically aligned with the box lid"):
        robot.move_gripper("vertically aligned with the box lid")
    # If the gripper isn't around the lid, put it around the lid.
    if check("the robot's gripper is not around box lid and the robot's gripper is open"):
        robot.move_gripper("near the box lid", close_gripper=True)
    # If the gripper is around the lid and closed, move it over to the box and put
    # the lid on top, making sure to open the gripper to release the lid.
    if check("the robot's gripper is around box lid and the robot's gripper is closed"):
        robot.move_gripper("above the box", open_gripper=True)