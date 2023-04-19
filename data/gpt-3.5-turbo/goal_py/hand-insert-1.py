# Steps:
    #  1. Move the gripper close to the puck
    #  2. Pick up the puck
    #  3. Move the gripper to the target
    #  4. Release the puck
    # Although this is called "hand-insert", we'll use the gripper to pick up
    # and move the puck.
    # First, move the gripper close to the puck.
    if check("the robot's gripper is not near the puck"):
        robot.move_gripper("near the puck")
    # If the gripper is near the puck but not around it, grab the puck.
    if check("the robot's gripper is near the puck and the robot's gripper is open"):
        robot.move_gripper("around the puck", close_gripper=True)
    # Once the gripper has the puck, move it to the target location.
    if check("the robot's gripper is around the puck and not near the target location"):
        robot.move_gripper("near the target location")
    # Release the puck at the target location.
    if check("the robot's gripper is near the target location and the robot's gripper is closed"):
        robot.move_gripper("above the target location", open_gripper=True)