# box-close: pick up the box lid and place it on the box
# def box_close(robot):
    # Steps:
    #  1. Put gripper above the box lid
    #  2. Grab the box lid with the gripper
    #  3. Move the gripper above the box
    #  4. Place the box lid on the box
    # First, put the gripper above the box lid.
    if check("the robot's gripper is not above the box lid"):
        robot.move_gripper("above the box lid")
    # If the gripper isn't around the box lid, put it around the box lid.    
    if check("the robot's gripper is not around the box lid and the robot's gripper is open"):
        robot.move_gripper("near the box lid", close_gripper=True)
    # Move the gripper above the box once the box lid is grabbed.
    if check("the robot's gripper is near the box lid and the robot's gripper is closed"):
        robot.move_gripper("above the box")
    # Place the box lid on the box.
    if check("the robot's gripper is above the box"):
        robot.move_gripper("on top of the box")