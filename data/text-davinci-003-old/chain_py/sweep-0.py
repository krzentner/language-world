
    # Steps:
    #  1. Put gripper above cube
    #  2. Grab the cube
    #  3. Move the cube sideways to goal
    # First, put the gripper above the cube.
    if check("the robot's gripper is not above cube"):
        robot.put("gripper above cube")
    # If the cube isn't below the gripper as seen from above, move the gripper
    # above the cube.
    if check("the robot's gripper is not near cube and the robot's gripper is not vertically aligned with the cube"):
        robot.grab("cube")
    # If the gripper is near the cube, we've probably grabbed the cube and can
    # move it to the target location.
    if check("the robot's gripper is near the cube and the cube is below the robot's gripper"):
        robot.slide("the cube to the goal")