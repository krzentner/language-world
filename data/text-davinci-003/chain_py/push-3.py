
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck to goal
    # First, put the gripper above the puck.
    if check("the robot's gripper is not above the puck"):
        robot.put("gripper above puck")
    # If the gripper is still not near the puck, try to trap the puck between
    # the gripper and a flat surface.
    if check("the gripper is not near puck"):
        robot.push("gripper into puck")
    # If the gripper is now near the puck, slide the puck to the goal by
    # pushing on it.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.slide("puck to goal")