# Steps:
    #  1. Put the gripper above the box lid
    #  2. Grab the box lid with the gripper
    #  3. Move the box lid above the box
    #  4. Place the box lid on the box
    # First, put the gripper above the box lid.
    if check("the robot's gripper is not above the box lid"):
        robot.move_gripper("above the box lid")
    # If the gripper is above the box lid, grab the box lid.
    if check("the robot's gripper is above the box lid and the robot's gripper is open"):
        robot.move_gripper("around the box lid", close_gripper=True)
    # Once we have the box lid, move it to be above the box.
    if check("the robot's gripper is around the box lid"):
        robot.move_gripper("above the box")
    # Finally, place the box lid on the box.
    if check("the robot's gripper is above the box and the box lid is downward aligned with the box"):
        robot.move_gripper("on top of the box", close_gripper=False)