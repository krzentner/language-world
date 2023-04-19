
    # Steps:
    #  1. Put gripper near the hole
    #  2. Push the peg out of the hole with the gripper
    #  3. Move peg to the target location
    # First, put the gripper near the hole.
    if check("the robot's gripper is not near the hole"):
        robot.move_gripper("near the hole")
    # If the gripper is near the hole and the peg is still in the hole, we can
    # push the peg out of the hole.
    if check("the robot's gripper is near the hole and the peg is still in the hole"):
        robot.move_gripper("above the peg", close_gripper=True)
    # If the gripper is near the peg and closed, we should have a good grip on
    # the peg and can move it to the target location.
    if check("the robot's gripper is above the peg and the robot's gripper is closed"):
        robot.move_gripper("near the target location")