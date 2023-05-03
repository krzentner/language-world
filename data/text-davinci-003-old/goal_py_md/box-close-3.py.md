

# box-close: pick up the box lid and place it on the box
# def box_close(robot):
    # Steps:
    #  1. Put gripper above box lid
    #  2. Grab box lid with the gripper
    #  3. Move the box lid to the box, then place it on the box
    # First, put the gripper above the box lid.
    if check("the robot's gripper is not above the box lid"):
        robot.move_gripper("above the box lid")
    # If the gripper isn't around the box lid, put it around the box lid.
    if check("the robot's gripper is not around box lid and the robot's gripper is open"):
        robot.move_gripper("near the box lid", close_gripper=True)
    # If the gripper is near the box lid, we've probably trapped the box lid and can
    # move it to the box.
    if check("the robot's gripper is near the box lid"):
        robot.move_gripper("above the box")
    # Once the gripper is above the box, place the lid on the box.
    if check("the robot's gripper is above the box"):
        robot.move_gripper("above the box")