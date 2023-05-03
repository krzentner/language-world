
    # Steps:
    #  1. Put gripper above cube
    #  2. Grab cube with gripper
    #  3. Move cube to goal
    # First, put the gripper above the cube.
    if check("the robot's gripper is not above cube"):
        robot.put("gripper above cube")
    # If the gripper is still above the cube, grab it by moving the gripper
    # around the cube.
    # Don't need to be too precise here because the cube is small.
    if check("the robot's gripper is above cube and the robot's gripper is not around cube"):
        robot.grab("cube")
    # If the gripper is around the cube, move the cube to the goal.
    if check("the robot's gripper is around cube"):
        robot.move("cube to goal")