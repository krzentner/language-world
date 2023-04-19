
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Move puck to target location
    # In order to pick up the puck, we need to put the gripper above the puck.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # If the gripper is positioned above the puck but not around it, move the
    # gripper around the puck.
    if check("the robot's gripper is above puck and the robot's gripper is not around puck"):
        robot.move_gripper("around the puck")
    # When the gripper is around the puck, move it near the target.
    if check("the robot's gripper is around puck"):
        robot.move_gripper("near the target location")