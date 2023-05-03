
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck to target location
    # First, put the gripper roughly above the puck.
    if check("the robot's gripper is not above puck"):
        robot.move_gripper("above the puck", close_gripper=True)
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck"):
        robot.move_gripper("near the puck", close_gripper=True)
    # Once the gripper is around the puck, just move it to the target location.
    if check("the robot's gripper is near puck"):
        robot.move_gripper("near the target location")