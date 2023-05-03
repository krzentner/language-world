
    # Steps:
    # 1. Put gripper above cube
    # 2. Drop gripper around cube
    # 3. Sweep cube towards goal
    # If the robot's gripper is not above the cube, move the gripper above the
    # cube.
    # We don't need to be careful about the direction, since the cube is small
    # and we're just sweeping it.
    if check("the robot's gripper is not above cube"):
        robot.put("gripper above cube")
    # If the gripper is above the cube and not around it, put the gripper around
    # the cube.
    if check("the robot's gripper is above cube and the robot's gripper is not around cube"):
        robot.drop("gripper around cube")
    # If the gripper is around the cube, sweep it towards the target location.
    if check("the robot's gripper is around cube"):
        robot.sweep("cube to goal")