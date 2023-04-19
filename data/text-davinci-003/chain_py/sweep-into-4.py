
    # Steps:
    #  1. Put gripper above cube
    #  2. Push the gripper into cube from above
    #  3. Sweep the cube to the goal

    # First, put the gripper above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.reach("above cube")

    # If the gripper isn't around the cube, move down towards it.
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.push("gripper into the cube")

    # Once the gripper is around the cube and closed, start sweeping it to the
    # goal.
    if check("the robot's gripper is around the cube and the robot's gripper is closed"):
        robot.sweep("cube to goal")