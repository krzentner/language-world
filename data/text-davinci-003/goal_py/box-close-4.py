
    # Steps:
    #  1. Put the gripper above the box lid
    #  2. Drop the gripper around the box lid
    #  3. Close the gripper around the box lid
    #  4. Move the box lid above the box
    # If the gripper is not near the box lid, move it to the box lid.
    if check("the robot's gripper is not near the box lid"):
        robot.move_gripper("near the box lid")
    # Once the gripper is near the box lid, close the gripper around the box
    # lid to pick it up.
    if check("the robot's gripper is not closed"):
        robot.move_gripper("above the box", close_gripper=True)
    # Now that we have the box lid, move it to the box.
    if check("the robot's gripper is closed and the box lid is not above the box"):
        robot.move_gripper("near the box")