
    # Steps:
    #  1. Put gripper above puck
    #  2. Close gripper around puck
    #  3. Lift puck off of the board
    #  4. Move puck to goal
    # If the gripper isn't above the puck, move it above the puck.
    # We don't need to be careful here, since the puck is small and the gripper
    # is far away.
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    # Once it's aligned, close the gripper around the puck.
    # This should be enough to pick up the puck.
    if check("the robot's gripper is above the puck"):
        robot.close("gripper around puck")
    # Now that the gripper is closed, lift the puck off of the board.
    if check("the robot's gripper is closed and the puck is below the robot's gripper"):
        robot.lift("puck off of board")
    # Now that the puck is lifted up, move it to the goal.
    if check("the puck is above the robot's gripper"):
        robot.place("puck at goal")