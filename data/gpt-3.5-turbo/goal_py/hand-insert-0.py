# Steps:
    #  1. Move gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move gripper to target location
    # First, put the gripper roughly above the puck, so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # Once we're above the puck, we can drop the gripper around it.
    if check("the robot's gripper is not around puck"):
        robot.move_gripper("near the puck")
    # Once the gripper is around the puck, we can close it to pick up the puck.
    if check("the robot's gripper is around the puck and open"):
        robot.move_gripper("around the puck", close_gripper=True)
    # Once the gripper has the puck, we can move it to the target location.
    if check("the robot's gripper is around the puck and closed"):
        robot.move_gripper("near the target location", open_gripper=True)