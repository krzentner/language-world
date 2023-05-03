
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move around the wall with the puck
    #  5. Move puck to goal
    # First, put the gripper above the puck.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.move_gripper("near the puck", close_gripper=True)
    # If the gripper is around the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.move_gripper("around the wall", close_gripper=True)
    # If the gripper is around the wall and the puck is in front, we can push the
    # puck to the goal.
    if check("the puck is forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the target location")