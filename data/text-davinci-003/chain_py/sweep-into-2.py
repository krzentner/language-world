
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Sweep the cube towards the goal
    # First, put the gripper above the cube, so that we don't bump it while trying
    # to grab it.
    if check("the robot's gripper is not above the cube"):
        robot.place("gripper above cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    # If the cube is near the gripper, try sweeping it to the goal.
    if check("the robot's gripper is near cube"):
        robot.sweep("cube to goal")